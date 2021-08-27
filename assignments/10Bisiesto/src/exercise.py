
def main():
    #escribe tu código abajo de esta línea
    def areaRect(x):
    w=x/4
    w2=round(w,0)

    if w == w2:
        print("TRUE")
        return w
    else:
        print("FASE")
        return w


a = int(input("Dame un año: " ))
r = areaRect(a)
    pass

if __name__=='__main__':
    main()
