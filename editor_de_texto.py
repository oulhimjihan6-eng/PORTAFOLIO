import tkinter as tk
# Crear la clase EditorDeTexto que hereda de tk.Tk
class EditorDeTexto(tk.Tk):
   def __init__(self,*args, **kwargs):
       super().__init__(*args, **kwargs)
       self.title("Editor de Texto")
       self.geometry("800x600")
       self.config(bg="lightgray")


# crtear la ventana prtincipal
   def crear_ventana_principal(self):
        self.ventana_principal = tk.Tk(self)
        self.ventana_principal.config(bg="lightgray")

# crear la zona donde se escribira el texto y botones para guardar y abrir archivos
   def crear_zona_texto(self):
       self.zona_texto = tk.Text(self.ventana_principal, wrap=tk.WORD, font=("Arial", 12))
       self.zona_texto.pack(fill="both", expand=True)
       self.boton_guardar=tk.Button(self.ventana_principal,text="guardar",command=self.guardar_archivo)
       self.boton_guardar.pack(side="left", padx=10, pady=10) 
# crear el menu de opciones y agregarlo a la ventana principal

   def crear_menu(self):
         self.menu = tk.Menu(self.ventana_principal)
         self.ventana_principal.config(menu=self.menu)
         self.menu_archivo = tk.Menu(self.menu, tearoff=0)
         self.menu.add_cascade(label="Archivo", menu=self.menu_archivo)
         self.menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
         self.menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
         self.menu_archivo.add_separator()
         self.menu_archivo.add_command(label="Salir", command=self.ventana_principal.quit)

mi_editor = EditorDeTexto()
mi_editor.mainloop()
