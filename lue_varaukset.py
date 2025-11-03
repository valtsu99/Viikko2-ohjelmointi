"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""


def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
    
    # Jaetaan varaus osiin
    varaus_tiedot = varaus.split("|")
    
    # Muunnetaan varaus osiin
    varausnumero = int(varaus_tiedot[0])
    tuntihinta = float(varaus_tiedot[5])
    maksettu = varaus_tiedot[6].strip().lower() == "kyllä"
    
    from datetime import datetime
    paiva = datetime.strptime(varaus_tiedot[2], "%d.%m.%Y")
    suomalainenpaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus_tiedot[3], "%H.%M")
    suomalainenaika = aika.strftime("%H.%M")
    
    # Tulostetaan tiedot
    print(f"Varausnumero: {varausnumero}")
    print(f"Varaaja: {varaus_tiedot[1]}")
    print(f"Päivämäärä: {suomalainenpaiva}")
    print(f"Aloitusaika: {suomalainenaika}")
    print(f"Tuntimäärä: {varaus_tiedot[4]}")
    print(f"Tuntihinta: {tuntihinta} €")
    print(f"Kokonaishinta: {tuntihinta * float(varaus_tiedot[4])} €")
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    print(f"Kohde: {varaus_tiedot[7]}")
    print(f"Puhelin: {varaus_tiedot[8]}")
    print(f"Sähköposti: {varaus_tiedot[9]}")
    
    
if __name__ == "__main__":
    main()