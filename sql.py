import sqlite3

class BookReg():
    def __init__(self):
        self.connect = sqlite3.connect("bookreg.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            ('''CREATE TABLE IF NOT EXISTS
             book_reg(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                book TEXT NOT NULL,
                due REAL NOT NULL
             )
            
            ''')
        )
        self.connect.commit()
    
    def add_book(self, user, book, due):
        self.cursor.execute(
            '''INSERT INTO book_reg VALUES(NULL, ?, ?, ?)''', (user, book, due)
        )
        self.connect.commit()
    
    def del_book(self, user, book):
        self.cursor.execute(
            """DELETE FROM book_reg WHERE user = '{user}' AND book = 
            '{book}'""".format(user=user, book=book)
        )
        self.connect.commit()

    def get_books(self, user):
        self.cursor.execute(
            "SELECT book FROM book_reg WHERE user = '{user}'".format(user=user)
        )
        return self.cursor.fetchall()
    

