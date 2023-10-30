import pandas as pd

def reorganize_data_merge(dataframes):
    """
    Riorganizza i dati nei file Excel, integrando le celle vuote con dati dai file correlati.

    :param dataframes: Un dizionario con i nomi dei file Excel e i rispettivi DataFrame pandas.
    :return: Un dizionario con i DataFrame riorganizzati.
    """
    reorganized_data = {}

    # Creare un dizionario di mapping per ciascuna colonna
    column_mapping = {column: {} for column in dataframes[next(iter(dataframes))].columns}

    # Popolare il dizionario di mapping con dati dai DataFrame
    for filename, df in dataframes.items():
        for column in df.columns:
            # Usare una chiave univoca basata sul nome della colonna e il nome del file
            unique_column_key = f"{column} ({filename})"
            column_mapping[unique_column_key] = df[column]

    # Esempio: Riorganizza i dati integrando i dati dai file correlati e mantenendo corrispondenze
    for filename, df in dataframes.items():
        reorganized_df = df.copy()
        for column in df.columns:
            for related_file, related_data in column_mapping.items():
                if related_file != filename:  # Evita di copiare dati dallo stesso file
                    unique_column_key = f"{column} ({related_file})"
                    reorganized_df[column].fillna(related_data, inplace=True)
        reorganized_data[filename] = reorganized_df

    return reorganized_data
