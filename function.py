import mysql.connector
from fastapi import HTTPException

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pashabd"
    )

def getdata():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM userinfo")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    formatted_data = []
    for row in results:
        data_item = {
            "id": row[0],
            "name": row[1],
            "username": row[2],
            "password": row[3]
        }
        formatted_data.append(data_item)
    return formatted_data

def insert_data_into_table(name, UserName, Password):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO `userinfo` (`name`, `UserName`, `Password`) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (name, UserName, Password))
        connection.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
    finally:
        cursor.close()
        connection.close()

def fetch_data_from_user_id(UserID):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT `UserID`, `name`, `UserName`, `Password` FROM `userinfo` WHERE UserID = %s"
    try:
        cursor.execute(query, (UserID,))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        formatted_data = []
        for row in results:
            data_item = {
                "id": row[0],
                "name": row[1],
                "username": row[2],
                "password": row[3]
            }
            formatted_data.append(data_item)
        return formatted_data
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Database error: {err}")
