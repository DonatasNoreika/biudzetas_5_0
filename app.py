from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("""1 - įvesti pajamas
2 - įvesti išlaidas
3 - ataskaita
4 - balansas
0 - išeiti
"""))
    match veiksmas:
        case 1:
            suma = float(input("Suma: "))
            siuntejas = input("Siuntėjas: ")
            info = input("Papildoma informacija: ")
            biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
        case 2:
            suma = float(input("Suma: "))
            budas = input("Mokėjimo būdas: ")
            isigyta = input("Įsigyta prekė/paslauga: ")
            info = input("Papildoma informacija: ")
            biudzetas.prideti_islaidu_irasa(suma, budas, isigyta, info)
        case 3:
            print("-------------------")
            print("Ataskaita:")
            for irasas in biudzetas.zurnalas:
                print(irasas)
            print("-------------------")
        case 4:
            print("Balansas:", biudzetas.gauti_balansa())
        case 0:
            break
        case _:
            print("Nera tokio pasirinkimo")
