def hacer_grandioso(lista):
    for i in range (len(lista)):
        lista[i]= lista[i]      
    return lista


nombres = ["Harry Houdini ","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]
magos = ["Harry Houdini ","David Blaine","Teller"]
cientificos = ["Newton","Hawking","Einstein"]


    
datos_hacer_grand= hacer_grandioso (nombres)

i=0
while i <len(datos_hacer_grand):
    print(datos_hacer_grand[i])
    i=i+1 