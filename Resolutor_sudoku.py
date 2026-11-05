import tkinter as tk
import random
import pygame
    # crear la clase resolutor_sudoku que hereda de tk.Tk
class pagina_sudoku(tk.Tk):
  def __init__(self,*args, **kwargs): 
         super().__init__(*args, **kwargs)
         self.title("Resolutor de Sudoku")
         self.geometry("800x600")
         self.config(bg="lightpink")
  

    # crear la ventana principal
  def crear_ventana_principal(self):
          self.ventana_principal = tk.Tk(self)
          self.ventana_principal.config(bg="lightpink")
  
    # crear la zona donde se escribira el sudoku y botones para resolver y limpiar el sudoku
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
         self.menu.add_cascade(label="Inicio", menu=self.menu_archivo)
         self.menu_archivo.add_command(label="Crear", command=self.abrir_archivo)
         self.menu_archivo.add_command(label="Configurar", command=self.guardar_archivo)
         self.menu_archivo.add_separator()
         self.menu_archivo.add_command(label="Salir", command=self.ventana_principal.quit)



     # crear funcion para resolver el sudoku con backtrainig
  def resolver_sudoku(self, tablero):
            vacio = self.encontrar_vacio(tablero)
            if not vacio:
                return True
            fila, columna = vacio
            for num in range(1, 10):
                if self.es_valido(tablero, num, (fila, columna)):
                    tablero[fila][columna] = num
                    if self.resolver_sudoku(tablero):
                        return True
                    tablero[fila][columna] = 0
            return False
 # buscar una casilla vacía
  def encontrar_vacio(self, tablero):

        for fila in range(9):
            for columna in range(9):

                if tablero[fila][columna] == 0:
                    return fila, columna

        return None

    # comprobar si el número es válido
  def es_valido(self, tablero, num, posicion):

        fila, columna = posicion

        # comprobar fila
        for columna_actual in range(9):
            if tablero[fila][columna_actual] == num:
                return False

        # comprobar columna
        for fila_actual in range(9):
            if tablero[fila_actual][columna] == num:
                return False

        # comprobar cuadrado 3x3
        inicio_fila = (fila // 3) * 3
        inicio_columna = (columna // 3) * 3

        for fila_actual in range(
            inicio_fila,
            inicio_fila + 3
        ):

            for columna_actual in range(
                inicio_columna,
                inicio_columna + 3
            ):

                if tablero[fila_actual][columna_actual] == num:
                    return False

        return True
