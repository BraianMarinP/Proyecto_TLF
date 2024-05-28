
"""

    Estudiantes Braian Marin Puerta, Juan Pablo Alviz Velasquez, Maria Juanita Camargo Prado

"""
# Declaraciones de los tokens
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

# Variable que nos ayuda a guardar el resultado del analisis y que es
# usada en los distintos metodos
global resultado
resultado = ""

class AnalizadorLexico:

    # Metodo que ayuda a cortar las palabras identificadas
    # de una cadena que ha sido procesada.
    def recortar_cadena(self, cadena1, cadena2):
        while cadena2.startswith(" "):
            cadena2 = cadena2[1:]
        if cadena2.startswith(cadena1):
            return cadena2[len(cadena1):], True
        return cadena2, False

    # Este metodo verifica si la cadena enviada cumple con el criterio de identificador
    # este consiste en empezar por cualquier letra, mayuscula o minuscula, luego
    # puede contener tantas letras como numeros se desee sin simbolos ni espacios.
    def es_identificador(self, cadena):
        if not cadena:
            return False
        if not (cadena[0].isalpha()):  # debe comenzar con una letra
            return False
        for char in cadena[1:]:
            if not (char.isalnum()):  # debe ser alfanumérico
                return False
        return True

    # Este metodo verifica si la cadena enviada cumple con el criterio
    # de un numero entero, por ejemplo 23123
    def es_entero(self, cadena):
        if not cadena:
            return False
        for char in cadena:
            if not char.isdigit():
                return False
        return True

    # Este metodo verifica si la cadena enviada cumple con el criterio
    # de un numero con punto flotante, es decir por ejemplo 2312.531
    def es_flotante(self, cadena):
        if not cadena:
            return False
        partes = cadena.split('.')
        if len(partes) != 2:
            return False
        return self.es_entero(partes[0]) and self.es_entero(partes[1])

    def analizar(self):
        # Variable donde se guarda el analisis de las cadenas
        global resultado
        # Arreglo con todos los tokens declarados del lenguaje
        categorias = [
            palabras_reservadas_bucles, palabras_decision, palabras_clase,
            metodos_publicos, metodos_privados, palabra_entero, palabras_reales,
            palabra_cadena, palabra_caracter, comentario, operadores_aritmeticos,
            operadores_logicos, operadores_relacionales, operadores_asignacion,
            simbolos_abrir, simbolos_cerrar
        ]
        
        # Categorias o tokens para marcar las cadenas
        nombres_categorias = [
            "palabras_reservadas_bucles", "palabras_decision", "palabras_clase",
            "metodos_publicos", "metodos_privados", "palabra_entero", "palabras_reales",
            "palabra_cadena", "palabra_caracter", "comentario", "operadores_aritmeticos",
            "operadores_logicos", "operadores_relacionales", "operadores_asignacion",
            "simbolos_abrir", "simbolos_cerrar"
        ]
        
        # Método que verifica si la cadena pertenece a alguna categoria de las palabras
        # reservadas, este es un metodo interno de otro metodo de la clase AnalizadorLexico
        def procesar_cadena(cadena2, contador_lineas):
            global resultado
            for nombre_categoria, categoria in zip(nombres_categorias, categorias):
                for cadena1 in categoria:
                    cadena2, recortado = self.recortar_cadena(cadena1, cadena2)
                    if recortado:
                        resultado += f"{nombre_categoria}: {cadena1} linea: {contador_lineas}\n"
                        return cadena2, True
            return cadena2, False
        
        # Abrir y leer el archivo de texto
        with open('script.txt', 'r', encoding='utf-8') as file:
            script = file.read()
        lineas_script = script.split("\n")

        contador_lineas = 1
        print(f"Total de líneas del script {contador_lineas}")
        # Se procesa cada linea del script
        for cadena2 in lineas_script:
            # Ciclo que se ejecuta mientras la cadena no esté vacía
            while cadena2:
                procesado = False
                #Vericiamos si es un comentario
                if cadena2.strip().startswith("☺☺☺"):
                        resultado += f"Comentario: {cadena2.strip()} linea: {contador_lineas}\n"
                        cadena2 = ""
                        procesado = True
                # Si la cadena no está procesada como comentario
                # se intenta procesar como alguno de los tokens
                if not procesado:
                    # Retorna la cadena recortada y procesado como True en caso
                    # de haberse procesado correctamente, por le contrario
                    # devuelve la cadena sin cortar y procesado como False
                    cadena2, procesado = procesar_cadena(cadena2, contador_lineas)
                # En caso de no haber sido procesada entre las palabras reservadas
                # se procesa de la siguiente manera.
                if not procesado and cadena2:
                    # Extraer identificador o número
                    i = 0
                    while i < len(cadena2) and (cadena2[i].isalnum() or cadena2[i] == '.'):
                        i += 1
                    subcadena = cadena2[:i]
                    # Este condicional verifica si la subcadena es un identificador
                    if self.es_identificador(subcadena):
                        resultado += f"Identificador: {subcadena} linea: {contador_lineas}\n"
                        cadena2 = cadena2[i:]
                    # Este condicional verifica si la subcadena es un numero entero
                    elif self.es_entero(subcadena):
                        resultado += f"Entero: {subcadena} linea: {contador_lineas}\n"
                        cadena2 = cadena2[i:]
                    # Este condicional verifica si es un numero de punto flotante
                    elif self.es_flotante(subcadena):
                        resultado += f"Flotante: {subcadena} linea: {contador_lineas}\n"
                        cadena2 = cadena2[i:]
                    else:
                        error = True
                        #Verificamos si no se trata de asignación de cadena
                        if cadena2[0] == "'":
                            for k in range(1, len(cadena2)):
                                if cadena2[k] == "'":
                                    #print(f"Último valor de k: {k} para el corte de la cadena: {cadena2}")
                                    subcadena = cadena2[:k+1]
                                    resultado += f"asignacion_cadena: {subcadena} linea: {contador_lineas}\n"
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
import matplotlib.pyplot as plt
import networkx as nx

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
        #self.cargar_tabla()
        
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
        # Cargar datos en la tabla
        self.cargar_tabla()

    def cargar_tabla(self):
        global resultado
        # Método para cargar la tabla con la información de la variable global
        self.tree.delete(*self.tree.get_children())  # Limpiar la tabla primero
        filas = resultado.split("\n")
        for fila in filas:
            token_end_idx = fila.find(" ")
            linea_start_idx = fila.rfind(" linea: ")
            
            if token_end_idx == -1 or linea_start_idx == -1:
                continue  # Saltar líneas que no tienen el formato esperado
            
            token = fila[:token_end_idx]
            palabra = fila[token_end_idx + 1:linea_start_idx]
            linea = fila[linea_start_idx + len(" linea: "):]

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
        # Crear el grafo dirigido
        G = nx.DiGraph()
        palabra = f"{palabra}"
        # Crear nodos y aristas
        for i in range(len(palabra)):
            G.add_node(f'q{i}')
            G.add_edge(f'q{i}', f'q{i+1}', label=palabra[i])
        
        # Añadir nodo final
        G.add_node(f'q{len(palabra)}')
        
        # Posiciones para los nodos
        pos = nx.spring_layout(G)
        
        # Dibujar nodos
        nx.draw_networkx_nodes(G, pos, node_color='white', edgecolors='black', node_size=1500)
        nx.draw_networkx_nodes(G, pos, nodelist=['q0'], node_color='green', edgecolors='black', node_size=1500)
        nx.draw_networkx_nodes(G, pos, nodelist=[f'q{len(palabra)}'], node_color='yellow', edgecolors='black', node_size=1500)
        
        # Dibujar aristas
        nx.draw_networkx_edges(G, pos)
        
        # Dibujar etiquetas de los nodos
        nx.draw_networkx_labels(G, pos, font_color='black')
        
        # Dibujar etiquetas de las aristas
        edge_labels = {(f'q{i}', f'q{i+1}'): palabra[i] for i in range(len(palabra))}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        # Mostrar la gráfica
        plt.show()

if __name__ == "__main__":
    analizador = AnalizadorLexico()
    analizador.analizar()
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
