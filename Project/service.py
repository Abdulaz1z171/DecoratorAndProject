import psycopg2
import utils
db_params = {
    'host' : 'localhost',
    'database' : 'n42',
    'password' : 'temur_1336',
    'user' : 'postgres',
    'port': 5432
}


class DbConnect:
    def __init__(self,db_params):
        self.db_params = db_params
        self.conn = psycopg2.connect(**db_params)
    
    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur
    

    def __exit__(self,exc_tb,exc_type,exc_val):
        if self.conn and not self.conn.closed:
            self.conn.commit()
            self.conn.close()


def login():
    with DbConnect(db_params) as cur:
        user_name = input('Enter username! ')
        select_user = 'SELECT * FROM users;'
        cur.execute(select_user)
        for data in cur.fetchall():
            if user_name == data[1]:
                raw_password = input('Enter user password! ')
                hash_password = data[2]
                utils.check_password(raw_password, hash_password)
                if utils.check_password:
                    print('this operation was succesfull')
                else:
                    print('This password incorrect')
                    data[5] += 1
            

            else:
                print('This user not found')


login()
