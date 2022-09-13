import snowflake.connector

# Json'a çevirmeye çalış, ayrı method aç
from reader import sql_reader

PASSWORD = ...
USER = ...
ACCOUNT = ...
WAREHOUSE = ...
DATABASE = ...
SCHEMA = ...

print("Connecting...")
con = snowflake.connector.connect(
  user=USER,
  password=PASSWORD,
  account=ACCOUNT,
  warehouse=WAREHOUSE,
  database=DATABASE,
  schema=SCHEMA
)

x = sql_reader('deneme')

con.cursor().execute("USE WAREHOUSE " + WAREHOUSE)
con.cursor().execute("USE DATABASE " + DATABASE)
con.cursor().execute("USE SCHEMA " + SCHEMA)


try:
    user_result = con.cursor().execute("SELECT CURRENT_USER(), CURRENT_ROLE()")
    result = con.cursor().execute(x.query)
    result_list = result.fetch_pandas_all()

    print(result_list)

finally:
    con.cursor().close()

con.cursor().close()