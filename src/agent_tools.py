import sqlite3

def list_databases() -> list[str]:
    pass

def list_tables(database: str, schema: str = "public") -> list[TableInfo]:
    pass

def get_table_schema(database: str, table: str) -> TableSchema:
    pass

def search_schema(database: str, query: str, top_k: int = 5) -> list[SchemaMatch]:
    pass

def get_foreign_keys(database:str, table: str) -> list[ForeignKey]:
    pass
