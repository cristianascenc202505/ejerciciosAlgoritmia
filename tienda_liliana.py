import random

compra=float(input("Digite el valor de la compra: "))
b_r=0
b_v=1
b_b=2
b_n=3
b_a=4
bolsa= random.randint(0,4)

if compra <= 50.000:
    print(f"El valor de la compra no supera los $ 50.000 ,por lo cual no aplica ningun descuento \n \nValor de compra {compra:.3f} ")
else:
    if compra > 50.000:
        print(f"El valor de la compra supera los $ 50.000 ,por lo cual aplica descuento segun balota \nValor de compra {compra:.3f} \n")
        
        print("Intoduce la mano en la bolsa y saca una balota para obtener un descuento en tu compra \n")
        if bolsa==0:
            d=compra*1.0
            t_pago=compra-d
            print(f"Ha sacado la balota Roja obteniendo el (100%) de descuento.\nEl valor de la compra es {compra:.3f}.\nEl valor del descuento {d:.3f}\nTotal a pagar menos el descuento {t_pago:.3f}")
        elif bolsa==1:
            d=(compra*100)/100
            t_pago=compra-d
            print(f"Ha sacado la balota Verde obteniendo el (50%) de descuento.\nEl valor de la compra es {compra:.3f}.\nEl valor del descuento {d:.3f}.\nTotal a pagar menos el descuento {t_pago:.3f}")
        elif bolsa==2:
            d=(compra*50)/100
            t_pago=compra-d
            print(f"Ha sacado la balota Blanca obteniendo el (30%) de descuento.\nEl valor de la compra es {compra:.3f}.\nEl valor del descuento {d:.3f}.\nTotal a pagar menos el descuento {t_pago:.3f}")
        elif bolsa==3:
            d=(compra*30)/100
            t_pago=compra-d
            print(f"Ha sacado la balota Negra obteniendo el (20%) de descuento. \nEl valor de la compra es {compra:.3f}. \nEl valor del descuento {d:.3f}. \nTotal a pagar menos el descuento {t_pago:.3f}")
        elif bolsa==4:
            d=(compra*20)/100
            t_pago=compra-d
            print(f"Ha sacado la balota Amarilla obteniendo el (10%) de descuento. \nEl valor de la compra es {compra:.3f}.\nEl valor del descuento {d:.3f}.\nTotal a pagar menos el descuento {t_pago:.3f}")
        
    
    