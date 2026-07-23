import sqlite3
c = sqlite3.connect('tamheed.db')
c.row_factory = sqlite3.Row
for r in c.execute("SELECT * FROM student_signals ORDER BY id"):
    print(dict(r))