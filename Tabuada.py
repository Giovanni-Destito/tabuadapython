def tabuada(x,y,z):
    for i in range(x , y+1):
        tb = (z * i)
        print(z,'x',i,'=',tb)



z = int(input('Digite o número da tabuada que deseja: '))
x = int(input('Multiplicador inicial da tabuada: '))
y = int(input('Multiplicador final da tabuada: '))

tabuada(x,y,z)
