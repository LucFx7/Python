import random

def llegir_llista_enters():
    llista = []
    j="j"
    while j!=".":
        j=input("Introdueix un número enter: ")
        if j!=".":
            llista.append(int(j))
    return llista

def senars_llista(llista):
    for e in llista:
        if e%2!=0:
            print(e)
            

def sumar_parells_llista(llista):
  return  (sum(n for n in llista if n%2==0))

def cercar_numero_llista(llista, numero):
    if numero in llista:
        print("El numero {} esta dins la llista".format(numero))
    else:
        print("El numero {} no esta dins la llista".format(numero))
        
    return llista
        
"""a = llegir_llista_enters()
llista = [int(n) for n in a]
numero=int(input("Introdueix un numero que vulguis cercar:"))"""


def llegir_llista_paraules():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix una paraula: ")
        if a!=".":     
            l.append(a)
    return l

def crear_paraula_llista(llista):
    return [p[0] for p in llista]
    
"""a = llegir_llista_paraules()
print(crear_paraula_llista(a))"""

def crear_llista_aleatoris():
    return [random.randint(1,100) for i in range(5)]

"""a=crear_llista_aleatoris()
print(a)"""


def comparar_llistes(llista1,llista2):
    r = []
    for i, (a,b) in enumerate(zip(llista1,llista2)):
        if a == b:
            r.append(2)
        elif b in llista1:
            r.append(1)
        else:
            r.append(0)
    return r
"""llista1 = [random.randint(1,9) for i in range(5)]
llista2 = [random.randint(1,9) for i in range(5)]
Comparar = ("la llista 1 {} i la llista 2 {} i si les comparam 0, si l'element no hi es, 1, si l'element hi es pero no a la mateixa posicio, i 2, si esta en la mateixa posicio: {}".format(llista1,llista2, comparar_llistes(llista1,llista2)))

print(Comparar)"""

def majors_edat(edat1, edat2):
    if edat1 > 17:
        print("Edat1 es major d'edat")
    else:
        print("Edat1 no es major d'edat")
    if edat2 > 17:
        print("Edat2 es major d'edat")
    else:
        print("Edat2 no es major d'edat")
    
    
def menu():
    op = 0
    while op < 1 or op > 9:
        print("Menu")
        print("1. llegir_llista_enters")
        print("2. senars_llista")
        print("3. sumar_parells_llista")
        print("4. cercar_numero_llista")
        print("5. llegir_llista_paraules")
        print("6. crear_paraula_llista")
        print("7. crear_llista_aleatoris")
        print("8. comparar_llistes")
        print("9. majors_edat")
        print("10. Sortir")
        op = int(input("Introdueix una opcio: "))
    return op

b = True
while b:
    op = menu()
    match(op):
        case 1:
            a = llegir_llista_enters()
            llista = [int(n) for n in a]
            print(llista)
        case 2:
            senars_llista(llista)            
        case 3:
            print(sumar_parells_llista(llista))
        case 4:
            numero=int(input("Introdueix un numero que vulguis cercar:"))
            cercar_numero_llista(llista, numero)
        case 5:
            a = llegir_llista_paraules()
            print(a)
        case 6:
            print(crear_paraula_llista(a))
        case 7:
            a=crear_llista_aleatoris()
            print(a)
        case 8:
            llista1 = [random.randint(1,9) for i in range(5)]
            llista2 = [random.randint(1,9) for i in range(5)]
            Comparar = ("la llista 1 {} i la llista 2 {} i si les comparam 0, si l'element no hi es, 1, si l'element hi es pero no a la mateixa posicio, i 2, si esta en la mateixa posicio: {}".format(llista1,llista2, comparar_llistes(llista1,llista2)))
            print(Comparar)
        case 9:
            edat1 = int(input("Introdueix la edat 1: "))
            edat2 = int(input("Introdueix la edat 2: "))
            majors_edat(edat1, edat2)
        case 10:
            b = False
        


   
    




        
    
    

       
    
    



    





  
        
            


    
            

            