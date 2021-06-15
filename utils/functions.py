from datetime import date, datetime, timedelta
from nltk.corpus import stopwords
from math import *
import re
import matplotlib.pyplot as plt
from numpy import where


# Analizzo con un solo loop tutto ciò che posso analizzare nella chat
def Analysis(data) -> dict:
    analisi = dict()
    # Nome del Gruppo o della chat
    nome_chat = 'Team'
    # Conteggio totale messaggio
    utenti = dict()
    # Conteggio messaggi giorno per giorno
    d_utente_giorno_numero_messaggi = dict()
    d_utente_giorno_numero_messaggi[nome_chat] = daily_messages_dict(data)
    # Conteggio messaggi ogni ora
    d_utente_ora_numero_messaggi = dict()
    d_utente_ora_numero_messaggi[nome_chat] = hourly_messages_dict()
    # Conteggio messaggi ogni giorno della settimana
    d_utente_dayweek_numero_messaggi = dict()
    d_numero_dayweek = numero_dayweek_converter()
    d_utente_dayweek_numero_messaggi[nome_chat] = weekly_messages_dict()
    # Conto tutte le parole scritte dagli utenti
    d_utente_parole_numerouso = dict()
    stop_words_eng = set(stopwords.words("english"))
    stop_words_ita = set(stopwords.words("italian"))
    stop_words_private = {"https", "www", "é"}
    stop_words = stop_words_eng | stop_words_ita | stop_words_private
    d_utente_parole_numerouso[nome_chat] = dict()
    for messaggio in data['messages']:

        # Ricordo gli utenti e conto quanti messaggi hanno scritto
        utente = 'inizializzazione'
        if 'from' in messaggio.keys():
            utente = messaggio['from']
        elif 'actor' in messaggio.keys():
            utente = messaggio['actor']
        if utente == 'inizializzazione':
            print('Errore: Owner del messaggio sconosciuto')
            continue
        if utente not in utenti.keys():
            utenti[utente] = 0
        utenti[utente] += 1

        giorno_ora_messaggio = Telegram_from_text_to_date(messaggio['date'])
        # Messaggi di ogni utente giorno per giorno
        if utente not in d_utente_giorno_numero_messaggi.keys():
            d_utente_giorno_numero_messaggi[utente] = daily_messages_dict(data)
        giorno_messaggio = date(giorno_ora_messaggio.year,
                                giorno_ora_messaggio.month, giorno_ora_messaggio.day)
        d_utente_giorno_numero_messaggi[utente][giorno_messaggio.__str__(
        )] += 1
        d_utente_giorno_numero_messaggi[nome_chat][giorno_messaggio.__str__(
        )] += 1

        # Messaggi di ogni utente nelle ore
        if utente not in d_utente_ora_numero_messaggi.keys():
            d_utente_ora_numero_messaggi[utente] = hourly_messages_dict()
        time_messaggio = giorno_ora_messaggio.hour
        d_utente_ora_numero_messaggi[utente][time_messaggio] += 1
        d_utente_ora_numero_messaggi[nome_chat][time_messaggio] += 1

        # Messaggi di ogni utente nei giorni della settimana
        if utente not in d_utente_dayweek_numero_messaggi.keys():
            d_utente_dayweek_numero_messaggi[utente] = weekly_messages_dict()
        dayweek_messaggio = giorno_ora_messaggio.weekday()
        d_utente_dayweek_numero_messaggi[utente][d_numero_dayweek[dayweek_messaggio]] += 1
        d_utente_dayweek_numero_messaggi[nome_chat][d_numero_dayweek[dayweek_messaggio]] += 1

        # Parole di ogni utente mai scritte
        if 'text' in messaggio.keys():
            if utente not in d_utente_parole_numerouso:
                d_utente_parole_numerouso[utente] = dict()
            messages = good_formatting(messaggio['text'])
            parole = split_stringa(messages)
            for parola in set(parole)-{''}:
                if parola in stop_words:
                    continue
                ripetizioni = parole.count(parola)
                if parola not in d_utente_parole_numerouso[nome_chat].keys():
                    d_utente_parole_numerouso[utente][parola] = ripetizioni
                    d_utente_parole_numerouso[nome_chat][parola] = ripetizioni
                elif parola not in d_utente_parole_numerouso[utente].keys():
                    d_utente_parole_numerouso[utente][parola] = ripetizioni
                    d_utente_parole_numerouso[nome_chat][parola] += ripetizioni
                else:
                    d_utente_parole_numerouso[utente][parola] += ripetizioni
                    d_utente_parole_numerouso[nome_chat][parola] += ripetizioni

    analisi['utenti'] = utenti
    analisi['utenti messaggi al giorno'] = d_utente_giorno_numero_messaggi
    analisi['utenti messaggi ogni ora'] = d_utente_ora_numero_messaggi
    analisi['utenti messaggi dayweek'] = d_utente_dayweek_numero_messaggi
    analisi['utenti parole'] = d_utente_parole_numerouso

    return analisi


# Ritorna il giorno e l'ora nella classe datetime
def Telegram_from_text_to_date(stringa) -> datetime:
    ldata = stringa.split('T')
    lgiorno = ldata[0].split('-')
    lgiorno = [int(x) for x in lgiorno]
    lora = ldata[1].split(':')
    lora = [int(x) for x in lora]
    day_hour = datetime(lgiorno[0], lgiorno[1], lgiorno[2],
                        lora[0], lora[1], lora[2])
    return day_hour


