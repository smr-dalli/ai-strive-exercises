import db_interface as sql

teachers_table = """CREATE TABLE teachers(
                            name varchar(20) NOT NULL,
                            surname varchar(20) NOT NULL,
                            id int NOT NULL PRIMARY KEY,
                            country char(20),
                            specality varchar(20) NOT NULL,
                            salary int,
                            FOREIGN KEY(id) REFERENCES projects(st)
                            );"""

sql.sql_query(teachers_table)
sql.upload_data('teachers_table','./datasets/teachers.csv')
df = sql.pandas_select('select * from teachers_table')
print(df)
sql.close()