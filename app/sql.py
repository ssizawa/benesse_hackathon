import mysql.connector as mysql
import sqlalchemy as db
import datetime

# *****************
# 初期設定
# *****************
dt_now = datetime.datetime.now()
user_name = "izawa"
password = "izawa"
host = "database"  # docker-composeで定義したMySQLのサービス名
database_name = "tasks_db"
conn = mysql.connect(
    host="database",
    user="izawa",
    passwd="izawa",
    port=3306,
    database="tasks_db",
    buffered = True
)

class sql_arg:
    def get_user(self, name, password):
        conn.ping(reconnect = True)
        cur = conn.cursor()
        sql = "select password, point from User where name='"+str(name)+"'"
        cur.execute(sql)
        result_pass = cur.fetchall()
        return result_pass

    def insert_user(self, name, password):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        # print(values[1])
        sql = "insert into User (name, password) VALUE ( '"+str(name)+ "' , '" + str(password) + "'" + ")"
        # print(sql)
        cur.execute(sql)
        conn.commit()

    def get_form_vec(self, name):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        sql = "select name, question1, question2, question3, question4, question5, question6, question7 from User where name !='"+str(name)+"'"
        cur.execute(sql)
        form_vec = cur.fetchall()
        return form_vec

    def get_movie(self):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        sql = "select * from Movie"
        cur.execute(sql)
        movie = cur.fetchall()
        return movie

    def get_like_user(self, name):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        sql = "select title, rating from User_info where pic ='"+str(name)+"'"
        cur.execute(sql)
        form_vec = cur.fetchall()
        return form_vec

    def get_like_movie(self, title):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        sql = "select title, caption, teather, price, img from Movie where title ='"+str(title)+"'"
        cur.execute(sql)
        like_movie = cur.fetchall()
        return like_movie

    def update_form(self, name, q1, q2, q3, q4, q5, q6, q7):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        sql = "update User set question1='"+q1+"', question2='"+q2+"', question3='"+q3+"', question4='"+q4+"', question5='"+q5+"', question6='"+q6+"', question7='"+q7+"' where name='"+str(name)+"'"
        cur.execute(sql)
        conn.commit()

    def update_point(self, new_point, name):
        conn.ping(reconnect=True)
        cur = conn.cursor() 
        sql = "update User set point='"+str(new_point)+"' where name='"+str(name)+"'"
        cur.execute(sql)
        conn.commit()

    