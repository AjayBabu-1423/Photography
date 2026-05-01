from flask import Flask, request, jsonify, render_template, send_from_directory, abort, session, redirect
import sqlite3, os, uuid, secrets
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'vip-visualeyes-secret-key-2024')

UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp', 'mp4', 'mov'}

# ── ADMIN PASSWORD — change this in production! ───
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'vip@admin2024')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ─── DB ───────────────────────────────────────────
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT, type TEXT, date TEXT, time TEXT,
        location TEXT, package TEXT, photographer TEXT,
        amount INTEGER, status TEXT, notes TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first TEXT, last TEXT, email TEXT, phone TEXT,
        city TEXT, source TEXT, notes TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT, session TEXT, amount INTEGER,
        paid INTEGER DEFAULT 0, due_date TEXT,
        status TEXT DEFAULT 'Pending', notes TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS galleries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT, client TEXT, photos INTEGER DEFAULT 0,
        password TEXT, download_type TEXT DEFAULT 'yes',
        expiry TEXT, status TEXT DEFAULT 'Live',
        downloads INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS gallery_photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gallery_id INTEGER NOT NULL,
        filename TEXT NOT NULL,
        original_name TEXT,
        size INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (gallery_id) REFERENCES galleries(id) ON DELETE CASCADE
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT, client TEXT, phone TEXT, datetime TEXT,
        channel TEXT, message TEXT,
        status TEXT DEFAULT 'Scheduled',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT, phone TEXT,
        event_type TEXT, event_date TEXT,
        venue TEXT, message TEXT,
        status TEXT DEFAULT 'New',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    # ── Customer access tokens ────────────────────
    c.execute('''CREATE TABLE IF NOT EXISTS customer_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT UNIQUE NOT NULL,
        client_name TEXT NOT NULL,
        email TEXT DEFAULT '',
        gallery_ids TEXT DEFAULT '',
        active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    # Seed sample data if empty
    count = c.execute("SELECT COUNT(*) FROM bookings").fetchone()[0]
    if count == 0:
        c.executemany("INSERT INTO bookings(client,type,date,time,location,package,photographer,amount,status) VALUES(?,?,?,?,?,?,?,?,?)", [
            ('Priya & Arjun','Wedding Photography','2024-12-14','10:00','Besant Nagar Beach','Royal','Lokesh & Ajay',55000,'Confirmed'),
            ('Meena Krishnan','Family Portrait','2024-12-17','16:00','Studio, Ocheri','Essential','Lokesh',15000,'Confirmed'),
            ('Tech Corp','Corporate Event','2024-12-20','09:00','Ranipet SIPCOT','Premium','Ajay',30000,'Pending'),
            ('Rahul Sharma','Birthday Videography','2024-12-22','18:00','Home','Essential','Lokesh',15000,'Confirmed'),
        ])
        c.executemany("INSERT INTO clients(first,last,email,phone,city,source) VALUES(?,?,?,?,?,?)", [
            ('Priya','& Arjun Mehta','priya@email.com','98400 11111','Chennai','Instagram'),
            ('Meena','Krishnan','meena.k@gmail.com','94440 22222','Ranipet','Referral'),
            ('Tech Corp','Ltd','hr@techcorp.in','044 2222 3333','Ranipet','Google'),
            ('Rahul','Sharma','rahul@email.com','99400 44444','Vellore','Instagram'),
        ])
        c.executemany("INSERT INTO payments(client,session,amount,paid,due_date,status) VALUES(?,?,?,?,?,?)", [
            ('Priya & Arjun','Wedding Photography — Royal',55000,27500,'2024-12-01','Partial'),
            ('Meena Krishnan','Family Portrait — Essential',15000,0,'2024-12-10','Overdue'),
            ('Tech Corp','Corporate Event — Premium',30000,30000,'2024-12-05','Paid'),
        ])
        c.executemany("INSERT INTO galleries(title,client,photos,download_type,status,downloads) VALUES(?,?,?,?,?,?)", [
            ('Priya & Arjun Wedding','Priya & Arjun',0,'yes','Live',0),
            ('Meena Family Portraits','Meena Krishnan',0,'yes','Live',0),
            ('TechCorp Annual Day','Tech Corp Ltd',0,'watermark','Live',0),
        ])
        c.executemany("INSERT INTO reminders(type,client,datetime,channel,message,status) VALUES(?,?,?,?,?,?)", [
            ('Session Reminder (1 day before)','Priya & Arjun','2024-12-13 09:00','WhatsApp',"Hi Priya! Your wedding session is tomorrow. — Lokesh, VIP VisualEye's 📸",'Scheduled'),
            ('Payment Due Reminder','Meena Krishnan','2024-12-12 10:00','WhatsApp',"Hi Meena! Invoice of ₹15,000 is overdue. — Ajay, VIP VisualEye's",'Sent'),
            ('Gallery Ready Notification','Priya & Arjun','2024-12-01 14:00','Email',"Your wedding gallery is ready! — VIP VisualEye's",'Sent'),
        ])
        c.executemany("INSERT INTO inquiries(name,email,phone,event_type,status) VALUES(?,?,?,?,?)", [
            ('Kavya Nair','kavya@email.com','98100 11111','Wedding','New'),
            ('Kiran & Swati','kiran@email.com','97200 22222','Pre-Wedding','Replied'),
            ('Ravi Kumar','ravi@email.com','96300 33333','Corporate Event','Converted'),
        ])
        # Demo customer token
        c.execute("INSERT OR IGNORE INTO customer_tokens(token,client_name,email,gallery_ids) VALUES(?,?,?,?)",
                  ('demo-priya-2024', 'Priya & Arjun', 'priya@email.com', '1'))

    conn.commit()
    conn.close()

init_db()

# ─── AUTH HELPERS ─────────────────────────────────
def is_admin():
    return session.get('role') == 'admin'

def get_customer_token():
    token = session.get('customer_token')
    if not token:
        return None
    conn = get_db()
    row = conn.execute("SELECT * FROM customer_tokens WHERE token=? AND active=1", (token,)).fetchone()
    conn.close()
    return dict(row) if row else None

def require_admin(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not is_admin():
            return jsonify({'error': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper

# ─── PAGES ────────────────────────────────────────
@app.route('/')
def home():
    if is_admin():
        return render_template('index.html', mode='admin')
    return render_template('index.html', mode='login')

@app.route('/admin')
def admin_page():
    if is_admin():
        return render_template('index.html', mode='admin')
    return render_template('index.html', mode='login')

@app.route('/client/<token>')
def customer_access(token):
    conn = get_db()
    row = conn.execute("SELECT * FROM customer_tokens WHERE token=? AND active=1", (token,)).fetchone()
    conn.close()
    if not row:
        return render_template('index.html', mode='invalid_token')
    session['role'] = 'customer'
    session['customer_token'] = token
    session['customer_name'] = row['client_name']
    session['customer_gallery_ids'] = row['gallery_ids'] or ''
    return render_template('index.html', mode='customer')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# ─── AUTH API ─────────────────────────────────────
@app.route('/api/auth/admin-login', methods=['POST'])
def admin_login():
    d = request.json or {}
    if d.get('password', '') == ADMIN_PASSWORD:
        session['role'] = 'admin'
        return jsonify({'success': True, 'message': 'Welcome, Admin!'})
    return jsonify({'success': False, 'message': 'Incorrect password'}), 401

@app.route('/api/auth/me')
def auth_me():
    if is_admin():
        return jsonify({'role': 'admin'})
    ct = get_customer_token()
    if ct:
        return jsonify({'role': 'customer', 'name': ct['client_name'], 'gallery_ids': ct['gallery_ids']})
    return jsonify({'role': 'guest'}), 401

@app.route('/api/auth/logout', methods=['POST'])
def api_logout():
    session.clear()
    return jsonify({'success': True})

# ─── CUSTOMER TOKEN MANAGEMENT ────────────────────
@app.route('/api/customer-tokens', methods=['GET'])
@require_admin
def list_tokens():
    conn = get_db()
    rows = conn.execute("SELECT * FROM customer_tokens ORDER BY created_at DESC").fetchall()
    conn.close()
    result = []
    for r in rows:
        d = dict(r)
        d['link'] = f'/client/{d["token"]}'
        result.append(d)
    return jsonify(result)

@app.route('/api/customer-tokens', methods=['POST'])
@require_admin
def create_token():
    d = request.json or {}
    client_name = d.get('client_name', '').strip()
    if not client_name:
        return jsonify({'error': 'Client name required'}), 400
    token = secrets.token_urlsafe(16)
    conn = get_db()
    conn.execute("INSERT INTO customer_tokens(token,client_name,email,gallery_ids) VALUES(?,?,?,?)",
                 (token, client_name, d.get('email', ''), d.get('gallery_ids', '')))
    conn.commit()
    conn.close()
    return jsonify({'token': token, 'link': f'/client/{token}', 'message': 'Customer link created!'})

@app.route('/api/customer-tokens/<int:tid>', methods=['DELETE'])
@require_admin
def delete_token(tid):
    conn = get_db()
    conn.execute("DELETE FROM customer_tokens WHERE id=?", (tid,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Token deleted'})

@app.route('/api/customer-tokens/<int:tid>/toggle', methods=['PUT'])
@require_admin
def toggle_token(tid):
    conn = get_db()
    conn.execute("UPDATE customer_tokens SET active = 1 - active WHERE id=?", (tid,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Token toggled'})

# ─── SERVE UPLOADED PHOTOS ────────────────────────
@app.route('/static/uploads/<path:filename>')
def serve_upload(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ─── DASHBOARD ────────────────────────────────────
@app.route('/api/dashboard')
@require_admin
def dashboard():
    conn = get_db()
    bookings_count = conn.execute("SELECT COUNT(*) FROM bookings WHERE status != 'Completed'").fetchone()[0]
    revenue = conn.execute("SELECT COALESCE(SUM(paid),0) FROM payments").fetchone()[0]
    clients_count = conn.execute("SELECT COUNT(*) FROM clients").fetchone()[0]
    galleries_count = conn.execute("SELECT COUNT(*) FROM galleries WHERE status='Live'").fetchone()[0]
    overdue_sum = conn.execute("SELECT COALESCE(SUM(amount-paid),0) FROM payments WHERE status='Overdue'").fetchone()[0]
    overdue_count = conn.execute("SELECT COUNT(*) FROM payments WHERE status='Overdue'").fetchone()[0]
    upcoming = conn.execute("SELECT client,type,date,time,location FROM bookings ORDER BY date ASC LIMIT 5").fetchall()
    conn.close()
    return jsonify({
        'bookings_count': bookings_count, 'revenue': revenue,
        'clients_count': clients_count, 'galleries_count': galleries_count,
        'overdue_sum': overdue_sum, 'overdue_count': overdue_count,
        'upcoming': [dict(r) for r in upcoming]
    })

# ─── BOOKINGS ─────────────────────────────────────
@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    if is_admin():
        conn = get_db()
        rows = conn.execute("SELECT * FROM bookings ORDER BY date DESC").fetchall()
        conn.close()
        return jsonify([dict(r) for r in rows])
    ct = get_customer_token()
    if ct:
        name = ct['client_name']
        conn = get_db()
        rows = conn.execute("SELECT * FROM bookings WHERE client LIKE ? ORDER BY date DESC", (f'%{name}%',)).fetchall()
        conn.close()
        return jsonify([dict(r) for r in rows])
    return jsonify({'error': 'Unauthorized'}), 403

@app.route('/api/bookings', methods=['POST'])
def add_booking():
    if not (is_admin() or get_customer_token()):
        return jsonify({'error': 'Unauthorized'}), 403
    d = request.json
    pkg_prices = {'Essential': 15000, 'Premium': 30000, 'Royal': 55000}
    amount = d.get('amount') or pkg_prices.get(d.get('package', 'Essential'), 15000)
    conn = get_db()
    conn.execute("INSERT INTO bookings(client,type,date,time,location,package,photographer,amount,status,notes) VALUES(?,?,?,?,?,?,?,?,?,?)",
        (d.get('client'), d.get('type', 'Photography'), d.get('date'), d.get('time', '10:00'),
         d.get('location'), d.get('package', 'Essential'), d.get('photographer', 'Lokesh'), amount, 'Pending', d.get('notes', '')))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Booking confirmed!'})

@app.route('/api/bookings/<int:id>', methods=['PUT'])
@require_admin
def update_booking(id):
    d = request.json
    conn = get_db()
    conn.execute("UPDATE bookings SET status=? WHERE id=?", (d['status'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Updated'})

@app.route('/api/bookings/<int:id>', methods=['DELETE'])
@require_admin
def delete_booking(id):
    conn = get_db()
    conn.execute("DELETE FROM bookings WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deleted'})

# ─── CLIENTS ──────────────────────────────────────
@app.route('/api/clients', methods=['GET'])
@require_admin
def get_clients():
    conn = get_db()
    rows = conn.execute("""
        SELECT c.*,
        (SELECT COUNT(*) FROM bookings WHERE client LIKE '%'||c.first||'%') as booking_count,
        (SELECT COALESCE(SUM(amount),0) FROM payments WHERE client LIKE '%'||c.first||'%') as total_spent
        FROM clients c ORDER BY c.created_at DESC
    """).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/api/clients', methods=['POST'])
@require_admin
def add_client():
    d = request.json
    conn = get_db()
    conn.execute("INSERT INTO clients(first,last,email,phone,city,source,notes) VALUES(?,?,?,?,?,?,?)",
        (d.get('first'), d.get('last', ''), d.get('email', ''), d.get('phone', ''),
         d.get('city', ''), d.get('source', ''), d.get('notes', '')))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Client saved!'})

@app.route('/api/clients/<int:id>', methods=['DELETE'])
@require_admin
def delete_client(id):
    conn = get_db()
    conn.execute("DELETE FROM clients WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deleted'})

# ─── PAYMENTS ─────────────────────────────────────
@app.route('/api/payments', methods=['GET'])
@require_admin
def get_payments():
    conn = get_db()
    rows = conn.execute("SELECT * FROM payments ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/api/payments', methods=['POST'])
@require_admin
def add_payment():
    d = request.json
    amount = int(d.get('amount', 0))
    deposit = int(d.get('deposit', 0))
    status = 'Paid' if deposit >= amount else 'Partial' if deposit > 0 else 'Pending'
    conn = get_db()
    conn.execute("INSERT INTO payments(client,session,amount,paid,due_date,status,notes) VALUES(?,?,?,?,?,?,?)",
        (d.get('client'), d.get('session', ''), amount, deposit,
         d.get('due_date', ''), status, d.get('notes', '')))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Invoice created! Status: {status}'})

@app.route('/api/payments/<int:id>/paid', methods=['PUT'])
@require_admin
def mark_paid(id):
    conn = get_db()
    conn.execute("UPDATE payments SET paid=amount, status='Paid' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Marked as fully paid'})

@app.route('/api/payments/<int:id>/partial', methods=['PUT'])
@require_admin
def record_partial(id):
    d = request.json
    received = int(d.get('received', 0))
    conn = get_db()
    row = conn.execute("SELECT amount, paid FROM payments WHERE id=?", (id,)).fetchone()
    if row:
        new_paid = min(row['paid'] + received, row['amount'])
        new_status = 'Paid' if new_paid >= row['amount'] else 'Partial'
        conn.execute("UPDATE payments SET paid=?, status=? WHERE id=?", (new_paid, new_status, id))
        conn.commit()
        conn.close()
        return jsonify({'message': f'Recorded ₹{received}', 'status': new_status, 'new_paid': new_paid})
    conn.close()
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/payments/<int:id>', methods=['DELETE'])
@require_admin
def delete_payment(id):
    conn = get_db()
    conn.execute("DELETE FROM payments WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deleted'})

# ─── GALLERIES ────────────────────────────────────
@app.route('/api/galleries', methods=['GET'])
def get_galleries():
    conn = get_db()
    if is_admin():
        galleries = conn.execute("SELECT * FROM galleries ORDER BY created_at DESC").fetchall()
    else:
        ct = get_customer_token()
        if not ct:
            conn.close()
            return jsonify({'error': 'Unauthorized'}), 403
        gallery_ids_str = ct.get('gallery_ids', '')
        if gallery_ids_str:
            ids = [int(x.strip()) for x in gallery_ids_str.split(',') if x.strip().isdigit()]
            if ids:
                placeholders = ','.join('?' * len(ids))
                galleries = conn.execute(
                    f"SELECT * FROM galleries WHERE id IN ({placeholders}) AND status='Live' ORDER BY created_at DESC", ids
                ).fetchall()
            else:
                galleries = []
        else:
            name = ct['client_name']
            galleries = conn.execute(
                "SELECT * FROM galleries WHERE client LIKE ? AND status='Live' ORDER BY created_at DESC",
                (f'%{name}%',)
            ).fetchall()
    result = []
    for g in galleries:
        gd = dict(g)
        photos = conn.execute(
            "SELECT id, filename, original_name, size, created_at FROM gallery_photos WHERE gallery_id=? ORDER BY created_at ASC",
            (g['id'],)
        ).fetchall()
        gd['photo_list'] = [dict(p) for p in photos]
        gd['photos'] = len(gd['photo_list'])
        result.append(gd)
    conn.close()
    return jsonify(result)

@app.route('/api/galleries', methods=['POST'])
@require_admin
def add_gallery():
    d = request.json
    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO galleries(title,client,password,download_type,expiry,status,photos) VALUES(?,?,?,?,?,?,?)",
        (d.get('title'), d.get('client', ''), d.get('password', ''), d.get('download_type', 'yes'),
         d.get('expiry', ''), 'Live', 0))
    gallery_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'message': 'Gallery created!', 'gallery_id': gallery_id})

@app.route('/api/galleries/<int:id>', methods=['DELETE'])
@require_admin
def delete_gallery(id):
    conn = get_db()
    photos = conn.execute("SELECT filename FROM gallery_photos WHERE gallery_id=?", (id,)).fetchall()
    for p in photos:
        fpath = os.path.join(UPLOAD_FOLDER, p['filename'])
        if os.path.exists(fpath):
            os.remove(fpath)
    conn.execute("DELETE FROM gallery_photos WHERE gallery_id=?", (id,))
    conn.execute("DELETE FROM galleries WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Gallery and all photos deleted'})

# ─── UPLOAD PHOTOS ────────────────────────────────
@app.route('/api/galleries/<int:gallery_id>/upload', methods=['POST'])
@require_admin
def upload_to_gallery(gallery_id):
    conn = get_db()
    gallery = conn.execute("SELECT * FROM galleries WHERE id=?", (gallery_id,)).fetchone()
    if not gallery:
        conn.close()
        return jsonify({'error': 'Gallery not found'}), 404
    files = request.files.getlist('files')
    if not files:
        conn.close()
        return jsonify({'error': 'No files received'}), 400
    saved, errors = [], []
    for f in files:
        if not f.filename or not allowed_file(f.filename):
            if f.filename: errors.append(f'{f.filename} — unsupported format')
            continue
        ext = f.filename.rsplit('.', 1)[1].lower()
        safe_name = f'gal{gallery_id}_{uuid.uuid4().hex[:8]}.{ext}'
        fpath = os.path.join(UPLOAD_FOLDER, safe_name)
        try:
            f.save(fpath)
            size = os.path.getsize(fpath)
            conn.execute("INSERT INTO gallery_photos(gallery_id,filename,original_name,size) VALUES(?,?,?,?)",
                         (gallery_id, safe_name, secure_filename(f.filename), size))
            saved.append({'filename': safe_name, 'original_name': f.filename, 'size': size})
        except Exception as e:
            errors.append(f'{f.filename} — {str(e)}')
    conn.execute("UPDATE galleries SET photos=(SELECT COUNT(*) FROM gallery_photos WHERE gallery_id=?) WHERE id=?",
                 (gallery_id, gallery_id))
    conn.commit()
    conn.close()
    return jsonify({'message': f'{len(saved)} photo(s) uploaded', 'files': saved, 'errors': errors, 'gallery_id': gallery_id})

# ─── PHOTOS ───────────────────────────────────────
@app.route('/api/photos/<int:photo_id>/download')
def download_photo(photo_id):
    conn = get_db()
    photo = conn.execute("SELECT * FROM gallery_photos WHERE id=?", (photo_id,)).fetchone()
    if not photo:
        conn.close()
        abort(404)
    if not is_admin():
        ct = get_customer_token()
        if not ct:
            conn.close()
            abort(403)
        allowed_ids = [int(x.strip()) for x in (ct.get('gallery_ids') or '').split(',') if x.strip().isdigit()]
        if photo['gallery_id'] not in allowed_ids:
            conn.close()
            abort(403)
        gallery = conn.execute("SELECT download_type FROM galleries WHERE id=?", (photo['gallery_id'],)).fetchone()
        if not gallery or gallery['download_type'] == 'no':
            conn.close()
            abort(403)
    conn.execute("UPDATE galleries SET downloads=downloads+1 WHERE id=?", (photo['gallery_id'],))
    conn.commit()
    fname = photo['filename']
    orig = photo['original_name'] or fname
    conn.close()
    return send_from_directory(UPLOAD_FOLDER, fname, as_attachment=True, download_name=orig)

@app.route('/api/photos/<int:photo_id>', methods=['DELETE'])
@require_admin
def delete_photo(photo_id):
    conn = get_db()
    photo = conn.execute("SELECT * FROM gallery_photos WHERE id=?", (photo_id,)).fetchone()
    if photo:
        fpath = os.path.join(UPLOAD_FOLDER, photo['filename'])
        if os.path.exists(fpath):
            os.remove(fpath)
        gid = photo['gallery_id']
        conn.execute("DELETE FROM gallery_photos WHERE id=?", (photo_id,))
        conn.execute("UPDATE galleries SET photos=(SELECT COUNT(*) FROM gallery_photos WHERE gallery_id=?) WHERE id=?", (gid, gid))
        conn.commit()
    conn.close()
    return jsonify({'message': 'Photo deleted'})

# ─── REMINDERS ────────────────────────────────────
@app.route('/api/reminders', methods=['GET'])
@require_admin
def get_reminders():
    conn = get_db()
    rows = conn.execute("SELECT * FROM reminders ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/api/reminders', methods=['POST'])
@require_admin
def add_reminder():
    d = request.json
    conn = get_db()
    conn.execute("INSERT INTO reminders(type,client,phone,datetime,channel,message,status) VALUES(?,?,?,?,?,?,?)",
        (d.get('type'), d.get('client'), d.get('phone', ''), d.get('datetime'),
         d.get('channel', 'WhatsApp'), d.get('message', ''), 'Scheduled'))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Reminder scheduled!'})

@app.route('/api/reminders/<int:id>', methods=['DELETE'])
@require_admin
def delete_reminder(id):
    conn = get_db()
    conn.execute("DELETE FROM reminders WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Deleted'})

@app.route('/api/reminders/<int:id>', methods=['PUT'])
@require_admin
def update_reminder(id):
    d = request.json
    conn = get_db()
    conn.execute("UPDATE reminders SET status=? WHERE id=?", (d.get('status', 'Sent'), id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Reminder updated'})

# ─── INQUIRIES ────────────────────────────────────
@app.route('/api/inquiries', methods=['GET'])
@require_admin
def get_inquiries():
    conn = get_db()
    rows = conn.execute("SELECT * FROM inquiries ORDER BY created_at DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/api/inquiries', methods=['POST'])
def add_inquiry():
    d = request.json
    conn = get_db()
    conn.execute("INSERT INTO inquiries(name,email,phone,event_type,event_date,venue,message,status) VALUES(?,?,?,?,?,?,?,?)",
        (d.get('name'), d.get('email', ''), d.get('phone', ''), d.get('event_type', ''),
         d.get('event_date', ''), d.get('venue', ''), d.get('message', ''), 'New'))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Inquiry received!'})

@app.route('/api/inquiries/<int:id>/status', methods=['PUT'])
@require_admin
def update_inquiry(id):
    d = request.json
    conn = get_db()
    conn.execute("UPDATE inquiries SET status=? WHERE id=?", (d['status'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Updated'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
