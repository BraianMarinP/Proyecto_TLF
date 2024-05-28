palabras_reservadas_bucles = ["Mientras", "Para"]
palabras_decision = ["si", "sino", "otro"]
palabras_clase = ["clase", "interfaz", "enumerador", "extiende", "implementa"]
metodos_publicos = [
    "metodo publico ent",
    "metodo publico flot",
    "metodo publico dob",
    "metodo publico Cadena",
    "metodo publico car",
    "metodo publico nada"
]
metodos_privados = [
    "metodo privado ent",
    "metodo privado flot",
    "metodo privado dob",
    "metodo privado Cadena",
    "metodo privado car",
    "metodo privado nada"
]
palabra_entero = ["ent"]
palabras_reales = ["flot", "dob"]
palabra_cadena = ["Cadena"]
palabra_caracter = ["car"]
comentario = ["☺☺☺"]
operadores_aritmeticos = ["⊕", "⊥", "⊗", "⊘", "⊙", "△"]
operadores_logicos = ["⇔", "⇒", "!"]
operadores_relacionales = ["::", "!!", "♦", "♣", "♦::", "♣::"]
operadores_asignacion = ["=", "⊕=", "⊥=", "⊗=", "⊘=", "○="]
simbolos_abrir = ["(", "[", "{"]
simbolos_cerrar = [")", "]", "}"]

global resultado
resultado = ""

