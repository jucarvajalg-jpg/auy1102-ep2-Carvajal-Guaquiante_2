"""Catálogo de libros de BiblioTech.

Antes de registrar un libro nuevo, el sistema valida su código ISBN-13.
"""


def validar_isbn13(isbn):
    """Devuelve True si `isbn` es un ISBN-13 válido.

    Acepta el ISBN con o sin guiones: "978-956-12-1234-5" o "9789561212345".

    Regla del dígito verificador (ISBN-13):
      1. Se toman los primeros 12 dígitos.
      2. Se multiplican alternadamente por 1 y por 3 (el primero por 1,
         el segundo por 3, el tercero por 1, y así sucesivamente).
      3. Se suman los productos.
      4. verificador = 10 - (suma % 10). Si el resultado es 10, el verificador es 0.
      5. El ISBN es válido si el verificador coincide con el dígito 13.
    """
    limpio = isbn.replace("-", "")
    if len(limpio) != 13 or not limpio.isdigit():
        return False

    suma = 0
    for posicion, digito in enumerate(limpio[:12]):
        peso = 1 if posicion % 2 == 0 else 3
        suma += int(digito) * peso

    verificador = (10 - (suma % 10)) % 10
    return verificador == int(limpio[12])
