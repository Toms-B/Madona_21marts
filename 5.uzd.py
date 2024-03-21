def fails(vards, fails):
    try:
        with open(fails, 'a') as f:
            f.write(vards + '\n')
        print("Vārds veiksmīgi ierakstīts failā.")
    except IOError:
        print("Kļūda")

if name == "__main":
    fails = "lietotajs.txt"
    while True:
        vards = input("Ievadiet vārdu")
        if vards.lower() == 'iziet':
            break
        vardafails(vards, fails)