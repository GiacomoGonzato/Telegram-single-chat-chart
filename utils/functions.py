from datetime import date, time, timedelta
from math import *
import matplotlib.pyplot as plt


# Analizzo con un solo loop tutto ciò che posso analizzare nella chat
def Analysis(data) -> dict:
    analisi = dict()
    # Conteggio totale messaggio
    utenti = dict()
    # Conteggio messaggi giorno per giorno
    d_utente_giorno_numero_messaggi = dict()
    # Conteggio messaggi ora per ora
    d_utente_ora_numero_messaggi = dict()
    for messaggio in data['messages']:

        # Ricordo gli utenti e conto quanti messaggi hanno scritto
        utente = 'inizializzazione variabile'
        if 'from' in messaggio.keys():
            utente = messaggio['from']
        elif 'actor' in messaggio.keys():
            utente = messaggio['actor']
        if utente == 'inizializzazione variabile':
            print('Owner del messaggio sconosciuto')
            continue
        if utente not in utenti.keys():
            utenti[utente] = 0
        else:
            utenti[utente] += 1

        giorno_ora_messaggio = Telegram_from_text_to_date(messaggio['date'])
        # Messaggi di ogni utente giorno per giorno
        if utente not in d_utente_giorno_numero_messaggi.keys():
            d_utente_giorno_numero_messaggi[utente] = daily_messages_dict(data)
        d_utente_giorno_numero_messaggi[utente][giorno_ora_messaggio[0]] += 1

        # Messaggi di ogni utente ora per ora
        if utente not in d_utente_ora_numero_messaggi.keys():
            d_utente_ora_numero_messaggi[utente] = hourly_messages_dict()
        time_messaggio = giorno_ora_messaggio[1]
        ora_messaggio = time_messaggio.hour
        d_utente_ora_numero_messaggi[utente][ora_messaggio] += 1

    analisi['utenti'] = utenti
    analisi['utenti messaggi al giorno'] = d_utente_giorno_numero_messaggi
    analisi['utenti messaggi ogni ora'] = d_utente_ora_numero_messaggi

    return analisi


# Ritorna ((YYYY,MM,GG),(HH,MM,SS)) con classe DATETIME
def Telegram_from_text_to_date(stringa) -> tuple:
    ldata = stringa.split('T')
    lgiorno = ldata[0].split('-')
    lgiorno = [int(x) for x in lgiorno]
    lora = ldata[1].split(':')
    lora = [int(x) for x in lora]
    day = date(lgiorno[0], lgiorno[1], lgiorno[2])
    hour = time(lora[0], lora[1], lora[2])
    return (day, hour)


# Utenti della chat e numero delle loro azioni
def Utenti_chat(data, solo_utenti=False) -> dict:
    utenti = dict()
    for messaggio in data['messages']:
        utente = 'inizializzazione variabile'
        if 'from' in messaggio.keys():
            utente = messaggio['from']
        elif 'actor' in messaggio.keys():
            utente = messaggio['actor']
        if utente == 'inizializzazione variabile':
            print('Owner del messaggio sconosciuto')
            continue
        if utente not in utenti.keys():
            utenti[utente] = 0
        else:
            utenti[utente] += 1
    if solo_utenti:
        utenti = set(utenti.keys())
    return utenti


# Inizializzo il dizionario del numero di messaggi spedito ogni giorno
def daily_messages_dict(data):
    numero_messaggi_giorno = dict()
    first_day = Telegram_from_text_to_date(data['messages'][0]['date'])
    last_day = Telegram_from_text_to_date(data['messages'][-1]['date'])
    first_day = first_day[0]
    last_day = last_day[0]
    t = timedelta(days=1)
    today = first_day
    while today <= last_day:
        numero_messaggi_giorno[today] = 0
        today = today + t
    return numero_messaggi_giorno


# Inizializzo il dizionario del numero di messaggi spedito ogni ora
def hourly_messages_dict():
    numero_messaggi_ora = dict()
    for ora in range(24):
        numero_messaggi_ora[ora] = 0
    return numero_messaggi_ora


# Stampo e salvo un grafico a barre verticali per i giorni
def grafico_verticale_giorni(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine):
    size = (len(lista_x)/5, sqrt(len(lista_x)))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.946,
        bottom=0.184,
        left=0.063,
        right=0.987,
        hspace=0.2,
        wspace=0.2
    )
    plt.title(titolo_grafico)
    n = [i for i in range(len(lista_x))]

    plt.ylabel(descrizione_y)
    plt.xlabel(descrizione_x)

    plt.bar(n, lista_y, width=0.6)
    plt.xticks(n, lista_x, rotation=90)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
#    plt.show()


# Stampo e salvo un grafico a barre verticali per le ore
def grafico_verticale_ore(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine):
    size = (len(lista_x)/5, sqrt(len(lista_x)))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.926,
        bottom=0.127,
        left=0.129,
        right=0.969,
        hspace=0.2,
        wspace=0.2
    )
    plt.title(titolo_grafico)
    n = [i for i in range(len(lista_x))]

    plt.ylabel(descrizione_y)
    plt.xlabel(descrizione_x)

    plt.bar(n, lista_y, width=0.6)
    plt.xticks(n, lista_x, rotation=90)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
#    plt.show()


# Dato un dizionario creo due liste (asse_x, asse_y) ordinate
def ordina_dizionario_to_lista(dizionario, decrescente=False):
    asse_x = [x for x in dizionario.keys()]
    asse_x.sort(reverse=decrescente)
    asse_y = [dizionario[x] for x in asse_x]
    return (asse_x, asse_y)
