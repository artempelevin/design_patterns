from typing import Optional


class SimpleSingletonClass:
    _instance: Optional["SimpleSingletonClass"] = None

    def __new__(cls, *args, **kwargs) -> "SimpleSingletonClass":
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance


class DatabaseSingletonClass:
    _db_connector: Optional["DatabaseSingletonClass"] = None
    database_url: str  # Object attributes have become class attributes

    def __new__(cls, database_url: str) -> "DatabaseSingletonClass":
        if not cls._db_connector:
            cls._db_connector = super().__new__(cls)
            cls.database_url = database_url

        return cls._db_connector

    def open(self) -> None:
        # Some business logics...
        ...

    def close(self) -> None:
        # Some business logics...
        ...


def main() -> None:
    simple_singleton_1 = SimpleSingletonClass()
    simple_singleton_2 = SimpleSingletonClass()
    assert simple_singleton_1 is simple_singleton_2

    db_1 = DatabaseSingletonClass(database_url='sqlite:///database.sqlite')
    db_2 = DatabaseSingletonClass(database_url='sqlite:///database.sqlite')
    assert db_1 is db_2


if __name__ == '__main__':
    main()
