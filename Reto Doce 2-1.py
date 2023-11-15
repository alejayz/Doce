def numVocales(x: str)->int: #se define la función
    letra = 0
    for i in x: #se utiliza un ciclo for para recorrer el texto
        if i.isalpha() and i in "aeiou" or i in "AEIOU": #como condicion se verifica que se tomen en cuenta solo las letras y que sean vocales
            letra += 1 
    return letra


if __name__ == "__main__":
    s = "mbox-short.txt" #se define una variable con el archivo a utilizar
    with open(s, "r") as file: #se abre el archivo
        vocales = numVocales(file.read())
        print(f"Hay {vocales} vocales en el archivo.") #imprime el número de vocales