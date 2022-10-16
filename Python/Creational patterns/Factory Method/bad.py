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


def client_code(database_type: str, connect_params: dict[str, str | int]) -> None:
    if database_type == 'MySQL':        # Branching in the code!!!
        db = MySQLDatabase(host=connect_params['host'], port=connect_params['port'])
    elif database_type == 'SQLite':
        db = SQLiteDatabase(path_to_database=connect_params['path'])
    # For support the new type database, you will have to add another check :(
    else:
        raise ValueError('Unknown database type')
    db.open()
    # Some business logics with a database ....
    db.close()


def main() -> None:
    client_code(database_type='MySQL', connect_params={'host': '127.0.0.1', 'port': 3306})
    client_code(database_type='SQLite', connect_params={'path': 'db/database.sqlite'})


if __name__ == '__main__':
    main()
