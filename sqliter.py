import sqlite3

class SQLighter:
    def __init__(self, database_file):
        self.connection=sqlite3.connect(database_file)
        self.cursor=self.connection.cursor()
    #def create_table(self):
      #  with self.connection:
      #      self.cursor.execute('create table if not exists users(user_id INT,status BOOLEAN)')
       #     self.connection.commit()

    def get_subsriptions(self,status=True):
        with self.connection:
            return self.connection.execute('select *from "subscriptions" where "status"=?',(status,)).fetchall()


    def subscriber_exists(self,user_id):
        with self.connection:
            result=self.cursor.execute('select *from "subscriptions" where "user_id"=?',(user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self,user_id,status=True):
        return self.cursor.execute('insert into  "subscriptions" ("user_id","status") values(?,?)',(user_id,status))

    def update_subscriber(self,user_id,status):
        return self.cursor.execute('update  "subscriptions" set "status"=? where "user_id" =?',(status,user_id))

    def close(self):
        self.connection.close()









