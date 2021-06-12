from datetime import date, time, timedelta
import matplotlib.pyplot as plt


# Analizzo con un solo loop tutto ciò che posso analizzare nella chat
def Analysis(data) -> dict:
    analisi = dict()
    # Conteggio totale messaggio
    utenti = dict()
    # Conteggio messaggi giorno per giorno
    d_giorno_numero_messaggi = daily_messages_dict(data)
    d_utente_giorno_numero_messaggi = dict()
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

        # Messaggi di ogni utente giorno per giorno
        giorno_ora_messaggio = Telegram_from_text_to_date(messaggio['date'])
        if utente not in d_utente_giorno_numero_messaggi.keys():
            d_utente_giorno_numero_messaggi[utente] = d_giorno_numero_messaggi
        d_utente_giorno_numero_messaggi[utente][giorno_ora_messaggio[0]] += 1

    analisi['utenti'] = utenti
    analisi['utenti messaggi al giorno'] = d_utente_giorno_numero_messaggi

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

# Stampo e salvo un grafico a barre verticali


def grafico_verticale():

    fig = plt.figure(figsize=(len(calendario)/5, math.sqrt(len(calendario))))
    plt.title("Chat/Gruppo: " + nome)

    x = []
    c = list(calendario.keys())
    n = []
    for i in range(len(calendario)):
        x.append((int(c[i].split("-")[2]),
                int(c[i].split("-")[1]), int(c[i].split("-")[0])))
        n.append(i)

    plt.ylabel("Numero di messaggi")
    plt.xlabel("Data")

    y = list(calendario.values())

    plt.bar(n, y, width=0.6)
    plt.xticks(n, x, rotation=90)

    storico = "Storico_" + nome + "_" + str(flag) + ".png"

    fig.savefig(storico)

    plt.show()
