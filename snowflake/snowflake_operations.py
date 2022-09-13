from dataclasses import dataclass

@dataclass
class QueryOperations:
    query_filename: str = None
    query: str = None

    def sql_reader(self):
        if self.query_filename:
            with open(f"sql/{self.query_filename}.sql", "r") as query_file:
                self.query = f"----{self.query_filename}----\n" + \
                    query_file.read()
        print(self.query)