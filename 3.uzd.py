import json

def jsonfails(filename):
    try:
        with open(filename, 'r') as json_fails:
            dati = json.load(json_fails)
            print(dati)
            
    except Exception as e:
        print(f"Kļūda{e}")