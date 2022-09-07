#For create database is necessarity run scripts

#Import Sqlite
import sqlite3 as lite
from tkinter.tix import INTEGER

#Criando conexão
con = lite.connect('dados.db')

#Create Table
#with abre e fecha o banco de dados.
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100), telefone VARCHAR(16), dia_em DATE, estado TEXT,sobre TEXT)")
    