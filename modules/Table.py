class Table:
    def __init__(self, table_name, table_type, multi_files, file_path, insert_query):
        self.table_name = table_name
        self.table_type = table_type
        self.multi_files = multi_files
        self.file_path = file_path
        self.insert_query = insert_query

    def __str__(self):
        return f"Table: {self.table_name}, Type: {self.table_type}, Multi_files: {self.multi_files}, File: {self.file_path}, Query: {self.insert_query}"

