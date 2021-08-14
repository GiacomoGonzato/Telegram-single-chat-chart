from datetime import date, datetime, timedelta
from nltk.corpus import stopwords
from math import *
import re


# Analizzo con un solo loop tutto ciò che posso analizzare nella chat
def Analysis(data) -> dict:
    analisi = dict()
    # Nome del Gruppo o della chat
    nome_chat = 'Team'
    # Conteggio totale messaggio
    utenti = set()
    utenti.add(nome_chat)
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
    # Inizio analisi parole
    stop_words_eng = set(stopwords.words("english"))
    stop_words_ita = set(stopwords.words("italian"))
    stop_words_private = {"https", "www", "é", ""}
    # Conto tutte le parole scritte dagli utenti
    stop_words = stop_words_eng | stop_words_ita | stop_words_private
    d_utente_parole_numerouso = dict()
    d_utente_parole_numerouso[nome_chat] = dict()
    # Conto le parole più gettonate di ogni mese
    d_utente_mese_parole_numerouso = dict()
    d_utente_mese_parole_numerouso[nome_chat] = monthly_parole_dict(data)
    for messaggio in data['messages']:

        # Ricordo gli utenti
        utente = 'inizializzazione'
        if 'from' in messaggio.keys():
            utente = messaggio['from']
        elif 'actor' in messaggio.keys():
            utente = messaggio['actor']
        if utente == 'inizializzazione':
            print('Errore: Owner del messaggio sconosciuto')
            continue
        if utente not in utenti:
            utenti.add(utente)

        giorno_ora_messaggio = Telegram_from_text_to_date(messaggio['date'])
        # Messaggi di ogni utente giorno per giorno
        if utente not in d_utente_giorno_numero_messaggi.keys():
            d_utente_giorno_numero_messaggi[utente] = daily_messages_dict(data)
        giorno_messaggio = date(giorno_ora_messaggio.year,
                                giorno_ora_messaggio.month, giorno_ora_messaggio.day)
        stringa_giorno_messaggio = giorno_messaggio.__str__()
        d_utente_giorno_numero_messaggi[utente][stringa_giorno_messaggio] += 1
        d_utente_giorno_numero_messaggi[nome_chat][stringa_giorno_messaggio] += 1

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

        # Inizio analisi delle parole
        if 'text' in messaggio.keys():
            if utente not in d_utente_parole_numerouso:
                d_utente_mese_parole_numerouso[utente] = monthly_parole_dict(
                    data)
                d_utente_parole_numerouso[utente] = dict()
            messages = good_formatting(messaggio['text'])
            parole = split_stringa(messages)
            stringa_mese_messaggio = stringa_giorno_messaggio[:-3]
            for parola in set(parole)-stop_words:
                ripetizioni = parole.count(parola)
                # Conteggio parole mai scritte da ogni utente
                if parola not in d_utente_parole_numerouso[nome_chat].keys():
                    d_utente_parole_numerouso[utente][parola] = ripetizioni
                    d_utente_parole_numerouso[nome_chat][parola] = ripetizioni
                elif parola not in d_utente_parole_numerouso[utente].keys():
                    d_utente_parole_numerouso[utente][parola] = ripetizioni
                    d_utente_parole_numerouso[nome_chat][parola] += ripetizioni
                else:
                    d_utente_parole_numerouso[utente][parola] += ripetizioni
                    d_utente_parole_numerouso[nome_chat][parola] += ripetizioni
                # Aggrego le parole per utenti e mese
                if parola not in d_utente_mese_parole_numerouso[nome_chat][stringa_mese_messaggio].keys():
                    d_utente_mese_parole_numerouso[utente][stringa_mese_messaggio][parola] = ripetizioni
                    d_utente_mese_parole_numerouso[nome_chat][stringa_mese_messaggio][parola] = ripetizioni
                elif parola not in d_utente_mese_parole_numerouso[utente][stringa_mese_messaggio].keys():
                    d_utente_mese_parole_numerouso[utente][stringa_mese_messaggio][parola] = ripetizioni
                    d_utente_mese_parole_numerouso[nome_chat][stringa_mese_messaggio][parola] += ripetizioni
                else:
                    d_utente_mese_parole_numerouso[utente][stringa_mese_messaggio][parola] += ripetizioni
                    d_utente_mese_parole_numerouso[nome_chat][stringa_mese_messaggio][parola] += ripetizioni

    # Conto il numero dei messaggi totali scritti da un utente a partire dal numero di messaggi scritti ogni mese
    giorni = d_utente_giorno_numero_messaggi[nome_chat].keys()
    d_utente_numero_messaggi = {user: sum((d_utente_giorno_numero_messaggi[user][giorno]
                                           for giorno in giorni)) for user in utenti}

    # Inserisco tutti i dati nella variabile di output
    analisi['utenti'] = d_utente_numero_messaggi
    analisi['utenti messaggi al giorno'] = d_utente_giorno_numero_messaggi
    analisi['utenti messaggi ogni ora'] = d_utente_ora_numero_messaggi
    analisi['utenti messaggi dayweek'] = d_utente_dayweek_numero_messaggi
    analisi['utenti parole'] = d_utente_parole_numerouso
    analisi['utenti mese parole'] = d_utente_mese_parole_numerouso

    return analisi


# Ritorna il giorno e l'ora nella classe datetime
def Telegram_from_text_to_date(stringa) -> datetime:
    ldata = stringa.split('T')
    lgiorno = [int(x) for x in ldata[0].split('-')]
    lora = [int(x) for x in ldata[1].split(':')]
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
    giorni = {first_day + timedelta(days=i)
              for i in range((last_day-first_day).days + 1)}
    for giorno in giorni:
        numero_messaggi_giorno[giorno.__str__()] = 0
    return numero_messaggi_giorno


# Inizializzo il dizionario del numero di messaggi spedito ogni ora
def hourly_messages_dict() -> dict:
    numero_messaggi_ora = {ora: 0 for ora in range(24)}
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


# Inizializzo il dizionario della classifica mensile delle parole più gettonate
def monthly_parole_dict(data) -> dict:
    numero_parole_mese = dict()
    first_day = Telegram_from_text_to_date(data['messages'][0]['date'])
    last_day = Telegram_from_text_to_date(data['messages'][-1]['date'])
    first_day = date(first_day.year, first_day.month, 1)
    last_day = date(last_day.year, last_day.month, 27)
    mesi = {(first_day + timedelta(days=i)).__str__()[:-3]
            for i in range(0, (last_day - first_day).days + 1, 25)}
    for stringa_mese in mesi:
        numero_parole_mese[stringa_mese] = dict()
    return numero_parole_mese


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


# Dato il file json stampo a video tutte le possibili chiavi che posso trovare nei messaggi
def stampa_chiavi(data) -> None:
    chiavi = set()
    s = [{chiave for chiave in messaggio.keys()}
         for messaggio in data['messages']]
    for x in s:
        chiavi = chiavi.union(x)
    chiavi = sorted([chiave for chiave in chiavi])
    for x in chiavi:
        print(x)
