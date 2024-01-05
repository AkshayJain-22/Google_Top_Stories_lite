from news_scrapper import scrapper
from google_functions import sheet_append

def final_results(names,sport):
    results = []
    for name in names:
        individual = scrapper(name)
        sheet_append(name,sport,individual)
        results.append(individual)
    return(results)