CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    salt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    age INTEGER NOT NULL,
    address TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS Doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    doctor_type TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS Appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER,
    start_hour TEXT NOT NULL,
    end_hour TEXT NOT NULL,
    date TEXT NOT NULL,
    room INTEGER NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id)
);

CREATE TABLE IF NOT EXISTS ReservedAppointments(
    appointment_id INTEGER,
    patient_id INTEGER,
    status TEXT NOT NULL,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(id),
    FOREIGN KEY (patient_id) REFERENCES Patients(id)
);