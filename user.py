import sqlite3,uuid,bcrypt
class User():
    def __init__(self, name, email, password, subjects):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.subjects = subjects
    def register(db,name, email, password, subjects):
        user = User(name,email,password,subjects)
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO users(id, name, email, passworld, subjects) VALUES(?,?,?,?,?)
            """, (user.id,user.name,user.email,user.password,",".join(user.subjects)))
            conn.commit()
        return user
    def login(db,email,passworld):
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT id, name, passworld FROM users WHERE email = ?""",(email,))
            user = cur.fetchone()
            if user and bcrypt.checkpw(passworld.encode(),user[2]):
                return {"id":user[0], "name":user[1]}
            return None