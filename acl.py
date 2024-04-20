def tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "Extendida"
    else:
        return "El número no corresponde a una lista de acceso"
while True:
    try:
       numero_acl = int(input("Por favor, ingresa el número de ACL IPv4: "))
       tipo = tipo_acl(numero_acl)
       print("Tipo de ACL:", tipo)
       break
    except ValueError:
                     print("Error: Ingresa un número válido para la ACL IPv4.")
