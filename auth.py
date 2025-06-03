def login():
    print("=== Inicio de sesión ===")
    usuario_valido = "admin"
    contrasena_valida = "1234"

    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario == usuario_valido and contrasena == contrasena_valida:
        print("Acceso concedido.")
        return True
    else:
        print("Acceso denegado. Usuario o contraseña incorrectos.")
        return False