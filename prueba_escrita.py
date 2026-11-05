
import tkinter as tk
import random
import time


class PruebaEscritura:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Prueba de Escritura Veloz")
        self.ventana.geometry("600x350")

        self.frases = [
            "Python es un lenguaje fácil de aprender.",
            "La práctica hace al maestro.",
            "Programar puede ser divertido.",
            "Me gusta aprender cosas nuevas.",
            "La velocidad de escritura mejora con práctica."
        ]

        self.frase_actual = ""
        self.tiempo_inicio = 0

        # Título
        self.titulo = tk.Label(
            ventana,
            text="Prueba de Escritura Veloz",
            font=("Helvetica", 22)
        )
        self.titulo.pack(pady=15)

        # Instrucciones
        self.instrucciones = tk.Label(
            ventana,
            text="Escribe la siguiente frase lo más rápido y preciso posible:"
        )
        self.instrucciones.pack(pady=5)

        # Frase que debe escribir el usuario
        self.frase = tk.Label(
            ventana,
            text="Pulsa 'Comenzar' para empezar",
            font=("Helvetica", 14),
            wraplength=550
        )
        self.frase.pack(pady=20)

        # Campo de texto
        self.entrada = tk.Entry(
            ventana,
            font=("Helvetica", 14),
            width=50
        )
        self.entrada.pack(pady=10)

        # Botones
        self.boton_comenzar = tk.Button(
            ventana,
            text="Comenzar",
            command=self.comenzar
        )
        self.boton_comenzar.pack(pady=10)

        self.boton_comprobar = tk.Button(
            ventana,
            text="Comprobar",
            command=self.comprobar
        )
        self.boton_comprobar.pack()

        # Resultado
        self.resultado = tk.Label(
            ventana,
            text="",
            font=("Helvetica", 12)
        )
        self.resultado.pack(pady=15)

    def comenzar(self):
        # Elegir una frase aleatoria
        self.frase_actual = random.choice(self.frases)

        # Mostrar la frase
        self.frase.config(text=self.frase_actual)

        # Limpiar el campo de texto
        self.entrada.delete(0, tk.END)

        # Poner el cursor en el campo
        self.entrada.focus()

        # Guardar el momento de inicio
        self.tiempo_inicio = time.time()

        self.resultado.config(text="¡Escribe la frase!")

    def comprobar(self):
        # Comprobar que se haya iniciado la prueba
        if self.tiempo_inicio == 0:
            self.resultado.config(
                text="Primero pulsa 'Comenzar'."
            )
            return

        # Calcular el tiempo transcurrido
        tiempo_final = time.time()
        tiempo = tiempo_final - self.tiempo_inicio

        # Obtener el texto escrito
        texto_escrito = self.entrada.get()

        # Comprobar si coincide exactamente
        if texto_escrito == self.frase_actual:
            resultado = "¡Correcto!"
        else:
            resultado = "Hay errores en la frase."

        # Calcular palabras por minuto
        palabras = len(texto_escrito.split())
        minutos = tiempo / 60

        if minutos > 0:
            velocidad = palabras / minutos
        else:
            velocidad = 0

        self.resultado.config(
            text=f"{resultado}\n"
                 f"Tiempo: {tiempo:.2f} segundos\n"
                 f"Velocidad: {velocidad:.2f} palabras por minuto"
        )


# Crear la ventana
ventana = tk.Tk()

# Crear la aplicación
app = PruebaEscritura(ventana)

# Ejecutar el programa
ventana.mainloop()