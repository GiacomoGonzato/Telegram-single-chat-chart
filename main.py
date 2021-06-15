import json
from utils.functions import Analysis, grafico_orizzontale_parole, grafico_orizzontale_utenti, grafico_verticale_dayweek, grafico_verticale_giorni, grafico_verticale_ore, ordina_dizionario_to_lista, stampa_chiavi


# Importo il file della Chat in un Json (dizionario di dizionari)
with open('C:\\Users\\Giacomo\\Desktop\\Python\\Chat_da_analizzare\\result.json', encoding="utf8") as f:
    data = json.load(f)

# stampa_chiavi(data)

# Utenti che hanno mai scritto o sono mai stati nel gruppo e quante azioni hanno mai fatto
# Analisi possibili: -'utenti'                      Nome utente -> numero totale di messaggi inviati
#                    -'utenti messaggi al giorno'   Nome utente -> data giorno -> numero messaggio inviati quel giorno
#                    -'utenti messaggi ogni ora'    Nome utente -> orario -> numero messaggio inviati in quell'ora
#                    -'utenti messaggi dayweek'     Nome utente -> giorno settimana -> numero messaggio inviati quel giorno
#                    -'utenti parole'               Nome utente -> parola -> numero utilizzi
#                    -'utenti mese pasole'          Nome utente -> mese -> parola -> numero utilizzi
analisi = Analysis(data)

# Classifica utenti che hanno mandato più messaggi
if False:
    lista_y, lista_x = ordina_dizionario_to_lista(analisi['utenti'], True)
    descrizione_y = 'Utenti'
    descrizione_x = 'Numero messaggi'
    titolo_grafico = 'Classifica utenti'
    nome_immagine = titolo_grafico.replace(' ', '_')
    grafico_orizzontale_utenti(lista_x, descrizione_x, lista_y,
                               descrizione_y, titolo_grafico, nome_immagine, 18)
    for i in range(len(lista_y)):
        print(i+1, ') ', lista_x[-1-i], ' messaggi scritti da ', lista_y[-1-i])


# Grafico messaggi al giorno
if False:
    descrizione_x = 'Data'
    descrizione_y = 'Numero messaggi'
    for utente in analisi['utenti messaggi al giorno'].keys():
        lista_x, lista_y = ordina_dizionario_to_lista(
            analisi['utenti messaggi al giorno'][utente])
        titolo_grafico = 'Messaggi giornalieri di ' + utente
        nome_immagine = titolo_grafico.replace(' ', '_')
        grafico_verticale_giorni(lista_x, descrizione_x, lista_y,
                                 descrizione_y, titolo_grafico, nome_immagine, 35)

# Grafico messaggi ogni ora
if False:
    descrizione_x = 'Orario'
    descrizione_y = 'Numero messaggi'
    for utente in analisi['utenti messaggi ogni ora'].keys():
        lista_x, lista_y = ordina_dizionario_to_lista(
            analisi['utenti messaggi ogni ora'][utente])
        titolo_grafico = 'Messaggi orari di ' + utente
        nome_immagine = titolo_grafico.replace(' ', '_')
        grafico_verticale_ore(lista_x, descrizione_x, lista_y,
                              descrizione_y, titolo_grafico, nome_immagine, 16)


# Grafico messaggi ogni giorno della settimana
if False:
    descrizione_x = 'Giorno della settimana'
    descrizione_y = 'Numero messaggi'
    for utente in analisi['utenti messaggi dayweek'].keys():
        lista_x = ['Lunedì', 'Martedì', 'Mercoledì',
                   'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
        lista_y = [analisi['utenti messaggi dayweek'][utente][dayweek]
                   for dayweek in lista_x]
        titolo_grafico = 'Messaggi settimanali di ' + utente
        nome_immagine = titolo_grafico.replace(' ', '_')
        grafico_verticale_dayweek(lista_x, descrizione_x, lista_y,
                                  descrizione_y, titolo_grafico, nome_immagine, 18)


# Grafico parole più usate
if False:
    lunghezza_classifica = 30
    descrizione_y = 'Utenti'
    descrizione_x = 'Parole'
    for utente in analisi['utenti parole'].keys():
        if len(analisi['utenti parole'][utente]) == 0:
            continue
        lista_y, lista_x = ordina_dizionario_to_lista(analisi['utenti parole'][utente],
                                                      True, True)
        listac_y = lista_y[:lunghezza_classifica]
        listac_x = lista_x[:lunghezza_classifica]
        listac_x.reverse()
        listac_y.reverse()
        titolo_grafico = 'Classifica parole di ' + utente
        nome_immagine = titolo_grafico.replace(' ', '_')
        grafico_orizzontale_parole(listac_x, descrizione_x, listac_y,
                                   descrizione_y, titolo_grafico, nome_immagine, 40)
        print()
        print(utente)
        print()
        for i in range(len(listac_y)):
            print(i+1, ') ', listac_x[-1-i], ' parola: ', listac_y[-1-i])


# DA FINIRE. CON QUESTA ANALISI POSSO RICAVARE SIA LA CLASSIFICA DELLE PAROLE PIU' GETTONATE
# MESE PER MESE CHE UN GRAFICO TEMPORALE MENSILE DELL'UTILIZZO DI DETERMINATE PAROLE

# Grafico parole più usate aggregate per mese
if True:
    parole_da_graficare = {'caffè', 'umana'}
    parole_da_graficare = {parola.lower() for parola in parole_da_graficare}
    lunghezza_classifica = 30
    descrizione_y = 'Utenti'
    descrizione_x = 'Parole'
    for utente in analisi['utenti parole'].keys():
        if len(analisi['utenti parole'][utente]) == 0:
            continue
        lista_y, lista_x = ordina_dizionario_to_lista(analisi['utenti parole'][utente],
                                                      True, True)
        listac_y = lista_y[:lunghezza_classifica]
        listac_x = lista_x[:lunghezza_classifica]
        listac_x.reverse()
        listac_y.reverse()
        titolo_grafico = 'Classifica parole di ' + utente
        nome_immagine = titolo_grafico.replace(' ', '_')
        grafico_orizzontale_parole(listac_x, descrizione_x, listac_y,
                                   descrizione_y, titolo_grafico, nome_immagine, 40)
        print()
        print(utente)
        print()
        for i in range(len(listac_y)):
            print(i+1, ') ', listac_x[-1-i], ' parola: ', listac_y[-1-i])
