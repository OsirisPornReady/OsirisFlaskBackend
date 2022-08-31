from connection import Connection
from schema_tables_interface import SchemaTablesInterface
from table_crud_interface import TableCrudInterface

# 用实例化的形式定义各操作的好处是可以连接到不同的数据库并行操作，全局变量就不可以

pg_conn = Connection()
pg_conn = pg_conn.connect()
schema_user_tables = SchemaTablesInterface(pg_conn, 'schema_user')


def login():
    table_user = schema_user_tables.get_table('table_user')
    print(table_user)



if __name__ == '__main__':
    login()