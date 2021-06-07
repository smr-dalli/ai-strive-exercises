import db_interface as sql
import sqlite3
import pandas as pd

student_table = """CREATE TABLE student(
                           name char(20) NOT NULL,
                           surname char(20) NOT NULL,
                           id int NOT NULL PRIMARY KEY,
                           country char(20),
                           FOREIGN KEY(id) REFERENCES projects (st)
                           );
                         """

sql.sql_query(student_table)

sql.upload_data('student_table','./student.csv')

df = sql.pandas_select('select * from student_table')
print(len(df.name))
sql.close()
