from snowflake.snowflake_operations import QueryOperations

def sql_reader(name: str):

    x = QueryOperations()
    x.query_filename = name

    QueryOperations.sql_reader(x)

    return x