# Inizializzo il dizionario del numero di messaggi spedito ogni giorno
def daily_messages_dict(data) -> dict:
    numero_messaggi_giorno = dict()
    first_day = Telegram_from_text_to_date(data['messages'][0]['date'])
    last_day = Telegram_from_text_to_date(data['messages'][-1]['date'])
    first_day = date(first_day.year, first_day.month, first_day.day)
    last_day = date(last_day.year, last_day.month, last_day.day)
    t = timedelta(days=1)
    today = first_day
    while today <= last_day:
        numero_messaggi_giorno[today.__str__()] = 0
        today = today + t
    return numero_messaggi_giorno


# Inizializzo il dizionario del numero di messaggi spedito ogni ora
def hourly_messages_dict() -> dict:
    numero_messaggi_ora = dict()
    for ora in range(24):
        numero_messaggi_ora[ora] = 0
    return numero_messaggi_ora


# Inizializzo il dizionario del numero di messaggi spedito ogni giorno della settimana
def weekly_messages_dict() -> dict:
    numero_messaggi_dayweek = dict()
    numero_messaggi_dayweek['Lunedì'] = 0
    numero_messaggi_dayweek['Martedì'] = 0
    numero_messaggi_dayweek['Mercoledì'] = 0
    numero_messaggi_dayweek['Giovedì'] = 0
    numero_messaggi_dayweek['Venerdì'] = 0
    numero_messaggi_dayweek['Sabato'] = 0
    numero_messaggi_dayweek['Domenica'] = 0
    return numero_messaggi_dayweek


# Inizializzo il dizionario che converte numero in giorno della settimana
def numero_dayweek_converter() -> dict:
    convertitore = dict()
    convertitore[0] = 'Lunedì'
    convertitore[1] = 'Martedì'
    convertitore[2] = 'Mercoledì'
    convertitore[3] = 'Giovedì'
    convertitore[4] = 'Venerdì'
    convertitore[5] = 'Sabato'
    convertitore[6] = 'Domenica'
    return convertitore


# Stampo e salvo un grafico a barre verticali per i giorni
def grafico_verticale_giorni(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
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
    n = [i for i in range(len(lista_x))]
    tick_char_size = char_size * 0.7

    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.bar(n, lista_y, width=0.6)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(n, lista_x, rotation=90, fontsize=10)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Stampo e salvo un grafico a barre orizzontali della classifica utenti
def grafico_orizzontale_utenti(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
    size = (2 * len(lista_x), len(lista_x))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.946,
        bottom=0.086,
        left=0.161,
        right=0.987,
        hspace=1,
        wspace=1
    )

    tick_char_size = char_size * 0.7

    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(fontsize=tick_char_size)

    plt.barh(lista_y, lista_x)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Stampo e salvo un grafico a barre verticali per le ore
def grafico_verticale_ore(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
    size = (len(lista_x)/4, sqrt(len(lista_x)))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.926,
        bottom=0.127,
        left=0.129,
        right=0.969,
        hspace=0.2,
        wspace=0.2
    )
    n = [i for i in range(len(lista_x))]
    tick_char_size = char_size * 0.7

    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.bar(n, lista_y, width=0.7)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(n, lista_x, rotation=70, fontsize=tick_char_size)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Stampo e salvo un grafico a barre verticali per i giorni della settimana
def grafico_verticale_dayweek(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
    size = (2 * len(lista_x), len(lista_x))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.946,
        bottom=0.168,
        left=0.063,
        right=0.987,
        hspace=0.2,
        wspace=0.2
    )

    n = [i for i in range(len(lista_x))]
    tick_char_size = char_size * 0.7

    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.bar(n, lista_y, width=0.7)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(n, lista_x, rotation=0, fontsize=tick_char_size)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Stampo e salvo un grafico a barre orizzontali della classifica utenti
def grafico_orizzontale_parole(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
    size = (2 * len(lista_x), len(lista_x))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.946,
        bottom=0.086,
        left=0.068,
        right=0.987,
        hspace=0.2,
        wspace=0.2
    )

    tick_char_size = char_size * 0.7

    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(fontsize=tick_char_size)

    plt.barh(lista_y, lista_x)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Dato un dizionario creo due liste (asse_x, asse_y) ordinate secondo la chiave (False) o valore (True)
def ordina_dizionario_to_lista(dizionario, per_valore=False, decrescente=False) -> tuple:
    asse_x = [x for x in dizionario.keys()]
    if not per_valore:
        asse_x.sort(reverse=decrescente)
    else:
        # Criterio di riordinamento
        def sort_val_dict(x):
            return dizionario[x]
        asse_x.sort(key=sort_val_dict, reverse=decrescente)
    asse_y = [dizionario[x] for x in asse_x]
    return (asse_x, asse_y)


# Data una stringa la divido in tutte le sue parole utili
def split_stringa(text) -> list:
    divisione = re.split(r'\W+', text)
    return divisione


# Formatto bene il testo in caso di citazioni
def good_formatting(messaggio) -> str:
    if not (type(messaggio) is str):
        messaggio = " ".join([x if type(x) is str else x['text']
                              for x in messaggio])
    return messaggio.lower()
