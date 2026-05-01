<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>VIP VisualEye's Photography</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet"/>
<style>
:root {
  --gold: #C9A84C;
  --gold2: #E8C96A;
  --gold3: #F5E090;
  --black: #0A0A0A;
  --dark: #111111;
  --card: #161616;
  --card2: #1C1C1C;
  --silver: #C0C0C0;
  --silver2: #E8E8E8;
  --text: #F0EDE8;
  --muted: #7A7870;
  --border: rgba(201,168,76,0.15);
  --border2: rgba(201,168,76,0.3);
  --radius: 4px;
  --radius-lg: 8px;
  --font-display: 'Cinzel', serif;
  --font-body: 'Jost', sans-serif;
  --font-accent: 'Cormorant Garamond', serif;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--black);color:var(--text);font-family:var(--font-body);min-height:100vh;overflow-x:hidden;}

/* GOLD TEXTURE OVERLAY */
body::before{content:'';position:fixed;inset:0;background:radial-gradient(ellipse at 20% 50%,rgba(201,168,76,0.03) 0%,transparent 60%),radial-gradient(ellipse at 80% 20%,rgba(201,168,76,0.04) 0%,transparent 50%);pointer-events:none;z-index:0;}

/* NAV */
nav{display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;background:rgba(10,10,10,0.97);backdrop-filter:blur(20px);position:sticky;top:0;z-index:100;border-bottom:1px solid var(--border);}
.logo-area{display:flex;flex-direction:column;line-height:1;}
.logo-vip{font-family:var(--font-display);font-size:1.4rem;font-weight:900;background:linear-gradient(135deg,#C9A84C,#F5E090,#C9A84C);-webkit-background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.15em;}
.logo-sub{font-family:var(--font-body);font-size:0.55rem;font-weight:300;letter-spacing:0.35em;color:var(--silver);text-transform:uppercase;margin-top:1px;}
.nav-links{display:flex;gap:0.1rem;flex-wrap:wrap;}
.nav-btn{background:none;border:none;color:var(--muted);font-family:var(--font-body);font-size:0.78rem;font-weight:400;padding:0.5rem 0.9rem;border-radius:var(--radius);cursor:pointer;transition:all 0.2s;letter-spacing:0.08em;text-transform:uppercase;}
.nav-btn:hover,.nav-btn.active{color:var(--gold);background:rgba(201,168,76,0.06);}
.nav-cta{background:linear-gradient(135deg,var(--gold),var(--gold2));color:var(--black);border:none;font-family:var(--font-display);font-size:0.7rem;font-weight:700;padding:0.6rem 1.4rem;border-radius:var(--radius);cursor:pointer;transition:all 0.2s;letter-spacing:0.12em;text-transform:uppercase;}
.nav-cta:hover{transform:scale(1.03);box-shadow:0 4px 20px rgba(201,168,76,0.35);}

/* PAGES */
.page{display:none;padding:2rem;max-width:1200px;margin:0 auto;position:relative;z-index:1;}
.page.active{display:block;animation:fadeUp 0.4s ease;}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}

/* HERO */
.hero{text-align:center;padding:3.5rem 1rem 2.5rem;position:relative;}
.crown-deco{font-size:2rem;margin-bottom:0.75rem;display:block;}
.hero-eyebrow{font-family:var(--font-body);font-size:0.7rem;font-weight:400;letter-spacing:0.45em;text-transform:uppercase;color:var(--gold);margin-bottom:1.2rem;}
.hero h1{font-family:var(--font-display);font-size:clamp(2rem,5vw,3.8rem);font-weight:900;letter-spacing:0.08em;line-height:1.1;margin-bottom:0.5rem;}
.hero h1 .gold{background:linear-gradient(135deg,#C9A84C,#F5E090,#C9A84C);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hero h1 .silver{background:linear-gradient(135deg,#999,#E8E8E8,#999);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hero-tagline{font-family:var(--font-accent);font-size:1.15rem;font-style:italic;color:var(--silver);margin:1rem auto 2rem;max-width:480px;line-height:1.6;}
.divider-gold{display:flex;align-items:center;gap:1rem;justify-content:center;margin:1.5rem auto;max-width:320px;}
.divider-gold::before,.divider-gold::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);}
.divider-dot{width:5px;height:5px;border-radius:50%;background:var(--gold);}
.hero-actions{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;}

/* BUTTONS */
.btn-gold{background:linear-gradient(135deg,var(--gold),var(--gold2));color:var(--black);border:none;font-family:var(--font-display);font-size:0.72rem;font-weight:700;padding:0.85rem 2rem;border-radius:var(--radius);cursor:pointer;transition:all 0.25s;letter-spacing:0.15em;text-transform:uppercase;box-shadow:0 4px 20px rgba(201,168,76,0.25);}
.btn-gold:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(201,168,76,0.4);}
.btn-outline{background:transparent;color:var(--gold);border:1px solid var(--border2);font-family:var(--font-display);font-size:0.72rem;font-weight:600;padding:0.85rem 2rem;border-radius:var(--radius);cursor:pointer;transition:all 0.2s;letter-spacing:0.15em;text-transform:uppercase;}
.btn-outline:hover{background:rgba(201,168,76,0.07);}
.btn-sm{font-size:0.7rem;padding:0.45rem 1rem;border-radius:var(--radius);}

/* STATS */
.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:1px;background:var(--border);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;margin:2.5rem 0;}
.stat-card{background:var(--card);padding:1.5rem 1rem;text-align:center;}
.stat-num{font-family:var(--font-display);font-size:1.8rem;font-weight:700;background:linear-gradient(135deg,var(--gold),var(--gold3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.stat-label{font-size:0.72rem;color:var(--muted);margin-top:0.3rem;letter-spacing:0.1em;text-transform:uppercase;}

/* SECTION */
.section-header{margin-bottom:2rem;}
.section-header h2{font-family:var(--font-display);font-size:1.5rem;font-weight:700;letter-spacing:0.08em;color:var(--text);}
.section-header p{font-size:0.85rem;color:var(--muted);margin-top:0.4rem;letter-spacing:0.04em;}
.gold-rule{display:flex;align-items:center;gap:0.75rem;margin:0.75rem 0;}
.gold-rule::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--gold),transparent);max-width:120px;}
.gold-rule-dot{width:4px;height:4px;border-radius:50%;background:var(--gold);flex-shrink:0;}

/* CARDS */
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.5rem;}
.card-gold{background:var(--card);border:1px solid var(--border2);border-radius:var(--radius-lg);padding:1.5rem;}
.grid-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.25rem;}
.grid-3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem;}

/* BADGES */
.badge{display:inline-block;font-size:0.68rem;font-weight:500;padding:0.25rem 0.7rem;border-radius:2px;letter-spacing:0.08em;text-transform:uppercase;}
.badge-gold{background:rgba(201,168,76,0.12);color:var(--gold2);border:1px solid rgba(201,168,76,0.2);}
.badge-silver{background:rgba(192,192,192,0.1);color:var(--silver2);border:1px solid rgba(192,192,192,0.15);}
.badge-green{background:rgba(0,180,100,0.1);color:#4ECB7F;border:1px solid rgba(0,180,100,0.15);}
.badge-red{background:rgba(220,60,60,0.1);color:#E07070;border:1px solid rgba(220,60,60,0.15);}
.badge-muted{background:rgba(255,255,255,0.04);color:var(--muted);border:1px solid rgba(255,255,255,0.06);}

/* FORMS */
label{display:block;font-size:0.72rem;font-weight:500;color:var(--muted);margin-bottom:0.4rem;margin-top:1rem;letter-spacing:0.1em;text-transform:uppercase;}
input,select,textarea{width:100%;background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:var(--radius);padding:0.75rem 1rem;color:var(--text);font-family:var(--font-body);font-size:0.88rem;transition:border-color 0.2s;letter-spacing:0.02em;}
input:focus,select:focus,textarea:focus{outline:none;border-color:var(--gold);background:rgba(201,168,76,0.04);}
textarea{resize:vertical;min-height:100px;}
select option{background:var(--dark);}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:1rem;}
@media(max-width:600px){.form-row{grid-template-columns:1fr;}.nav-links{display:none;}}

/* TABLE */
.table-wrap{overflow-x:auto;}
table{width:100%;border-collapse:collapse;font-size:0.85rem;}
th{text-align:left;padding:0.85rem 1rem;color:var(--gold);font-weight:500;font-size:0.68rem;text-transform:uppercase;letter-spacing:0.12em;border-bottom:1px solid var(--border2);}
td{padding:0.9rem 1rem;border-bottom:1px solid var(--border);vertical-align:middle;color:var(--text);}
tr:last-child td{border-bottom:none;}
tr:hover td{background:rgba(201,168,76,0.03);}

/* PACKAGES */
.package-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:1rem;margin:1rem 0;}
.package-card{border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.25rem;cursor:pointer;transition:all 0.2s;position:relative;}
.package-card:hover{border-color:var(--border2);}
.package-card.selected{border-color:var(--gold);background:rgba(201,168,76,0.05);}
.package-card.selected::after{content:'✦';position:absolute;top:10px;right:12px;color:var(--gold);font-size:0.8rem;}
.pkg-name{font-family:var(--font-display);font-size:0.8rem;font-weight:600;letter-spacing:0.1em;color:var(--gold);margin-bottom:0.5rem;}
.pkg-price{font-family:var(--font-display);font-size:1.4rem;font-weight:700;color:var(--text);}
.pkg-price span{font-size:0.75rem;color:var(--muted);font-family:var(--font-body);}
.pkg-features{margin-top:0.8rem;}
.pkg-features li{font-size:0.78rem;color:var(--muted);list-style:none;padding:0.2rem 0;}
.pkg-features li::before{content:'— ';color:var(--gold);font-size:0.7rem;}

/* GALLERY */
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:8px;}
.gallery-item{position:relative;border-radius:var(--radius);overflow:hidden;aspect-ratio:1;cursor:pointer;border:1px solid var(--border);}
.gallery-placeholder{width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:2.5rem;}
.gallery-overlay{position:absolute;inset:0;background:rgba(10,10,10,0.8);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity 0.2s;border:1px solid var(--border2);}
.gallery-item:hover .gallery-overlay{opacity:1;}
.progress-bar{height:2px;background:var(--border);border-radius:1px;margin-top:0.75rem;}
.progress-fill{height:100%;border-radius:1px;background:linear-gradient(90deg,var(--gold),var(--gold3));}

/* PAYMENT METHOD */
.method-btn{flex:1;min-width:90px;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius);padding:0.65rem;text-align:center;cursor:pointer;transition:all 0.2s;font-size:0.78rem;color:var(--muted);font-family:var(--font-body);letter-spacing:0.04em;}
.method-btn:hover,.method-btn.selected{border-color:var(--border2);color:var(--gold);background:rgba(201,168,76,0.06);}

/* CLIENT */
.client-avatar{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:var(--font-display);font-weight:700;font-size:0.85rem;flex-shrink:0;border:1px solid var(--border2);background:rgba(201,168,76,0.08);color:var(--gold);}
.client-row{display:flex;align-items:center;gap:1rem;padding:1rem;border-radius:var(--radius);transition:background 0.2s;cursor:pointer;border-bottom:1px solid var(--border);}
.client-row:last-child{border-bottom:none;}
.client-row:hover{background:rgba(201,168,76,0.03);}

/* CALENDAR */
.calendar-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;}
.cal-day-name{text-align:center;font-size:0.65rem;color:var(--gold);padding:0.5rem 0;font-weight:500;letter-spacing:0.1em;text-transform:uppercase;}
.cal-day{aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:0.82rem;border-radius:var(--radius);cursor:pointer;transition:all 0.2s;color:var(--muted);position:relative;}
.cal-day:hover{background:rgba(201,168,76,0.08);color:var(--text);}
.cal-day.today{background:rgba(201,168,76,0.12);color:var(--gold);font-weight:600;}
.cal-day.has-event::after{content:'';position:absolute;bottom:3px;left:50%;transform:translateX(-50%);width:4px;height:4px;border-radius:50%;background:var(--gold);}
.cal-day.selected{background:var(--gold);color:var(--black);font-weight:700;}
.cal-day.other-month{color:rgba(122,120,112,0.25);}

/* CONTACT */
.contact-method{display:flex;align-items:center;gap:1rem;padding:1rem;background:rgba(201,168,76,0.04);border:1px solid var(--border);border-radius:var(--radius-lg);margin-bottom:0.75rem;transition:border-color 0.2s;}
.contact-method:hover{border-color:var(--border2);}
.contact-icon{width:38px;height:38px;border-radius:var(--radius);display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0;background:rgba(201,168,76,0.1);border:1px solid var(--border2);}

/* REMINDER */
.reminder-item{display:flex;gap:1rem;padding:1.1rem;border-radius:var(--radius-lg);background:var(--card2);border:1px solid var(--border);margin-bottom:0.75rem;align-items:flex-start;}
.reminder-icon{width:36px;height:36px;border-radius:var(--radius);display:flex;align-items:center;justify-content:center;font-size:0.9rem;flex-shrink:0;background:rgba(201,168,76,0.1);}

