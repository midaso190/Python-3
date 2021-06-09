boodschappen = {"Wit brood": 2, "Mangosap": 3, "Pindakaas": 2, "Wc-papier": 2, "Borrelnootjes": 3}

def makeproduct():
    begin = input("Welk product is het? ")
    end = input("Hoeveel kost het? ")
    boodschappen[begin] = end

def changeproduct():
    changfr = input("Welk product wil je veranderen? ")
    changto = input("Waar wil je het naar veranderen? ")
    changprc = input("En wat is de prijs daarvan? ")
    del boodschappen[changfr]
    boodschappen[changto] = changprc

def deleteproduct():
    delet = input("Welk product wil je verwijderen? ")
    del boodschappen[delet]
       
def shopping():
    shoppinglist = int(0)
    doorgaan2 = True
    while doorgaan2 == True:
        prc = input("Welk product wil je kopen? (typ x als je klaar bent) ")
        if prc == "x":
            doorgaan2 = False
            shoppingstr = str(shoppinglist)
            print("Prijs: " + shoppingstr)
        else:
            if prc in boodschappen:
                add = int(boodschappen[prc])
                shoppinglist = shoppinglist + add
            else:
                print("Dit product zit niet in uw boodschappenlijst.")

def bepaalkeuze (keuze):
    if keuze == "1":
        print("Boodschappenlijst:")
        print(boodschappen)
    
    if keuze == "2":
        makeproduct()

    if keuze == "3":
        changeproduct()

    if keuze == "4":
        deleteproduct()
    
    if keuze == "5":
        shopping()

def main():
    keuze = "0"
    while keuze != "x":
        print("Welkom bij SANEX online supermarkten.")
        print("")
        print("Opties:")
        print("- Productenoverzicht   (1)")
        print("- Product toevoegen    (2)")
        print("- Product aanpassen    (3)")
        print("- Product verwijderen  (4)")
        print("- Boodschappen doen    (5)")
        print("- Stoppen              (x)")
        keuze = input("Hoe kan ik u helpen? ")
        bepaalkeuze(keuze)
main()  
