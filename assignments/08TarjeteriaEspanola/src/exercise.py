
def main():
    #escribe tu código abajo de esta línea
def areaRect(x,y):
    w=x*35
    v=y*12

    if w>v:
        print("El número máximo de tarjetas que se pueden hacer es: ",v )
        return v
    else:
        print("El número máximo de tarjetas que se pueden hacer es: ",w )
        return w


a = int(input("Dame la cantidad de pliegos de papel albanene: " ))
b = int(input("Dame la cantidad de plumones: " ))

r = areaRect(b,a)
    pass

if __name__=='__main__':
    main()
