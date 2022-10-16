from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class MySQLDatabase(Database):
    def __init__(self, host: str, port: int) -> None:
        self.host = host  # For future connection
        self.port = port  # For future connection

    def open(self) -> None:
        print(f"Success connect to remote MySQL database: {self.host}:{self.port}")

    def close(self) -> None:
        print(f"Success disconnect from MySQL database: {self.host}:{self.port}")


class SQLiteDatabase(Database):
    def __init__(self, path_to_database: str) -> None:
        self.path_to_database = path_to_database  # For future connection

    def open(self) -> None:
        print(f"Success connect to local SQLite database: {self.path_to_database}")

    def close(self) -> None:
        print(f"Success disconnect from local SQLite database: {self.path_to_database}")


class DatabaseProvider(ABC):
    @abstractmethod
    def provide_database(self) -> Database:
        pass


class MySQLDatabaseProvider(DatabaseProvider):
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def provide_database(self) -> Database:
        return MySQLDatabase(host=self.host, port=self.port)


class SQLLiteDatabaseProvider(DatabaseProvider):
    def __init__(self, path_to_database: str) -> None:
        self.path_to_database = path_to_database

    def provide_database(self) -> Database:
        return SQLiteDatabase(path_to_database=self.path_to_database)


def client_code(database_provider: DatabaseProvider) -> None:
    db = database_provider.provide_database()
    db.open()
    # Some business logics with a database ....
    db.close()


def main() -> None:
    client_code(database_provider=MySQLDatabaseProvider(host='127.0.0.1', port=3306))
    client_code(database_provider=SQLLiteDatabaseProvider(path_to_database='db/database.sqlite'))


if __name__ == '__main__':
    main()
