import db_interface as sql
import sqlite3
import pandas as pd

projects_table = """CREATE TABLE projects(
                           name char(20) NOT NULL,
                           topic char(20) NOT NULL,
                           st int NOT NULL,
                           id int NOT NULL PRIMARY KEY,
                           grade float,
                           tch varchar(20) NOT NULL,
                           FOREIGN KEY(st) REFERENCES student (id) ON UPDATE RESTRICT,
                           FOREIGN KEY(tch) REFERENCES teachers (id) ON UPDATE RESTRICT
                           );
                         """

sql.sql_query(projects_table)


sql.upload_data('projects_table','./datasets/projects.csv')

df = sql.pandas_select('select * from projects_table')
print(df)
sql.close()
