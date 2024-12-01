from inicio import Sesion, user
import customtkinter as ctk
import os
from PIL import ImageTk, Image

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

        # Frame para contener el botón y el logo
        self.top_frame = ctk.CTkFrame(master=self.app)
        self.top_frame.pack(side="top", fill="x")

        # Etiqueta de bienvenida centrada
        self.bienvenida_label = ctk.CTkLabel(master=self.top_frame, text=f"Bievenido de vuelta {user}")
        self.bienvenida_label.pack(expand=True, fill="x", padx=10, pady=10)

        # Botón "Menu" en la parte superior izquierda
        self.menu_button = ctk.CTkButton(master=self.top_frame, text="Menu", command=self.frame_menu)
        self.menu_button.pack(side="left", padx=10, pady=(5, 0))  # Ajustar el padding para moverlo más arriba

        # Logo en la parte superior derecha
        logoV = ctk.CTkImage(
            light_image=Image.open((os.path.join(carpeta_imagenes, "logoOpaco.png"))),
            size=(100, 100)
        )
        
        self.etLogoV = ctk.CTkLabel(master=self.top_frame, image=logoV, text="")
        self.etLogoV.pack(side="right", padx=10, pady=(5, 0))

        # Frame que se desplegará
        self.nuevo_frame = None

        self.app.mainloop()

    def frame_menu(self):
        # Si el frame ya está desplegado, lo ocultamos
        if self.nuevo_frame is not None:
            self.nuevo_frame.destroy()
            self.nuevo_frame = None
            return

        self.nuevo_frame = ctk.CTkFrame(master=self.app, corner_radius=20)
        self.nuevo_frame.pack(pady=20, fill="both", expand=True)

        # Crear un frame contenedor para los botones
        contenedor_botones = ctk.CTkFrame(master=self.nuevo_frame)
        contenedor_botones.pack(side="left", padx=10, pady=10)

        for i in range(4):
            boton = ctk.CTkButton(master=contenedor_botones, text=f"Carro {i + 1}", command=lambda i=i: self.boton_click(i))
            boton.pack(side="top", padx=10, pady=10, fill="x")  # Apilar los botones verticalmente

    def boton_click(self, i):
        # Acción a realizar al hacer clic en un botón
        print(f"Has hecho clic en el Carro me voya matar {i + 1}")

app = Ventana()