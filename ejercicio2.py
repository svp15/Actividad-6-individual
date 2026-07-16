class ArticuloCientifico:

    def __init__(self, titulo, autor, palabras_claves=None,
                 publicacion=None, anio=None, resumen=None):
        self.titulo = titulo
        self.autor = autor
        self.palabras_claves = palabras_claves if palabras_claves is not None else [None] * 3
        self.publicacion = publicacion
        self.anio = anio
        self.resumen = resumen

    def imprimir(self):
        print("Título del artículo =", self.titulo)
        print("Autor del artículo =", self.autor)
        print("Palabras clave =")

        for palabra in self.palabras_claves:
            print(palabra)

        print("Publicación =", self.publicacion)
        print("Año =", self.anio)
        print("Resumen =", self.resumen)


if __name__ == "__main__":
    palabras = ["Física", "Espacio", "Tiempo"]

    articulo = ArticuloCientifico(
        "La teoría especial de la relatividad",
        "Albert Einstein",
        palabras,
        "Anales de Física",
        1913,
        "Las leyes de la física son las mismas en todos los sistemas de referencia inerciales."
    )

    articulo.imprimir()
