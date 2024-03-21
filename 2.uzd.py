import csv

def teksts(filename):
    with open(filename, 'r', encoding='utf-8') as teksta_fails:
        lasit = csv.reader(teksta_fails)
        print("Teksta fails CSV formātā:", lasit)
        