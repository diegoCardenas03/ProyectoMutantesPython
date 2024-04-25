from functions import *
# PRUEBAS:
adn = ['ATGCGA',
       'CAGTGC',
       'TCATGT',
       'AGCAGG',
       'CCCCTA',
       'TCACCG']  # Hay una diagonal principal AAAA, y una diagonal CCCC debajo, retorna True
print(is_mutant(adn))

adn = ['ATGCGA',
       'TGGTGC',
       'TCAGGT',
       'AGCAAG',
       'CACCTG',
       'TCACCG']  # Hay solo una diagonal de izquierda a derecha CCCC, retorna False
print(is_mutant(adn))

adn = ['ATGCCA',
       'CAGCAC',
       'TTCAGT',
       'ACAAGG',
       'ACCCTA',
       'TCACTG']  # Hay dos diagonales inversas, AAAA, CCCC, retorna True
print(is_mutant(adn))

adn = ['TTAAAA',
       'CGCTAC',
       'ACAAAG',
       'AGTTGT',
       'CCAGTA',
       'ATTTTG']  # Hay dos horizontales AAAA, TTTT, retorna True
print(is_mutant(adn))

adn = ['ATTCGA',
       'CTCTAC',
       'ATAAAG',
       'ATACTT',
       'CCAGTA',
       'TAAATG']  # Hay dos verticales, TTTT, AAAA, retorna True
print(is_mutant(adn))

adn = ['ATTCGA',
       'CGCTAC',
       'AAAAGG',
       'AGTTGT',
       'CCAGTA',
       'TATATG']  # Hay solo una horizontal AAAA, retorna False
print(is_mutant(adn))

adn = ['TTATAA',
       'TGCTAC',
       'TCAAAG',
       'TGTTGT',
       'CCAGTA',
       'TAGATG']  # Hay una vertical TTTT, y una diagonal inversa GGGG, retorna true

print(is_mutant(adn))

adn = []
j = 5
for i in range(0, 6):

    while True:
        print('Recordatorio: Los genes pueden ser A,G,C o T')
        string_adn = input('Ingrese los 6 genes en una linea: ').upper()  # Ingreso en una String las lineas de los genes.
        if len(string_adn) == 6 and contains_adn(string_adn):  # Con una función verifico que cada letra sea válida.
            print('Recibido.')
            if j != 0:
                print(f'{j} lineas restantes...')
            j -= 1
            adn.append(string_adn)
            break
        else:
            print('Ha ingresado los genes incorrectamente...')
            print('Intente de nuevo.')
            continue
print(' ')
print('Matriz ingresada: ')
for adn_line in adn:
    print(adn_line)

print(' ')

if is_mutant(adn):
    print('Es mutante.')
else:
    print('No es mutante.')
