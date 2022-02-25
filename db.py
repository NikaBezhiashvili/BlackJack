

import sqlite3

cursor = sqlite3.connect('database.db')


cursor.execute("""CREATE TABLE IF NOT EXISTS KRN_Players(
                    ID   integer Primary key autoincrement,
                    Nickname varchar2(20) not null,
                    Password varchar2(20) not null,
                    Balance number
                )""")

cursor.commit()