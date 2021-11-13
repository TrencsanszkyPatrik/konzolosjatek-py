#Határozzuk meg a jatek végét, az újrakezdést és az egésznek a kezdését

def jatek_vege(reason):
    print("\n" + reason)
    ujrakezdes()

def ujrakezdes():
    print("Szeretnéd előről kezdeni a játékot?")
    answer = input(">").lower()
    if "igen" in answer:
        inditas()
    else:
         jatek_vege()



nev = input("Add meg a karakterneved:  ")


def inditas():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟                                                                                     ╢")
    print("╟                     Üdvözöllek a játékomban, " +str(nev)+ "!                          ╢")
    print("╟                                                                                     ╢")
    print("╟Patriknak hívnak, és ez az első PYHTON-ban írt játékom. Nem valami nagyszám, de,     ╢")
    print("╟remélem élvezhető lesz! Jó szórakozást!                                              ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
    print("\n")
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print('╟Ha készen állsz a játékra, gépeld be azt a szót, hogy "indítás", és nyomj egy entert ╢')
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")

    answer = input(">").lower()

    if "indítás" in answer:
        egyes_szoba()
    else:
        
        
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟Helytelen válasz. Nézz meg, nem-e írtál el valamit!                                  ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
        inditas()

#legelső szoba, háram választási lehetőséggel


def egyes_szoba():
    
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟Egy üres szobában kelsz fel, egyetlen egy dolog van előtted, egy sima kulcs..        ╢")
    print("╟Mit teszel?                                                                          ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
    print("\n")
    

    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟a, Felveszed, majd kinyitod az előtted lévő ajtót.                                   ╢")
    print("╟                                                                                     ╢")
    print("╟b, A szobába maradsz, és félsz tovább haladni.                                       ╢")
    print("╟                                                                                     ╢")
    print("╟c, Megpróbálod kinyitni az ajtót, hátha nyitva találod.                              ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")


    answer = input(">")

    if answer == "a":
        
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟A kulcs kinyitotta az ajtót, haladhatsz tovább...                                    ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
        kettes_szoba()
    elif answer == "b":
        
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟A szobák falai elkezdenek összeszűkülni, ami miatt a karaktered be is pánikolt..     ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
        egyes_szoba_2()
    elif answer == "c":
            
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟Az ajtót többszöri próbálkozásra se sikerült kinyitnod..                             ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
    egyes_szoba_3()

def egyes_szoba_2():
    
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟Mit teszel?                                                                          ╢")
    print("╟                                                                                     ╢")
    print("╟a, Felkapod a lehető leggyorsabban a kulcsot, és kinyitot vele az ajtót              ╢")
    print("╟                                                                                     ╢")
    print("╟b, Feladod az egészet, és meghalsz..                                                 ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")

    
    answer = input(">")

    if answer == "a":
        
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟Felkaptad a kulcsot, ezáltal haladhatsz tovább...                                    ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
        kettes_szoba()
    elif answer == "b":
        
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟A karaktered feladta, és a falak teljesen összepréselték..                           ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
    
    jatek_vege("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    jatek_vege("╟A karaktered meghalt.. Sajnálatos                                                    ╢")
    jatek_vege("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")

    ujrakezdes()

def egyes_szoba_3():
    
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟Az ajtó nem nyílik, sőt mi több, idegességedben annyira megrántottad a kilincset,    ╢")
    print("╟hogy belülről letörted, így az egyetlen kijutásra alkalmas utadat is tönkretetted.   ╢") 
    print("╟                                                                                     ╢")
    print("╟Komolyan, nem lett volna egyszerűbb kinyitni a kulcssal?                             ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
    

    jatek_vege("╟A karaktered meghalt.. Sajnálatos                                                    ╢")
    
    ujrakezdes()


def kettes_szoba():
    
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟Az ajtót kitárva, egy sötét folyosó mered a szemed elé, mindent a feketeség leple    ╢")
    print("╟fed, a végéből kiszűrődő halovány világitást leszámítva.                             ╢")
    print("╟Mit teszel?                                                                          ╢")
    print("╟                                                                                     ╢")
    print("╟a, Tovább haladsz a fény felé, hátha ott majd megleled a kiutat.                     ╢")
    print("╟                                                                                     ╢")
    print("╟b, Inkább visszamész a szobába, mert a félelem legyőzte kiváncsiságod..              ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")

    answer = input(">")

    if answer == "a":
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟Ahogyan közeledsz a szoba felé, egyre furcsább hangok szűrűdnek ki a szobából..      ╢")
        print("╟                                                                                     ╢")
        print("╟Kinyitod teljesen az ajtót, majd belépsz. Amint bementél az ajtó egyből becsapódott..╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
        harmas_szoba()
    elif answer == "b":    
        print("\n")
        print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
        print("╟Hosszas idő után, rákell jönnöd arra, hogy egy idióta vagy. Nem érkezik segítség, és ╢")
        print("╟egy üres szoba közepén maradsz egyedül.                                              ╢")
        print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
        
 
        jatek_vege("A karaktered meghalt.. Sajnálatos                                                ╢")
        
        ujrakezdes()

def harmas_szoba():
    
    print("\n")
    print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
    print("╟                                                                                     ╢")
    print("╟                                                                                     ╢")
    print("╟                                                                                     ╢")
    print("╟                                                                                     ╢")
    print("╟                                                                                     ╢")
    print("╟                                                                                     ╢")
    print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
    
    answer = input(">")

    if  answer == "a":
            print("\n")
            print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
            print("╟                                                                                     ╢")
            print("╟                                                                                     ╢")
            print("╟                                                                                     ╢")
            print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")

    elif answer == "b":
        
            print("\n")    
            print("╥ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╥")
            print("╟                                                                                     ╢")
            print("╟                                                                                     ╢")
            print("╨ ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ― ╨")
       

inditas() #lefutattja a programot