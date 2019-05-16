import hashlib
import sqlite3
from itertools import product
from string import ascii_letters as letters, digits
from contextlib import contextmanager


class HashedMessagesManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

    def commit(self, msg, hash_func):
        self.cursor
        msg = ''.join(msg)
        query = """\
            INSERT INTO hashed_strings(message, encrypted_message)
            VALUES(?, ?);
        """
        self.cursor.execute(query, (msg, hash_func(msg)))


def generate_product(iterable, repeat):
    for i in range(1, repeat+1):
        for combination in product(iterable, repeat=i):
            yield combination

def make_it_secret(message):
    return hashlib.md5(message.encode()).hexdigest()


if __name__ == "__main__":
    DB_NAME = 'cipher_breaker.db'
    hashed_msg_manager = HashedMessagesManager(DB_NAME)
    
    with hashed_msg_manager:
        for item in generate_product(letters+digits, 5):
            hashed_msg_manager.commit(item, make_it_secret)
