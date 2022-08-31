from sqlalchemy.orm import Session


class Crud:  # 大部分是原子化的crud操作
    def __init__(self, engine):  # 获取对应数据库连接
        self.engine = engine

    def insert(self, table_instance):
        session = Session(bind=self.engine)
        try:
            session.add(table_instance)
            session.commit()
        except Exception:
            print('插入数据时发生异常')
            session.rollback()
        finally:
            session.close()

    def insert_batch(self, *table_instance_list):
        session = Session(bind=self.engine)
        try:
            session.add_all(table_instance_list)
            session.commit()
        except Exception:
            print('插入多条数据时发生异常')
            session.rollback()
        finally:
            session.close()

    def insert_list(self, table_instance_list):
        session = Session(bind=self.engine)
        try:
            session.add_all(table_instance_list)
            session.commit()
        except Exception:
            print('插入多条数据时发生异常')
            session.rollback()
        finally:
            session.close()

    def select(self, table_class, row_id):
        session = Session(bind=self.engine)
        try:
            session.query(table_class).filter(table_class.id == row_id).first()
        except Exception:
            print('查询数据时发生异常')
            session.rollback()
        finally:
            session.close()

    def update(self, table_class, row_id, table_instance):
        session = Session(bind=self.engine)
        try:
            session.query(table_class).filter(table_class.id == row_id).first().update(table_instance)
            session.commit()
        except Exception:
            print('更新数据时发生异常')
            session.rollback()
        finally:
            session.close()

    def delete(self, table_class, row_id):
        session = Session(bind=self.engine)
        try:
            session.query(table_class).filter(table_class.id == row_id).first().delete()
            session.commit()
        except Exception:
            print('删除数据时发生异常')
            session.rollback()
        finally:
            session.close()


if __name__ == '__main__':
    pass
