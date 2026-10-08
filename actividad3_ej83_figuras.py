# Actividad 3 - Ejercicio 8.3: Figuras
# Programacion Orientada a Objetos 2026-2S - Juan Diego Toro Zuluaga

import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:

    def __init__(self):
        self.volumen = 0
        self.superficie = 0

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        self.volumen = volumen

    def get_superficie(self):
        return self.superficie

    def set_superficie(self, superficie):
        self.superficie = superficie


class Cilindro(FiguraGeometrica):

    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        self.volumen = math.pi * self.radio ** 2 * self.altura
        return self.volumen

    def calcular_superficie(self):
        self.superficie = 2 * math.pi * self.radio * self.altura + 2 * math.pi * self.radio ** 2
        return self.superficie


class Esfera(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        self.volumen = (4 / 3) * math.pi * self.radio ** 3
        return self.volumen

    def calcular_superficie(self):
        self.superficie = 4 * math.pi * self.radio ** 2
        return self.superficie


class Piramide(FiguraGeometrica):

    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        self.volumen = self.base ** 2 * self.altura / 3
        return self.volumen

    def calcular_superficie(self):
        self.superficie = self.base ** 2 + 2 * self.base * self.apotema
        return self.superficie


class VentanaFigura(tk.Toplevel):
    """Ventana base: arma los campos de entrada y las etiquetas de resultado."""

    def __init__(self, titulo, nombres_campos):
        super().__init__()
        self.title(titulo)
        self.resizable(False, False)

        self.campos = []
        for i, nombre in enumerate(nombres_campos):
            tk.Label(self, text=nombre + " (cm)").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            campo = tk.Entry(self, width=12)
            campo.grid(row=i, column=1, padx=10, pady=5)
            self.campos.append(campo)

        fila = len(nombres_campos)
        tk.Button(self, text="Calcular", width=10,
                  command=self.calcular).grid(row=fila, column=0, columnspan=2, pady=10)

        self.etiqueta_volumen = tk.Label(self, text="Volumen =")
        self.etiqueta_volumen.grid(row=fila + 1, column=0, columnspan=2, padx=10, sticky="w")

        self.etiqueta_superficie = tk.Label(self, text="Superficie =")
        self.etiqueta_superficie.grid(row=fila + 2, column=0, columnspan=2, padx=10,
                                      pady=(0, 10), sticky="w")

    def crear_figura(self, valores):
        pass

    def calcular(self):
        try:
            valores = [float(campo.get()) for campo in self.campos]
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
            return

        figura = self.crear_figura(valores)
        self.etiqueta_volumen.config(text="Volumen = %.2f cm3" % figura.calcular_volumen())
        self.etiqueta_superficie.config(text="Superficie = %.2f cm2" % figura.calcular_superficie())


class VentanaCilindro(VentanaFigura):

    def __init__(self):
        super().__init__("Cilindro", ["Radio", "Altura"])

    def crear_figura(self, valores):
        return Cilindro(valores[0], valores[1])


class VentanaEsfera(VentanaFigura):

    def __init__(self):
        super().__init__("Esfera", ["Radio"])

    def crear_figura(self, valores):
        return Esfera(valores[0])


class VentanaPiramide(VentanaFigura):

    def __init__(self):
        super().__init__("Pirámide", ["Base", "Altura", "Apotema"])

    def crear_figura(self, valores):
        return Piramide(valores[0], valores[1], valores[2])


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.resizable(False, False)

        tk.Label(self, text="Seleccione una figura").pack(padx=20, pady=10)
        tk.Button(self, text="Cilindro", width=12, command=VentanaCilindro).pack(padx=20, pady=5)
        tk.Button(self, text="Esfera", width=12, command=VentanaEsfera).pack(padx=20, pady=5)
        tk.Button(self, text="Pirámide", width=12, command=VentanaPiramide).pack(padx=20, pady=(5, 15))


ventana = VentanaPrincipal()
ventana.mainloop()
