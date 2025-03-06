import csv
import traceback
import requests
from bs4 import BeautifulSoup, element
from re import match

pattern = r'https:\/\/www\.volby\.cz\/pls\/ps2017nss\/ps3(?:1|11|2)\?xjazyk=CZ&xkraj=(?:[1-9]|1[0-4])&xnumnuts=\d+'
pattern2 = r'https:\/\/www\.volby\.cz\/pls\/ps2017nss\/ps3(?:6|61)\?xjazyk=CZ'

def validate_source_url(sourceUrl: str) -> str:
  """
  Zkontroluje, zda je zadaný odkaz validní.
  """
  print(match(pattern, sourceUrl))
  if match(pattern2, sourceUrl):
    print ("vyber zahranicnich okrsku neni implementovan")
    return False
    # downloadExpatsResult = input("stahnout? (ano/ne)")
    # if downloadExpatsResult == "ano":
    #   if "ps361" in sourceUrl:
    #     sourceUrl.replace("ps361", "ps36")
    #     return False
    #   elif "ps36" in sourceUrl:
    #     return False
    # else:
    #   return False

  elif match(pattern, sourceUrl):
    print("vyber obce")
    if "ps31" in sourceUrl:
      valid_url = sourceUrl.replace("ps31", "ps32")
      return valid_url
    elif "ps311" in sourceUrl:
      valid_url = sourceUrl.replace("ps311", "ps32")
      return valid_url
    elif "ps32" in sourceUrl:
      return sourceUrl
  else:
    print("Neplatný odkaz")
    return False



def get_html_as_soup(url: str):
  """
  Stáhne html a naparsuje do soup.
  """
  res = requests.get(url)
  return BeautifulSoup(res.text, 'html.parser')

def extract_results_to_dict(code: element.Tag):
  """
  uklada data do slovniku
  """
  town_result_summary = {}
  town_result_link_url = f"https://www.volby.cz/pls/ps2017nss/{code.find("a").get("href")}"

  soup = get_html_as_soup(town_result_link_url)

  town_name = soup.find_all("h3")[2].getText().split(": ")[1].strip()
  
  town_results = soup.find("table", {"id": "ps311_t1"})
  voters = town_results.find("td", {"headers": "sa2"})
  envelopes = town_results.find("td", {"headers": "sa3"})
  valid_votes = town_results.find("td", {"headers": "sa6"})

  town_result_summary["kód obce"] = code.find("a").getText()
  town_result_summary["název obce"] = town_name
  town_result_summary["voliči v seznamu"] = voters.getText().replace(" ", "")
  town_result_summary["vydané obálky"] = envelopes.getText().replace(" ", "")
  town_result_summary["platné hlasy"] = valid_votes.getText().replace(" ", "")

  party_titles_t1 = soup.find_all("td", {"headers": "t1sa1 t1sb2"})
  party_results_t1 = soup.find_all("td", {"headers": "t1sa2 t1sb3"})
  party_titles_t2 = soup.find_all("td", {"headers": "t2sa1 t2sb2"})
  party_results_t2 = soup.find_all("td", {"headers": "t2sa2 t2sb3"})

  for i in range(len(party_titles_t1)):
    town_result_summary[party_titles_t1[i].getText()] = party_results_t1[i].getText().replace(" ", "")

  for i in range(len(party_titles_t2)):
    if party_titles_t2[i].getText() != "-":
      town_result_summary[party_titles_t2[i].getText()] = party_results_t2[i].getText().replace(" ", "")

  return town_result_summary

def zapis_data(data: list, jmeno_souboru: str) -> str:
  """
  Zkus zapsat udaje z par. 'data' do souboru formatu .csv.
  """
  print(data)
  
  try:
    csv_soubor = open(jmeno_souboru, mode="w", encoding="utf-8")
    cols = data[0].keys()
    
  except FileExistsError:
    return traceback.format_exc()
  except IndexError:
    return traceback.format_exc()
  else:
    zapis = csv.DictWriter(csv_soubor, fieldnames=cols)
    zapis.writeheader()
    zapis.writerows(data)
    return "Saved"
  finally:
    csv_soubor.close()

def scrape_election_results(url: str, filename: str):
  """
  Stáhne data z voleb z url a uloží je do souboru.
  """
  valid_url = validate_source_url(url)
  if valid_url == False:
    print("Neplatný odkaz")
    return "Neplatný odkaz"

  print("stahuji data pro: ", valid_url)
  soup = get_html_as_soup(valid_url)
  town_name = soup.find_all("h3")[1].getText()
  print(town_name)
  
  town_codes = soup.find_all("td", {"headers": "t1sa1 t1sb1"})

  full_results = [
    extract_results_to_dict(code)
    for code in town_codes[1:]
  ]
  
  zapis_data(full_results, filename)
  return town_name

if __name__ == "__main__":
  test_url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4203" 
  test_name = "example_vysledky.csv"

  scrape_election_results(test_url, test_name)

