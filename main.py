import datetime
import os

def request_birthdate():
    str = input("Digite a data de nascimento: ")
    birthdate = get_date_by_string(str)
    if (birthdate == datetime.datetime.min):
        print("A data informada é inválida!")
        request_birthdate()
        return

    now = datetime.datetime.today()
    if (birthdate >= now):
        print("Essa pessoa ainda não nasceu!")
        request_birthdate()
        return

    age = get_age(birthdate)
    print(f"A idade é: {age} anos.")
    print("")
    print("Deseja verificar outra idade?")
    print("")
    print("S - Sim")
    print("N - Não")
    print("")

    request_action()

def get_date_by_string(str):
    ret = datetime.datetime.min
    try:
        ret = datetime.datetime.strptime(str, "%d/%m/%Y")
    except:
        pass

    return ret

def get_age(date):
    today = date.today()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    return age

def request_action():
    key = input().upper()
    if (key == "S"):
        clear_console()
        request_birthdate()
    elif (key == "N"):
        clear_console()
        quit()
    else:
        request_action()

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

clear_console()
request_birthdate()