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
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure((0,1),weight=2)

        # Frame para contener el mensaje de bienvenida
        self.top_frame = ctk.CTkFrame(master=self.app, width=200, height=100)
        self.top_frame.grid(row= 0, column=0, padx=0, pady=0, sticky="new")
        self.top_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # Frame para contener el boton de menu
        self.frame_menu = ctk.CTkFrame(master=self.top_frame)
        self.frame_menu.grid(row=0, column= 0, pady=10, padx=20, sticky="w")

        # Etiqueta de bienvenida centrada
        self.bienvenida_label = ctk.CTkLabel(master=self.top_frame, text=f"Bienvenido de vuelta {user}")
        self.bienvenida_label.grid(row= 0, column=1, padx=(0,20), pady=20, sticky="nesw")

        # Botón "Menu" en la parte superior izquierda
        self.menu_button = ctk.CTkButton(master=self.frame_menu, text="Menu", command=self.toggle_menu)
        self.menu_button.grid(row= 0, column=0, padx=(10,10), pady=(20))  # Ajustar el padding para moverlo más arriba

        # Logo en la parte superior derecha
        logoV = ctk.CTkImage(
            light_image=Image.open((os.path.join(carpeta_imagenes, "logoOpaco.png"))),
            size=(100, 100),
            ) 
        self.etLogoV = ctk.CTkLabel(master=self.top_frame, image=logoV, text="")
        self.etLogoV.grid(row= 0, column=2,padx=(0,50), pady=0, sticky="e")
        
        # Frame que se desplegará
        self.nuevo_frame = None
        self.menu_visible = False
        self.app.mainloop()
        
    #def frame_menu(self):
     #   self.toggle_menu()

    def toggle_menu(self):
        if self.menu_visible:
            self.nuevo_frame.grid_forget()
        else:
            #self.nuevo_frame.grid(row=0, column=0, sticky="nesw", padx=20, pady=20)
            self.createMenuButtons()
        self.menu_visible = not self.menu_visible
        
    def createMenuButtons(self):
        self.nuevo_frame = ctk.CTkFrame(master=self.app, corner_radius=20)
        self.nuevo_frame.grid(row= 1, column=0, padx=20, pady=20, sticky="nw")

        # Crear un frame contenedor para los botones
        contenedor_botones = ctk.CTkFrame(master=self.nuevo_frame)
        contenedor_botones.grid(row= 1, column=0, padx=0, pady=0, sticky="sw")
        #crear los botones
        for i in range(4):
            boton = ctk.CTkButton(master=contenedor_botones, text=f"Carro {i + 1}", command=lambda i=i: self.boton_click(i))
            boton.grid(row= i, column=0, padx=20, pady=20)  # Apilar los botones verticalmente

    def boton_click(self, i):
        # Acción a realizar al hacer clic en un botón
        print(f"Has hecho clic en el Carro me voya matar {i + 1}")
    
app = Ventana()