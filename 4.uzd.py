import json
import csv

def read_file(filename):
    try:
        with open (filename, 'r', encoding='utf8') as file:
            content=file.read()
            return content
        
    except Exception as e:
        return f"Kļūda:{e}"
        
def lasit_json(failanosaukums):
    with open(failanosaukums, 'r') as json_fails:
        dati = json.load(json_fails)
        print("JSON fails satur šādu informāciju:")
        print(dati)

def lasit_csv(fails):
    with open(fails, 'r', newline='', encoding='utf-8') as csv_fails:
        lasitajs = csv.reader(csv_fails)
        print("CSV fails satur šādu informāciju:")
        for rinda in lasitajs:
            print(', '.join(rinda))


def error(faili, paplasinajums):
    if paplasinajums == 'json':
        lasit_json(faili)
    elif paplasinajums == 'txt':
        lasit_txt(faili)
    elif paplasinajums == 'csv':
        lasit_csv(faili)
    else:
        print("šāds paplašinājuma fails nav pieejams.")