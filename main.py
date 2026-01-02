###Calculadora de limite

def limite_calc():
    while True:
        try:
            saldo = float(input("Insira o Saldo médio: "))
            if type(saldo) is float:
                break
        except ValueError:
            print("\nERRO! Insira um valor válido")
            
            
    if saldo <500: print("\nNão há limite")
    elif 500 <= saldo <=1000: print(f"\nSeu limite é de: {saldo*0.08:.2f}")
    elif saldo >1000: print(f"\nSeu limite é de: {saldo*0.14:.2f}")
    
limite_calc()
