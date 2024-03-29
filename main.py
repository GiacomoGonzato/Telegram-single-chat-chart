import json
from utils.first_aggregation import Analysis, ordina_dizionario_to_lista, stampa_chiavi
from utils.chart import *


# Importo il file della Chat in un Json (dizionario di dizionari)
with open('C:\\Users\\Giacomo\\Desktop\\Python\\Chat_da_analizzare\\result.json', encoding="utf8") as f:
    data = json.load(f)

if False:
    stampa_chiavi(data)

# Utenti che hanno mai scritto o sono mai stati nel gruppo e quante azioni hanno mai fatto
# Analisi possibili: -'utenti'                      Nome utente -> numero totale di messaggi inviati
#                    -'utenti messaggi al giorno'   Nome utente -> data giorno -> numero messaggio inviati quel giorno
#                    -'utenti messaggi ogni ora'    Nome utente -> orario -> numero messaggio inviati in quell'ora
#                    -'utenti messaggi dayweek'     Nome utente -> giorno settimana -> numero messaggio inviati quel giorno
#                    -'utenti parole'               Nome utente -> parola -> numero utilizzi
#                    -'utenti mese parole'          Nome utente -> mese -> parola -> numero utilizzi
analisi = Analysis(data)

# Classifica utenti che hanno mandato più messaggi
if False:
    lista_y, lista_x = ordina_dizionario_to_lista(analisi['utenti'], True)
    descrizione_y = 'Utenti'
    descrizione_x = 'Numero messaggi'
    titolo_grafico = 'Classifica utenti'
    nome_immagine = titolo_grafico.replace(' ', '_')
    for i in range(len(lista_y)):
        print(i+1, ') ', lista_x[-1-i], ' messaggi scritti da ', lista_y[-1-i])
    del lista_x[lista_y.index('Team')]
    lista_y.remove('Team')
    grafico_orizzontale_utenti(lista_x, descrizione_x, lista_y,
                               descrizione_y, titolo_grafico, nome_immagine, 18)


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


# Grafico parole più usate + WordCloud
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

        titolo_grafico_wc = 'WordCloud di ' + utente
        nome_immagine_wc = titolo_grafico_wc.replace(' ', '_')
        grafico_wordcloud(analisi['utenti parole'][utente], titolo_grafico_wc, nome_immagine_wc, 40)

        print()
        print(utente)
        print()
        for i in range(len(listac_y)):
            print(i+1, ') ', listac_x[-1-i], ' parola: ', listac_y[-1-i])


# Grafico parole aggregate per mese
if False:
    parole_da_graficare = {'bro'}
    utenti_da_plottare = {}
    # Se l'insieme è vuoto plotto per tutti gli utenti
    if len(utenti_da_plottare) == 0:
        utenti_da_plottare = {utente for utente in analisi['utenti'].keys()}
    parole_da_graficare = {parola.lower() for parola in parole_da_graficare}
    descrizione_x = 'Mesi'
    descrizione_y = 'Frequenza di utilizzo'
    d_utente_list_y = dict()
    lista_x = sorted([mese for mese in
                      analisi['utenti mese parole']['Team'].keys()])
    mese_parole_numerouso_team = analisi['utenti mese parole']['Team']
    for utente in utenti_da_plottare:
        d_utente_list_y[utente] = dict()
        mese_parole_numerouso = analisi['utenti mese parole'][utente]
        d_lists_y = dict()
        # Faccio il grafico per ogni parola
        for parola in parole_da_graficare:
            lista_y = [100 * mese_parole_numerouso[mese][parola]/sum(mese_parole_numerouso[mese].values())
                       if parola in mese_parole_numerouso[mese].keys() else 0 for mese in lista_x]
            d_utente_list_y[utente][parola] = [100 * mese_parole_numerouso[mese][parola]/sum(mese_parole_numerouso_team[mese].values())
                                               if parola in mese_parole_numerouso[mese].keys() else 0 for mese in lista_x]
            d_lists_y[parola] = lista_y
            titolo_grafico = 'Frequenza utilizzo mensile della parola ' + \
                parola + ' per ' + utente + ' rispetto a utente'
            nome_immagine = titolo_grafico.replace(' ', '_')
            grafico_verticale_mesi_parole(lista_x, descrizione_x, lista_y,
                                          descrizione_y, titolo_grafico, nome_immagine, 18)

        # Faccio un grafico riassuntivo per tutte le parole
        if len(parole_da_graficare) >= 2:
            titolo_grafico = 'Frequenza utilizzo mensile parole per ' + utente
            nome_immagine = titolo_grafico.replace(' ', '_')
            grafico_verticale_mesi_parole_riassunto(lista_x, descrizione_x, d_lists_y,
                                                    descrizione_y, titolo_grafico, nome_immagine, 18)

    # Faccio un grafico di confronto tra l'utilizzo delle parole tra i vari utenti
    for parola in parole_da_graficare:
        titolo_grafico = 'Confronto frequenza utilizzo mensile parole per ' + \
            parola + ' rispetto al gruppo'
        nome_immagine = titolo_grafico.replace(' ', '_')
        grafico_mesi_parole_confronto(lista_x, descrizione_x, d_utente_list_y,
                                      descrizione_y, titolo_grafico, nome_immagine, parola, 18)
