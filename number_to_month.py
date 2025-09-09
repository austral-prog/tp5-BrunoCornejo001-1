def number_to_month(month):
    num = int(input("Ingrese un numero entre el 1 y el 12:"))
    if num == 1:
        return "enero"
    elif num == 2:
        return "febrero"
    elif num == 3:
        return "marzo"
    elif num == 4:
        return "abril"
    elif num == 5:
        return "mayo"
    elif num == 6:
        return "junio"
    elif num == 7:
        return "julio"
    elif num == 8:
        return "agosto"
    elif num == 9:
        return "septiembre"
    elif num == 10:
        return "octubre"
    elif num == 11:
        return "noviembre"
    elif num == 12:
        return "diciembre"
    elif num < 1 or num > 12:
        return "error"
