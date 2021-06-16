from math import *
import matplotlib.pyplot as plt


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


# Stampo e salvo un grafico a barre verticali per i mesi delle parole
def grafico_verticale_mesi_parole(lista_x, descrizione_x, lista_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
    size = (2 * len(lista_x), len(lista_x))
    fig = plt.figure(figsize=size)
    fig.subplots_adjust(
        top=0.897,
        bottom=0.295,
        left=0.096,
        right=0.981,
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
    plt.xticks(n, lista_x, rotation=90, fontsize=tick_char_size)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()
