import sqlite3
conn = sqlite3.connect('licence_plate.db')

c = conn.cursor()

#c.execute('CREATE TABLE licence_plate (id integer,plates text)')

#c.execute("INSERT INTO licence_plate VALUES (1,'CZ20FSE')")

# number_plate = [
#     (2,'DL8CAF5030'),
#     (3,'B58BPS'),
#     (4,'HR26DK8337'),
#     (5,'YX38590'),
#     (6,'KWI3MXR'),
#     (7,'COVID19'),
#     (8,'KA05NB1786'),
#     (9,'MH20DV2366'),
#     (10,'XYZABC19'),]
# c.executemany("INSERT INTO licence_plate VALUES (?,?)", number_plate)

c.execute("SELECT * FROM licence_plate")
print(c.fetchall())

conn.commit()

conn.close()