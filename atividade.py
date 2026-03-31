import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.100",
    port=3309,
    user="root",
    password="root123"
    database="AnaLuiza"
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS analuiza_Isis_mariadias")
cursor.execute("CREATE TABLE USUARIO (id INT, username VARCHAR(255), email VARCHAR(50), senha VARCHAR(100), idade INT)")
id_INT = int(input("id"))
username = input("username")
email = input("email")
senha = input("senha")
idade = int(input("idade"))
