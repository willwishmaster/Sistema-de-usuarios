from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import pymysql

root = Tk() # crear el objeto de Tkinter
root.title("Sistema de usuarios v 1.0")
screen_width = root.winfo_screenwidth() # Obtiene el ancho de la pantalla actual
screen_height = root.winfo_screenheight() # Obtiene el alto de la pantalla actual
width = 1280 # Define el ancho de la ventana
height = 500 # # Define la altura de la ventana
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
print((screen_width/2), (screen_height/2), (width/2), (height/2))
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================FRAME==============================================
Top = Frame(root, width=1280, height=50, bd=1, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=2, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=900, height=500, bd=2, relief="raise")
Right.pack(side=RIGHT)
#==================================FORM FRAME==============================================
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)

Buttons = Frame(Left, width=300, height=100, bd=2, relief="raise" ,highlightbackground='green',highlightthicknes=3)
Buttons.pack(side=BOTTOM)

#==================================LABEL WIDGET=======================================

txt_title = Label(Top, width=900, font=('arial', 24), text = "Sistema de usuarios v 1.0")
txt_title.pack()

txt_firstname = Label(Forms, text="Nombre:", font=('arial', 16), bd=15)
txt_firstname.grid(row=0, sticky="e") # Pendiente
txt_apellido = Label(Forms, text="Apellido:", font=('arial', 16), bd=15)
txt_apellido.grid(row=1, sticky="e")
txt_gender = Label(Forms, text="Sexo:", font=('arial', 16), bd=15)
txt_gender.grid(row=2, sticky="e")
txt_address = Label(Forms, text="Direccion:", font=('arial', 16), bd=15)
txt_address.grid(row=3, sticky="e")
txt_username = Label(Forms, text="Usuário:", font=('arial', 16), bd=15)
txt_username.grid(row=4, sticky="e")
txt_password = Label(Forms, text="Contraseña:", font=('arial', 16), bd=15)
txt_password.grid(row=5, sticky="e")

#==================================ENTRY WIDGET=======================================
firstname = Entry(Forms, width=30)
firstname.grid(row=0, column=1)
lastname = Entry(Forms, width=30)
lastname.grid(row=1, column=1)
# RadioGroup.grid(row=2, column=1)
address = Entry(Forms, width=30)
address.grid(row=3, column=1)
username = Entry(Forms, width=30)
username.grid(row=4, column=1)
password = Entry(Forms, show="*", width=30)
password.grid(row=5, column=1)


if __name__ == '__main__':
    # Read()
    root.mainloop()