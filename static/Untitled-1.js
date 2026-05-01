const API = "http://127.0.0.1:5000";

// Add Booking
document.getElementById("bookingForm").addEventListener("submit", function(e) {
    e.preventDefault();

    fetch(API + "/add-booking", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            phone: document.getElementById("phone").value,
            date: document.getElementById("date").value,
            package: document.getElementById("package").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert("Booking Added!");
        loadBookings();
    });
});

// Load Bookings
function loadBookings() {
    fetch(API + "/bookings")
    .then(res => res.json())
    .then(data => {
        const table = document.querySelector("#bookingTable tbody");
        table.innerHTML = "";

            data.forEach(b => {
    table.innerHTML += `
        <tr>
            <td>${b.name}</td>
            <td>${b.email}</td>
            <td>${b.phone}</td>
            <td>${b.date}</td>
            <td>${b.package}</td>

            <!-- STATUS DROPDOWN -->
            <td>
                <select onchange="updateStatus(${b.id}, this.value)">
                    <option ${b.status=="Pending"?"selected":""}>Pending</option>
                    <option ${b.status=="Confirmed"?"selected":""}>Confirmed</option>
                    <option ${b.status=="Paid"?"selected":""}>Paid</option>
                </select>
            </td>

            <!-- DELETE BUTTON -->
            <td>
                <button onclick="deleteBooking(${b.id})">Delete</button>
            </td>
        </tr>
    `;
        });
    });
}

// Load data when page opens
window.onload = loadBookings;

function uploadGallery() {
    let input = document.getElementById("galleryFiles");

    if (!input.files.length) {
        alert("Please select files first!");
        return;
    }

    let formData = new FormData();

    for (let i = 0; i < input.files.length; i++) {
        formData.append("files", input.files[i]);
    }

    fetch(API + "/upload", {   // 👈 uses your API variable
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        alert("Upload success!");
        console.log(data);

        // OPTIONAL: show images
        showGallery(data.files);
    })
    .catch(err => {
        console.error(err);
        alert("Upload failed!");
    });
}

function showGallery(files) {
    const container = document.getElementById("gallery-list");

    files.forEach(file => {
        container.innerHTML += `
            <div style="margin:10px; display:inline-block;">
                <img src="/static/uploads/${file}" width="150"><br>
                <a href="/static/uploads/${file}" download>Download</a>
            </div>
        `;
    });
}