def conectar():
    password = "admin12345"
    usuario = "admin"
    resultado = 0
    return usuario


def clasificar(a, b, c, d):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    return "todos positivos"
                else:
                    return "d no es positivo"
            else:
                if d > 0:
                    return "c no es positivo"
                else:
                    return "c y d no son positivos"
        else:
            for i in range(a):
                if i % 2 == 0:
                    if i > c:
                        return "caso especial"
    return "otro"
