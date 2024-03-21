def kolonna(fails):
    try:
        with open(fails, 'r', encoding='utf-8') as teksta_fails:
            print("Ceturtās kolonnas dati:")
            for rinda in teksta_fails:
                kolonnas = rinda.split()  
                if len(kolonnas) >= 4:  
                    ceturta_kolonna = kolonnas[3]  
                    print(ceturta_kolonna)
                else:
                    print("Nav ceturtās kolonnas")
    except Exception as e:
        print(f"Kļūda {e}")