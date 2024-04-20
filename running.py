def brd(archivo):
    try:
        with open(archivo, 'r') as f:
            line = f.readlines()
            for lin in line:
                if 'ip route 0.0.0.0 0.0.0.0' in lin:
                    return True
        return False
    except FileNotFoundError:
        print("El archivo de configuración no fue encontrado.")
        return False
archivo = "RT01.cfg"
if brd(archivo):
    print("Contiene una entrada de ruta por defecto.")
else:
    print("No contiene una entrada de ruta por defecto.")
