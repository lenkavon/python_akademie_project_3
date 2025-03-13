from scraper.election_result import scrape_election_results

def main():
  print("Tento skript stáhne výsledky voleb z URL.")
  print("Zadejte prosím URL voleb, které chcete stáhnout.")
  print("Příklad: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4203")
  election_Url = input("Zadejte URL voleb: ")
  print("Zadejte prosím název souboru, do kterého chcete uložit výsledky.")
  print("Příklad: 'vysledky'")
  print("Tímto se výsledky uloží do souboru s názvem 'vysledky.csv'")
  save_as = input("Zadejte název souboru pro uložení výsledků: ")
  
  results = scrape_election_results(election_Url, save_as + ".csv")
  print(results)
  if results == "Neplatný odkaz":
    print("Nepodařilo se uložit výsledky")
    tryAgain = input("Začít znovu? A/N: ")
    if tryAgain == "A":
      return main()
    else:
      print("Nashledanou!")
      exit()
  else:
    print("Výsledky uloženy do", save_as + ".csv")


if __name__ == "__main__":
  main()