# creacion
flores = ["rosas", 222, 33.8]
print(flores)


# lista en blanco
y=[]
print(y)

# lectura de los elementos de izquierda a derecha basado en su indice

eluno=flores[0]
print(eluno)
eldos=flores[1]
print(eldos)
eltres=flores[2]
print(eltres)

# lectura de derecha a izquierda
reluno=flores[-1]
print(reluno)
reldos=flores[-2]
print(reldos)
reltres=flores[-3]
print(reltres)

# recorrer lista con un for

for i in flores:
    print(i)

# concatenar listas

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

# creacion de listas. repeticion de listas

d=[0] * 4
print(d)

f=[1,2,3] * 3
print(f)

f=f*2
print(f)

# rebanar listas

ls=["a","b","c","d","e","f"]
# rebanar los elementos 1 y 2

lsr1 = ls[1 : 3]
print(ls)
print(lsr1)

# rebanar el elemento 3 y 4
lsr2=ls[3:5]
print(ls)
print(lsr2)

# rebanar el elemento 1
lsr3=ls[0:1]
print(ls)
print(lsr3)

# rebanar el elemento 0 y 1
lsr4=ls[0:2]
print(ls)
print(lsr4)

# rebanar hasta el 4 elemento
lsr5=ls[:4]
print(ls)
print(lsr5)

# rebanar desde el 2 elemento
lsr6=ls[2:]
print(ls)
print(lsr6)

# metodos de listas

# adicionar elementos al final de la lista

ls.append("z")
print(ls)

ls.append("p")
print(ls)

# extend

ls1=["a","b","c"]
ls2=["d","e","f"]
ls1.extend(ls2)
print(ls1)

ls2.extend(ls1)
print(ls2)


# ordenar listas

ls=[98,56,3,0,1,4,-1]
print(ls)
ls.sort()
print(ls)

# reversar o voltear listas

ls=[5,2,0,8,-2]
print(ls)
ls.reverse()
print(ls)

#count
#cuenta el numero de ocurrencias de un elemnto
# el 4 tiene 2 ocurrencias


ls=[-1,0,1,3,4,56.98,4]
a=ls.count(4)
print(ls)
print(a)

# en que poscicion de la lista se encuentra el elemento 1

ls=[-1,0,1,3,8,56,98,4]
print(ls)
a=ls.index(1,1)
print(a)


numeros = [1, 2, 2, 3, 9, 5, 6, 10]
palabras = ["Yo", "amo", "Python", "Yo", "amo"]
print(numeros)
#para hallar el indice del elemento 9
#4
print(numeros.index(9))
print(numeros.index(2))
print(palabras.index("Yo"))
#print(palabras.index("soy"))

# Insertar elementos en una determinada posicion

ls=[-1,0,1,3,4,56,98,47]
print(ls)
ls.insert(2,899)
print(ls)

# borrar elementos de la lista basado en el index
ls=[9,569,71,-2,76.5,102]
print(ls)
e=ls.pop(4)
print(e)
print(ls)

#remove
ls=[9,569,71,-2,76.5,102]
print(ls)
ls.remove(76.5)
print(ls)








