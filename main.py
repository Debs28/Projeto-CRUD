# importanto o Tkinter
from email.mime import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor, position
from tkcalendar import Calendar,DateEntry
from views import *


################# cores ###############
co0 = "#b877a8"  # roxo
co1 = "#b8008a"  # rosa escuro
co2 = "#ff3366"  # rosa claro
co3 = "#ffcc33"  # amarelo
co4 = "#ccff33"  #verde tela fundo
co5 = "#1f0441"   # azul escuro
co6 = "#fc1068"   # rosa
co7 = "##fb0c06"   # vermelha
co8 = "#feffff"  # branca
co9 =  "#403d3d"   # letra


#Criando janela

janela =Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co5)
janela.resizable(width=FALSE,height=FALSE)

#dividindo a tela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403,bg=co3, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403,bg=co5, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

#Criando Label
app_nome = Label(frame_cima,text='Formulário de Consultoria', anchor=NW, font=('Ivy 16 bold') ,bg=co1, fg=co8, relief='flat')
app_nome.place(x=10, y=20)

#Variavel tree global
global tree

#função inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    dtconsulta = e_consul.get()
    estado = e_estado.get()
    sobre = e_consobre.get()
     
    listainsert = [nome,email,telefone,dtconsulta,estado,sobre] 
    
    if nome == '':
        messagebox.showerror('Erro','O nome não pode ser vazio')
    else:
       inseririnfo(listainsert)
       messagebox.showinfo('SUCESSO','Os dados foram inseridos com sucesso!!')

       e_nome.delete(0, 'end')
       e_email.delete(0, 'end')
       e_tel.delete(0, 'end')
       e_consul.delete(0, 'end')
       e_estado.delete(0, 'end')
       e_consobre.delete(0, 'end')
       
    for widget in frame_direita.winfo_children():
        widget.destroy()   
    
    
    mostar()
 
 
 
#função atualizar      
def atualizar():
    
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = tree_lista[0]
        
        
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_consul.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_consobre.delete(0, 'end')    
        
        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_tel.insert(0, tree_lista[3])
        e_consul.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_consobre.insert(0, tree_lista[6])
       
       
    except IndexError:
        messagebox.showerror('ERRO', 'Selecione o dado na tabela!')    
        
        #função inserir
    def update():
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_tel.get()
        dtconsulta = e_consul.get()
        estado = e_estado.get()
        sobre = e_consobre.get()
        
        listainsert = [nome,email,telefone,dtconsulta,estado,sobre,valor_id] 
        
        if nome == '':
            messagebox.showerror('Erro','O nome não pode ser vazio')
        else:
            atualizarinfo(listainsert)
            messagebox.showinfo('SUCESSO','Os dados foram atualizados com sucesso!!')

            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_consul.delete(0, 'end')
            e_estado.delete(0, 'end')
            e_consobre.delete(0, 'end')
        
        for widget in frame_direita.winfo_children():
            widget.destroy() 
            mostar()  
        
    bt_confirmar = Button(frame_baixo,command=update,text='CONFIRMAR', width=10, font=('Ivy 9 bold') ,bg=co5, fg=co8, relief='raised', overrelief='ridge')
    bt_confirmar.place(x=105, y=370)
        
 
 #Função Deletar

def deletar():
      try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = [tree_lista[0]]
        
        delete(valor_id)
        messagebox.showinfo("SUCESSO", "Os dados foram deletados com sucesso!")
        
        for widget in frame_direita.winfo_children():
            widget.destroy()   
    
        mostar()
      except IndexError:
        messagebox.showerror('ERRO', 'Selecione o dado na tabela!')     
        
#Config Frame baixo

#Nome
lb_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10 bold') ,bg=co8, fg=co9, relief='flat')
lb_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo,width=45, justify='left' ,relief='solid')
e_nome.place(x=10, y=40)


#Email
lb_email = Label(frame_baixo,text='E-mail *', anchor=NW, font=('Ivy 10 bold') ,bg=co8, fg=co9, relief='flat')
lb_email.place(x=10, y=70)
e_email = Entry(frame_baixo,width=45, justify='left' ,relief='solid')
e_email.place(x=10, y=100)

#Telefone
lb_tel = Label(frame_baixo,text='Telefone *', anchor=NW, font=('Ivy 10 bold') ,bg=co8, fg=co9, relief='flat')
lb_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo,width=45, justify='left' ,relief='solid')
e_tel.place(x=10, y=160)

#DataConsulta
lb_dtconsul = Label(frame_baixo,text='Data Consulta *', anchor=NW, font=('Ivy 10 bold') ,bg=co8, fg=co9, relief='flat')
lb_dtconsul.place(x=10, y=190)
e_consul = DateEntry(frame_baixo,width=12, background= '#b877a8', foreground='white', borderwidth=2, year=2022)
e_consul.place(x=10, y=220)

#Estado
lb_estado = Label(frame_baixo,text='Estado da Consulta *', anchor=NW, font=('Ivy 10 bold') ,bg=co8, fg=co9, relief='flat')
lb_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo,width=20, justify='left' ,relief='solid')
e_estado.place(x=160, y=220)  

#ConsultaSobre
lb_consobre = Label(frame_baixo,text='Consulta Sobre *', anchor=NW, font=('Ivy 10 bold') ,bg=co8, fg=co9, relief='flat')
lb_consobre.place(x=15, y=260)
e_consobre = Entry(frame_baixo,width=45, justify='left' ,relief='solid')
e_consobre.place(x=10, y=290)

#Confg Botões
#Btn Inserir
bt_inserir = Button(frame_baixo,command=inserir,text='INSERIR', width=10, font=('Ivy 9 bold') ,bg=co2, fg=co8, relief='raised', overrelief='ridge')
bt_inserir.place(x=10, y=340)

#Btn Atualizar
bt_atualizar = Button(frame_baixo,command=atualizar,text='ATUALIZAR', width=10, font=('Ivy 9 bold') ,bg=co0, fg=co8, relief='raised', overrelief='ridge')
bt_atualizar.place(x=105, y=340)

#Btn Deletar
bt_deletar = Button(frame_baixo,command=deletar,text='DELETAR', width=10, font=('Ivy 9 bold') ,bg=co4, fg=co8, relief='raised', overrelief='ridge')
bt_deletar.place(x=190, y=340)

def mostar():
    
    global tree

    #Tabela
    lista = mostrarinfo()
            

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


mostar()
janela.mainloop() 