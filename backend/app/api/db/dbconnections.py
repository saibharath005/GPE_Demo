from urllib.parse import quote
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Sancus Connection Parameters
# user_name="sancusadmin@sancus-core-db"
# user_password= "Tredence@123"
# host_name="sancus-core-db.mysql.database.azure.com"
# port_number="3306"
# schema_name = "GPE_DEV"

# Local Connection Parameters
user_name="test"
user_password= "Tredence@123"
host_name="20.98.64.154"
port_number="3306"
schema_name = "GPE_DEV"

def get_db_connection():
    """
    This method is used to create MySQL Database Connections
    """

    engine_conf = f"mysql+pymysql://{user_name}:%s@{host_name}:{port_number}/{schema_name}" % quote(user_password)
    engine = db.create_engine(engine_conf)
    # session = sessionmaker(bind=engine)
    # session = session()

    return engine

def get_sql_df(query):
    """
    This method is used to execute MySQL DB  Queries
    """
    engine = get_db_connection()

    temp_df = pd.read_sql_query(query, engine)

    return temp_df

def put_sql_df(temp_df,table_name):
    """
    This method is used to execute MySQL DB  Queries
    """
    engine = get_db_connection()

    temp_df.to_sql(table_name, con=engine,if_exists='append',chunksize=16000, index=False)

    return "Success"

def sql_query_executor(query):
    """
    This method is used to execute MySQL DB  Queries
    """
    engine = get_db_connection()
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.execute(query)
    session.commit()
    session.close()

    return "Success"
