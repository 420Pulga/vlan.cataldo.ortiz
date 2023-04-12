#ejercicio N1

vlan = input("Ingrese el nomero de la VLAN que desea configurar: ")
despri = input("Ingrese el nombre de la vlan: ")
purtroncal = input("Ingrese el puerto del trocal: ")
puervlan = input("Ingrese el puerto de acceso para la vlan: ")

lista = [
    
    f"vlan {vlan}\n",
    f"name {despri}\n",

    f"interface {puervlan}",
    f"Switchport Access vlan {vlan}",
    f"Description ***{despri}***",
    "Duplex full",
    "Speed 100",
    "Spanning-tree portfast\n",
    
    f"interface {puervlan}",
    f"Switchport trunk allowed vlan add {vlan}",
    
]

for lista in lista:
    print(lista)
    
print("Para validar la configuración ejecute lo siguiente:")
print(
 "Show interface trunk\n",
 "Show vlan\n",
 f"Show  interfaces {puervlan} switchport")