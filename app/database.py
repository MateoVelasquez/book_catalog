"""
Database Manager

Provides a singleton class for managing the connection to the MongoDB database.
"""
import os
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure

class DatabaseManager:
    _instance = None

    def __new__(cls):
        """
        Create a new instance of DatabaseManager if it doesn't exist.

        Returns:
            DatabaseManager: The DatabaseManager instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_database()
        return cls._instance

    def _initialize_database(self):
        """
        Initializes the MongoDB database connection using the provided connection string and database name.

        Raises:
            ConnectionError: If unable to establish a connection to the MongoDB server.
        """
        try:
            connection_str = os.environ.get('MONGO_URL', "mongodb://localhost:27017/")
            db_name = os.environ.get("MONGO_DATABASE_NAME", "local")
            self.mongo_client = MongoClient(connection_str)
            self.database = self.mongo_client.get_database(db_name)
        except ConnectionFailure:
            raise ConnectionError("Failed to connect to the MongoDB server.")

    def get_database(self) -> Database:
        """
        Get the MongoDB database instance.

        Returns:
            Database: The MongoDB database instance.
        """
        return self.database


db_manager = DatabaseManager()