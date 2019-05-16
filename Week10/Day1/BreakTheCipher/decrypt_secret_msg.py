import sqlite3


def read_secret_message(filename):
    with open(filename) as secret_msg:
        for line in secret_msg.readlines():
            yield line.strip()

def decrypt_line(db_name, msg_line):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query ="""\
        SELECT message 
            FROM hashed_strings
        WHERE encrypted_message = ?
        
    """

    cursor.execute(query, (msg_line, ))
    decrypted_line = cursor.fetchone()
    
    conn.close()

    return decrypted_line[0] if decrypted_line else ''


if __name__ == "__main__":
    DB_NAME = 'cipher_breaker.db'
    SECRET_MSG = 'secret_message.txt'

    msg = ' '.join([decrypt_line(DB_NAME, line) 
              for line in read_secret_message(SECRET_MSG)])
    print(msg)
