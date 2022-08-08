from sqlalchemy import MetaData


class TableDict:
    def __init__(self, engine, schema):  # 获取对应schema的所有table
        metadata = MetaData(bind=engine, schema=schema)  # 传给了bind参数，也能写成bind=metadata
        metadata.reflect()
        self.engine = engine
        self.schema = schema
        self.tables = metadata.tables

    def get_table(self, table_name):
        table = self.tables['{schema}.{table_name}'.format(schema=self.schema, table_name=table_name)]
        return table


if __name__ == '__main__':
    pass
