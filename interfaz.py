# PARA QUE LES FUNCIONE TIENEN QUE INSTALAR LA LIBRERIA CON -pip install customtkinter-
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel,CTkButton,CTkCheckBox
from tkinter import PhotoImage

root = CTk() 
root.geometry("500x600+350+20")
root.minsize(480,500)
root.config(bg ='#010101')
root.title("Inicio de Sesión")

frame = CTkFrame(root, fg_color='#010101')
frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)

frame.columnconfigure([0,1], weight=1)
frame.rowconfigure([0,1,2,3,4,5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

correo = CTkEntry(frame, placeholder_text='Usuario', border_color='#2cb67d', fg_color='#010101', width=220, height=40)
correo.grid(columnspan=2, row=1,padx=4, pady =4)

contrasenna = CTkEntry(frame,show="*", placeholder_text= 'Contraseña',
 border_color='#2cb67d', fg_color= '#010101', width =220,height=40)
contrasenna.grid(columnspan=2, row=2,padx=4, pady =4)

checkbox = CTkCheckBox(frame, text="Recuerdame",hover_color='#7f5af0', 
	border_color='#2cb67d', fg_color='#2cb67d')
checkbox.grid(columnspan=2, row=3,padx=4, pady =4)

bt_iniciar = CTkButton(frame, border_color='#2cb67d', fg_color='#010101',
	hover_color='#2cb67d',corner_radius=12,border_width=2,
    text='Entrar')
bt_iniciar.grid(columnspan=2, row=4,padx=4, pady =4)

root.mainloop()