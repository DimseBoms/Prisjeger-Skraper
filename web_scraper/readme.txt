Et Python skript som skal samle inn prisdata fra enhver.no. Skriptet kjører på en privat server med jevne mellomrom.

Dersom en skal kjøre skriptet på egen maskin så er du nødt for å installere Python sammen med modulene i 'requirements.txt', i tillegg til å installere en nettleser sammen med nettleserens webdriver. En webdriver er grensesnittet mellom programmeringspråket og nettleseren. Det er dette grensesnittet som tillater oss å kommunisere med nettleseren i form av kode.

Skriptet er for øyeblikket tilpasset til å kjøre på en raspberry pi med open source versjonen av Chromium(https://www.chromium.org/) og ChromeDriver(https://chromedriver.chromium.org/) som webdriver men dette kan tilpasses i drivervariablene dersom skriptet skal kjøres på et annet system.

Dmitriy Safiullin
