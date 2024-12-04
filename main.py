# este main es una prueba de la prueba de la prueba de la prueba


import os
import customtkinter as ctk
from PIL import Image
from inicio import Sesion, user

Sesion()
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")

class Ventana:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Ventus Novus")
        self.app.iconbitmap(os.path.join(carpeta_imagenes, "logoSimple.ico"))
        self.app.resizable(True, True)

        # Frame para contener el mensaje de bienvenida
        self.top_frame = ctk.CTkFrame(master=self.app)
        self.top_frame.grid(row=0, column=2, padx=20, pady=20)

        # Frame para contener el botón de menú
        self.frame_menu = ctk.CTkFrame(master=self.app)
        self.frame_menu.grid(row=0, column=0, pady=10, padx=10)

        # Etiqueta de bienvenida centrada
        self.bienvenida_label = ctk.CTkLabel(master=self.top_frame, text=f"Bienvenido de vuelta {user}")
        self.bienvenida_label.grid(row=0, column=2, padx=20, pady=20)

        # Botón "Menu" en la parte superior izquierda
        self.menu_button = ctk.CTkButton(master=self.frame_menu, text="Menu", command=self.toggle_menu)
        self.menu_button.grid(row=0, column=0, padx=20, pady=20)

        # Cargar la imagen del logo
        try:
            self.logoV = ctk.CTkImage(
                light_image=Image.open(os.path.join(carpeta_imagenes, "logoOpaco.png")),
                size=(100, 100),
            )
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.logoV = None  # Asignar None si hay un error

        # Verificar si la imagen se cargó correctamente antes de crear el label
        if self.logoV is not None:
            self.etLogoV = ctk.CTkLabel(master=self.app, image=self.logoV, text="")
            self.etLogoV.grid(row=0, column=1, sticky='ne')  # 'ne' significa noreste (esquina superior derecha)

        # Frame que se desplegará
        self.nuevo_frame = None
        self.menu_visible = False

        # Mostrar la ventana
        self.app.mainloop()

    def toggle_menu(self):
        if self.menu_visible:
            self.nuevo_frame.grid_forget()
        else:
            self.frame_menu()
        self.menu_visible = not self.menu_visible

    def frame_menu(self):
        # Si el frame ya está desplegado, lo ocultamos
        if self.nuevo_frame is not None:
            self.nuevo_frame.destroy()
            self.nuevo_frame = None
            return

        self.nuevo_frame = ctk.CTkFrame(master=self.app, corner_radius=20)
        self.nuevo_frame.grid(row=0, column=0, padx=20, pady=20)

        # Crear un frame contenedor para los botones
        contenedor_botones = ctk.CTkFrame(master=self.nuevo_frame)
        contenedor_botones.grid(row=0, column=0, padx=20, pady=20)

        for i in range(4):
            boton = ctk.CTkButton(master=contenedor_botones, text=f"Carro {i + 1}", command=lambda i=i: self.boton_click(i))
            boton.grid(row= 0, column=0, padx=20, pady=20)  # Apilar los botones verticalmente

    def boton_click(self, i):
        # Acción a realizar al hacer clic en un botón
        print(f"Has hecho clic en el Carro me voya matar {i + 1}")
    
app = Ventana()