import sqlite3

def find_patners(db,subject):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, subjects FROM users")
        users = cur.fetchall()
        partners = [u[0] for u in users if subject in u[1].split(",")]
    return partners