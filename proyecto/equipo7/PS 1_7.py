Costo_auto=int(input("Ingrese el valor del vehiculo:$ "))
Enganche=(Costo_auto*0.35)
Mensualidad=((Costo_auto-Enganche)*(1+0.12)/36)
print(f"El enganche del vehiculo sera de:${Enganche}")
print(f"La cuota mensual seria de:${Mensualidad}, por 36 meses")
