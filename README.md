# Projekt : Elections Scraper
```py
"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lenka Urban
email: lenka.vondr@gmail.com
"""
```

### How to start

if you already have local env you can just start it with 
```bash
source projekt3/bin/activate
```
for runnning the streamlit app -run 
```bash
streamlit run {path/to/project/}result_visualiser.py 
````
#### First time (mac)
- create and start the virtual env

```bash
python<version> -m venv projekt3
source projekt3/bin/activate
```
- see if it was setup properly
```bash
pip list
```
- install dependencies
```bash
pip install -r requirements.txt
```
- when finished with work

```bash 
deactivate
```

### How to run the scraper

```bash 
election_results()
```

## Komentar k reseni

nejak mi nesedi, ze to neni genericke reseni, ale asi to ani jinak nejde, kdyz se zmeni struktura stranky, tak se musi zmenit i kod. 
tentokrat jsem nechala cely scraper v jednom souboru, aby se snaze kontroloval. 
neresila jsem zahranici - bylo by to podobne reseni jako pro obce.
neresila jsem testy. 
chtela jsem si vyzkouset streamlit - pridavam applikaci s grafem a inputem


## Zadání projektu
Závěrečný projekt prověří tvé znalosti nejenom z posledních lekcí, ale z celého kurzu. Tvým úkolem bude vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu

Napiš takový skript, který vybere jakýkoliv územní celek z [tohoto](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)
odkazu Např. X u Benešov [odkazuje sem](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101) . Z tohoto odkazu chcete vyscrapovat výsledky hlasování pro všechny obce.

1) Můžeš stahovat výsledky hlasování:
Pomocí odkazů ve sloupci číslo, např. 529303,
2) pomocí odkazů ve sloupci Výběr okrsku, tedy sloupec se symbolem X.

Je na tobě, který sloupec použiješ, ale dobře si jednotlivé odkazy prohlédni, jestli tě opravdu odkážou na výsledky obce.

## Jak postupovat
- Na svém počítači si vytvoříš vlastní virtuální prostředí (speciálně pro tento úkol),
- Do nově vytvořeného prostředí si přes IDE (nebo příkazový řádek) nainstalujete potřebné knihovny třetích stran,
- Vygenerujete soubor requirements.txt, který obsahuje soupis všech knihoven a jejich verzí (nevypisovat ručně!)
- Výsledný soubor budete spouštět pomocí 2 argumentů (ne pomocí funkce input). První argument obsahuje odkaz, který územní celek chcete scrapovat (př. územní celek Prostějov ), druhý argument obsahuje jméno výstupního souboru (př. vysledky_prostejov.csv)
- Pokud uživatel nezadá oba argumenty (ať už nesprávné pořadí, nebo argument, který neobsahuje správný odkaz), program jej upozorní a nepokračuje.
- Následně dopište README.md soubor, který uživatele seznámíte se svým projektem. Jak nainstalovat potřebné knihovny ze souboru requirements.txt, jak spustit váš soubor, příp. doplnit ukázku, kde demonstrujete váš kód na konkrétním odkaze s konkrétním výpisem.

## Projekt musí splňovat tyto body

```py
"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
"""
import ...

```

1) Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit  (viz. ukázka výše),
2) Soubor s programem (..nebo také skript) s příponou .py, který pro správný běh potřebuje 2 argumenty pro spuštění,
3) soubor se seznamem pouze relevantních knihoven a jejich verzí k projektu (requirements.txt),
4) stručnou dokumentaci (popis, instalace knihoven, ukázka) (README.md),
5) soubor s uloženým výstupem (.csv),
6) zápis organizovaný do krátkých a přehledných funkcí.

## Výstup bude obsahovat

Ve výstupu (soubor .csv) každý řádek obsahuje informace pro konkrétní obec. Tedy podobu:

1) kód obce
2) název obce
3) voliči v seznamu
4) vydané obálky
5) platné hlasy
6) kandidující strany (co sloupec, to počet hlasů pro stranu pro všechny strany).

