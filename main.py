class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f'Titlu: {self.titlu}, Autor: {self.autor}, ISBN: {self.isbn}'


class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f'Cartea "{carte.titlu}" a fost adăugată în bibliotecă.')

    def elimina_carte(self, isbn):
        for carte in self.carti:
            if carte.isbn == isbn:
                self.carti.remove(carte)
                print(f'Cartea "{carte.titlu}" a fost eliminată din bibliotecă.')
                return
        print(f'Nu există nicio carte cu ISBN-ul {isbn} în bibliotecă.')

    def afiseaza_carti(self):
        if not self.carti:
            print('Biblioteca este goală.')
        else:
            print('Cărți în bibliotecă:')
            for carte in self.carti:
                print(carte)

if __name__ == "__main__":
    biblioteca = Biblioteca()

    carte1 = Carte("Harry Potter", "J.K. Rowling", "9753")
    carte2 = Carte("Dune", "Frank Herbert", "1449")

    biblioteca.adauga_carte(carte1)
    biblioteca.adauga_carte(carte2)

    biblioteca.afiseaza_carti()

    biblioteca.elimina_carte("9753")

    biblioteca.afiseaza_carti()

