# Laget av Dmitriy Safiullin. Sist oppdatert: 17.11.2021
# Programmet henter prisdata fra enhver.no. Prisdata blir lagret i ./data mappen.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from datetime import date
import os
import json

start_tid = datetime.now()
print(f'Startet: {start_tid}.')

# Oppsett av virtuell nettleser
NETTSIDE_URL = 'https://enhver.no/priser/'
DRIVER_URL = "/usr/lib/chromium-browser/chromedriver"
options = Options()
options.headless = True
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=options, executable_path=DRIVER_URL)
driver.get(NETTSIDE_URL)

# Henter data og setter den inn i produkter{}
produkter = {'butikker': [], 'varer': {}}
# Henter butikkdata
butikker = []
for butikk_span in driver.find_elements_by_xpath("//span[@class='retailer-name']"):
    butikk = butikk_span.find_element_by_tag_name('img').get_attribute('title')
    butikker.append(butikk)
produkter.update({'butikker': butikker})
# Henter prisdata
for rad in driver.find_elements_by_xpath("//tr[@class='product']"):
    produkt = rad.find_element_by_tag_name('td').text.replace('\n', ', ')
    pris_liste_tmp = []
    col_index = 0
    for celle in rad.find_elements_by_tag_name('td'):
        if col_index != 0:
            pris_liste_tmp.append(celle.text)
        col_index += 1
    produkter['varer'].update({produkt: pris_liste_tmp})
driver.quit()

# Lager mappen data dersom den ikke eksisterer og skriver data til fil
if not os.path.isdir('./data'):
    os.mkdir('./data')
fil = f'./data/produkter-{date.today()}.json'
with open(fil, "w") as outfile:
    json.dump(produkter, outfile, sort_keys=True, indent=2)
    print(f'Suksess. Data skrevet til {fil}.')
print(f'Kjøretid: {datetime.now() - start_tid}.')
