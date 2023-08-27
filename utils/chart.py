from math import *
from wordcloud import WordCloud
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
    size = (10 * len(lista_x), 5 * len(lista_x))
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

    plt.grid(linestyle='-', linewidth=3, zorder=0)
    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(fontsize=tick_char_size)

    plt.barh(lista_y, lista_x, zorder=3)

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

    plt.grid(linestyle='-', linewidth=3, zorder=0)
    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.bar(n, lista_y, width=0.7, zorder=3)
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

    plt.grid(linestyle='-', linewidth=3, zorder=0)
    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.bar(n, lista_y, width=0.7, zorder=3)
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

    plt.grid(linestyle='-', linewidth=3, zorder=0)
    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(fontsize=tick_char_size)

    plt.barh(lista_y, lista_x, zorder=3)

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

    plt.grid(linestyle='-', linewidth=6, zorder=0)
    plt.title(titolo_grafico, fontsize=char_size)
    plt.ylabel(descrizione_y, fontsize=char_size)
    plt.xlabel(descrizione_x, fontsize=char_size)
    plt.bar(n, lista_y, width=0.7, zorder=3)
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(n, lista_x, rotation=90, fontsize=tick_char_size)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Stampo e salvo un grafico a barre verticali per i mesi delle parole che sia riassuntivo per tutte le parole
def grafico_verticale_mesi_parole_riassunto(lista_x, descrizione_x, d_lists_y, descrizione_y, titolo_grafico, nome_immagine, char_size=18):
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
    plt.grid(linestyle='-', linewidth=6, zorder=0)
    sum_value_list = [fsum([lista[i] for lista in d_lists_y.values()])
                      for i in range(len(lista_x))]
    for parola in d_lists_y.keys():
        plt.bar(n, sum_value_list, width=0.7, label=parola, zorder=3)
        sum_value_list = [somma_precedente - valore for somma_precedente, valore
                          in zip(sum_value_list, d_lists_y[parola])]
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(n, lista_x, rotation=90, fontsize=tick_char_size)
    if max([abs(x) for x in sum_value_list]) >= 0.001:
        print('ERRORE DI APPROSSIMAZIONE DEL GRAFICO ' +
              nome_immagine + '.png SUPERIORE A 0.001')
    plt.legend(prop={'size': char_size})
    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    # plt.show()
    plt.close()


# Stampo e salvo un grafico a barre verticali per i mesi delle parole che sia riassuntivo per tutte le parole
def grafico_mesi_parole_confronto(lista_x, descrizione_x, d_utente_list_y, descrizione_y, titolo_grafico, nome_immagine, parola, char_size=18):
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
    plt.grid(linestyle='-', linewidth=6, zorder=0)
    for utente in d_utente_list_y.keys():
        plt.plot(n, d_utente_list_y[utente][parola],
                 'o-', label=utente, linewidth=8, zorder=3)
    plt.legend(prop={'size': char_size})
    plt.yticks(fontsize=tick_char_size)
    plt.xticks(n, lista_x, rotation=90, fontsize=tick_char_size)

    nome_immagine += ".png"
    fig.savefig(nome_immagine)
    plt.close()


def grafico_wordcloud(dizionario_frequenza, titolo_grafico, nome_immagine, char_size):
    wc = WordCloud(width=3200, height=1600, background_color='white')
    wc.generate_from_frequencies(dizionario_frequenza)

    size = (20, 10)
    plt.figure(figsize=size)
    plt.title(titolo_grafico, fontsize=char_size)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    nome_immagine += ".png"

    plt.savefig(nome_immagine, face_color=None, bbox_inches='tight')
    plt.close()
