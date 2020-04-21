print("Bienvenido a mi calculadora v:")
primer_dato = int(input("Ingrese el primer dato:\n \n"))
segundo_dato = int(input("Ingrese el segundo dato:\n \n"))
operador = int(input("\n1.-Suma \n2.-Resta\n3.-Multiplicacion\n4.-Division\n" ))
if operador==1:
	print(primer_dato + segundo_dato)
elif operador==2:
	print(primer_dato - segundo_dato)
elif operador==3:
	print(primer_dato * segundo_dato)
elif operador==4:
	print(primer_dato / segundo_dato)

input()