/* MODAL */
.modal-overlay{position:fixed;inset:0;background:rgba(5,5,5,0.9);display:none;align-items:center;justify-content:center;z-index:200;padding:1rem;backdrop-filter:blur(4px);}
.modal-overlay.open{display:flex;}
.modal{background:var(--card);border:1px solid var(--border2);border-radius:var(--radius-lg);padding:2rem;max-width:520px;width:100%;max-height:88vh;overflow-y:auto;animation:fadeUp 0.25s ease;}
.modal-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:1px solid var(--border);}
.modal-header h3{font-family:var(--font-display);font-size:1.1rem;letter-spacing:0.08em;color:var(--gold);}
.modal-close{background:none;border:none;color:var(--muted);font-size:1.1rem;cursor:pointer;width:28px;height:28px;border-radius:var(--radius);display:flex;align-items:center;justify-content:center;}
.modal-close:hover{background:rgba(255,255,255,0.06);color:var(--text);}

/* TOAST */
#toast{position:fixed;bottom:2rem;right:2rem;background:var(--card);border:1px solid var(--gold);color:var(--gold);padding:0.85rem 1.5rem;border-radius:var(--radius-lg);font-size:0.85rem;font-weight:500;transform:translateY(100px);opacity:0;transition:all 0.3s;z-index:999;font-family:var(--font-body);letter-spacing:0.04em;}
#toast.show{transform:translateY(0);opacity:1;}

/* QUICK ACTION BUTTONS */
.quick-action{background:rgba(201,168,76,0.04);border:1px solid var(--border);border-radius:var(--radius-lg);padding:1.25rem;text-align:left;cursor:pointer;color:var(--text);transition:all 0.2s;width:100%;}
.quick-action:hover{border-color:var(--border2);background:rgba(201,168,76,0.07);}
.quick-action .qa-icon{font-size:1.4rem;margin-bottom:0.6rem;display:block;}
.quick-action .qa-title{font-family:var(--font-display);font-size:0.78rem;font-weight:600;letter-spacing:0.1em;color:var(--gold);}
.quick-action .qa-sub{font-size:0.75rem;color:var(--muted);margin-top:0.2rem;}

/* UPCOMING SESSION */
.session-item{display:flex;align-items:center;justify-content:space-between;padding:1rem 0;border-bottom:1px solid var(--border);}
.session-item:last-child{border-bottom:none;}

/* OVERDUE ALERT */
.alert-gold{padding:1rem;background:rgba(201,168,76,0.06);border:1px solid rgba(201,168,76,0.2);border-left:3px solid var(--gold);border-radius:var(--radius-lg);margin-top:1rem;}

/* SCROLLBAR */
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:transparent;}
::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px;}

/* ── VISITING CARD ── */
.card-scene{width:340px;height:210px;perspective:1000px;margin:0 auto;}
.card-3d{width:100%;height:100%;position:relative;transform-style:preserve-3d;transition:transform 0.75s cubic-bezier(.4,0,.2,1);cursor:pointer;}
.card-scene:hover .card-3d,.card-scene.flipped .card-3d{transform:rotateY(180deg);}
.card-face{position:absolute;inset:0;border-radius:14px;backface-visibility:hidden;overflow:hidden;}
.card-back-face{transform:rotateY(180deg);}

