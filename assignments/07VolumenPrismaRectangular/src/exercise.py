
def main():
    #escribe tu código abajo de esta línea
    def areaRect(x,y):
    ss=x*y
    return ss

def volumenRect(x,y):
    ss1=x*y
    print("El volumen del prisma es: ",ss1 )
    return ss1

h = float(input ("Dame la base: " ))
b = float(input ("Dame la altura: " ))
p=float(input("Dame la profundidad: "))

a = areaRect(h,b)
v = volumenRect (a,p)

    pass

if __name__=='__main__':
    main()
