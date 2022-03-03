# Project:  Raumberechnungsprogramm fuer Markler
# Author:   Jasmon Goeckemeyer
# Date:     19.02.2022
# Version:  1.0

# function to calcute the surface
def raumBerechnung(programmAbschnitt):

    seiteA = float(input(f' {programmAbschnitt} Wie lang ist die Seite A? : '))
    seiteB = float(input(f' {programmAbschnitt} Wie lang ist die Seite B? : '))

    return seiteA * seiteB

# function to parse userinput to boolean
def userEingabeZuBoolean(userEingabe):
    boolscherWert = None

    if userEingabe == "y":
        boolscherWert = True
    elif userEingabe == "n":
        boolscherWert = False

    return boolscherWert

# ------------------------- PROGRAM START --------------------------------------
raumAnzahl = int(input("[FRAGE] Wie viele Räume hat das Objekt?: "))
raumNummer = 1
gesamtFlaeche = 0.0

# main loop
while raumAnzahl > 0:

    userAntwort = None
    while userAntwort is None:
        userAntwort = userEingabeZuBoolean(input("[RAUM "
            + str(raumNummer)
            + "] Besteht der Raum aus mehreren Rechtecken? (y|n) : ").lower())

    if userAntwort == True:
        anzahlTeilrechtecke = int(input(" [TEILFLÄCHE] "
            + "Aus wie vielen Teilrechtecken besteht die Fläche? : "))

        teilFlaechenNummer = 1

        while anzahlTeilrechtecke > 0:
            gesamtFlaeche += raumBerechnung("[TEILFLÄCHE "
                + str(teilFlaechenNummer)
                + "]")
            anzahlTeilrechtecke -= 1
            teilFlaechenNummer += 1

    elif userAntwort == False:
        gesamtFlaeche += raumBerechnung("[VOLLFLÄCHE]")

    raumNummer += 1
    raumAnzahl -= 1

print("[ERGEBNIS] Die Gesamtflaeche des Objekts betraegt: "
    + str(gesamtFlaeche)
    + " Meter.")

# ------------------------- PROGRAM END -----------------------------------------