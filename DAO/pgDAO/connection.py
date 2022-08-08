from sqlalchemy import create_engine


class Connection:
    def __init__(self, dialect='postgresql', driver='', username='postgres', password='123456', host='localhost',
                 port='5432', database='osiris'):
        self.config = {
            'dialect': dialect,
            'driver': '+' + driver if driver else driver,
            'username': username,
            'password': password,
            'host': host,
            'port': port,
            'database': database
        }

    def connect(self):
        connURL = '{dialect}{driver}://{username}:{password}@{host}:{port}/{database}'.format(
            dialect=self.config['dialect'],
            driver=self.config['driver'],
            username=self.config['username'],
            password=self.config['password'],
            host=self.config['host'],
            port=self.config['port'],
            database=self.config['database']
        )

        init_engine = create_engine(connURL)  # postgresql://postgres:123456@localhost:5432/osiris
        init_engine.connect()  # 是不是可以去掉
        return init_engine


conn = Connection()
engine = conn.connect()


if __name__ == '__main__':
    pass
