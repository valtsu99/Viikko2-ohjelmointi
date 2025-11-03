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


def tulosta_varaus(varaus_tiedot, rivinumero=None):
    """Tulostaa yhden varauksen tiedot (robustimpi käsittely)"""
    try:
        if len(varaus_tiedot) < 10:
            raise ValueError(f"Liian vähän kenttiä ({len(varaus_tiedot)})")
        # Trimmaa kentät
        f = [s.strip() for s in varaus_tiedot]

        # Normalisoi päivämäärä YYYY-M-D -> YYYY-MM-DD
        date_raw = f[2]
        parts = date_raw.replace('/', '-').split('-')
        if len(parts) == 3:
            year, month, day = parts
            month = month.zfill(2)
            day = day.zfill(2)
            date_norm = f"{year}-{month}-{day}"
        else:
            raise ValueError(f"Virheellinen päivämäärä: '{date_raw}'")

        # Normalisoi aika H:M -> HH:MM
        time_raw = f[3].replace('.', ':')
        tparts = time_raw.split(':')
        if len(tparts) == 2:
            hour = tparts[0].zfill(2)
            minute = tparts[1].zfill(2)
            time_norm = f"{hour}:{minute}"
        else:
            raise ValueError(f"Virheellinen aika: '{time_raw}'")

        from datetime import datetime
        paiva = datetime.strptime(date_norm, "%Y-%m-%d")
        suomalainenpaiva = paiva.strftime("%d.%m.%Y")
        aika = datetime.strptime(time_norm, "%H:%M")
        suomalainenaika = aika.strftime("%H.%M")

        varausnumero = int(f[0])
        varaaja = f[1]
        tuntimaara = int(f[4])
        tuntihinta = float(f[5])
        maksettu = f[6].lower() in ("true", "kyllä", "yes", "1")

        print(f"\nVarausnumero: {varausnumero}")
        print(f"Varaaja: {varaaja}")
        print(f"Päivämäärä: {suomalainenpaiva}")
        print(f"Aloitusaika: {suomalainenaika}")
        print(f"Tuntimäärä: {tuntimaara}")
        print(f"Tuntihinta: {tuntihinta} €")
        print(f"Kokonaishinta: {tuntihinta * tuntimaara} €")
        print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
        print(f"Kohde: {f[7]}")
        print(f"Puhelin: {f[8]}")
        print(f"Sähköposti: {f[9]}")
        print("-" * 50)

    except Exception as e:
        prefix = f"Rivillä {rivinumero}: " if rivinumero is not None else ""
        print(f"{prefix}Virhe varauksen käsittelyssä: {e}")


def main():
    varaukset = "varaukset.txt"
    try:
        with open(varaukset, "r", encoding="utf-8") as f:
            for i, rivi in enumerate(f, start=1):
                rivi = rivi.strip()
                if not rivi:
                    continue
                varaus_tiedot = rivi.split("|")
                tulosta_varaus(varaus_tiedot, rivinumero=i)

    except FileNotFoundError:
        print(f"Tiedostoa {varaukset} ei löydy")
    except Exception as e:
        print(f"Tapahtui virhe: {e}")

if __name__ == "__main__":
    main()