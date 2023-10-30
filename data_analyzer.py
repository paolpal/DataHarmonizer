import pandas as pd

def analyze_data(dataframe):
    """
    Analizza i dati in un DataFrame pandas e restituisce informazioni rilevanti.

    :param dataframe: Il DataFrame pandas contenente i dati da analizzare.
    :return: Un dizionario con le informazioni raccolte.
    """
    data_info = {}

    # Esempio: Calcola il numero totale di righe
    data_info["Numero totale di righe"] = len(dataframe)

    # Esempio: Elenca i nomi delle colonne
    data_info["Nomi delle colonne"] = dataframe.columns.tolist()

    # Puoi aggiungere altre analisi specifiche ai tuoi dati

    return data_info

if __name__ == "__main__":
    # Esempio di utilizzo del modulo
    excel_file_path = "esempio.xlsx"  # Specifica il percorso del file Excel da analizzare
    data = pd.read_excel(excel_file_path)  # Leggi il file Excel
    analysis_result = analyze_data(data)  # Esegui l'analisi
    # Puoi ora lavorare con le informazioni raccolte
