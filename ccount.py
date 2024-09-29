
import argparse
import string
import matplotlib.pyplot as plt
import time 
from loguru import logger


#funzione che agisce su due liste 
def istogramma(x,y):
    plt.figure(figsize=(12, 6))
    plt.bar(x, y)
    plt.xlabel("lettere")
    plt.ylabel("frequenze")
    plt.title("Istogramma")
    plt.show()


#funzione che agisce su un dizionario
def istogramma2(diz):
    plt.figure(figsize=(12, 6))
    x=list(diz.keys())
    y=list(diz.values())
    plt.bar(x,y)
    plt.xlabel("lettere")
    plt.ylabel("frequenze")
    plt.title("Istogramma")
    plt.show()


 


def count_characters(file_path, plot_histogram, etime):
    start = time.time()
   
    counts = {char: 0 for char in string.ascii_lowercase}
    # Rough equivalent
    # counts = {}
    # for char in string.ascii_lowercase:
    #     counts[char] = 0
    with open(file_path,'r',encoding='ISO-8859-1',errors='ignore') as input_file:
        logger.debug(f'Reading input data from {file_path}...')
        data = input_file.read()
    logger.debug(f'Done, {len(data)} character(s) found.')
    logger.info('Counting characters...')
    for char in data.lower():
        if char in counts:
            counts[char] += 1
    logger.info(f'Character counts: {counts}')
    num_characters = sum(counts.values())
    logger.info(f'Total number of characters: {num_characters}')
    for key, value in counts.items():
        counts[key] = value / num_characters
    logger.info(f'Character frequences: {counts}')
    
    end = time.time()
    
    if plot_histogram:
        #lettere=list(counts.keys())
        #valori=list(counts.values()) #adesso sono le frequenze, cambiato dentro il ciclo for in cui aggiorno valori del dizionario
        #istogramma(lettere,valori)
        istogramma2(counts)

    
    a= end - start
    if etime:
        logger.info(f"Tempo di esecuzione: {a:.6f} secondi")


     

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Count the characters in a text file')
    parser.add_argument('file')
    parser.add_argument('--histogram', action='store_true',
        help='plot a histogram of the character frequencies')
    parser.add_argument('--time', action='store_true',
        help='Tempo di esecuzione per contare i caratteri')
    
    args = parser.parse_args()
    count_characters(args.file, args.histogram, args.time)
