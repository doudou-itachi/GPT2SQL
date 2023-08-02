from langchain import SQLDatabase
from langchain.chains import SQLDatabaseSequentialChain
from langchain.chat_models import ChatOpenAI
from sqlalchemy import create_engine


class DataBaseConnect:
    def __init__(self, database_name: str, database_type: str, name: str, password: str, ipaddr: str):
        self.name = name
        self.password = password
        self.ip = ipaddr
        self.database_name = database_name
        self.database_type = database_type

    @property
    def get_database_uri(self) -> str:
        # connect mysql
        if str(self.database_type).lower() == "mysql":
            database_uri = f"{self.database_type.lower()}+pymysql://{self.name}:{self.password}@{self.ip}/{self.database_name}?charset=utf8mb4"
        # connect PostgreSQL
        elif str(self.database_type).lower() == "postgresql":
            database_uri = f"{self.database_type.lower()}+psycopg2://{self.name}:{self.password}@{self.ip}/{self.database_name}"
        # connect SQLite
        # Set the database URI for SQLite
        # The database file will be created in the same directory as your script.
        elif str(self.database_type).lower() == "sqlite":
            database_uri = f"sqlite:///{self.database_name}.db"
        else:
            # For other database types, use the SQLAlchemy engine to create the URI Adjust the database_type, driver,
            # and other connection parameters as needed. For example, to connect to a SQL Server database,
            # use the following format: database_uri = f"mssql+pyodbc://{self.name}:{self.password}@{self.ip}/{
            # self.database_name}?driver=ODBC Driver 17 for SQL Server" You may need to install additional
            # database-specific libraries and dependencies.
            engine = create_engine(f"{self.database_type}://{self.name}:{self.password}@{self.ip}/{self.database_name}")
            database_uri = engine.url
        return database_uri

    @property
    def get_connect(self) -> SQLDatabase:
        return SQLDatabase.from_uri(self.get_database_uri)

    def get_chain(self, llm: ChatOpenAI, return_intermediate_steps: bool = True) -> SQLDatabaseSequentialChain:
        return SQLDatabaseSequentialChain.from_llm(llm, self.get_connect, verbose=True,
                                                   return_intermediate_steps=return_intermediate_steps)

    def get_result(self, prompt: str, llm: ChatOpenAI) -> dict:
        return self.get_chain(llm)(prompt)
