class Config:
    SECRET_KEY = "hello"
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://rcAprimaDB:YAKBmWXTU8#2@rcaprimadb.database.windows.net/RC-BI-Data?driver=ODBC Driver 17 for SQL Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
