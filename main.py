from inicio import Sesion, user
import customtkinter as ctk
import os
from PIL import ImageTk, Image

Sesion()
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "Imagenes")
ctk.set_appearance_mode("Dark")

class Ventana:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Ventus Novus")
        self.app.iconbitmap(os.path.join(carpeta_imagenes, "logoSimple.ico"))
        self.app.resizable(False, False)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0, weight=1)

        # Frame para contener el mensaje de bienvenida
        self.top_frame = ctk.CTkFrame(master=self.app, width=200, height=200)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0, sticky="new")
        self.top_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # Frame para contener el botón de menú
        self.frame_menu = ctk.CTkFrame(master=self.top_frame)
        self.frame_menu.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # Etiqueta de bienvenida centrada
        self.bienvenida_label = ctk.CTkLabel(master=self.top_frame, text=f"Bienvenido de vuelta {user}")
        self.bienvenida_label.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nesw")

        # Botón "Menu" en la parte superior izquierda
        self.menu_button = ctk.CTkButton(master=self.frame_menu, text="Menu", command=self.toggle_menu, border_color='#000000', fg_color='#4d5053',
                                hover_color='#a6a6a6', corner_radius=12, border_width=2)
        self.menu_button.grid(row=0, column=0, padx=(10, 10), pady=(20))

        # Logo en la parte superior derecha
        logoV = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, "logoSimple.png")),
            size=(100, 100),
        )
        self.etLogoV = ctk.CTkLabel(master=self.top_frame, image=logoV, text="")
        self.etLogoV.grid(row=0, column=2, padx=(0, 50), pady=0, sticky="e")

        # Frames que se desplegarán
        self.frame_menu_desplegado = None
        self.frames_imagenes = {}
        self.menu_visible = False
        self.frame_imagenes_visible = [False] * 4  # Lista para llevar el estado de visibilidad de los frames de imágenes
        self.ventana_actual = None
        self.app.mainloop()

    def toggle_menu(self):
        if self.menu_visible:
            # Ocultar el menú
            if self.frame_menu_desplegado and self.frame_menu_desplegado.winfo_exists():
                self.frame_menu_desplegado.grid_forget()
                self.frame_menu_desplegado = None
            # Ocultar el frame de imágenes si está visible
            self.ocultar_frames_imagenes()
            # Cerrar la ventana actual si existe
            self.cerrar_ventana_actual()
        else:
            # Crear frame para el menú
            self.frame_menu_desplegado = ctk.CTkFrame(master=self.app, corner_radius=20)
            self.frame_menu_desplegado.grid(row=1, column=0, padx=20, pady=(0,150), sticky="nw")

            # Crear botones en el frame del menú
            self.createMenuButtons()

        self.menu_visible = not self.menu_visible

    def createMenuButtons(self):
        # Crear un frame contenedor para los botones a la izquierda
        contenedor_botones = ctk.CTkFrame(master=self.frame_menu_desplegado)
        contenedor_botones.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Crear los botones
        botones_texto = ["Carro deportivo", "Camionetas", "Motos", "Carros Familiares"]
        for i, texto in enumerate(botones_texto):
            boton = ctk.CTkButton(master=contenedor_botones, text=texto, command=lambda i=i: self.boton_click(i), border_color='#000000', fg_color='#4d5053',
                                hover_color='#a6a6a6', corner_radius=12, border_width=2)
            boton.grid(row=i, column=0, padx=20, pady=10)

    def ocultar_frames_imagenes(self):
        # Ocultar todos los frames de imágenes si están visibles
        for i, frame in self.frames_imagenes.items():
            if self.frame_imagenes_visible[i] and frame.winfo_exists():
                frame.grid_forget()
                self.frame_imagenes_visible[i] = False

    def cerrar_ventana_actual(self):
        # Cerrar la ventana actual si existe
        if self.ventana_actual and self.ventana_actual.winfo_exists():
            self.ventana_actual.destroy()
            self.ventana_actual = None

    def boton_click(self, i):
        # Ocultar el frame de imágenes al hacer clic en cualquiera de los botones
        self.ocultar_frames_imagenes()

        # Cerrar la ventana anterior si existe
        self.cerrar_ventana_actual()

        # Acción a realizar al hacer clic en un botón
        self.ventana_actual = ctk.CTkToplevel(master=self.app)
        self.ventana_actual.geometry("800x600")
        self.ventana_actual.title(f"Imágenes de {['Carros deportivos', 'Camionetas', 'Motos', 'Carros Familiares'][i]}")
        self.ventana_actual.grid_rowconfigure(0, weight=1)
        self.ventana_actual.grid_columnconfigure(0, weight=1)

        frame_imagenes = ctk.CTkFrame(master=self.ventana_actual, corner_radius=20)
        frame_imagenes.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        frame_imagenes.grid_rowconfigure(0, weight=1)
        frame_imagenes.grid_columnconfigure((0,1), weight=1)

        # Crear 4 frames dentro del frame de imágenes y centrarlos
        for j in range(4):
            frame_interno = ctk.CTkFrame(master=frame_imagenes, width=100, height=100)
            frame_interno.grid(row=j // 2, column=j % 2, padx=10, pady=50)

            # Asignar imagen a cada frame
            imagen_path = os.path.join(carpeta_imagenes, f"imagen_{i}_{j}.png")
            imagen = ctk.CTkImage(light_image=Image.open(imagen_path), size=(160, 160))
            etiqueta_imagen = ctk.CTkLabel(master=frame_interno, image=imagen, text="")
            etiqueta_imagen.grid(row=0, column=0, padx=10, pady=10)

        self.frames_imagenes[i] = frame_imagenes
        self.frame_imagenes_visible[i] = True

# Crear la instancia de la ventana
app = Ventana()