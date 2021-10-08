# Laget av Dmitriy Safiullin. Sist oppdatert: 10.08.2021
# Programmet henter prisdata fra enhver.no. Prisdata blir lagret i ./data mappen.

# Importsetninger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
import json

# Globale variabler
NETTSIDE_URL = 'https://enhver.no/priser/'
DRIVER_URL = "/usr/lib/chromium-browser/chromedriver"
TR_XPATH = "/html/body/div/div/div/div/div/div/div/table/tbody/tr[@class='product']"

# Oppsett av virtuell nettleser
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_URL)
driver.get(NETTSIDE_URL)

# Teller produkter som er funnet
antall_produkter = len(driver.find_elements_by_xpath(TR_XPATH))
antall_butikker = len(driver.find_element_by_xpath(TR_XPATH).find_elements_by_tag_name("td")) - 1
print("Antall produkter funnet: " + str(antall_produkter))
print("Antall butikker funnet: " + str(antall_butikker))

# TODO:
# Finn ut hvilke butikker som er med i tabellen og hvilke indexer de
# hører til. Butikkdataen skal deretter settes inn som et
# eget nøkkel -> verdier forhold i produkter{} i samme stil som
# produktene selv.
# Eksempel: Butikker:{'Kiwi', 'Meny', 'osv', 'osv'}

# Henter produktnavn og setter dem inn som nøkler i produkter{}
produkter = {}

# Henter prisinformasjon og putter den inn som verdier i produkter{}
for rad in driver.find_elements_by_xpath(TR_XPATH):
    produkt = rad.find_element_by_tag_name("td").text.replace("\n", ", ")
    pris_liste_tmp = []
    col_index = 0
    for celle in rad.find_elements_by_tag_name("td"):
        if col_index != 0 :
            pris_liste_tmp.append(celle.text)
        col_index += 1
    print(str(produkt) + ": " + str(pris_liste_tmp))
    produkter.update({produkt: pris_liste_tmp})
driver.quit()

# TODO:
# Feilhåndtering for I/O. Dersom mappen ikke eksisterer skal
# skal den lages mens programmet kjøres.

# Skriver data til fil
fil = f"./data/produkter-{date.today()}.json"
with open(fil, "w") as outfile:
    json.dump(produkter, outfile)
print(f"Data skrevet til fil: {fil}")

# TODO: Logging av programmets atferd.
# Spesielt feillogger i tilfelle det vil
# være Nødvendig å feilsøke programmet.
