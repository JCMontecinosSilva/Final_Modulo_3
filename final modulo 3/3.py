

nombres = ["Harry Houdini ","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]
magos = ["Harry Houdini ","David Blaine","Teller"]
cientificos = ["Newton","Hawking","Einstein"]



def solo_magos(lista):
    for i in range (len(lista)):
        lista[i]= lista[i]      
    return lista

datos_solo_mago= solo_magos(magos)

i=0
while i <len(datos_solo_mago):
    print(datos_solo_mago[i])
    i=i+1 
    
print("")   
def solo_cientificos(lista):
    for i in range (len(lista)):
        lista[i]= lista[i]      
    return lista
    
datos_solo_cientificos= solo_cientificos (cientificos)

i=0
while i <len(datos_solo_cientificos):
    print(datos_solo_cientificos[i])
    i=i+1 
    
print("")     
        
def hacer_grandioso(lista):
    for i in range (len(lista)):
        lista[i]= lista[i]      
    return lista
    
datos_hacer_grand= hacer_grandioso (magos)

i=0
while i <len(datos_hacer_grand):
    print("El Grandioso "+datos_hacer_grand[i])
    i=i+1 