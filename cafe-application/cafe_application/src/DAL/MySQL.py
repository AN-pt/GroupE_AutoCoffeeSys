from datetime import datetime
import mysql.connector
from mysql.connector import Error

class MySQL:
    def __init__(self):
        try:
            self.__connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Libraryofconf1d3nc4!",
                database="cafe_management"
            )
            self.__cursor = self.__connection.cursor()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def close(self):
        if self.__connection.is_connected():
            self.__cursor.close()
            self.__connection.close()

    def getConnection(self):
        return self.__connection

    def getCursor(self):
        return self.__cursor

    def executeQuery(self, query, *values) -> list:
        formatted_query = self.formatQuery(query, *values)
        print(formatted_query)
        result = []
        try:
            self.__cursor.execute(formatted_query)
            column_names = [desc[0] for desc in self.__cursor.description]
            for row in self.__cursor.fetchall():
                result.append(dict(zip(column_names, row)))
        except Error as e:
            print(f"Error while executing query: {e}")
        return result

    def executeUpdate(self, query, *values) -> int:
        formatted_query = self.formatQuery(query, *values)
        print(formatted_query)
        try:
            self.__cursor.execute(formatted_query)
            self.__connection.commit()
            return self.__cursor.rowcount
        except Error as e:
            print(f"Error while executing update: {e}")

    def formatQuery(self, query, *values) -> str:
        for value in values:
            if isinstance(value, str) or isinstance(value, datetime):
                string_value = f"'{value}'"
            elif isinstance(value, bool):
                string_value = "1" if value else "0"
            elif isinstance(value, int) or isinstance(value, float):
                string_value = str(value)
            else:
                string_value = f"'{str(value)}'"
            query = query.replace("?", string_value, 1)
        return query