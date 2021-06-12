import json
from utils.functions import Analysis, grafico_verticale_giorni, grafico_verticale_ore, ordina_dizionario_to_lista


# Importo il file della Chat in un Json (dizionario di dizionari)
with open('C:\\Users\\Giacomo\\Desktop\\Python\\Chat_da_analizzare\\result.json', encoding="utf8") as f:
    data = json.load(f)

# Utenti che hanno mai scritto o sono mai stati nel gruppo e quante azioni hanno mai fatto
# Analisi possibili: -'utenti'                      Nome utente -> numero totale di messaggi inviati
#                    -'utenti messaggi al giorno'   Nome utente -> data giorno -> numero messaggio inviati quel giorno
#                    -'utenti messaggi ogni ora'    Nome utente -> orario -> numero messaggio inviati in quell'ora
analisi = Analysis(data)

# Grafico messaggi al giorno
for utente in analisi['utenti'].keys():
    lista_x, lista_y = ordina_dizionario_to_lista(
        analisi['utenti messaggi al giorno'][utente])
    descrizione_x = 'Data'
    descrizione_y = 'Numero messaggi'
    titolo_grafico = 'Messaggi giornalieri di ' + utente
    nome_immagine = titolo_grafico.replace(' ', '_')
    grafico_verticale_giorni(lista_x, descrizione_x, lista_y,
                             descrizione_y, titolo_grafico, nome_immagine)

# Grafico messaggi ogni ora
for utente in analisi['utenti'].keys():
    lista_x, lista_y = ordina_dizionario_to_lista(
        analisi['utenti messaggi ogni ora'][utente])
    descrizione_x = 'Orario'
    descrizione_y = 'Numero messaggi'
    titolo_grafico = 'Messaggi orari di ' + utente
    nome_immagine = titolo_grafico.replace(' ', '_')
    grafico_verticale_ore(lista_x, descrizione_x, lista_y,
                          descrizione_y, titolo_grafico, nome_immagine)
