from customtkinter import *

# Usuario y contraseña
user = "admin"
contra = "admin"

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal,"Imagenes")

class Sesion:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("500x600+350+20")
        self.root.minsize(480, 500)
        self.root.config(bg='#010101')
        self.root.title("Inicio de Sesión")
        self.root.iconbitmap(os.path.join(carpeta_imagenes,"logoSimple.ico"))
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion_si_no_hay_datos)
        
        frame = CTkFrame(self.root, fg_color='#a6a6a6')
        frame.grid(column=0, row=0, sticky='nsew', padx=0, pady=0)

        frame.columnconfigure([0, 1], weight=1)
        frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.correo = CTkEntry(frame, placeholder_text='Usuario', border_color='#000000', fg_color='#4d5053', width=220, height=40, text_color="white")
        self.correo.grid(columnspan=2, row=1, padx=4, pady=4)

        self.contrasenna = CTkEntry(frame, show="*", placeholder_text='Contraseña',
                                    border_color='#000000', fg_color='#4d5053', width=220, height=40, text_color="white")
        self.contrasenna.grid(columnspan=2, row=2, padx=4, pady=4)

        # Crear el botón y vincularlo al método validar
        bt_iniciar = CTkButton(frame, border_color='#000000', fg_color='#4d5053',
                                hover_color='#a6a6a6', corner_radius=12, border_width=2,
                                text='Entrar', command=self.validar)  # Aquí se vincula el método
        bt_iniciar.grid(columnspan=2, row=4, padx=4, pady=4)

        self.info_login = None

        self.root.mainloop()

    def validar(self):
        # aqui se pide el user y la contra
        obtener_usuario = self.correo.get() 
        obtener_contrasena = self.contrasenna.get() 
        
        # Verifica si el usuario y la contraseña son correctos
        if obtener_usuario != user or obtener_contrasena != contra:
            # En caso de tener ya tener una etiqueta creada, la borra pa q no se acumulen
            if self.info_login is not None:
                self.info_login.destroy()
            # Crea esta etiqueta siempre que el login sea incorrecto
            self.info_login = CTkLabel(self.root, text="Usuario o contraseña incorrectos.", fg_color="#4d5053", text_color="white")
            self.info_login.grid(columnspan=2, row=5, padx=4, pady=4)  # Usar grid aquí
        else:
            # En caso de tener ya una etiqueta creada, la borra para que no se acumulen x2
            if self.info_login is not None:
                self.info_login.destroy()
            # Crea este mensaje si los datos (admin) estan buenos
            self.info_login = CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...", fg_color="#4d5053", text_color="white")
            self.info_login.grid(columnspan=2, row=5, padx=4, pady=4)  # Usar grid aquí
            
            # esta mamada nada mas hace que se tarde 2 segundos en cerrarse
            self.root.after(2000, self.root.destroy)  # hace q se vea mas serio
    def cerrar_aplicacion_si_no_hay_datos(self):
        # Verificar si los campos están vacíos y cerrar la aplicación si es así
        if not self.correo.get() or not self.contrasena.get():
            sys.exit()

if __name__ == "__main__":
    Sesion()