from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import pymysql

root = Tk() # crear el objeto de Tkinter
root.title("Sistema de usuarios v 1.0")
screen_width = root.winfo_screenwidth() # Obtiene el ancho de la pantalla actual
screen_height = root.winfo_screenheight() # Obtiene el alto de la pantalla actual
width = 1280 # Define el ancho de la ventana
height = 600 # # Define la altura de la ventana
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
print((screen_width/2), (screen_height/2), (width/2), (height/2))
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==========================VARIABLES REPRESENTAN LOS CUADROS DE TEXTO =================
CODIGO = StringVar()
NOMBRES = StringVar()
APELLIDOS = StringVar()
GENERO = StringVar()
DIRECCION = StringVar()
CELULAR = StringVar()
EMAIL = StringVar()


#==================================METHODS============================================

def Database():
    global conn, cursor # 
    #conn : Objeto que permite conectar a la BD
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'bdregistro')
    #cursor: Objeto que permite trabajar con los datos obtenidos de la BD
    cursor = conn.cursor()

#========================Cargar el tree con los datos de la BD=======================
    
def Load():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM estudiantes ORDER BY apellidos ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    cursor.close()
    conn.close()
    txt_result.config(text="Datos cargados correctamente.", fg="black")
    
def Insert():
    if  CODIGO.get() == "" or NOMBRES.get() == "" or APELLIDOS.get() == "" or GENERO.get() == "" or DIRECCION.get() == "" or CELULAR.get() == "" or EMAIL.get() == "":
        txt_result.config(text="Por favor completar los campos requeridos!", fg="red")
    else:
        Database()
        #cursor.execute("INSERT INTO `member` (firstname, lastname, gender, address, username, password) VALUES(?, ?, ?, ?, ?, ?)",
        cursor.execute("INSERT INTO `estudiantes` (codigo,nombres,apellidos, genero, direccion, celular, email) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                       (str(CODIGO.get()), str(NOMBRES.get()), str(APELLIDOS.get()), str(GENERO.get()), str(DIRECCION.get()), str(CELULAR.get()), str(EMAIL.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `estudiantes` ORDER BY `apellidos` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        conn.commit()
        CODIGO.set("")
        NOMBRES.set("")
        APELLIDOS.set("")
        GENERO.set("")
        DIRECCION.set("")
        CELULAR.set("")
        EMAIL.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Los datos fueron registrados!", fg="green")

def Actualizar():
    Database()
    if GENERO.get() == "":
        txt_result.config(text="Por favor, indique su genero", fg="red")
    else:
        tree.delete(*tree.get_children())
        # cursor.execute("UPDATE `estudiantes` SET `codigo` = %s WHERE `id` = %s", (str(CODIGO.get()), int(est_id)))
        
        cursor.execute("UPDATE `estudiantes` SET `codigo` = %s, `nombres` = %s, `apellidos` = %s, `genero` = %s, `direccion` = %s, `celular` = %s, `email` = %s WHERE `id` = %s",
                       (str(CODIGO.get()), str(NOMBRES.get()), str(APELLIDOS.get()), str(GENERO.get()), str(DIRECCION.get()), str(CELULAR.get()), str(EMAIL.get()), int(est_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `estudiantes` ORDER BY `apellidos` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        conn.commit()
        CODIGO.set("")
        NOMBRES.set("")
        APELLIDOS.set("")
        GENERO.set("")
        DIRECCION.set("")
        CELULAR.set("")
        EMAIL.set("")
        btn_create.config(state=NORMAL)
        btn_read.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="El registro fue actualizado!", fg="green")
        
def OnSelected(event):
    global est_id;
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    est_id = selecteditem[0]
    CODIGO.set("")
    NOMBRES.set("")
    APELLIDOS.set("")
    GENERO.set("")
    DIRECCION.set("")
    CELULAR.set("")
    EMAIL.set("")    
    CODIGO.set(selecteditem[1])
    NOMBRES.set(selecteditem[2])
    APELLIDOS.set(selecteditem[3])
    GENERO.set(selecteditem[4])
    DIRECCION.set(selecteditem[5])
    CELULAR.set(selecteditem[6])
    EMAIL.set(selecteditem[7])
    
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)

#==================================FRAME==============================================
Top = Frame(root, width=1280, height=50, bd=1, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=700, bd=2, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=900, height=700, bd=2, relief="raise")
Right.pack(side=RIGHT)
#==================================FORM FRAME==============================================
Forms = Frame(Left, width=300, height=700)
Forms.pack(side=TOP)
#==================================BUTTONS==============================================
Buttons = Frame(Left, width=300, height=100, bd=2, relief="raise")
Buttons.pack(side=BOTTOM)
#==================================RADIO BUTTONS==============================================
RadioGroup = Frame(Forms)
Male = Radiobutton(RadioGroup, text="Masculino", variable=GENERO, value="Masculino", font=('arial', 16)).pack(side=LEFT)
Female = Radiobutton(RadioGroup, text="Femenino", variable=GENERO, value="Femenino", font=('arial', 16)).pack(side=LEFT)


#,highlightbackground='green',highlightthicknes=3
#==================================LABEL WIDGET=======================================

txt_title = Label(Top, width=900, font=('arial', 24), text = "Sistema de usuarios v 1.0")
txt_title.pack()

txt_codigo = Label(Forms, text="Codigo:", font=('arial', 16), bd=15)
txt_codigo.grid(row=0, sticky="e") # Pendiente
txt_nombres = Label(Forms, text="Nombre:", font=('arial', 16), bd=15)
txt_nombres.grid(row=1, sticky="e") # Pendiente
txt_apellidos = Label(Forms, text="Apellido:", font=('arial', 16), bd=15)
txt_apellidos.grid(row=2, sticky="e")
txt_genero = Label(Forms, text="Sexo:", font=('arial', 16), bd=15)
txt_genero.grid(row=3, sticky="e")
txt_direccion = Label(Forms, text="Direccion:", font=('arial', 16), bd=15)
txt_direccion.grid(row=4, sticky="e")
txt_celular = Label(Forms, text="celular:", font=('arial', 16), bd=15)
txt_celular.grid(row=5, sticky="e")
txt_email = Label(Forms, text="email:", font=('arial', 16), bd=15)
txt_email.grid(row=6, sticky="e")

txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================CUADROS DE TEXTO WIDGET=======================================
codigo = Entry(Forms, textvariable=CODIGO, width=30)
codigo.grid(row=0, column=1)
nombres = Entry(Forms, textvariable=NOMBRES, width=30)
nombres.grid(row=1, column=1)
apellidos = Entry(Forms,textvariable=APELLIDOS, width=30)
apellidos.grid(row=2, column=1)
RadioGroup.grid(row=3, column=1)
direccion = Entry(Forms,textvariable=DIRECCION, width=30)
direccion.grid(row=4, column=1)
celular = Entry(Forms, textvariable=CELULAR,width=30)
celular.grid(row=5, column=1)
email = Entry(Forms, textvariable=EMAIL, width=30)
email.grid(row=6, column=1)

#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Crear", command=Insert)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Leer",)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Actualizar" , command=Actualizar)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete",)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", )
btn_exit.pack(side=LEFT)

#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("ID", "codigo","nombres", "apellidos", "genero", "direccion", "celular", "email"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('codigo', text="codigo", anchor=W)
tree.heading('nombres', text="nombres", anchor=W)
tree.heading('apellidos', text="apellidos", anchor=W)
tree.heading('genero', text="genero", anchor=W)
tree.heading('direccion', text="direccion", anchor=W)
tree.heading('celular', text="celular", anchor=W)
tree.heading('email', text="email", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=200)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected) # Permite seleccionar un registro



if __name__ == '__main__':
    Load()
    root.mainloop()