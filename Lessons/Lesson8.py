###############################################################################
###  Pandas Tutorials - Lesson 8                                            ###
###############################################################################

# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/08%20-%20Lesson.ipynb

import pandas as pd
import pandas.io.sql
import pyodbc
from sqlalchemy import create_engine, MetaData, Table, select, engine

# Opening a SQL connection - Version 1 ##########################################

TableName = "data"

DB = {
    'drivername': 'mssql+pyodbc',
    'servername': 'DAVID-THINK',
    # 'port': '5432',
    # 'username': 'lynn',
    # 'password': '',
    'database': 'BizIntel',
    'driver': 'SQL Server Native Client 11.0',
    'trusted_connection': 'yes',
    'legacy_schema_aliasing': False
}

# Create the connection
engine = create_engine(DB['drivername'] + '://' + DB['servername'] + '/' +
                       DB['database'] + '?' + 'driver=' + DB['driver'] +
                       ';' + 'trusted_connection=' + DB['trusted_connection'],
                       legacy_schema_aliasing=DB['legacy_schema_aliasing'])
conn = engine.connect()

# Required for querying tables
metadata = MetaData(conn)

# Table to query
tbl = Table(TableName, metadata, autoload=True, schema='dbo')
# tbl.create(checkfirst=true)

# Select all
sql = tbl.select()

# Run the SQL query
result = conn.execute(sql)

# Insert result set to a dataframe
df = pd.DataFrame(data=list(result), columns=result.keys())

# Close the connection handle
conn.close()

print('Done')


# Open a SQL connection - Version 2 ###########################################

server = 'DAVID-THINK'
db = 'BizIntel'

# Create connection
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=' +
                      DB['servername'] + ';DATABASE=' + DB['database'] +
                      ';Trusted_Connection=yes')

# Specify query
sql = """

SELECT TOP 5 *
FROM data

"""

df = pandas.io.sql.read_sql(sql, conn)
df.head()


# Open a SQL connection - Version 3 ###########################################

ServerName = "DAVID-THINK"
Database = "BizIntel"
Driver = "driver=SQL Server Native Client 11.0"

# Create the engine
engine = create_engine('mysql+pyodbc://' +
                       ServerName + '/' + Database + '?' + Driver)

df = pd.read_sql_query("SELECT TOP 5 * FROM data", engine)


