import sqlite3
import os
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('QA.db')
        cur = con.cursor()
        cur.execute("create table IF NOT EXISTS QuestionAnswer (id int, question text, answer text)")
        count = 0
        for filename in os.listdir(r"Database_chatbot"):
            if filename.endswith(".bin"):
                with open(r'Database_chatbot'+'\\'+filename, 'r', encoding='utf-8-sig') as file_parser:
                    for line in file_parser.readlines():
                        if not line:
                            break
                        else:
                            print(line)
                            a = line.split('\\')
                            count += 1
                            print(a)
                            cur.execute("insert into QuestionAnswer values ("+str(count)+",'"+a[0]+"', '"+a[1]+"')")
                            con.commit()
        return con
    except Error:
        print(Error)


if __name__ == '__main__':
    sql_connection()
