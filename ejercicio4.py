combustible = float(input("Ingrese el combustible utilizado durante el recorrido (L): "))
recorrido = float(input("Ingrese el recorrido realizado (km): "))
km_por_litro_de_combustible = combustible/recorrido
print("\nSu consumo de combustible por kilómetro recorrido es: ", km_por_litro_de_combustible,"L/km")