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
        
        cadena2 = " identificador123 Mientras { dob} cadena"

        def procesar_cadena(cadena2):
            global resultado
            for nombre_categoria, categoria in zip(nombres_categorias, categorias):
                for cadena1 in categoria:
                    cadena2, recortado = self.recortar_cadena(cadena1, cadena2)
                    if recortado:
                        resultado += f"{nombre_categoria}: '{cadena1}'\n"
                        return cadena2, True
            return cadena2, False

        while cadena2:
            cadena2, procesado = procesar_cadena(cadena2)
            if not procesado and cadena2 and not cadena2[0].isspace():
                # Extraer identificador o verificamos si esa parte de la cadena
                # es un identificador
                i = 0
                while i < len(cadena2) and cadena2[i].isalnum():
                    i += 1
                identificador = cadena2[:i]
                if self.es_identificador(identificador):
                    resultado += f"Identificador encontrado: '{identificador}'\n"
                    cadena2 = cadena2[i:]
                else:
                    cadena2 = cadena2[1:]
            elif not procesado:
                cadena2 = cadena2[1:]

        print(resultado)
        print(f"Cadena final: '{cadena2}'")

if __name__ == "__main__":
    analizador = AnalizadorLexico()
    analizador.analizar()
