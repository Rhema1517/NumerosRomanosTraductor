class RomanNumerals:
    @staticmethod
    def from_roman(val : int) -> str:
        romanos={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        sumatoria =[]
        vacio=[]
        for n2 in val:
            for n,c in romanos.items():
                if n2 == c:
                    sumatoria.append(n)
        respuesta1 = sumatoria[-1]
        while sumatoria != vacio:
            if len(sumatoria) > 1:
                if sumatoria[-1] <= sumatoria[-2]:
                    respuesta1=respuesta1+sumatoria[-2] 
                    sumatoria.pop()
                else:
                     respuesta1=respuesta1-sumatoria[-2] 
                     sumatoria.pop()
            else:
                sumatoria = vacio
        return respuesta1

    @staticmethod
    def to_roman(val : int) -> str: #resive el numero int y lo pasa a str romano
        cadena = str(val)
        w = 0
        lista = []
        for i in cadena:
            lista.append(int(f"{i:0<{len(cadena)-w}} "))
            w += 1
        romanos={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        #numero=int(input())
        respuesta = ''
        for n2 in lista:
        #n2 funciona bien
            for n in romanos:
        # calculadora de 
                if (n == 50 or n == 500) and n2 >= (n-n/5) and n2 <= (n+(n/5)*3):
                    if n2> n:
                        respuesta = respuesta + romanos[n]
                        n2 = n2 - n
                        while n2 >= int(n/5):
                            respuesta = respuesta + romanos[n/5]
                            n2 = n2- n/5
                    elif n2 < n:
                        respuesta = respuesta + romanos[n/5] + romanos[n]
                    else:
                        respuesta = respuesta + romanos[n]
                if n2 == 0 or n2 == 00 or n2 == 000 or n2 == 0000 or n2 == 00000:
                    continue
                if ( n == 10 or n == 100 or n == 1000) and n2 >= (n-n/10) and n2 <= (n+n+n):
                    if n2 == (n-n/10) and not n == 10:
                        respuesta = respuesta + romanos[n/10] + romanos[n]
                    if n2 == (n+n+n):
                        respuesta = respuesta + romanos[n] + romanos[n] + romanos[n]
                    if n2 == (n+n):
                        respuesta = respuesta + romanos[n] + romanos[n]
                if n2 <= (n+3) and n2 >= n-1:
                    if n2 == 5:
                        respuesta = respuesta + 'V'
                    elif n2== n+1:
                        respuesta = respuesta + romanos[n]
                        respuesta = respuesta + 'I'
                    elif n2 == n+2:
                        respuesta = respuesta + romanos[n]
                        respuesta = respuesta +'II'
                    elif n2 == n+3 and not romanos[n] == 'I':
                        respuesta = respuesta + romanos[n]
                        respuesta = respuesta + 'III' #tengo que parchear el 4 que da en este momento IIII
                    elif n2 == n-1: # con esto p}
                        respuesta = respuesta + 'I' + romanos[n]
                    elif n != 50 and n != 500 and n == n2:
                        respuesta = respuesta + romanos[n]
     
        return(respuesta)
p=RomanNumerals()
print(p.to_roman(2812))
p.from_roman('VI')