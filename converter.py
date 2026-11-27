import requests
from bs4 import BeautifulSoup

VALUUTAD = ["USD", "EUR", "GBP"]


def konverteeri(summa, alg, siht):
    url = f"https://www.x-rates.com/calculator/?from={alg}&to={siht}&amount={summa}"
    vastus = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    otsi_konverteeritud = BeautifulSoup(vastus.text, "html.parser") # vastus.text on SUUR tekst, kuhu me panime kõik HTML kood et hiljem leida konverteeritud arv soovitud valuutas


    tulemus = otsi_konverteeritud.find("span", class_="ccOutputRslt") # otsib koht kus on juba konverteeritud arv x-rates.com kodulehel
    """ "ccOutputRslt" classi abiga leiame arv """
    tekst = tulemus.text
    arv = tekst.split()[0]
    return float(arv)


def main():
    print("=== Valuutakalkulaator ===")
    print("Valuutad:" + str(VALUUTAD)[1:-1]) # [1:-1] et ei panna [] väljundisse

    try:
        summa = float(input("Sisesta summa: "))
    except ValueError:
        print("Palun sisesta arv!")
        return

    algus = input("Millisest valuutast: ").upper()
    siht = input("Millisesse valuutasse: ").upper()

    if algus not in VALUUTAD or siht not in VALUUTAD:
        print("Kasuta ainult USD, EUR või GBP!")
        return

    tulemus = konverteeri(summa, algus, siht)
    print(f"{summa} {algus} = {tulemus:.2f} {siht}") # et formati korrektselt teha kasutasin AI!


main()