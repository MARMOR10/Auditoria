from urllib import request
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
import json
from urllib import response
import requests

root=Tk()
root.title("PRODUCTOS")
root.geometry("600x400")

miId=StringVar()
producto=StringVar()
description=StringVar()
price=StringVar()

def request_post():
    url='http://localhost:4000/products'  
    payload={'name':producto,'description':description, 'price':price}
    response =requests.post(url,json=payload)
    print(response.url)

    if response.status_code==200:
        print(response.content)
        
def request_put():
    print('actualizo')


def request_get():
    url='http://localhost:4000/products'   
    response = requests.get(url)
    print(response)

    if response.status_code==200:
        print(response.content)

    print('obtuvodtos')

def request_delete():
    print('elimino')

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	producto.set("")
	description.set("")
	price.set("")

tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0, y=140)
tree.column('#0',width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre del Producto", anchor=CENTER)
tree.heading('#2', text="Descripción", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text="Precio", anchor=CENTER)


e1=Entry(root, textvariable=miId)

l2=Label(root, text="Producto")
l2.place(x=50,y=10)
e2=Entry(root, textvariable=producto, width=50)
e2.place(x=120, y=10)

l3=Label(root, text="Descripción")
l3.place(x=50,y=40)
e3=Entry(root, textvariable=description)
e3.place(x=120, y=40)

l4=Label(root, text="Precio")
l4.place(x=50,y=70)
e4=Entry(root, textvariable=price, width=10)
e4.place(x=120, y=70)


b1=Button(root, text="Crear Producto", command=request_post)
b1.place(x=50, y=100)
b2=Button(root, text="Modificar Producto", command=request_put)
b2.place(x=180, y=100)
b3=Button(root, text="Mostrar Productos", command=request_get)
b3.place(x=320, y=100)
b4=Button(root, text="Eliminar Producto", command=request_delete)
b4.place(x=450, y=100)


root.mainloop()




