import sqlalchemy

def create_db_engine(connection_string):
    return sqlalchemy.create_engine(connection_string)

def execute_query(engine, query):
    with engine.connect() as connection:
        return connection.execute(query)
