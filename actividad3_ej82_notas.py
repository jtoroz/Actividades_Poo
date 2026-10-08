# Actividad 3 - Ejercicio 8.2: Notas
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import math
import tkinter as tk


class Notas:

    def __init__(self, lista_notas):
        self.lista_notas = lista_notas

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = 0
        for nota in self.lista_notas:
            suma += (nota - promedio) ** 2
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota > mayor:
                mayor = nota
        return mayor

    def calcular_menor(self):
        menor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota < menor:
                menor = nota
        return menor


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.resizable(False, False)

        self.campos = []
        for i in range(5):
            tk.Label(self, text="Nota " + str(i + 1)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            campo = tk.Entry(self, width=12)
            campo.grid(row=i, column=1, padx=10, pady=5)
            self.campos.append(campo)

        tk.Button(self, text="Calcular", width=10,
                  command=self.calcular).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self, text="Limpiar", width=10,
                  command=self.limpiar).grid(row=5, column=1, padx=10, pady=10)

        self.etiqueta_promedio = tk.Label(self, text="Promedio =")
        self.etiqueta_promedio.grid(row=6, column=0, columnspan=2, padx=10, sticky="w")

        self.etiqueta_desviacion = tk.Label(self, text="Desviación estándar =")
        self.etiqueta_desviacion.grid(row=7, column=0, columnspan=2, padx=10, sticky="w")

        self.etiqueta_mayor = tk.Label(self, text="Mayor nota =")
        self.etiqueta_mayor.grid(row=8, column=0, columnspan=2, padx=10, sticky="w")

        self.etiqueta_menor = tk.Label(self, text="Menor nota =")
        self.etiqueta_menor.grid(row=9, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")

    def calcular(self):
        lista_notas = []
        for campo in self.campos:
            lista_notas.append(float(campo.get()))

        notas = Notas(lista_notas)

        self.etiqueta_promedio.config(text="Promedio = %.2f" % notas.calcular_promedio())
        self.etiqueta_desviacion.config(text="Desviación estándar = %.2f" % notas.calcular_desviacion())
        self.etiqueta_mayor.config(text="Mayor nota = %.2f" % notas.calcular_mayor())
        self.etiqueta_menor.config(text="Menor nota = %.2f" % notas.calcular_menor())

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.etiqueta_promedio.config(text="Promedio =")
        self.etiqueta_desviacion.config(text="Desviación estándar =")
        self.etiqueta_mayor.config(text="Mayor nota =")
        self.etiqueta_menor.config(text="Menor nota =")


ventana = VentanaPrincipal()
ventana.mainloop()
