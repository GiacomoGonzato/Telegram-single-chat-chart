import json
from utils.functions import Analysis


# Importo il file della Chat in un Json (dizionario di dizionari)
with open('C:\\Users\\Giacomo\\Desktop\\Python\\Chat_DeLonghi\\result.json', encoding="utf8") as f:
    data = json.load(f)

# Utenti che hanno mai scritto o sono mai stati nel gruppo e quante azioni hanno mai fatto
analisi = Analysis(data)
for utente in analisi['utenti messaggi al giorno'].keys():
    print(utente)
    for giorno in analisi['utenti messaggi al giorno'][utente].keys():
        print(utente, ': ', giorno, '--> numero messaggi: ',
              analisi['utenti messaggi al giorno'][utente][giorno])

