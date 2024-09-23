import argparse   #da capire il funzionamento di questo modulo
import string   #serve per creare dizionario in modo comodo

from loguru import logger   #serve per fare print 



#definiamo una funzione fuori dal programma poi la eseguiao dopo, ora la sto solo importando
#vogliamo fare un programma che conta le occorrenze di ogni lettera
#vogliamo mettere il testo da schermo
def count_characters(file_path, plot_histogram):   #funzione con due variabili 
    counts = {char: 0 for char in string.ascii_lowercase}    #count è un dizionario, le chiavi sono char dentro la stringa asci
    #ossia sono tutte le lettere tra a-z. ogni chiave ha come valore fissato 0
    #facciamo un dizionario con tutte le lettere e poi impostiamo tutte le occorrenze a 0, poi man mano che le trovo le aumento
    # Rough equivalent
    # counts = {}
    # for char in string.ascii_lowercase:
    #     counts[char] = 0

    with open(file_path) as input_file:
        logger.debug(f'Reading input data from {file_path}...')
        data = input_file.read()  #quelllo che leggiamo lo mettiamo come nostro dato 


    #with modo per leggere il file e poi chiuderlo, dopo che leggiamo il file abbiamo tutto 

    #con il logger facciamo praticamente il print
    logger.debug(f'Done, {len(data)} character(s) found.')  #ci dice di quanti caratteri è fatto il nostro documento
    logger.info('Counting characters...')  

    #definisco la variabile char, controllo tutte le char dentro il mio insieme di dati, passiamo da data a data.lower perchè 
    #abbiamo convertito tutto il testo in minuscole 
    #controllo ogni lettera, se questo carattere è dentro il mio dizionario ( if char in counts) ossia è una chiave 
    #del mio dizionario allora aumenta di uno il valore della rispettivachiave
    for char in data.lower():
        if char in counts:
            counts[char] += 1

    #mi dice che ho contato i caratteri       
    logger.info(f'Character counts: {counts}')

    #sommo di valori di tutte le chiavi così vedo quale è il numero totale di lettere contante 
    num_characters = sum(counts.values())
    logger.info(f'Total number of characters: {num_characters}')


    for key, value in counts.items():  #costrutto per iterare dentro un dizionario, key la chiave del diz e value il valore
        #.items restituisce una tupla delle coppie chiave valore
        counts[key] = value / num_characters  #sostituiamo il valore di chiave conil nuo valore diviso il numero di caratteri




    #(Il codice itera su tutte le coppie chiave-valore di un dizionario chiamato counts, 
    # e aggiorna il valore associato a ciascuna chiave dividendo il valore originale per num_characters. Questo potrebbe essere utile, 
    # ad esempio, per normalizzare i valori nel dizionario, come nel caso in cui 
    # counts rappresenti un conteggio di caratteri o elementi e si desideri ottenere una proporzione rispetto al totale num_characters)



    logger.info(f'Character frequences: {counts}')  #occorrenze di ogni lettera
    if plot_histogram:
        # Do something...  #parte per fare un istogramma delle occorrenze
        pass


if __name__ == '__main__':
    #se lo script è eseguito direttamente e non importato da un altro modulo allora la variabile name vale maine viene eseguito il codice
    #se è importato la variabile main ha il valore del modulo da cui è importata
    parser = argparse.ArgumentParser(description='Count the characters in a text file')
    parser.add_argument('file')
    parser.add_argument('--histogram', action='store_true',
        help='plot a histogram of the character frequencies')  #argomento facolattivo, se questo viene dato allora 
        #args.histogram vale true  (utile per quando richiamo riga 62)
    
    #se metto -- davanti ad un argomento signidica che questo è opzionale
    args = parser.parse_args()   #gli argomenti sono quelli dati dall'utente da riga di comando 
    count_characters(args.file, args.histogram)  #richiamo la funzione count-characters impostando il valore delle variabile 