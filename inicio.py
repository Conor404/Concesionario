from customtkinter import *

# Usuario y contraseña
user = "admin"
contra = "admin"

class Sesion:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("500x600+350+20")
        self.root.minsize(480, 500)
        self.root.config(bg='#010101')
        self.root.title("Inicio de Sesión")
        
        frame = CTkFrame(self.root, fg_color='#010101')
        frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

        frame.columnconfigure([0, 1], weight=1)
        frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Guardar los campos de entrada como atributos de la instancia
        self.correo = CTkEntry(frame, placeholder_text='Usuario', border_color='#2cb67d', fg_color='#010101', width=220, height=40)
        self.correo.grid(columnspan=2, row=1, padx=4, pady=4)

        self.contrasenna = CTkEntry(frame, show="*", placeholder_text='Contraseña',
                                    border_color='#2cb67d', fg_color='#010101', width=220, height=40)
        self.contrasenna.grid(columnspan=2, row=2, padx=4, pady=4)

        # Crear el botón y vincularlo al método validar
        bt_iniciar = CTkButton(frame, border_color='#2cb67d', fg_color='#010101',
                                hover_color='#2cb67d', corner_radius=12, border_width=2,
                                text='Entrar', command=self.validar)  # Aquí se vincula el método
        bt_iniciar.grid(columnspan=2, row=4, padx=4, pady=4)

        self.info_login = None  # Inicializar la variable para la etiqueta de información

        self.root.mainloop()

    def validar(self):
        # Obtener el nombre de usuario y la contraseña
        obtener_usuario = self.correo.get()  # Accede al campo de usuario
        obtener_contrasena = self.contrasenna.get()  # Accede al campo de contraseña
        
        # Verifica si el usuario y la contraseña son correctos
        if obtener_usuario != user or obtener_contrasena != contra:
            # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
            if self.info_login is not None:
                self.info_login.destroy()
            # Crea esta etiqueta siempre que el login sea incorrecto
            self.info_login = CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
            self.info_login.grid(columnspan=2, row=5, padx=4, pady=4)  # Usar grid aquí
        else:
            # En caso de tener ya un elemento "info_login" (etiqueta) creado, lo borra
            if self.info_login is not None:
                self.info_login.destroy()
            # Crea esta etiqueta siempre que el login sea correcto
            self.info_login = CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...")
            self.info_login.grid(columnspan=2, row=5, padx=4, pady=4)  # Usar grid aquí
            
            # Cerrar la ventana después de un breve retraso
            self.root.after(2000, self.root.destroy)  # Espera 2 segundos y luego cierra la ventana

if __name__ == "__main__":
    Sesion()