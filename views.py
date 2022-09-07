#Import Sqlite
import sqlite3 as lite

#CRUD
#C = criar/inserir
#R = acessar/mostrar as informações
#U = atualizar
#D = deletar

#criando conexão
con = lite.connect('dados.db')


#Inserir informações (create)
def inseririnfo(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, sobre) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)


#Acessar informações
def mostrarinfo():
    lista=[]
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
    return lista 
    


    

def atualizarinfo(i):
    
    #Atualizar Informação
    with con:
        cur = con.cursor()
        query = "UPDATE  formulario  SET nome=?, email=?, telefone=?,dia_em=?, estado=?, sobre=?  WHERE id=?"
        cur.execute(query,i)

#Deletar
def delete(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)