/* card front – black/gold geometric */
.card-front-bg{width:100%;height:100%;background:#0d0d0d;position:relative;display:flex;align-items:center;justify-content:center;}
.card-front-bg::before{content:'';position:absolute;top:-30px;right:-20px;width:140px;height:260px;background:linear-gradient(160deg,#B8860B,#C9A84C,#8B6914);clip-path:polygon(30% 0%,100% 0%,100% 100%,0% 100%);opacity:0.85;}
.card-front-bg::after{content:'';position:absolute;bottom:-40px;left:-20px;width:100px;height:200px;background:linear-gradient(160deg,#8B6914,#C9A84C);clip-path:polygon(0% 0%,60% 0%,100% 100%,0% 100%);opacity:0.7;}
.card-logo-wrap{position:relative;z-index:2;text-align:center;}
.card-logo-vip{font-family:'Cinzel',serif;font-size:2.6rem;font-weight:900;background:linear-gradient(160deg,#C9A84C,#F5E090,#C9A84C);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;letter-spacing:0.05em;}
.card-logo-cam{font-size:1.4rem;margin-left:4px;vertical-align:middle;opacity:0.9;}
.card-logo-sub{font-family:'Jost',sans-serif;font-size:0.55rem;letter-spacing:0.45em;color:#C0C0C0;text-transform:uppercase;margin-top:4px;}
.card-logo-photo{font-family:'Jost',sans-serif;font-size:0.42rem;letter-spacing:0.6em;color:#888;text-transform:uppercase;margin-top:2px;}
.card-crown{font-size:1rem;display:block;margin-bottom:2px;}

/* card back */
.card-back-bg{width:100%;height:100%;background:#0d0d0d;position:relative;display:flex;flex-direction:column;justify-content:center;padding:0 1.5rem;}
.card-back-bg::before{content:'';position:absolute;top:-20px;right:-15px;width:110px;height:240px;background:linear-gradient(160deg,#B8860B,#C9A84C);clip-path:polygon(25% 0%,100% 0%,100% 100%,0% 100%);opacity:0.85;}
.card-back-bg::after{content:'';position:absolute;bottom:-30px;left:-15px;width:80px;height:160px;background:linear-gradient(160deg,#8B6914,#C9A84C);clip-path:polygon(0% 0%,55% 0%,100% 100%,0% 100%);opacity:0.6;}
.card-names{font-family:'Cinzel',serif;font-size:1.1rem;font-weight:700;color:#fff;line-height:1.3;position:relative;z-index:2;}
.card-title-lbl{font-family:'Jost',sans-serif;font-size:0.6rem;letter-spacing:0.25em;color:#C9A84C;text-transform:uppercase;margin-bottom:0.6rem;position:relative;z-index:2;}
.card-details{margin-top:0.6rem;position:relative;z-index:2;}
.card-detail-row{display:flex;align-items:center;gap:0.5rem;margin-bottom:0.35rem;}
.card-detail-icon{width:18px;height:18px;border-radius:50%;background:rgba(201,168,76,0.15);border:1px solid rgba(201,168,76,0.4);display:flex;align-items:center;justify-content:center;font-size:0.55rem;flex-shrink:0;}
.card-detail-text{font-family:'Jost',sans-serif;font-size:0.62rem;color:#ddd;line-height:1.3;}
.card-mini-logo{position:absolute;bottom:12px;right:16px;z-index:2;text-align:right;}
.card-mini-vip{font-family:'Cinzel',serif;font-size:0.75rem;font-weight:900;background:linear-gradient(135deg,#C9A84C,#F5E090);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.card-mini-sub{font-family:'Jost',sans-serif;font-size:0.32rem;letter-spacing:0.3em;color:#888;text-transform:uppercase;}

/* share card */
.card-share-bar{display:flex;gap:0.75rem;justify-content:center;margin-top:1.5rem;flex-wrap:wrap;}
.share-btn{display:flex;align-items:center;gap:0.4rem;background:rgba(201,168,76,0.07);border:1px solid var(--border2);color:var(--gold);font-family:var(--font-body);font-size:0.75rem;padding:0.5rem 1rem;border-radius:var(--radius);cursor:pointer;transition:all 0.2s;letter-spacing:0.04em;}
.share-btn:hover{background:rgba(201,168,76,0.14);}

/* ── FRAMES ── */
.frames-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1.25rem;}
.frame-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;cursor:pointer;transition:all 0.25s;}
.frame-card:hover{border-color:var(--border2);transform:translateY(-3px);box-shadow:0 8px 30px rgba(201,168,76,0.1);}
.frame-card.active-frame{border-color:var(--gold);box-shadow:0 0 0 2px rgba(201,168,76,0.25);}
.frame-preview{width:100%;aspect-ratio:1;position:relative;display:flex;align-items:center;justify-content:center;background:#111;overflow:hidden;}
.frame-label{padding:0.75rem 1rem;display:flex;align-items:center;justify-content:space-between;}
.frame-name{font-family:var(--font-display);font-size:0.72rem;letter-spacing:0.1em;color:var(--gold);}
.frame-type{font-size:0.68rem;color:var(--muted);}

/* upload zone */
.upload-zone{border:2px dashed var(--border2);border-radius:var(--radius-lg);padding:2.5rem;text-align:center;cursor:pointer;transition:all 0.2s;background:rgba(201,168,76,0.02);}
.upload-zone:hover{background:rgba(201,168,76,0.05);border-color:var(--gold);}
.upload-zone input{display:none;}

/* canvas wrap */
.canvas-wrap{position:relative;display:inline-block;border-radius:var(--radius);overflow:hidden;border:1px solid var(--border2);}
#frame-canvas{display:block;max-width:100%;border-radius:var(--radius);}

/* ── PRICE LIST ── */
.price-section-title{font-family:var(--font-display);font-size:0.72rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold);margin:2rem 0 1rem;display:flex;align-items:center;gap:0.75rem;}
.price-section-title::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--border2),transparent);}
.price-pkg-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:1rem;margin-bottom:1.5rem;}
.price-pkg{background:var(--card);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;transition:all 0.2s;}
.price-pkg:hover{border-color:var(--border2);transform:translateY(-2px);}
.price-pkg.featured{border-color:var(--gold);box-shadow:0 0 0 1px rgba(201,168,76,0.2);}
.price-pkg-top{padding:1.25rem 1.25rem 1rem;border-bottom:1px solid var(--border);}
.price-pkg-badge{font-size:0.62rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;padding:0.2rem 0.55rem;border-radius:2px;display:inline-block;margin-bottom:0.6rem;}
.price-pkg-name{font-family:var(--font-display);font-size:0.95rem;font-weight:700;letter-spacing:0.06em;color:var(--text);margin-bottom:0.5rem;}
.price-amt{font-family:var(--font-display);font-size:1.8rem;font-weight:900;background:linear-gradient(135deg,var(--gold),var(--gold3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;}
.price-amt-sub{font-family:var(--font-body);font-size:0.72rem;color:var(--muted);margin-top:0.2rem;}
.price-pkg-body{padding:1rem 1.25rem 1.25rem;}
.price-item{display:flex;align-items:flex-start;gap:0.5rem;padding:0.28rem 0;font-size:0.8rem;color:var(--muted);}
.price-item::before{content:'✦';color:var(--gold);font-size:0.6rem;margin-top:0.15rem;flex-shrink:0;}
.price-table-wrap{overflow-x:auto;margin-bottom:1.5rem;}
.price-table{width:100%;border-collapse:collapse;font-size:0.82rem;}
.price-table th{text-align:left;padding:0.7rem 1rem;color:var(--gold);font-size:0.65rem;letter-spacing:0.12em;text-transform:uppercase;border-bottom:1px solid var(--border2);font-weight:500;}
.price-table td{padding:0.75rem 1rem;border-bottom:1px solid var(--border);vertical-align:middle;}
.price-table tr:last-child td{border-bottom:none;}
.price-table tr:hover td{background:rgba(201,168,76,0.02);}
.edit-price-btn{background:none;border:1px solid var(--border);color:var(--muted);border-radius:var(--radius);padding:0.22rem 0.5rem;font-size:0.68rem;cursor:pointer;font-family:var(--font-body);}
.edit-price-btn:hover{border-color:var(--border2);color:var(--gold);}
.inline-edit{background:transparent;border:none;border-bottom:1px solid var(--border2);color:var(--text);font-family:var(--font-body);font-size:0.82rem;width:100%;outline:none;padding:0.1rem 0;}
.inline-edit:focus{border-bottom-color:var(--gold);}
.price-tag{font-weight:600;color:var(--gold);font-family:var(--font-display);}
.frame-price-tag{font-size:0.72rem;font-weight:600;color:var(--gold);font-family:var(--font-display);margin-top:2px;}

</style>
</head>
<body>

<!-- NAV -->
<div class="nav-links" id="navLinks">

  {% if mode == 'admin' %}
  <button class="nb active" onclick="nav('dashboard',this)">Dashboard</button>
  <button class="nb" onclick="nav('booking',this)">Booking</button>
  <button class="nb" onclick="nav('gallery',this)">Gallery</button>
  <button class="nb" onclick="nav('payments',this)">Payments</button>
  <button class="nb" onclick="nav('clients',this)">Clients</button>
  <button class="nb" onclick="nav('reminders',this)">Reminders</button>
  <button class="nb" onclick="nav('contact',this)">Contact</button>
  <button class="nb" onclick="nav('card',this)">My Card</button>
  <button class="nb" onclick="nav('frames',this)">Frames</button>
  {% else %}
  <button class="nb active" onclick="nav('booking',this)">Booking</button>
  <button class="nb" onclick="nav('gallery',this)">Gallery</button>
  <button class="nb" onclick="nav('contact',this)">Contact</button>
  <button class="nb" onclick="nav('card',this)">My Card</button>
  <button class="nb" onclick="nav('frames',this)">Frames</button>
  {% endif %}

</div>
<!-- ═══════════════ DASHBOARD ═══════════════ -->
<div id="page-dashboard" class="page {% if mode == 'admin' %}active{% endif %}">
  <div class="hero">
    <span class="crown-deco">👑</span>
    <div class="hero-eyebrow">VIP VisualEye's Photography & Videography</div>
    <h1><span class="gold">Lokesh</span> &amp; <span class="silver">Ajay</span></h1>
    <div class="divider-gold"><div class="divider-dot"></div></div>
    <p class="hero-tagline">Capturing royal moments, one frame at a time — Ocheri, Ranipet</p>
    <div class="hero-actions">
      <button class="btn-gold" onclick="showPage('booking',null);openModal('new-booking')">Book a Session</button>
      <button class="btn-outline" onclick="showPage('gallery',null)">View Galleries</button>
    </div>
  </div>

  <div class="stats-row">
    <div class="stat-card"><div class="stat-num">12</div><div class="stat-label">Active Bookings</div></div>
    <div class="stat-card"><div class="stat-num">₹2.4L</div><div class="stat-label">This Month</div></div>
    <div class="stat-card"><div class="stat-num">48</div><div class="stat-label">Total Clients</div></div>
    <div class="stat-card"><div class="stat-num">6</div><div class="stat-label">Live Galleries</div></div>
  </div>

  <div class="grid-2">
    <div class="card">
      <div class="section-header" style="margin-bottom:1rem;">
        <h2 style="font-size:1rem;">Upcoming Sessions</h2>
        <div class="gold-rule"><div class="gold-rule-dot"></div></div>
      </div>
      <div class="session-item">
        <div><div style="font-weight:500;font-size:0.9rem;">Priya &amp; Arjun — Wedding</div><div style="font-size:0.76rem;color:var(--muted);margin-top:2px;">Dec 14 · 10:00 AM · Besant Nagar Beach</div></div>
        <span class="badge badge-red">Tomorrow</span>
      </div>
      <div class="session-item">
        <div><div style="font-weight:500;font-size:0.9rem;">Meena — Family Portrait</div><div style="font-size:0.76rem;color:var(--muted);margin-top:2px;">Dec 17 · 4:00 PM · Studio, Ocheri</div></div>
        <span class="badge badge-gold">Dec 17</span>
      </div>
      <div class="session-item">
        <div><div style="font-weight:500;font-size:0.9rem;">Tech Corp — Annual Event</div><div style="font-size:0.76rem;color:var(--muted);margin-top:2px;">Dec 20 · 9:00 AM · Ranipet</div></div>
        <span class="badge badge-silver">Dec 20</span>
      </div>
      <div class="session-item">
        <div><div style="font-weight:500;font-size:0.9rem;">Rahul — Birthday Video</div><div style="font-size:0.76rem;color:var(--muted);margin-top:2px;">Dec 22 · 6:00 PM · Home</div></div>
        <span class="badge badge-muted">Dec 22</span>
      </div>
    </div>

    <div>
      <div class="card" style="margin-bottom:1.25rem;">
        <div class="section-header" style="margin-bottom:1rem;">
          <h2 style="font-size:1rem;">Quick Actions</h2>
          <div class="gold-rule"><div class="gold-rule-dot"></div></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;">
          <button class="quick-action" onclick="showPage('booking',null);openModal('new-booking')">
            <span class="qa-icon">📅</span>
            <div class="qa-title">New Booking</div>
            <div class="qa-sub">Schedule a session</div>
          </button>
          <button class="quick-action" onclick="showPage('clients',null);openModal('new-client')">
            <span class="qa-icon">👤</span>
            <div class="qa-title">Add Client</div>
            <div class="qa-sub">Create profile</div>
          </button>
          <button class="quick-action" onclick="showPage('gallery',null);openModal('upload-gallery')">
            <span class="qa-icon">🖼️</span>
            <div class="qa-title">Upload Gallery</div>
            <div class="qa-sub">Share photos</div>
          </button>
          <button class="quick-action" onclick="showPage('payments',null);openModal('new-invoice')">
            <span class="qa-icon">💳</span>
            <div class="qa-title">Send Invoice</div>
            <div class="qa-sub">Request payment</div>
          </button>
        </div>
      </div>
      <div class="alert-gold">
        <div style="font-size:0.75rem;color:var(--gold);font-weight:600;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.35rem;">⚠ Pending Payments</div>
        <div style="font-size:0.88rem;">3 invoices totalling <strong style="color:var(--gold);">₹42,000</strong> are overdue</div>
        <button onclick="showPage('payments',null)" style="margin-top:0.65rem;background:none;border:1px solid rgba(201,168,76,0.3);color:var(--gold);border-radius:var(--radius);padding:0.35rem 0.9rem;font-size:0.72rem;cursor:pointer;letter-spacing:0.06em;">View Invoices →</button>
      </div>
    </div>
  </div>

  <div class="card" style="margin-top:1.25rem;">
    <div class="section-header" style="margin-bottom:1.25rem;">
      <h2 style="font-size:1rem;">December 2024</h2>
      <div class="gold-rule"><div class="gold-rule-dot"></div></div>
    </div>
    <div id="mini-cal"></div>
  </div>
</div>

<!-- ═══════════════ BOOKING ═══════════════ -->
<div id="page-booking" class="page {% if mode != 'admin' %}active{% endif %}">
  <div class="section-header">
    <h2>Booking Management</h2>
    <div class="gold-rule"><div class="gold-rule-dot"></div></div>
    <p>All photography & videography sessions — Lokesh & Ajay</p>
  </div>
  <div style="display:flex;gap:0.75rem;margin-bottom:1.5rem;flex-wrap:wrap;align-items:center;">
    <input type="text" placeholder="Search bookings..." style="max-width:260px;"/>
    <select style="max-width:170px;"><option>All Types</option><option>Wedding</option><option>Portrait</option><option>Event</option><option>Videography</option></select>
    <select style="max-width:160px;"><option>All Status</option><option>Confirmed</option><option>Pending</option><option>Completed</option></select>
    <button class="btn-gold btn-sm" style="margin-left:auto;" onclick="openModal('new-booking')">+ New Booking</button>
  </div>
  <div class="card">
    <div class="table-wrap">
      <table><thead><tr><th>Client</th><th>Type</th><th>Date & Time</th><th>Location</th><th>Package</th><th>Amount</th><th>Status</th><th></th></tr></thead>
      <tbody id="booking-table-body"></tbody></table>
    </div>
  </div>
</div>

<!-- ═══════════════ GALLERY ═══════════════ -->
<div id="page-gallery" class="page">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
    <div class="section-header" style="margin:0;">
      <h2>Client Galleries</h2>
      <div class="gold-rule"><div class="gold-rule-dot"></div></div>
      <p>Secure photo & video delivery — vipvisualeyes</p>
    </div>
    <button class="btn-gold btn-sm" onclick="openModal('upload-gallery')">+ Create Gallery</button>
  </div>
  <div id="gallery-list"></div>
</div>

<!-- ═══════════════ PAYMENTS ═══════════════ -->
<div id="page-payments" class="page">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
    <div class="section-header" style="margin:0;">
      <h2>Payments & Invoices</h2>
      <div class="gold-rule"><div class="gold-rule-dot"></div></div>
      <p>vipvisualeyes14@gmail.com · UPI / Bank Transfer</p>
    </div>
    <button class="btn-gold btn-sm" onclick="openModal('new-invoice')">+ New Invoice</button>
  </div>
  <div class="stats-row" style="margin:0 0 1.5rem;">
    <div class="stat-card"><div class="stat-num">₹2.4L</div><div class="stat-label">Collected</div></div>
    <div class="stat-card"><div class="stat-num">₹42K</div><div class="stat-label">Overdue</div></div>
    <div class="stat-card"><div class="stat-num">₹95K</div><div class="stat-label">Upcoming</div></div>
    <div class="stat-card"><div class="stat-num">₹3.4L</div><div class="stat-label">Pipeline</div></div>
  </div>
  <div class="card">
    <div class="table-wrap">
      <table><thead><tr><th>Invoice #</th><th>Client</th><th>Session</th><th>Amount</th><th>Paid</th><th>Due Date</th><th>Status</th><th></th></tr></thead>
      <tbody id="payment-table-body"></tbody></table>
    </div>
  </div>
</div>

<!-- ═══════════════ CLIENTS ═══════════════ -->
<div id="page-clients" class="page">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
    <div class="section-header" style="margin:0;">
      <h2>Client Management</h2>
      <div class="gold-rule"><div class="gold-rule-dot"></div></div>
      <p>Ocheri, Ranipet & surrounding areas</p>
    </div>
    <button class="btn-gold btn-sm" onclick="openModal('new-client')">+ Add Client</button>
  </div>
  <div style="margin-bottom:1rem;"><input type="text" placeholder="Search by name, phone or email..."/></div>
  <div class="card"><div id="client-list"></div></div>
</div>

<!-- ═══════════════ REMINDERS ═══════════════ -->
<div id="page-reminders" class="page">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
    <div class="section-header" style="margin:0;">
      <h2>Reminders & Notifications</h2>
      <div class="gold-rule"><div class="gold-rule-dot"></div></div>
      <p>Auto-alerts via WhatsApp, SMS & Email</p>
    </div>
    <button class="btn-gold btn-sm" onclick="openModal('new-reminder')">+ Add Reminder</button>
  </div>
  <div class="grid-2" style="margin-bottom:1.5rem;">
    <div class="card" style="border-left:2px solid var(--gold);">
      <div style="font-size:0.68rem;color:var(--muted);font-weight:500;text-transform:uppercase;letter-spacing:0.12em;">Scheduled Today</div>
      <div style="font-family:var(--font-display);font-size:2rem;font-weight:700;color:var(--gold);margin:0.25rem 0;">3</div>
      <div style="font-size:0.8rem;color:var(--muted);">reminders going out</div>
    </div>
    <div class="card" style="border-left:2px solid var(--silver);">
      <div style="font-size:0.68rem;color:var(--muted);font-weight:500;text-transform:uppercase;letter-spacing:0.12em;">This Week</div>
      <div style="font-family:var(--font-display);font-size:2rem;font-weight:700;color:var(--silver2);margin:0.25rem 0;">11</div>
      <div style="font-size:0.8rem;color:var(--muted);">automated messages</div>
    </div>
  </div>
  <div id="reminder-list"></div>
</div>

<!-- ═══════════════ CONTACT ═══════════════ -->
<div id="page-contact" class="page">
  <div class="section-header">
    <h2>Contact & Inquiries</h2>
    <div class="gold-rule"><div class="gold-rule-dot"></div></div>
    <p>Manage incoming leads — VIP VisualEye's Photography</p>
  </div>
  <div class="grid-2">
    <div>
      <div class="card-gold" style="margin-bottom:1.25rem;">
        <div style="font-family:var(--font-display);font-size:0.85rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:1.25rem;">Studio Contact Details</div>
        <div class="contact-method">
          <div class="contact-icon">📞</div>
          <div>
            <div style="font-size:0.88rem;font-weight:500;">97155 54025</div>
            <div style="font-size:0.72rem;color:var(--muted);margin-top:1px;">Lokesh — Primary</div>
          </div>
        </div>
        <div class="contact-method">
          <div class="contact-icon">📞</div>
          <div>
            <div style="font-size:0.88rem;font-weight:500;">9894283672</div>
            <div style="font-size:0.72rem;color:var(--muted);margin-top:1px;">Ajay — Secondary</div>
          </div>
        </div>
        <div class="contact-method">
          <div class="contact-icon">📧</div>
          <div>
            <div style="font-size:0.88rem;font-weight:500;">vipvisualeyes14@gmail.com</div>
            <div style="font-size:0.72rem;color:var(--muted);margin-top:1px;">Email inquiries</div>
          </div>
        </div>
        <div class="contact-method">
          <div class="contact-icon">📍</div>
          <div>
            <div style="font-size:0.88rem;font-weight:500;">Ocheri, Ranipet</div>
            <div style="font-size:0.72rem;color:var(--muted);margin-top:1px;">Studio & field coverage</div>
          </div>
        </div>
        <div class="contact-method">
          <div class="contact-icon">📸</div>
          <div>
            <div style="font-size:0.88rem;font-weight:500;">@vipvisualeyes</div>
            <div style="font-size:0.72rem;color:var(--muted);margin-top:1px;">Instagram portfolio</div>
          </div>
        </div>
      </div>
      <div class="card">
        <div style="font-family:var(--font-display);font-size:0.85rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:1rem;">Recent Inquiries</div>
        <div id="inquiry-list"></div>
      </div>
    </div>

    <div class="card">
      <div style="font-family:var(--font-display);font-size:0.85rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:0.3rem;">New Client Inquiry</div>
      <p style="font-size:0.78rem;color:var(--muted);margin-bottom:1rem;">Share this form or embed on your website</p>
      <label>Full Name *</label>
      <input type="text" placeholder="Client's full name"/>
      <label>Email Address *</label>
      <input type="email" placeholder="client@email.com"/>
      <label>Phone Number</label>
      <input type="tel" placeholder="+91 "/>
      <label>Event Type</label>
      <select>
        <option>Select type...</option>
        <option>Wedding Photography</option>
        <option>Wedding Videography</option>
        <option>Wedding Photo + Video</option>
        <option>Portrait / Family</option>
        <option>Corporate Event</option>
        <option>Birthday / Celebration</option>
        <option>Pre-Wedding Shoot</option>
        <option>Other</option>
      </select>
      <label>Event Date</label>
      <input type="date"/>
      <label>Venue / Location</label>
      <input type="text" placeholder="Ranipet, Chennai, or other..."/>
      <label>Message</label>
      <textarea placeholder="Tell us about your event, vision, budget, and any special requests..."></textarea>
      <button class="btn-gold" style="width:100%;margin-top:1.25rem;" onclick="submitInquiry()">Send Inquiry to VIP VisualEye's</button>
    </div>
  </div>
</div>

<!-- ═══════════════ VISITING CARD ═══════════════ -->
<div id="page-card" class="page">
  <div class="section-header">
    <h2>Digital Visiting Card</h2>
    <div class="gold-rule"><div class="gold-rule-dot"></div></div>
    <p>Hover to flip · Share your card digitally with clients</p>
  </div>

  <div style="display:flex;flex-direction:column;align-items:center;gap:2rem;">

    <!-- CARD FLIP -->
    <div class="card-scene" id="cardScene" onclick="this.classList.toggle('flipped')" title="Click to flip">
      <div class="card-3d">

        <!-- FRONT -->
        <div class="card-face">
          <div class="card-front-bg">
            <div class="card-logo-wrap">
              <span class="card-crown">👑</span>
              <div style="display:flex;align-items:center;justify-content:center;gap:4px;">
                <div class="card-logo-vip">VIP</div>
                <span class="card-logo-cam">📷</span>
              </div>
              <div class="card-logo-sub">VisualEye's</div>
              <div class="card-logo-photo">Photography &nbsp;&amp;&nbsp; Videography</div>
            </div>
          </div>
        </div>

        <!-- BACK -->
        <div class="card-face card-back-face">
          <div class="card-back-bg">
            <div class="card-names">Lokesh<br/>Ajay</div>
            <div class="card-title-lbl">Photographers</div>
            <div class="card-details">
              <div class="card-detail-row">
                <div class="card-detail-icon">📞</div>
                <div class="card-detail-text">97155 54025<br/>9894283672</div>
              </div>
              <div class="card-detail-row">
                <div class="card-detail-icon">✉</div>
                <div class="card-detail-text">vipvisualeyes14@gmail.com</div>
              </div>
              <div class="card-detail-row">
                <div class="card-detail-icon">📍</div>
                <div class="card-detail-text">Ocheri, Ranipet</div>
              </div>
              <div class="card-detail-row">
                <div class="card-detail-icon">📸</div>
                <div class="card-detail-text">@vipvisualeyes</div>
              </div>
            </div>
            <div class="card-mini-logo">
              <div class="card-mini-vip">VIP VisualEye's</div>
              <div class="card-mini-sub">Photography</div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <p style="font-size:0.75rem;color:var(--muted);letter-spacing:0.06em;">Click card to flip · Hover to preview back</p>

    <!-- SHARE BAR -->
    <div class="card-share-bar">
      <button class="share-btn" onclick="shareWhatsApp()">📱 Share on WhatsApp</button>
      <button class="share-btn" onclick="copyContact()">📋 Copy Contact Info</button>
      <button class="share-btn" onclick="downloadCard()">⬇ Download Card</button>
      <button class="share-btn" onclick="showToast('Opening Instagram @vipvisualeyes')">📸 Instagram</button>
    </div>

    <!-- CARD DETAILS BELOW -->
    <div style="max-width:520px;width:100%;">
      <div class="card-gold" style="margin-bottom:1rem;">
        <div style="font-family:var(--font-display);font-size:0.8rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:1rem;">Card Details — Editable</div>
        <div class="form-row">
          <div><label>Name 1</label><input type="text" id="card-name1" value="Lokesh"/></div>
          <div><label>Name 2</label><input type="text" id="card-name2" value="Ajay"/></div>
        </div>
        <label>Title</label>
        <input type="text" id="card-title" value="Photographers"/>
        <div class="form-row">
          <div><label>Phone 1</label><input type="text" id="card-ph1" value="97155 54025"/></div>
          <div><label>Phone 2</label><input type="text" id="card-ph2" value="9894283672"/></div>
        </div>
        <label>Email</label>
        <input type="text" id="card-email" value="vipvisualeyes14@gmail.com"/>
        <label>Location</label>
        <input type="text" id="card-loc" value="Ocheri, Ranipet"/>
        <label>Instagram</label>
        <input type="text" id="card-insta" value="@vipvisualeyes"/>
        <button class="btn-gold" style="width:100%;margin-top:1.25rem;" onclick="updateCard()">Update Card</button>
      </div>

      <!-- QR placeholder -->
      <div class="card" style="text-align:center;padding:1.5rem;">
        <div style="font-family:var(--font-display);font-size:0.78rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:0.75rem;">WhatsApp QR Code</div>
        <div id="qr-box" style="width:120px;height:120px;background:rgba(201,168,76,0.06);border:1px solid var(--border2);border-radius:var(--radius);margin:0 auto;display:flex;align-items:center;justify-content:center;font-size:3rem;">📲</div>
        <div style="font-size:0.72rem;color:var(--muted);margin-top:0.75rem;">Scan to WhatsApp VIP VisualEye's</div>
        <a href="https://wa.me/919715554025" target="_blank" style="display:inline-block;margin-top:0.6rem;font-size:0.75rem;color:var(--gold);text-decoration:none;letter-spacing:0.04em;">wa.me/919715554025 →</a>
      </div>
    </div>
  </div>
</div>

<!-- ═══════════════ FRAMES + PRICE LIST ═══════════════ -->
<div id="page-frames" class="page">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;margin-bottom:1.5rem;">
    <div class="section-header" style="margin:0;">
      <h2>Frames & Price List</h2>
      <div class="gold-rule"><div class="gold-rule-dot"></div></div>
      <p>Apply branded frames · Share your full price list with clients</p>
    </div>
    <div style="display:flex;gap:0.6rem;flex-wrap:wrap;">
      <button class="btn-outline btn-sm" onclick="showTab('tab-frames','tab-prices')">🖼️ Frames</button>
      <button class="btn-outline btn-sm" onclick="showTab('tab-prices','tab-frames')">💰 Price List</button>
      <button class="btn-gold btn-sm" onclick="downloadPriceList()">⬇ Download Price List</button>
    </div>
  </div>

  <!-- ── TAB: FRAMES ── -->
  <div id="tab-frames">
    <div class="grid-2" style="margin-bottom:2rem;">
      <div>
        <div class="upload-zone" onclick="document.getElementById('photo-upload').click()">
          <input type="file" id="photo-upload" accept="image/*" onchange="loadPhoto(event)"/>
          <div style="font-size:2.5rem;margin-bottom:0.75rem;">🖼️</div>
          <div style="font-family:var(--font-display);font-size:0.82rem;letter-spacing:0.1em;color:var(--gold);">Upload Client Photo</div>
          <div style="font-size:0.75rem;color:var(--muted);margin-top:0.4rem;">JPG, PNG — any size</div>
        </div>
        <div id="canvas-area" style="margin-top:1.25rem;display:none;">
          <div class="canvas-wrap" style="width:100%;">
            <canvas id="frame-canvas" width="800" height="800"></canvas>
          </div>
          <div style="margin-top:0.75rem;padding:0.75rem;background:rgba(201,168,76,0.05);border:1px solid var(--border);border-radius:var(--radius-lg);">
            <div style="font-size:0.72rem;color:var(--gold);font-family:var(--font-display);letter-spacing:0.08em;margin-bottom:0.4rem;">Selected: <span id="selected-frame-name">Royal Gold</span> — <span id="selected-frame-price" class="price-tag">₹500</span></div>
          </div>
          <div style="display:flex;gap:0.75rem;margin-top:0.75rem;flex-wrap:wrap;">
            <button class="btn-gold" style="flex:1;" onclick="downloadFramed()">⬇ Download Framed Photo</button>
            <button class="btn-outline" style="flex:1;" onclick="shareFramed()">📱 Share via WhatsApp</button>
          </div>
          <div style="margin-top:0.75rem;">
            <label>Frame Opacity</label>
            <input type="range" min="50" max="100" value="100" id="frame-opacity" oninput="applyFrame()" style="margin-top:0.4rem;"/>
          </div>
        </div>
      </div>
      <div>
        <div style="font-family:var(--font-display);font-size:0.8rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:1rem;">Choose Frame Style</div>
        <div class="frames-grid" id="frames-grid"></div>
      </div>
    </div>
  </div>

  <!-- ── TAB: PRICE LIST ── -->
  <div id="tab-prices" style="display:none;">

    <!-- Hero price card -->
    <div style="background:linear-gradient(135deg,rgba(201,168,76,0.08),rgba(201,168,76,0.02));border:1px solid var(--border2);border-radius:var(--radius-lg);padding:1.75rem;margin-bottom:1.5rem;text-align:center;">
      <div style="font-size:1.5rem;margin-bottom:0.5rem;">👑</div>
      <div style="font-family:var(--font-display);font-size:1.3rem;letter-spacing:0.1em;color:var(--gold);">VIP VisualEye's Photography</div>
      <div style="font-size:0.75rem;color:var(--muted);margin-top:0.3rem;letter-spacing:0.15em;">OCHERI, RANIPET · 97155 54025 / 9894283672</div>
      <div style="font-size:0.72rem;color:var(--muted);margin-top:0.1rem;">vipvisualeyes14@gmail.com · @vipvisualeyes</div>
    </div>

    <!-- Photography Packages -->
    <div class="price-section-title">📸 Photography Packages</div>
    <div class="price-pkg-grid" id="photo-pkg-grid"></div>

    <!-- Videography Packages -->
    <div class="price-section-title">🎬 Videography Packages</div>
    <div class="price-pkg-grid" id="video-pkg-grid"></div>

    <!-- Add-ons Table -->
    <div class="price-section-title">✦ Add-Ons & Extras</div>
    <div class="card" style="margin-bottom:1.5rem;">
      <div class="price-table-wrap">
        <table class="price-table">
          <thead><tr><th>Service</th><th>Description</th><th>Price</th><th></th></tr></thead>
          <tbody id="addon-table"></tbody>
        </table>
      </div>
      <button class="btn-outline btn-sm" style="margin-top:1rem;" onclick="addAddon()">+ Add Row</button>
    </div>

    <!-- Frame Printing Price List -->
    <div class="price-section-title">🖼️ Photo Frame Prints</div>
    <div class="card" style="margin-bottom:1.5rem;">
      <div class="price-table-wrap">
        <table class="price-table">
          <thead><tr><th>Frame Style</th><th>Best For</th><th>Digital Price</th><th>Print Price</th><th></th></tr></thead>
          <tbody id="frame-price-table"></tbody>
        </table>
      </div>
    </div>

    <!-- Notes -->
    <div class="card" style="margin-bottom:1.5rem;">
      <div style="font-family:var(--font-display);font-size:0.78rem;letter-spacing:0.1em;color:var(--gold);margin-bottom:0.75rem;">Terms & Notes</div>
      <div id="price-notes" style="font-size:0.83rem;color:var(--muted);line-height:1.8;">
        ✦ 50% advance required to confirm booking<br/>
        ✦ Remaining payment due on delivery day<br/>
        ✦ Travel charges extra beyond 30 km from Ocheri, Ranipet<br/>
        ✦ Edited photos delivered within 7–10 working days<br/>
        ✦ Raw files not included unless specifically agreed<br/>
        ✦ GST applicable as per government norms
      </div>
    </div>

    <div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
      <button class="btn-gold" style="flex:1;min-width:180px;" onclick="downloadPriceList()">⬇ Download Price List PDF</button>
      <button class="btn-outline" style="flex:1;min-width:180px;" onclick="sharePriceList()">📱 Share on WhatsApp</button>
    </div>
  </div>
</div>

<!-- ═══════════════ MODALS ═══════════════ -->
<div id="modal-new-booking" class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h3>New Booking</h3>
      <button class="modal-close" onclick="closeModal('new-booking')">✕</button>
    </div>
    <label>Client Name *</label>
    <input type="text" id="book-client" placeholder="Client's name"/>
    <label>Session Type *</label>
    <select id="book-type">
      <option>Wedding Photography</option>
      <option>Wedding Videography</option>
      <option>Wedding Photo + Video</option>
      <option>Portrait Session</option>
      <option>Family Portrait</option>
      <option>Corporate Event</option>
      <option>Birthday / Celebration</option>
      <option>Pre-Wedding Shoot</option>
    </select>
    <label>Select Package</label>
    <div class="package-grid" id="pkg-select">
      <div class="package-card selected" onclick="selectPkg(this)">
        <div class="pkg-name">Essential</div>
        <div class="pkg-price">₹15,000<span>/session</span></div>
        <ul class="pkg-features"><li>4 hrs coverage</li><li>200 edited photos</li><li>Online gallery</li></ul>
      </div>
      <div class="package-card" onclick="selectPkg(this)">
        <div class="pkg-name">Premium</div>
        <div class="pkg-price">₹30,000<span>/session</span></div>
        <ul class="pkg-features"><li>8 hrs coverage</li><li>500 edited photos</li><li>Album included</li></ul>
      </div>
      <div class="package-card" onclick="selectPkg(this)">
        <div class="pkg-name">Royal</div>
        <div class="pkg-price">₹55,000<span>/session</span></div>
        <ul class="pkg-features"><li>Full day + video</li><li>Unlimited photos</li><li>2 photographers</li></ul>
      </div>
    </div>
    <div class="form-row">
      <div><label>Date *</label><input type="date" id="book-date"/></div>
      <div><label>Time *</label><input type="time" id="book-time" value="10:00"/></div>
    </div>
    <label>Location / Venue</label>
    <input type="text" id="book-location" placeholder="Venue name or address"/>
    <label>Photographer</label>
    <select id="book-photo"><option>Lokesh</option><option>Ajay</option><option>Lokesh & Ajay</option></select>
    <label>Notes</label>
    <textarea id="book-notes" placeholder="Shot list, special requests, client preferences..."></textarea>
    <button class="btn-gold" style="width:100%;margin-top:1.5rem;" onclick="saveBooking()">Confirm Booking</button>
  </div>
</div>

<div id="modal-new-client" class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h3>Add New Client</h3>
      <button class="modal-close" onclick="closeModal('new-client')">✕</button>
    </div>
    <div class="form-row">
      <div><label>First Name *</label><input type="text" id="cl-first" placeholder="First"/></div>
      <div><label>Last Name</label><input type="text" id="cl-last" placeholder="Last"/></div>
    </div>
    <label>Email</label>
    <input type="email" id="cl-email" placeholder="client@email.com"/>
    <label>Phone *</label>
    <input type="tel" id="cl-phone" placeholder="+91 XXXXX XXXXX"/>
    <label>City / Area</label>
    <input type="text" id="cl-city" placeholder="Ranipet, Chennai, Vellore..."/>
    <label>How did they find you?</label>
    <select id="cl-source"><option>Instagram (@vipvisualeyes)</option><option>Google</option><option>Referral</option><option>Walk-in</option><option>WhatsApp</option><option>Other</option></select>
    <label>Notes</label>
    <textarea id="cl-notes" placeholder="Any notes about this client..."></textarea>
    <button class="btn-gold" style="width:100%;margin-top:1.5rem;" onclick="saveClient()">Save Client</button>
  </div>
</div>

<div id="modal-upload-gallery" class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h3>Create Client Gallery</h3>
      <button class="modal-close" onclick="closeModal('upload-gallery')">✕</button>
    </div>
    <label>Gallery Title *</label>
    <input type="text" id="gal-title" placeholder="e.g. Priya & Arjun Wedding — Dec 2024"/>
    <label>Client Name</label>
    <input type="text" id="gal-client" placeholder="Client name"/>
    <label>Gallery Password (optional)</label>
    <input type="password" id="gal-pass" placeholder="Protect with a password"/>
    <label>Download Settings</label>
    <select id="gal-dl"><option value="yes">Full resolution download</option><option value="watermark">Download with VIP watermark</option><option value="no">View only — no download</option></select>
    <label>Gallery Expires On</label>
    <input type="date" id="gal-exp"/>
    <div style="margin-top:1.25rem;padding:1.5rem;background:rgba(201,168,76,0.03);border:1px dashed var(--border2);border-radius:var(--radius-lg);text-align:center;cursor:pointer;" onclick="showToast('File upload ready — connect your storage')">
      <div style="font-size:2rem;">📁</div>
      <div style="font-size:0.85rem;font-weight:500;margin-top:0.5rem;color:var(--gold);">Click to upload photos & videos</div>
      <div style="font-size:0.75rem;color:var(--muted);margin-top:0.3rem;">JPG, PNG, MP4, RAW — up to 100MB each</div>
    </div>
    <button class="btn-gold" style="width:100%;margin-top:1.5rem;" onclick="saveGallery()">Create Gallery</button>
  </div>
</div>

<div id="modal-new-invoice" class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h3>New Invoice</h3>
      <button class="modal-close" onclick="closeModal('new-invoice')">✕</button>
    </div>
    <label>Client *</label>
    <input type="text" id="inv-client" placeholder="Client name"/>
    <label>Session Description *</label>
    <input type="text" id="inv-desc" placeholder="e.g. Wedding Photography — Royal Package"/>
    <div class="form-row">
      <div><label>Total Amount (₹) *</label><input type="number" id="inv-amount" placeholder="55000"/></div>
      <div><label>Deposit (₹)</label><input type="number" id="inv-deposit" placeholder="15000"/></div>
    </div>
    <label>Due Date</label>
    <input type="date" id="inv-due"/>
    <label>Payment Method</label>
    <div style="display:flex;gap:0.6rem;flex-wrap:wrap;margin-top:0.5rem;">
      <div class="method-btn selected" onclick="selectMethod(this)">UPI / GPay</div>
      <div class="method-btn" onclick="selectMethod(this)">Bank Transfer</div>
      <div class="method-btn" onclick="selectMethod(this)">Cash</div>
      <div class="method-btn" onclick="selectMethod(this)">Razorpay</div>
    </div>
    <label>Notes</label>
    <textarea id="inv-notes" placeholder="VIP VisualEye's Photography — Ocheri, Ranipet&#10;Payment terms, bank details, etc."></textarea>
    <button class="btn-gold" style="width:100%;margin-top:1.5rem;" onclick="saveInvoice()">Send Invoice</button>
  </div>
</div>

<div id="modal-new-reminder" class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h3>Schedule Reminder</h3>
      <button class="modal-close" onclick="closeModal('new-reminder')">✕</button>
    </div>
    <label>Reminder Type</label>
    <select id="rem-type">
      <option>Session reminder (1 day before)</option>
      <option>Session reminder (1 week before)</option>
      <option>Payment due reminder</option>
      <option>Gallery ready notification</option>
      <option>Follow-up after delivery</option>
      <option>Custom message</option>
    </select>
    <label>Client</label>
    <input type="text" id="rem-client" placeholder="Client name"/>
    <label>Send Date & Time</label>
    <input type="datetime-local" id="rem-datetime"/>
    <label>Channel</label>
    <div style="display:flex;gap:0.6rem;flex-wrap:wrap;margin-top:0.5rem;">
      <div class="method-btn selected" onclick="selectMethod(this)">WhatsApp</div>
      <div class="method-btn" onclick="selectMethod(this)">Email</div>
      <div class="method-btn" onclick="selectMethod(this)">SMS</div>
    </div>
    <label>Message</label>
    <textarea id="rem-msg" placeholder="Hi {client}, this is Lokesh from VIP VisualEye's Photography. Just a reminder about your session tomorrow at {time}. Looking forward to capturing your special moments! 📸"></textarea>
    <button class="btn-gold" style="width:100%;margin-top:1.5rem;" onclick="saveReminder()">Schedule Reminder</button>
  </div>
</div>

<div id="toast"></div>

<script>
const APP_MODE = "{{ mode }}";

// ── DATA ──
let bookings = [
  {id:'BK001',client:'Priya & Arjun',type:'Wedding Photography',date:'2024-12-14',time:'10:00',location:'Besant Nagar Beach',pkg:'Royal',photographer:'Lokesh & Ajay',amount:55000,status:'Confirmed'},
  {id:'BK002',client:'Meena Krishnan',type:'Family Portrait',date:'2024-12-17',time:'16:00',location:'Studio, Ocheri',pkg:'Essential',photographer:'Lokesh',amount:15000,status:'Confirmed'},
  {id:'BK003',client:'Tech Corp',type:'Corporate Event',date:'2024-12-20',time:'09:00',location:'Ranipet SIPCOT',pkg:'Premium',photographer:'Ajay',amount:30000,status:'Pending'},
  {id:'BK004',client:'Rahul Sharma',type:'Birthday Videography',date:'2024-12-22',time:'18:00',location:'Home',pkg:'Essential',photographer:'Lokesh',amount:15000,status:'Confirmed'},
  {id:'BK005',client:'Ananya & Dev',type:'Pre-Wedding Shoot',date:'2025-01-05',time:'07:00',location:'Marina Beach',pkg:'Premium',photographer:'Lokesh & Ajay',amount:30000,status:'Pending'},
];

let clients = [
  {id:'CL001',first:'Priya',last:'& Arjun Mehta',email:'priya@email.com',phone:'98400 11111',city:'Chennai',source:'Instagram',bookings:2,totalSpent:85000},
  {id:'CL002',first:'Meena',last:'Krishnan',email:'meena.k@gmail.com',phone:'94440 22222',city:'Ranipet',source:'Referral',bookings:1,totalSpent:15000},
  {id:'CL003',first:'Tech Corp',last:'Ltd',email:'hr@techcorp.in',phone:'44 2222 3333',city:'Ranipet',source:'Google',bookings:3,totalSpent:90000},
  {id:'CL004',first:'Rahul',last:'Sharma',email:'rahul.s@email.com',phone:'99400 44444',city:'Vellore',source:'Instagram',bookings:1,totalSpent:15000},
  {id:'CL005',first:'Ananya',last:'& Dev',email:'ananya.d@email.com',phone:'80400 55555',city:'Chennai',source:'Google',bookings:1,totalSpent:30000},
];

let payments = [
  {id:'INV-001',client:'Priya & Arjun',session:'Wedding Photography — Royal',amount:55000,paid:27500,due:'2024-12-01',status:'Partial'},
  {id:'INV-002',client:'Meena Krishnan',session:'Family Portrait — Essential',amount:15000,paid:0,due:'2024-12-10',status:'Overdue'},
  {id:'INV-003',client:'Tech Corp',session:'Corporate Event — Premium',amount:30000,paid:30000,due:'2024-12-05',status:'Paid'},
  {id:'INV-004',client:'Rahul Sharma',session:'Birthday Video — Essential',amount:15000,paid:7500,due:'2024-12-20',status:'Partial'},
  {id:'INV-005',client:'Ananya & Dev',session:'Pre-Wedding — Premium',amount:30000,paid:0,due:'2024-12-28',status:'Pending'},
];

let galleries = [
  {id:'GAL001',title:'Priya & Arjun Wedding',client:'Priya & Arjun',photos:342,date:'2024-11-30',status:'Live',downloads:89,dl:'yes'},
  {id:'GAL002',title:'Meena Family Portraits',client:'Meena Krishnan',photos:54,date:'2024-12-01',status:'Live',downloads:12,dl:'yes'},
  {id:'GAL003',title:'TechCorp Annual Day',client:'Tech Corp Ltd',photos:187,date:'2024-11-15',status:'Live',downloads:143,dl:'watermark'},
];

let reminders = [
  {type:'Session reminder',client:'Priya & Arjun',datetime:'Dec 13 · 9:00 AM',channel:'WhatsApp',msg:'Hi Priya! This is Lokesh from VIP VisualEye\'s Photography. Your wedding session is tomorrow at 10:00 AM at Besant Nagar Beach. 📸👑',status:'Scheduled'},
  {type:'Payment reminder',client:'Meena Krishnan',datetime:'Dec 12 · 10:00 AM',channel:'WhatsApp',msg:'Hi Meena! Your invoice of ₹15,000 was due on Dec 10. Please complete your payment at your earliest. — Ajay, VIP VisualEye\'s',status:'Sent'},
  {type:'Gallery ready',client:'Priya & Arjun',datetime:'Dec 01 · 2:00 PM',channel:'Email',msg:'Your wedding gallery is ready! 342 beautifully edited photos are waiting for you at your private gallery link.',status:'Sent'},
  {type:'Session reminder',client:'Tech Corp',datetime:'Dec 19 · 9:00 AM',channel:'Email',msg:'Reminder: Your corporate event shoot is tomorrow at 9:00 AM at Ranipet SIPCOT. — VIP VisualEye\'s Photography',status:'Scheduled'},
];

let inquiries = [
  {name:'Kavya Nair',type:'Wedding',date:'Dec 10',status:'New'},
  {name:'Kiran & Swati',type:'Pre-Wedding',date:'Dec 09',status:'Replied'},
  {name:'Ravi Kumar',type:'Corporate Event',date:'Dec 08',status:'Converted'},
];

// ── RENDER ──
function renderBookings(){
  const sc={Confirmed:'badge-green',Pending:'badge-gold',Completed:'badge-silver'};
  document.getElementById('booking-table-body').innerHTML=bookings.map(b=>`
    <tr>
      <td><strong>${b.client}</strong><div style="font-size:0.72rem;color:var(--muted);">${b.photographer}</div></td>
      <td style="color:var(--muted);font-size:0.82rem;">${b.type}</td>
      <td style="font-size:0.83rem;">${fmtDate(b.date)} · ${b.time}</td>
      <td style="font-size:0.8rem;color:var(--muted);">${b.location}</td>
      <td><span class="badge badge-muted">${b.pkg}</span></td>
      <td style="font-weight:600;color:var(--gold);">₹${b.amount.toLocaleString()}</td>
      <td><span class="badge ${sc[b.status]||'badge-muted'}">${b.status}</span></td>
      <td><button onclick="showToast('Opening booking ${b.id}')" style="background:none;border:1px solid var(--border);color:var(--muted);border-radius:var(--radius);padding:0.28rem 0.6rem;font-size:0.72rem;cursor:pointer;">View</button></td>
    </tr>`).join('');
}

function renderGalleries(){
  const emojis=['🌸','🌿','✨','🎊','💫','🌊','🌅','🎭'];
  document.getElementById('gallery-list').innerHTML=galleries.map(g=>`
    <div class="card" style="margin-bottom:1.25rem;">
      <div style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
        <div>
          <div style="font-family:var(--font-display);font-size:0.95rem;letter-spacing:0.06em;">${g.title}</div>
          <div style="font-size:0.76rem;color:var(--muted);margin-top:3px;">${g.client} · ${g.photos} photos · ${g.date}</div>
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;align-items:center;">
          <span class="badge badge-green">${g.status}</span>
          <button onclick="showToast('Gallery link copied!')" style="background:none;border:1px solid var(--border);color:var(--muted);border-radius:var(--radius);padding:0.3rem 0.7rem;font-size:0.72rem;cursor:pointer;">📋 Copy Link</button>
          <button onclick="showToast('Opening gallery manager')" class="btn-outline btn-sm">Manage</button>
        </div>
      </div>
      <div style="display:flex;gap:2rem;font-size:0.78rem;color:var(--muted);margin-bottom:1rem;flex-wrap:wrap;">
        <span>📥 ${g.downloads} downloads</span>
        <span>⬇️ ${g.dl==='yes'?'Full resolution':g.dl==='watermark'?'With VIP watermark':'View only'}</span>
      </div>
      <div class="gallery-grid">${Array.from({length:Math.min(8,g.photos)},(_,i)=>`
        <div class="gallery-item" style="background:rgba(201,168,76,${0.05+i*0.01});">
          <div class="gallery-placeholder">${emojis[i%emojis.length]}</div>
          <div class="gallery-overlay">
            <button onclick="showToast('Downloading...')" style="background:var(--gold);border:none;color:var(--black);border-radius:var(--radius);padding:0.4rem 0.85rem;font-size:0.72rem;cursor:pointer;font-family:var(--font-display);letter-spacing:0.08em;font-weight:700;">⬇ Download</button>
          </div>
        </div>`).join('')}
      </div>
      <div class="progress-bar"><div class="progress-fill" style="width:${Math.round(g.downloads/g.photos*100)}%"></div></div>
      <div style="font-size:0.7rem;color:var(--muted);margin-top:0.4rem;">${g.downloads} of ${g.photos} photos downloaded</div>
    </div>`).join('');
}

function renderPayments(){
  const sc={Paid:'badge-green',Partial:'badge-gold',Overdue:'badge-red',Pending:'badge-muted'};
  document.getElementById('payment-table-body').innerHTML=payments.map(p=>`
    <tr>
      <td style="font-size:0.75rem;color:var(--muted);">${p.id}</td>
      <td><strong>${p.client}</strong></td>
      <td style="font-size:0.8rem;color:var(--muted);max-width:200px;">${p.session}</td>
      <td style="font-weight:600;">₹${p.amount.toLocaleString()}</td>
      <td style="color:#4ECB7F;">₹${p.paid.toLocaleString()}</td>
      <td style="font-size:0.8rem;color:var(--muted);">${p.due}</td>
      <td><span class="badge ${sc[p.status]}">${p.status}</span></td>
      <td style="display:flex;gap:0.4rem;">
        <button onclick="showToast('Invoice sent!')" style="background:none;border:1px solid var(--border);color:var(--muted);border-radius:var(--radius);padding:0.28rem 0.55rem;font-size:0.7rem;cursor:pointer;">📧</button>
        ${p.status!=='Paid'?`<button onclick="markPaid(this,'${p.id}')" style="background:rgba(0,180,100,0.08);border:1px solid rgba(0,180,100,0.2);color:#4ECB7F;border-radius:var(--radius);padding:0.28rem 0.6rem;font-size:0.7rem;cursor:pointer;">✓ Paid</button>`:''}
      </td>
    </tr>`).join('');
}

function markPaid(btn,id){
  const p=payments.find(x=>x.id===id);
  if(p){p.status='Paid';p.paid=p.amount;renderPayments();showToast('Payment marked as received!');}
}

function renderClients(){
  document.getElementById('client-list').innerHTML=clients.map(c=>`
    <div class="client-row">
      <div class="client-avatar">${c.first[0]}${c.last[0]}</div>
      <div style="flex:1;">
        <div style="font-weight:500;font-size:0.9rem;">${c.first} ${c.last}</div>
        <div style="font-size:0.75rem;color:var(--muted);margin-top:2px;">${c.phone} · ${c.city}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:0.85rem;font-weight:600;color:var(--gold);">₹${c.totalSpent.toLocaleString()}</div>
        <div style="font-size:0.72rem;color:var(--muted);">${c.bookings} session${c.bookings!==1?'s':''}</div>
      </div>
      <span class="badge badge-muted" style="margin-left:0.5rem;">${c.source}</span>
    </div>`).join('');
}

function renderReminders(){
  const icons={'Session reminder':'📅','Payment reminder':'💳','Gallery ready':'🖼️','Follow-up':'💬'};
  const sc={Scheduled:'badge-gold',Sent:'badge-green',Failed:'badge-red'};
  document.getElementById('reminder-list').innerHTML=reminders.map(r=>`
    <div class="reminder-item">
      <div class="reminder-icon">${icons[r.type]||'🔔'}</div>
      <div style="flex:1;">
        <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
          <span style="font-family:var(--font-display);font-size:0.78rem;letter-spacing:0.06em;">${r.type}</span>
          <span class="badge ${sc[r.status]}">${r.status}</span>
          <span class="badge badge-muted">${r.channel}</span>
        </div>
        <div style="font-size:0.77rem;color:var(--muted);margin-top:0.2rem;">${r.client} · ${r.datetime}</div>
        <div style="font-size:0.82rem;margin-top:0.4rem;color:var(--text);opacity:0.7;font-family:var(--font-accent);font-style:italic;">"${r.msg.substring(0,100)}${r.msg.length>100?'…':''}"</div>
      </div>
    </div>`).join('');
}

function renderInquiries(){
  const sc={New:'badge-red',Replied:'badge-gold',Converted:'badge-green'};
  document.getElementById('inquiry-list').innerHTML=inquiries.map(q=>`
    <div style="display:flex;align-items:center;justify-content:space-between;padding:0.75rem 0;border-bottom:1px solid var(--border);">
      <div>
        <div style="font-weight:500;font-size:0.88rem;">${q.name}</div>
        <div style="font-size:0.75rem;color:var(--muted);">${q.type} · ${q.date}</div>
      </div>
      <div style="display:flex;gap:0.4rem;align-items:center;">
        <span class="badge ${sc[q.status]}">${q.status}</span>
        <button onclick="showToast('Opening inquiry chat')" style="background:none;border:1px solid var(--border);color:var(--muted);border-radius:var(--radius);padding:0.25rem 0.55rem;font-size:0.7rem;cursor:pointer;">Reply</button>
      </div>
    </div>`).join('');
}

function renderMiniCal(){
  const days=['Su','Mo','Tu','We','Th','Fr','Sa'];
  const eventDays=[14,17,20,22];
  let h='<div class="calendar-grid">';
  days.forEach(d=>h+=`<div class="cal-day-name">${d}</div>`);
  for(let i=1;i<=31;i++){
    h+=`<div class="cal-day${i===13?' today':''}${eventDays.includes(i)?' has-event':''}" onclick="selDay(this)">${i}</div>`;
  }
  h+='</div>';
  document.getElementById('mini-cal').innerHTML=h;
}

// ── ACTIONS ──
function showPage(id,btn){
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  document.querySelectorAll('.nav-btn').forEach(b=>b.classList.remove('active'));
  if(btn) btn.classList.add('active');
}
function openModal(id){document.getElementById('modal-'+id).classList.add('open');}
function closeModal(id){document.getElementById('modal-'+id).classList.remove('open');}
document.querySelectorAll('.modal-overlay').forEach(m=>m.addEventListener('click',e=>{if(e.target===m)m.classList.remove('open');}));
function selectPkg(el){document.querySelectorAll('#pkg-select .package-card').forEach(c=>c.classList.remove('selected'));el.classList.add('selected');}
function selectMethod(el){el.parentElement.querySelectorAll('.method-btn').forEach(b=>b.classList.remove('selected'));el.classList.add('selected');}
function selDay(el){document.querySelectorAll('.cal-day').forEach(d=>d.classList.remove('selected'));el.classList.add('selected');}

function showToast(msg){
  const t=document.getElementById('toast');
  t.textContent='✦ '+msg;
  t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),3000);
}

function saveBooking(){
  const client=document.getElementById('book-client').value.trim();
  if(!client){showToast('Please enter a client name');return;}
  const pkg=document.querySelector('#pkg-select .package-card.selected .pkg-name')?.textContent||'Essential';
  const prices={Essential:15000,Premium:30000,Royal:55000};
  bookings.unshift({
    id:'BK'+(bookings.length+1).toString().padStart(3,'0'),
    client,type:document.getElementById('book-type').value,
    date:document.getElementById('book-date').value||'TBD',
    time:document.getElementById('book-time').value,
    location:document.getElementById('book-location').value||'TBD',
    photographer:document.getElementById('book-photo').value,
    pkg,amount:prices[pkg]||15000,status:'Pending'
  });
  renderBookings();closeModal('new-booking');showToast('Booking confirmed!');
  document.getElementById('book-client').value='';
}

function saveClient(){
  const first=document.getElementById('cl-first').value.trim();
  if(!first){showToast('Please enter a name');return;}
  clients.unshift({
    id:'CL'+(clients.length+1).toString().padStart(3,'0'),
    first,last:document.getElementById('cl-last').value,
    email:document.getElementById('cl-email').value,
    phone:document.getElementById('cl-phone').value,
    city:document.getElementById('cl-city').value,
    source:document.getElementById('cl-source').value,
    bookings:0,totalSpent:0
  });
  renderClients();closeModal('new-client');showToast('Client saved!');
  ['cl-first','cl-last','cl-email','cl-phone','cl-city'].forEach(id=>document.getElementById(id).value='');
}

function saveGallery(){
  const title=document.getElementById('gal-title').value.trim();
  if(!title){showToast('Please enter a gallery title');return;}
  galleries.unshift({
    id:'GAL'+(galleries.length+1).toString().padStart(3,'0'),
    title,client:document.getElementById('gal-client').value,
    photos:0,date:new Date().toISOString().split('T')[0],
    status:'Live',downloads:0,dl:document.getElementById('gal-dl').value
  });
  renderGalleries();closeModal('upload-gallery');showToast('Gallery created! Ready for uploads.');
}

function saveInvoice(){
  const client=document.getElementById('inv-client').value.trim();
  const amount=parseInt(document.getElementById('inv-amount').value)||0;
  if(!client||!amount){showToast('Please fill client and amount');return;}
  payments.unshift({
    id:'INV-'+(payments.length+1).toString().padStart(3,'0'),
    client,session:document.getElementById('inv-desc').value,
    amount,paid:0,due:document.getElementById('inv-due').value||'TBD',status:'Pending'
  });
  renderPayments();closeModal('new-invoice');showToast('Invoice sent to client!');
}

function saveReminder(){
  const client=document.getElementById('rem-client').value.trim();
  if(!client){showToast('Please enter a client');return;}
  reminders.unshift({
    type:document.getElementById('rem-type').value.split('(')[0].trim(),
    client,datetime:'Scheduled',
    channel:document.querySelector('#modal-new-reminder .method-btn.selected')?.textContent||'WhatsApp',
    msg:document.getElementById('rem-msg').value,status:'Scheduled'
  });
  renderReminders();closeModal('new-reminder');showToast('Reminder scheduled!');
}

function submitInquiry(){showToast('Inquiry received! Auto-reply sent from vipvisualeyes14@gmail.com');}

function fmtDate(d){
  if(!d||d==='TBD') return 'TBD';
  return new Date(d+'T00:00:00').toLocaleDateString('en-IN',{day:'numeric',month:'short',year:'numeric'});
}


// ── VISITING CARD ──
function updateCard(){
  const n1=document.getElementById('card-name1').value;
  const n2=document.getElementById('card-name2').value;
  const t=document.getElementById('card-title').value;
  const p1=document.getElementById('card-ph1').value;
  const p2=document.getElementById('card-ph2').value;
  const em=document.getElementById('card-email').value;
  const loc=document.getElementById('card-loc').value;
  const ig=document.getElementById('card-insta').value;
  document.querySelector('.card-names').innerHTML=`${n1}<br/>${n2}`;
  document.querySelector('.card-title-lbl').textContent=t;
  const rows=document.querySelectorAll('.card-detail-text');
  if(rows[0]) rows[0].innerHTML=`${p1}<br/>${p2}`;
  if(rows[1]) rows[1].textContent=em;
  if(rows[2]) rows[2].textContent=loc;
  if(rows[3]) rows[3].textContent=ig;
  showToast('Card updated!');
}

function shareWhatsApp(){
  const msg=encodeURIComponent(`👑 VIP VisualEye's Photography & Videography\n\n📸 Lokesh & Ajay — Photographers\n📞 97155 54025 / 9894283672\n✉ vipvisualeyes14@gmail.com\n📍 Ocheri, Ranipet\n📸 @vipvisualeyes\n\nBook your special session today!`);
  window.open(`https://wa.me/?text=${msg}`,'_blank');
}

function copyContact(){
  const txt=`VIP VisualEye's Photography & Videography\nLokesh & Ajay — Photographers\nPhone: 97155 54025 / 9894283672\nEmail: vipvisualeyes14@gmail.com\nLocation: Ocheri, Ranipet\nInstagram: @vipvisualeyes`;
  navigator.clipboard.writeText(txt).then(()=>showToast('Contact info copied!')).catch(()=>showToast('Copy: '+txt.substring(0,40)+'...'));
}

function downloadCard(){
  // Draw visiting card on canvas and download
  const cv=document.createElement('canvas');
  cv.width=1050; cv.height=600;
  const ctx=cv.getContext('2d');

  // Front side
  ctx.fillStyle='#0d0d0d';
  ctx.fillRect(0,0,525,600);
  // Gold triangles
  ctx.save();
  ctx.beginPath();ctx.moveTo(370,0);ctx.lineTo(525,0);ctx.lineTo(525,600);ctx.lineTo(200,600);ctx.closePath();
  const grd=ctx.createLinearGradient(370,0,525,600);
  grd.addColorStop(0,'#B8860B');grd.addColorStop(0.5,'#C9A84C');grd.addColorStop(1,'#8B6914');
  ctx.fillStyle=grd;ctx.globalAlpha=0.85;ctx.fill();ctx.restore();
  ctx.save();
  ctx.beginPath();ctx.moveTo(0,400);ctx.lineTo(160,400);ctx.lineTo(0,600);ctx.closePath();
  ctx.fillStyle='#C9A84C';ctx.globalAlpha=0.5;ctx.fill();ctx.restore();
  ctx.globalAlpha=1;
  // Logo text
  ctx.font='bold 72px Cinzel, serif';
  const grd2=ctx.createLinearGradient(160,220,365,300);
  grd2.addColorStop(0,'#C9A84C');grd2.addColorStop(0.5,'#F5E090');grd2.addColorStop(1,'#C9A84C');
  ctx.fillStyle=grd2;ctx.textAlign='center';ctx.fillText('VIP',262,310);
  ctx.font='16px Jost, sans-serif';ctx.fillStyle='#C0C0C0';ctx.letterSpacing='8px';ctx.fillText("VISUALEYE'S",262,345);
  ctx.font='11px Jost, sans-serif';ctx.fillStyle='#888';ctx.fillText('P H O T O G R A P H Y',262,368);

  // Back side
  ctx.fillStyle='#0d0d0d';ctx.fillRect(525,0,525,600);
  ctx.save();
  ctx.beginPath();ctx.moveTo(870,0);ctx.lineTo(1050,0);ctx.lineTo(1050,600);ctx.lineTo(700,600);ctx.closePath();
  ctx.fillStyle=grd;ctx.globalAlpha=0.85;ctx.fill();ctx.restore();
  ctx.globalAlpha=1;
  ctx.font='bold 28px Cinzel, serif';ctx.fillStyle='#ffffff';ctx.textAlign='left';
  const n1=document.getElementById('card-name1').value||'Lokesh';
  const n2=document.getElementById('card-name2').value||'Ajay';
  ctx.fillText(n1,560,110);ctx.fillText(n2,560,150);
  ctx.font='11px Jost, sans-serif';ctx.fillStyle='#C9A84C';ctx.letterSpacing='4px';ctx.fillText('PHOTOGRAPHERS',560,185);
  ctx.font='13px Jost, sans-serif';ctx.fillStyle='#ddd';ctx.letterSpacing='0px';
  const ph1=document.getElementById('card-ph1').value||'97155 54025';
  const ph2=document.getElementById('card-ph2').value||'9894283672';
  const em=document.getElementById('card-email').value||'vipvisualeyes14@gmail.com';
  const loc=document.getElementById('card-loc').value||'Ocheri, Ranipet';
  const ig=document.getElementById('card-insta').value||'@vipvisualeyes';
  ctx.fillText('📞  '+ph1+' / '+ph2,560,240);
  ctx.fillText('✉  '+em,560,275);
  ctx.fillText('📍  '+loc,560,310);
  ctx.fillText('📸  '+ig,560,345);

  const link=document.createElement('a');
  link.download='VIPVisualEyes_Card.png';
  link.href=cv.toDataURL('image/png');
  link.click();
  showToast('Card downloaded!');
}

// ── FRAMES ──
const FRAMES=[
  {id:'royal-gold',name:'Royal Gold',type:'Wedding / Portrait',colors:['#C9A84C','#F5E090','#8B6914'],style:'corner',digitalPrice:500,printPrice:1200},
  {id:'classic-black',name:'Classic Black',type:'All Events',colors:['#1a1a1a','#333','#C9A84C'],style:'border',digitalPrice:300,printPrice:800},
  {id:'diamond',name:'Diamond Crown',type:'Premium',colors:['#C0C0C0','#E8E8E8','#C9A84C'],style:'diamond',digitalPrice:600,printPrice:1500},
  {id:'floral-gold',name:'Floral Gold',type:'Wedding',colors:['#C9A84C','#F5E090','#fff'],style:'floral',digitalPrice:500,printPrice:1200},
  {id:'minimal-line',name:'Minimal Line',type:'Portrait',colors:['#C9A84C','#888','#111'],style:'minimal',digitalPrice:200,printPrice:600},
  {id:'event-bold',name:'Event Bold',type:'Events / Corporate',colors:['#111','#C9A84C','#F5E090'],style:'bold',digitalPrice:400,printPrice:1000},
];

let selectedFrame=FRAMES[0];
let uploadedImg=null;

// ── PRICE LIST DATA ──
let photoPkgs=[
  {name:'Essential',badge:'Starter',badgeColor:'badge-muted',price:15000,sub:'Per session',featured:false,items:['4 hours of coverage','200 edited photos','Online gallery','1 photographer — Lokesh or Ajay','Delivery in 7 days']},
  {name:'Premium',badge:'Popular',badgeColor:'badge-gold',price:30000,sub:'Per session',featured:true,items:['8 hours of coverage','500 edited photos','Online gallery + album','1 photographer','Teaser reel (30 sec)','Delivery in 7 days']},
  {name:'Royal',badge:'Full Day',badgeColor:'badge-silver',price:55000,sub:'Per session',featured:false,items:['Full day coverage','Unlimited edited photos','Album + canvas print','2 photographers','Full video highlight','Delivery in 10 days','Complimentary frame set']},
];

let videoPkgs=[
  {name:'Short Reel',badge:'Social Media',badgeColor:'badge-muted',price:8000,sub:'Up to 2 min',featured:false,items:['2–3 hours shoot','Edited reel (up to 2 min)','Background music','1 revision','Delivery in 5 days']},
  {name:'Highlight Film',badge:'Events',badgeColor:'badge-gold',price:20000,sub:'5–10 min film',featured:true,items:['Full event coverage','5–10 min highlight film','Cinematic editing','Background music + voiceover','2 revisions','Delivery in 7 days']},
  {name:'Cinematic Full',badge:'Wedding',badgeColor:'badge-silver',price:40000,sub:'Full film',featured:false,items:['Full day video coverage','Cinematic wedding film','Drone shots (if available)','Teaser + full film','Unlimited revisions','Delivery in 14 days']},
];

let addons=[
  {service:'Extra Hour',desc:'Additional coverage beyond package hours',price:2000},
  {service:'Printed Album',desc:'30–40 pages, premium quality',price:8000},
  {service:'Canvas Print',desc:'20×30 inch framed canvas',price:4500},
  {service:'Same-Day Teaser',desc:'5–10 edited photos on event day',price:3000},
  {service:'Drone Coverage',desc:'Aerial shots (subject to location)',price:5000},
  {service:'Photo Booth Setup',desc:'Props + instant prints for events',price:6000},
  {service:'USB Delivery',desc:'All photos on branded USB drive',price:1500},
];

// ── PRICE LIST RENDER ──
function renderPhotoPkgs(){
  document.getElementById('photo-pkg-grid').innerHTML=photoPkgs.map((p,i)=>`
    <div class="price-pkg${p.featured?' featured':''}">
      <div class="price-pkg-top">
        <span class="price-pkg-badge ${p.badgeColor}">${p.badge}</span>
        <div class="price-pkg-name">${p.name}</div>
        <div class="price-amt">₹${p.price.toLocaleString()}</div>
        <div class="price-amt-sub">${p.sub}</div>
      </div>
      <div class="price-pkg-body">
        ${p.items.map(it=>`<div class="price-item">${it}</div>`).join('')}
        <button class="btn-gold" style="width:100%;margin-top:1rem;font-size:0.72rem;" onclick="openModal('new-booking')">Book This Package</button>
      </div>
    </div>`).join('');
}

function renderVideoPkgs(){
  document.getElementById('video-pkg-grid').innerHTML=videoPkgs.map((p,i)=>`
    <div class="price-pkg${p.featured?' featured':''}">
      <div class="price-pkg-top">
        <span class="price-pkg-badge ${p.badgeColor}">${p.badge}</span>
        <div class="price-pkg-name">${p.name}</div>
        <div class="price-amt">₹${p.price.toLocaleString()}</div>
        <div class="price-amt-sub">${p.sub}</div>
      </div>
      <div class="price-pkg-body">
        ${p.items.map(it=>`<div class="price-item">${it}</div>`).join('')}
        <button class="btn-gold" style="width:100%;margin-top:1rem;font-size:0.72rem;" onclick="openModal('new-booking')">Book This Package</button>
      </div>
    </div>`).join('');
}

function renderAddons(){
  document.getElementById('addon-table').innerHTML=addons.map((a,i)=>`
    <tr>
      <td><strong>${a.service}</strong></td>
      <td style="color:var(--muted);">${a.desc}</td>
      <td class="price-tag">₹${a.price.toLocaleString()}</td>
      <td><button class="edit-price-btn" onclick="editAddonPrice(${i})">✏ Edit</button></td>
    </tr>`).join('');
}

function renderFramePriceTable(){
  document.getElementById('frame-price-table').innerHTML=FRAMES.map((f,i)=>`
    <tr>
      <td><strong>${f.name}</strong></td>
      <td style="color:var(--muted);font-size:0.78rem;">${f.type}</td>
      <td class="price-tag" id="fp-digital-${f.id}">₹${f.digitalPrice.toLocaleString()}</td>
      <td class="price-tag" id="fp-print-${f.id}">₹${f.printPrice.toLocaleString()}</td>
      <td style="display:flex;gap:0.35rem;">
        <button class="edit-price-btn" onclick="editFramePrice('${f.id}','digital')">✏</button>
        <button class="edit-price-btn" onclick="editFramePrice('${f.id}','print')">🖨</button>
      </td>
    </tr>`).join('');
}

function editAddonPrice(i){
  const a=addons[i];
  const newP=prompt(`Edit price for "${a.service}" (current: ₹${a.price}):`,a.price);
  if(newP&&!isNaN(newP)){addons[i].price=parseInt(newP);renderAddons();showToast('Price updated!');}
}

function editFramePrice(id,type){
  const f=FRAMES.find(x=>x.id===id);
  if(!f) return;
  const field=type==='digital'?'digitalPrice':'printPrice';
  const newP=prompt(`Edit ${type} price for "${f.name}" (current: ₹${f[field]}):`,f[field]);
  if(newP&&!isNaN(newP)){f[field]=parseInt(newP);renderFramePriceTable();renderFrameCards();showToast('Frame price updated!');}
}

function showTab(show,hide){
  document.getElementById(show).style.display='block';
  document.getElementById(hide).style.display='none';
}

function downloadPriceList(){
  // Build printable HTML price list
  const html=`<!DOCTYPE html><html><head><meta charset="UTF-8"/><title>VIP VisualEye's Price List</title>
  <style>body{font-family:Georgia,serif;background:#fff;color:#111;max-width:800px;margin:0 auto;padding:2rem;}
  h1{color:#C9A84C;font-size:2rem;text-align:center;margin-bottom:0.25rem;}
  .sub{text-align:center;color:#888;font-size:0.85rem;margin-bottom:2rem;}
  h2{color:#C9A84C;font-size:1.1rem;border-bottom:1px solid #e0c876;padding-bottom:0.4rem;margin:2rem 0 1rem;}
  table{width:100%;border-collapse:collapse;margin-bottom:1.5rem;font-size:0.88rem;}
  th{background:#0d0d0d;color:#C9A84C;padding:0.6rem 0.8rem;text-align:left;font-size:0.75rem;letter-spacing:0.08em;}
  td{padding:0.6rem 0.8rem;border-bottom:1px solid #eee;} .price{font-weight:700;color:#C9A84C;}
  .notes{background:#fafafa;border-left:3px solid #C9A84C;padding:1rem 1.25rem;font-size:0.82rem;color:#555;line-height:1.8;}
  @media print{body{padding:1rem;}}</style></head><body>
  <h1>👑 VIP VisualEye's Photography</h1>
  <div class="sub">Lokesh & Ajay — Photographers | 97155 54025 / 9894283672 | Ocheri, Ranipet<br/>vipvisualeyes14@gmail.com | @vipvisualeyes</div>
  <h2>📸 Photography Packages</h2>
  <table><tr><th>Package</th><th>Coverage</th><th>Inclusions</th><th>Price</th></tr>
  ${photoPkgs.map(p=>`<tr><td><strong>${p.name}</strong></td><td>${p.items[0]}</td><td>${p.items.slice(1).join(', ')}</td><td class="price">₹${p.price.toLocaleString()}</td></tr>`).join('')}
  </table>
  <h2>🎬 Videography Packages</h2>
  <table><tr><th>Package</th><th>Duration</th><th>Inclusions</th><th>Price</th></tr>
  ${videoPkgs.map(p=>`<tr><td><strong>${p.name}</strong></td><td>${p.sub}</td><td>${p.items.slice(1,3).join(', ')}</td><td class="price">₹${p.price.toLocaleString()}</td></tr>`).join('')}
  </table>
  <h2>✦ Add-Ons</h2>
  <table><tr><th>Service</th><th>Description</th><th>Price</th></tr>
  ${addons.map(a=>`<tr><td><strong>${a.service}</strong></td><td>${a.desc}</td><td class="price">₹${a.price.toLocaleString()}</td></tr>`).join('')}
  </table>
  <h2>🖼️ Photo Frame Prints</h2>
  <table><tr><th>Frame Style</th><th>Best For</th><th>Digital</th><th>Print</th></tr>
  ${FRAMES.map(f=>`<tr><td><strong>${f.name}</strong></td><td>${f.type}</td><td class="price">₹${f.digitalPrice.toLocaleString()}</td><td class="price">₹${f.printPrice.toLocaleString()}</td></tr>`).join('')}
  </table>
  <div class="notes">
  <strong>Terms & Notes:</strong><br/>
  ✦ 50% advance required to confirm booking<br/>
  ✦ Remaining payment due on delivery day<br/>
  ✦ Travel charges extra beyond 30 km from Ocheri, Ranipet<br/>
  ✦ Edited photos delivered within 7–10 working days<br/>
  ✦ Raw files not included unless specifically agreed<br/>
  ✦ GST applicable as per government norms
  </div>
  <script>window.onload=()=>window.print();<\/script>
  </body></html>`;
  const b=new Blob([html],{type:'text/html'});
  const u=URL.createObjectURL(b);
  window.open(u,'_blank');
  showToast('Price list opened — use Print/Save as PDF');
}

function sharePriceList(){
  const lines=['👑 *VIP VisualEye\'s Photography & Videography*','Lokesh & Ajay | Ocheri, Ranipet','','📸 *Photography Packages*'];
  photoPkgs.forEach(p=>lines.push(`• ${p.name}: ₹${p.price.toLocaleString()}`));
  lines.push('','🎬 *Videography Packages*');
  videoPkgs.forEach(p=>lines.push(`• ${p.name}: ₹${p.price.toLocaleString()}`));
  lines.push('','✦ *Add-Ons*');
  addons.forEach(a=>lines.push(`• ${a.service}: ₹${a.price.toLocaleString()}`));
  lines.push('','📞 97155 54025 / 9894283672','✉ vipvisualeyes14@gmail.com','📸 @vipvisualeyes');
  const msg=encodeURIComponent(lines.join('\n'));
  window.open(`https://wa.me/?text=${msg}`,'_blank');
}

function renderFrameCards(){
  document.getElementById('frames-grid').innerHTML=FRAMES.map(f=>`
    <div class="frame-card${f.id===selectedFrame.id?' active-frame':''}" onclick="selectFrame('${f.id}')" id="fc-${f.id}">
      <div class="frame-preview">
        <canvas id="prev-${f.id}" width="220" height="220"></canvas>
      </div>
      <div class="frame-label">
        <div>
          <div class="frame-name">${f.name}</div>
          <div class="frame-type">${f.type}</div>
          <div class="frame-price-tag">Digital ₹${f.digitalPrice.toLocaleString()} · Print ₹${f.printPrice.toLocaleString()}</div>
        </div>
        ${f.id===selectedFrame.id?'<span style="color:var(--gold);font-size:1rem;">✦</span>':''}
      </div>
    </div>`).join('');
  FRAMES.forEach(f=>drawFramePreview(f));
}

function drawFramePreview(f){
  const cv=document.getElementById('prev-'+f.id);
  if(!cv) return;
  const ctx=cv.getContext('2d');
  const w=220,h=220;
  ctx.clearRect(0,0,w,h);
  // Background
  ctx.fillStyle='#1a1a1a';ctx.fillRect(0,0,w,h);
  // Sample photo area
  ctx.fillStyle='#2a2a2a';ctx.fillRect(20,20,w-40,h-40);
  ctx.fillStyle='#333';ctx.font='28px serif';ctx.textAlign='center';ctx.fillText('📷',w/2,h/2+10);
  drawFrameOnCtx(ctx,w,h,f,1);
}

function drawFrameOnCtx(ctx,w,h,f,opacity){
  ctx.save();ctx.globalAlpha=opacity;
  const [c1,c2,c3]=f.colors;
  const bw=Math.round(w*0.045);

  if(f.style==='corner'){
    // Gold corner brackets
    const cs=Math.round(w*0.22);const lt=3;
    [[0,0,1,1],[w,0,-1,1],[0,h,1,-1],[w,h,-1,-1]].forEach(([x,y,sx,sy])=>{
      ctx.strokeStyle=c1;ctx.lineWidth=lt+1;ctx.beginPath();
      ctx.moveTo(x+sx*cs,y);ctx.lineTo(x,y);ctx.lineTo(x,y+sy*cs);ctx.stroke();
      ctx.strokeStyle=c2;ctx.lineWidth=lt-1;ctx.stroke();
    });
    // Bottom brand bar
    ctx.fillStyle='rgba(0,0,0,0.82)';ctx.fillRect(0,h-Math.round(h*0.15),w,Math.round(h*0.15));
    const grd=ctx.createLinearGradient(0,0,w,0);
    grd.addColorStop(0,c3);grd.addColorStop(0.5,c2);grd.addColorStop(1,c3);
    ctx.fillStyle=grd;ctx.font=`bold ${Math.round(w*0.055)}px Cinzel,serif`;ctx.textAlign='center';
    ctx.fillText("👑 VIP VisualEye's",w/2,h-Math.round(h*0.065));
    ctx.font=`${Math.round(w*0.032)}px Jost,sans-serif`;ctx.fillStyle='#aaa';
    ctx.fillText('PHOTOGRAPHY & VIDEOGRAPHY',w/2,h-Math.round(h*0.032));

  } else if(f.style==='border'){
    ctx.strokeStyle=c3;ctx.lineWidth=bw;ctx.strokeRect(bw/2,bw/2,w-bw,h-bw);
    ctx.strokeStyle=c1;ctx.lineWidth=1;ctx.strokeRect(bw+2,bw+2,w-bw*2-4,h-bw*2-4);
    ctx.fillStyle='rgba(0,0,0,0.85)';ctx.fillRect(0,h-Math.round(h*0.14),w,Math.round(h*0.14));
    ctx.fillStyle=c3;ctx.font=`bold ${Math.round(w*0.052)}px Cinzel,serif`;ctx.textAlign='center';
    ctx.fillText("👑 VIP VisualEye's",w/2,h-Math.round(h*0.055));
    ctx.font=`${Math.round(w*0.028)}px Jost,sans-serif`;ctx.fillStyle='#aaa';
    ctx.fillText('Photography',w/2,h-Math.round(h*0.022));

  } else if(f.style==='diamond'){
    // Silver + gold border with diamond cuts at corners
    ctx.strokeStyle=c1;ctx.lineWidth=4;ctx.strokeRect(4,4,w-8,h-8);
    ctx.strokeStyle=c3;ctx.lineWidth=1.5;ctx.strokeRect(10,10,w-20,h-20);
    const ds=14;
    [[4,4],[w-4,4],[4,h-4],[w-4,h-4]].forEach(([x,y])=>{
      ctx.fillStyle=c3;ctx.beginPath();
      ctx.moveTo(x,y-ds);ctx.lineTo(x+ds,y);ctx.lineTo(x,y+ds);ctx.lineTo(x-ds,y);ctx.closePath();ctx.fill();
    });
    ctx.fillStyle='rgba(0,0,0,0.8)';ctx.fillRect(0,h-Math.round(h*0.15),w,Math.round(h*0.15));
    const grd=ctx.createLinearGradient(0,0,w,0);grd.addColorStop(0,c1);grd.addColorStop(0.5,c2);grd.addColorStop(1,c1);
    ctx.fillStyle=grd;ctx.font=`bold ${Math.round(w*0.052)}px Cinzel,serif`;ctx.textAlign='center';
    ctx.fillText("👑 VIP VisualEye's",w/2,h-Math.round(h*0.06));
    ctx.font=`${Math.round(w*0.03)}px Jost,sans-serif`;ctx.fillStyle='#ccc';
    ctx.fillText('PHOTOGRAPHY',w/2,h-Math.round(h*0.025));

  } else if(f.style==='floral'){
    // Decorative floral corners using arcs
    const fc=Math.round(w*0.18);
    [[0,0],[w,0],[0,h],[w,h]].forEach(([x,y],i)=>{
      ctx.save();ctx.translate(x,y);
      if(i===1)ctx.scale(-1,1);if(i===2)ctx.scale(1,-1);if(i===3)ctx.scale(-1,-1);
      ctx.strokeStyle=c1;ctx.lineWidth=2;
      for(let a=0;a<5;a++){
        ctx.beginPath();ctx.arc(fc*0.3,fc*0.3,fc*0.25,0,Math.PI*2);
        ctx.globalAlpha=0.3+a*0.1;ctx.stroke();
      }
      ctx.restore();
    });
    ctx.globalAlpha=opacity;
    ctx.fillStyle='rgba(0,0,0,0.8)';ctx.fillRect(0,h-Math.round(h*0.15),w,Math.round(h*0.15));
    const grd=ctx.createLinearGradient(0,0,w,0);grd.addColorStop(0,c1);grd.addColorStop(0.5,c2);grd.addColorStop(1,c1);
    ctx.fillStyle=grd;ctx.font=`bold ${Math.round(w*0.05)}px Cinzel,serif`;ctx.textAlign='center';
    ctx.fillText("🌸 VIP VisualEye's",w/2,h-Math.round(h*0.06));
    ctx.font=`${Math.round(w*0.028)}px Jost,sans-serif`;ctx.fillStyle='#ccc';
    ctx.fillText('Photography & Videography',w/2,h-Math.round(h*0.025));

  } else if(f.style==='minimal'){
    ctx.strokeStyle=c1;ctx.lineWidth=1.5;
    ctx.strokeRect(10,10,w-20,h-20);
    const ml=Math.round(w*0.08);
    ctx.beginPath();ctx.moveTo(10+ml,h-Math.round(h*0.14));ctx.lineTo(w-10-ml,h-Math.round(h*0.14));ctx.stroke();
    ctx.fillStyle='rgba(0,0,0,0.75)';ctx.fillRect(0,h-Math.round(h*0.13),w,Math.round(h*0.13));
    ctx.fillStyle=c1;ctx.font=`${Math.round(w*0.045)}px Cinzel,serif`;ctx.textAlign='center';
    ctx.fillText("VIP VisualEye's Photography",w/2,h-Math.round(h*0.04));

  } else if(f.style==='bold'){
    // Bold top + bottom bars
    const bh=Math.round(h*0.12);
    ctx.fillStyle='rgba(0,0,0,0.9)';ctx.fillRect(0,0,w,bh);ctx.fillRect(0,h-bh,w,bh);
    const grd=ctx.createLinearGradient(0,0,w,0);grd.addColorStop(0,c2);grd.addColorStop(0.5,c3);grd.addColorStop(1,c2);
    ctx.fillStyle=grd;ctx.font=`bold ${Math.round(w*0.052)}px Cinzel,serif`;ctx.textAlign='center';
    ctx.fillText("👑 VIP VisualEye's",w/2,bh*0.7);
    ctx.font=`${Math.round(w*0.048)}px Cinzel,serif`;ctx.fillStyle=c2;
    ctx.fillText('Photography',w/2,h-Math.round(bh*0.28));
    ctx.strokeStyle=c2;ctx.lineWidth=1.5;
    ctx.strokeRect(3,bh+3,w-6,h-bh*2-6);
  }
  ctx.restore();
}

function selectFrame(id){
  selectedFrame=FRAMES.find(f=>f.id===id)||FRAMES[0];
  renderFrameCards();
  const nameEl=document.getElementById('selected-frame-name');
  const priceEl=document.getElementById('selected-frame-price');
  if(nameEl) nameEl.textContent=selectedFrame.name;
  if(priceEl) priceEl.textContent='₹'+selectedFrame.digitalPrice.toLocaleString();
  if(uploadedImg) applyFrame();
}

function loadPhoto(e){
  const file=e.target.files[0];
  if(!file) return;
  const reader=new FileReader();
  reader.onload=ev=>{
    const img=new Image();
    img.onload=()=>{
      uploadedImg=img;
      document.getElementById('canvas-area').style.display='block';
      applyFrame();
      showToast('Photo loaded! Select a frame.');
    };
    img.src=ev.target.result;
  };
  reader.readAsDataURL(file);
}

function applyFrame(){
  if(!uploadedImg) return;
  const cv=document.getElementById('frame-canvas');
  const ctx=cv.getContext('2d');
  const size=800;
  cv.width=size;cv.height=size;
  // Draw photo (cover fit)
  const iw=uploadedImg.width,ih=uploadedImg.height;
  const scale=Math.max(size/iw,size/ih);
  const sw=iw*scale,sh=ih*scale;
  const ox=(size-sw)/2,oy=(size-sh)/2;
  ctx.drawImage(uploadedImg,ox,oy,sw,sh);
  // Draw frame
  const op=parseInt(document.getElementById('frame-opacity').value)/100;
  drawFrameOnCtx(ctx,size,size,selectedFrame,op);
}

function downloadFramed(){
  if(!uploadedImg){showToast('Please upload a photo first');return;}
  const cv=document.getElementById('frame-canvas');
  const link=document.createElement('a');
  link.download=`VIPVisualEyes_${selectedFrame.name.replace(/\s/g,'_')}.jpg`;
  link.href=cv.toDataURL('image/jpeg',0.95);
  link.click();
  showToast('Framed photo downloaded!');
}

function shareFramed(){
  if(!uploadedImg){showToast('Please upload a photo first');return;}
  showToast('Sharing — use Download then send via WhatsApp');
}

renderBookings();renderGalleries();renderPayments();renderClients();renderReminders();renderInquiries();renderMiniCal();renderFrameCards();renderPhotoPkgs();renderVideoPkgs();renderAddons();renderFramePriceTable();

document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));

if (APP_MODE === "admin") {
  document.getElementById("page-dashboard").classList.add("active");
} else {
  document.getElementById("page-booking").classList.add("active");
}
</script>
</body>
</html>