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
simbolo_terminal = [";"]
separador_sentencia = ["\\n"]
simbolos = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", 
            "]", "^", "_", "`", "{", "|", "}", "~", "¿", "¡", "“", "”", "‘", "’"]


directorio = {
    "palabras_reservadas_bucles": ["Mientras ", "Para "],
    "palabras_decision": ["si ", "sino ", "otro "]
}

resultado = ""


class analizador_lexico:
    def recortar_cadena(self, cadena1, cadena2):
        if cadena2.startswith(" "):
            cadena2 = cadena2[1:]
        if cadena2.startswith(cadena1):
            return cadena2[len(cadena1):]
        return cadena2

    def analizar(self):
        # Ejemplo de uso
        catgoria1 = ["estaEsMi"]
        catgoria2 = ["cadena", "cualquiera"]
        categorias = [catgoria1, catgoria2]
        cadena2 = " estaEsMicadenacualquiera"

        for categoria in categorias:
            for cadena1 in categoria:
                cadena2 = self.recortar_cadena(cadena1, cadena2)
                print(f"Después de recortar '{cadena1}': '{cadena2}'")

        print(f"Cadena final: '{cadena2}'")


                        


if __name__ == "__main__":
    analizador = analizador_lexico()
    analizador.analizar()


    