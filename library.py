import sqlite3

from cloudinary import Search

connection = sqlite3.connect('library.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS library(
    ISBN INTEGER PRIMARY KEY,
    Titel TEXT NOT NULL,
    Jahr INTEGER NOT NULL,
    Beschreibung TEXT NOT NULL,
    Verlag TEXT NOT NULL,
    Menge INTEGER NOT NULL)
''')
connection.commit()
"""cursor.execute('''INSERT INTO library (ISBN, Titel, Jahr, Beschreibung, Verlag, Menge) 
                  VALUES (?, ?, ?, ?, ?, ?)''',
               (9780132350884, 'Clean Code', 2008, 'A Handbook of Agile Software Craftsmanship', 'Springer', 10))
cursor.execute('''INSERT INTO library (ISBN, Titel, Jahr, Beschreibung, Verlag, Menge) 
                  VALUES (?, ?, ?, ?, ?, ?)''',
               (9781491950357, 'The Pragmatic Daten Programmer', 1999, 'Your Journey to Mastery', 'Addison-Wesley', 5))
cursor.execute('''INSERT INTO library (ISBN, Titel, Jahr, Beschreibung, Verlag, Menge) 
                  VALUES (?, ?, ?, ?, ?, ?)''',
               (9781449331818, 'Learning Python', 2013, 'Powerful Object-Oriented Programming', "O'Reilly Media", 7))
cursor.execute('''INSERT INTO library (ISBN, Titel, Jahr, Beschreibung, Verlag, Menge) 
                  VALUES (?, ?, ?, ?, ?, ?)''',
               (9780321125217, 'Design Patterns', 1994, 'Elements of Reusable Object-Oriented Software', 'Addison-Wesley', 3))
cursor.execute('''INSERT INTO library (ISBN, Titel, Jahr, Beschreibung, Verlag, Menge) 
                  VALUES (?, ?, ?, ?, ?, ?)''',
               (9780131103627, 'The C Programming Language', 1978, 'The definitive guide to C programming', 'Prentice Hall', 2))"""

cursor.execute("SElECT Titel from library where Titel LIKE '%Daten%'")
cursor.execute("SELECT * from library where Verlag = 'Springer'")
cursor.execute("SELECT * from library where Menge < 3")
connection.commit()
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()