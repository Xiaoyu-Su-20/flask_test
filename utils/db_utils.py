from sqlalchemy import create_engine
import pandas as pd

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://rcAprimaDB:YAKBmWXTU8#2@rcaprimadb.database.windows.net/RC-BI-Data?driver=ODBC Driver 17 for SQL Server"


conn = create_engine(SQLALCHEMY_DATABASE_URI)

def pandas_read_sql(query, params=[]):
    if not params:
        df = pd.read_sql(query, conn)
    else:
        df = pd.read_sql(query, conn, params=params)

    return df

def get():
    try:
        query = "SELECT TOP 10 * FROM whoop"
        df = pandas_read_sql(query)
    except:
        df = pd.DataFrame([['No Database Connection']])
    return df