# PARA QUE LES FUNCIONE TIENEN QUE INSTALAR LA LIBRERIA CON -pip install customtkinter-
import customtkinter as ctk 
import os
from PIL import ImageTk, Image

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal,"Imagenes")

class Ventana:
    def __init__(self):
        self.app =ctk.CTk()
        self.app.geometry("1000x500")
        self.app.title("Ventus Novus")
        self.app.iconbitmap(os.path.join(carpeta_imagenes,"logoSimple.ico"))
        self.app.resizable(False,False)
        
        barra = ctk.CTkFrame(master=self.app, width=50, height=50, fg_color="black")
        barra.pack(side="top", fill="x", padx= 100)
        
        logoV = ctk.CTkImage(
			light_image= Image.open((os.path.join(carpeta_imagenes,"logoOpaco.png"))),
			size=(250,250)
		)
        
        etLogoV = ctk.CTkLabel(master = self.app, image= logoV, text="")
        
        etLogoV.pack(pady = 100)
        
        
        
        self.app.mainloop()
        
        
        
app = Ventana()