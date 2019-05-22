import sqlite3
from utils.constants import Constants


class DBManager:
    DB_NAME = Constants.DB_NAME

    @classmethod
    def get_salt(cls, username):
        conn = Constants.DB_ENIGNE.connect(cls.DB_NAME)
        cursor = conn.cursor()

        query = """
        SELECT salt FROM Users
        WHERE username = ?;
        """

        cursor.execute(query, (username, ))
        salt = cursor.fetchone()

        conn.close()
        return salt[0] if salt else None

    @classmethod
    def check_if_user_exists(cls, username):
        conn = sqlite3.connect(cls.DB_NAME)
        cursor = conn.cursor()

        query = """
        SELECT username FROM Users
        WHERE username = ?;
        """

        cursor.execute(query, (username, ))
        user = cursor.fetchone()

        conn.close()
        return user[0] if user else None

    @classmethod
    def get_id_by_name(cls, username):
        conn = sqlite3.connect(cls.DB_NAME)
        cursor = conn.cursor()

        query = """
        SELECT id FROM Users
        WHERE username = ?;
        """

        cursor.execute(query, (username, ))
        user_id = cursor.fetchone()

        conn.close()
        return user_id[0] if user_id else None

    @classmethod
    def find_user(cls, username, password):
        conn = sqlite3.connect(cls.DB_NAME)
        cursor = conn.cursor()

        doctor_query = """\
        SELECT status, username, password, salt, doctor_type FROM Users
            INNER JOIN Doctors
                ON Users.id = Doctors.user_id
        WHERE username = ? AND password = ?;
        """

        patient_query = """\
        SELECT status, username, password, salt, age, address FROM Users
            INNER JOIN Patients
                ON Users.id = Patients.user_id
        WHERE username = ? AND password = ?;
        """

        cursor.execute(doctor_query, (username, password))
        doctor = cursor.fetchone()
        if not doctor:
            cursor.execute(patient_query, (username, password))
            patient = cursor.fetchone()

        conn.close()
        return doctor if doctor else patient

    @classmethod
    def add_user(cls, user_type, *user_data):
        conn = sqlite3.connect(cls.DB_NAME)
        cursor = conn.cursor()

        username = user_data[0]
        password = user_data[1]
        salt = user_data[2]

        query = """\
        INSERT INTO Users(status, username, password, salt)
            VALUES(?, ?, ?, ?);
        """

        cursor.execute(query, (user_type, username, password, salt))
        conn.commit()

        user_id = cls.get_id_by_name(username)

        if user_type == Constants.DOCTOR_STR:
            cls.add_doctor(cursor, user_id, *user_data[3:])
        else:
            cls.add_patient(cursor, user_id, *user_data[3:])

        conn.commit()
        conn.close()

    @classmethod
    def add_doctor(cls, curosr, user_id, *data):
        query = """\
        INSERT INTO Doctors(user_id, doctor_type)
            VALUES(?, ?);
        """

        curosr.execute(query, (user_id, *data))

    @classmethod
    def add_patient(cls, curosr, user_id, *data):
        query = """\
        INSERT INTO Patients(user_id, age, address)
            VALUES(?, ?, ?);
        """

        curosr.execute(query, (user_id, *data))


if __name__ == "__main__":
    print(DBManager.check_if_user_exists('kam'))
