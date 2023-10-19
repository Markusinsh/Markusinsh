def materialaUzskaite (tips, izmers1, izmers2, skaits):
    if tips == "FINIERIS":
        print (f"Uzskaitīt {skaits} gab. finiera plāksnes, izmēri: {izmers1} cm x {izmers2} cm") # Ievietojiet šeit kodu, lai veiktu finiera plāksnes uzskaiti
    elif tips == "LISTE":
        print (f"Uzskaitīt {skaits} gab. listes detaļas, garums: {izmers1} cm")
        # Ievietojiet šeit kodu, lai veiktu listes detaļu uzskaiti
    elif tips == "STURIS":
        print (f"Uzskaitit {skaits} gab. stūru, izmēri: {izmers1} cm x {izmers2} cm")
        # Ievietojiet šeit kodu, lai veiktu stūru uzskaiti
    else:
        print("Nederigs tips")
 
def materialaAprekins (garums, platums, augstums, skaits):
    if garums <= 0 or platums <= 0 or augstums <= 0 or skaits <= 0:
        print("Nederīgi parametri. Visi parametri jābut pozitiem skaitliem un skaits jabūt lielākam par 0")
        return
    
    if augstums == 1:
        tips = "FINIERIS"
        izmers1 = garums
        izmers2 = platums
    elif augstums == 2:
        tips = "LISTE"
        izmers1 = garums
        izmers2 = None
    elif augstums == 3:
        tips = "STURIS"
        izmers1 = garums
        izmers2 = platums
    else:
        print("Nederīgs augstums. Augstumam jābut 1, 2 vai 3.")
        return
    
    materialaUzskaite(tips, izmers1, izmers1, skaits)

# Piemēri, kā izsaukt funkcijas: 
materialaAprekins (100, 50, 1, 5) # Pieņemsim, ka finiera plāknes augstums ir 1
materialaAprekins (80, 30, 2, 10) # Pieņemsim, ka listes augstums ir 2
materialaAprekins (60, 60, 3, 8)  # Pieņemsim, ka stūriem augstums ir 