class AnalizadorLexico:

    def recortar_cadena(self, cadena1, cadena2):
        while cadena2.startswith(" "):
            cadena2 = cadena2[1:]
        if cadena2.startswith(cadena1):
            return cadena2[len(cadena1):], True
        return cadena2, False

    def es_identificador(self, cadena):
        if not cadena:
            return False
        if not (cadena[0].isalpha()):  # debe comenzar con una letra
            return False
        for char in cadena[1:]:
            if not (char.isalnum()):  # debe ser alfanumérico
                return False
        return True

    def es_entero(self, cadena):
        if not cadena:
            return False
        for char in cadena:
            if not char.isdigit():
                return False
        return True

    def es_flotante(self, cadena):
        if not cadena:
            return False
        partes = cadena.split('.')
        if len(partes) != 2:
            return False
        return self.es_entero(partes[0]) and self.es_entero(partes[1])

    def analizar(self):
        global resultado
        categorias = [
            palabras_reservadas_bucles, palabras_decision, palabras_clase,
            metodos_publicos, metodos_privados, palabra_entero, palabras_reales,
            palabra_cadena, palabra_caracter, comentario, operadores_aritmeticos,
            operadores_logicos, operadores_relacionales, operadores_asignacion,
            simbolos_abrir, simbolos_cerrar
        ]
        
        nombres_categorias = [
            "palabras_reservadas_bucles", "palabras_decision", "palabras_clase",
            "metodos_publicos", "metodos_privados", "palabra_entero", "palabras_reales",
            "palabra_cadena", "palabra_caracter", "comentario", "operadores_aritmeticos",
            "operadores_logicos", "operadores_relacionales", "operadores_asignacion",
            "simbolos_abrir", "simbolos_cerrar"
        ]
        
        #cadena2 = " identificador123 Mientras { dob} cadena 233 224.34 23J %&$"

        def procesar_cadena(cadena2, contador_lineas):
            global resultado
            for nombre_categoria, categoria in zip(nombres_categorias, categorias):
                for cadena1 in categoria:
                    cadena2, recortado = self.recortar_cadena(cadena1, cadena2)
                    if recortado:
                        resultado += f"{nombre_categoria}: '{cadena1}' linea: {contador_lineas}\n"
                        return cadena2, True
            return cadena2, False
        
        # Abrir y leer el archivo de texto
        with open('script.txt', 'r', encoding='utf-8') as file:
            script = file.read()
        lineas_script = script.split("\n")

        contador_lineas = 1
        print(f"Total de líneas del script {contador_lineas}")
        for cadena2 in lineas_script:
            while cadena2:
                procesado = False
                #Vericiamos si es un comentario
                if cadena2.strip().startswith("☺☺☺"):
                        resultado += f"Comentario: '{cadena2.strip()}' linea: {contador_lineas}\n"
                        cadena2 = ""
                        procesado = True
                if not procesado:
                    cadena2, procesado = procesar_cadena(cadena2, contador_lineas)
                if not procesado and cadena2:
                    # Extraer identificador o número
                    i = 0
                    while i < len(cadena2) and (cadena2[i].isalnum() or cadena2[i] == '.'):
                        i += 1
                    subcadena = cadena2[:i]
                    if self.es_identificador(subcadena):
                        resultado += f"Identificador encontrado: '{subcadena}' linea: {contador_lineas}\n"
                        cadena2 = cadena2[i:]
                    elif self.es_entero(subcadena):
                        resultado += f"Entero encontrado: '{subcadena}' linea: {contador_lineas}\n"
                        cadena2 = cadena2[i:]
                    elif self.es_flotante(subcadena):
                        resultado += f"Flotante encontrado: '{subcadena}' linea: {contador_lineas}\n"
                        cadena2 = cadena2[i:]
                    else:
                        error = True
                        #Verificamos si no se trata de asignación de cadena
                        if cadena2[0] == "'":
                            for k in range(1, len(cadena2)):
                                if cadena2[k] == "'":
                                    #print(f"Último valor de k: {k} para el corte de la cadena: {cadena2}")
                                    subcadena = cadena2[:k+1]
                                    resultado += f"Asignacion de cadena: '{subcadena}' linea: {contador_lineas}\n"
                                    cadena2 = cadena2[k+1:]
                                    error = False
                                    break
                        # Manejar el error
                        # En caso de que no se haya podido identificar una subcadena
                        # Se cuenta el numero de caracteres hasta el siguiente espacio o finalizacion de la cadena
                        # print(f"Cadena restante: {cadena2} es error? -> {error}")
                        if i == 0 and error:
                            for caracter in cadena2:
                                i += 1
                                if caracter == " ":
                                    break
                            subcadena = cadena2[:i]
                        if error:
                            resultado += f"Error: '{subcadena}' linea: {contador_lineas}\n"
                            cadena2 = cadena2[i:]

                elif not procesado:
                    cadena2 = cadena2[1:]
            contador_lineas += 1

        print(resultado)
        #print(f"Cadena final: '{cadena2}'")

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz de Carga y Graficación")
        
        # Área de texto editable
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.text_area.grid(row=0, column=0, padx=10, pady=10)
        
        # Botón de carga
        self.load_button = tk.Button(root, text="Cargar", command=self.cargar)
        self.load_button.grid(row=1, column=0, padx=10, pady=10)
        
        # Tabla
        self.tree = ttk.Treeview(root, columns=("Token", "Palabra", "Linea"), show="headings")
        self.tree.heading("Token", text="Token")
        self.tree.heading("Palabra", text="Palabra")
        self.tree.heading("Linea", text="Linea")
        self.tree.grid(row=2, column=0, padx=10, pady=10)
        
        # Cargar datos en la tabla
        self.cargar_tabla()
        
        # Botón de graficar
        self.plot_button = tk.Button(root, text="Graficar", command=self.graficar)
        self.plot_button.grid(row=3, column=0, padx=10, pady=10)
    
    def cargar(self):
        # Método para cargar el archivo de texto
        try:
            with open("script.txt", "r") as file:
                contenido = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, contenido)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo 'script.txt' no se encuentra.")

    def cargar_tabla(self):
        global resultado
        # Método para cargar la tabla con la información de la variable global
        self.tree.delete(*self.tree.get_children())  # Limpiar la tabla primero
        filas = resultado.split("\n")
        for fila in filas:
            partes = fila.split(" encontrado: ")
            if len(partes) == 2:
                token = partes[0]
                palabra_linea = partes[1].rsplit(" linea: ", 1)
                if len(palabra_linea) == 2:
                    palabra, linea = palabra_linea
                    self.tree.insert("", "end", values=(token.strip(), palabra.strip(), linea.strip()))

    def graficar(self):
        # Método para graficar
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion[0])
            palabra = item["values"][1]
            self.realizar_grafica(palabra)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una fila de la tabla.")

    def realizar_grafica(self, palabra):
        # Método para realizar alguna acción con la palabra seleccionada (graficar)
        print(f"Graficando para la palabra: {palabra}")
        # Aquí iría el código para realizar la gráfica con la palabra

if __name__ == "__main__":
    analizador = AnalizadorLexico()
    analizador.analizar()
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
