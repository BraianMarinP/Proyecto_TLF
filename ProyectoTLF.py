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

        def procesar_cadena(cadena2):
            global resultado
            for nombre_categoria, categoria in zip(nombres_categorias, categorias):
                for cadena1 in categoria:
                    cadena2, recortado = self.recortar_cadena(cadena1, cadena2)
                    if recortado:
                        resultado += f"{nombre_categoria}: '{cadena1}'\n"
                        return cadena2, True
            return cadena2, False

        
        # Abrir y leer el archivo de texto
        with open('script.txt', 'r', encoding='utf-8') as file:
            script = file.read()
        lineas_script = script.split("\n")

        for cadena2 in lineas_script:
            while cadena2:
                procesado = False
                #Vericiamos si es un comentario
                if cadena2.strip().startswith("☺☺☺"):
                        resultado += f"Comentario: '{cadena2.strip()}'\n"
                        cadena2 = ""
                        procesado = True
                if not procesado:
                    cadena2, procesado = procesar_cadena(cadena2)
                if not procesado and cadena2:
                    # Extraer identificador o número
                    i = 0
                    while i < len(cadena2) and (cadena2[i].isalnum() or cadena2[i] == '.'):
                        i += 1
                    subcadena = cadena2[:i]
                    if self.es_identificador(subcadena):
                        resultado += f"Identificador encontrado: '{subcadena}'\n"
                        cadena2 = cadena2[i:]
                    elif self.es_entero(subcadena):
                        resultado += f"Entero encontrado: '{subcadena}'\n"
                        cadena2 = cadena2[i:]
                    elif self.es_flotante(subcadena):
                        resultado += f"Flotante encontrado: '{subcadena}'\n"
                        cadena2 = cadena2[i:]
                    else:
                        error = True
                        #Verificamos si no se trata de asignación de cadena
                        if cadena2[0] == "'":
                            for k in range(1, len(cadena2)):
                                if cadena2[k] == "'":
                                    print(f"Último valor de k: {k} para el corte de la cadena: {cadena2}")
                                    subcadena = cadena2[:k+1]
                                    resultado += f"Asignacion de cadena: '{subcadena}'\n"
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
                            resultado += f"Error: '{subcadena}'\n"
                            cadena2 = cadena2[i:]

                elif not procesado:
                    cadena2 = cadena2[1:]

        print(resultado)
        #print(f"Cadena final: '{cadena2}'")

if __name__ == "__main__":
    analizador = AnalizadorLexico()
    analizador.analizar()
