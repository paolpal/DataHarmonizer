import pandas as pd
import data_analyzer as da
from itertools import combinations
from functools import reduce

def reorganize_data_merge(dataframes):
    """
    Riorganizza i dati nei file Excel, integrando le celle vuote con dati dai file correlati.

    :param dataframes: Un dizionario con i nomi dei file Excel e i rispettivi DataFrame pandas.
    :return: Un dizionario con i DataFrame riorganizzati.
    """
    #for filename, df in dataframes.items():
    #    print(filename)
    #    print(df)

    
    for pair in combinations(dataframes.items(), 2):
            #print(pair[0][0]+" "+pair[1][0])
            sim = da.similarity(pair[0][1],pair[1][1])
            #print(len(sim['Colonna1']))

    return 

def merge_two_dataframes(df1, df2):
    return pd.merge(df1, df2, how='outer')

def merge_dataframes_ordered(dataframes):
    # Calcola tutte le possibili coppie di DataFrame
    all_pairs = list(combinations(dataframes.items(), 2))

    # Calcola la similarità per ciascuna coppia
    similarities = [(pair[0][1], pair[1][1], da.similarity(pair[0][1],pair[1][1])) for pair in all_pairs]
    #print(similarities[:][:])
    # Ordina le coppie in base alla similarità in ordine decrescente
    #similarities.sort(key=lambda x: len(x[2]['Colonna1']), reverse=True)

    # Unisci i DataFrame nell'ordine della similarità massima
    merged_df = pd.DataFrame()
    tables_dict = list(dataframes.items())
    tables = [t[1] for t in tables_dict] 
    #for pair in similarities:
    #    merged_df = pd.merge(merged_df, [pair[0][1]], how='outer', left_index=True, right_index=True)
    #    merged_df = pd.merge(merged_df, [pair[1][1]], how='outer', left_index=True, right_index=True)

    """for _, df in dataframes.items():
        print(merged_df)
        merged_df = pd.merge(merged_df,df,how='outer')"""
    merged_df = reduce(merge_two_dataframes, tables)
    


# Usa functools.reduce per applicare la funzione di merge a tutta la lista di DataFrame

    return merged_df
