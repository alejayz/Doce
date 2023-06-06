def NumConsonantes(x: str)->int: #se define la funcion
    letras = 0
    for i in x: #se utiliza un ciclo for para recorrer el texto
        if i.isalpha() and i not in "aeiou" and i not in "AEIOU": #como condicion se verifica que se tomen en cuenta solo las letras excluyendo las vocales
            letras += 1
    return letras


if __name__ == "__main__":
    s ='brain.txt' #se define una variable con el archivo a utilizar
    with open(s,"r") as f: #se abre el archivo
        Consonantes = NumConsonantes(f.read())
        print("Hay " + str(Consonantes) + " consonantes en el archivo") #imprime el numero de consonantes