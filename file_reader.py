import os
import pandas as pd

def read_excel_files(input_folder):
    """
    Legge i file Excel nella cartella di input e restituisce un dizionario in cui le chiavi sono i nomi dei file e i valori sono i DataFrame pandas corrispondenti.

    :param input_folder: La cartella contenente i file Excel da leggere.
    :return: Un dizionario con i nomi dei file e i DataFrame.
    """
    excel_data = {}

    # Verifica che la cartella di input esista
    if not os.path.exists(input_folder):
        print(f"La cartella {input_folder} non esiste.")
        return excel_data

    # Scandisci i file nella cartella di input
    for filename in os.listdir(input_folder):
        if filename.endswith(".xlsx"):  # Assumiamo che siano file Excel
            file_path = os.path.join(input_folder, filename)
            try:
                df = pd.read_excel(file_path)
                excel_data[filename] = df
                print(f"Lettura di {filename} completata.")
            except Exception as e:
                print(f"Errore durante la lettura di {filename}: {str(e)}")

    return excel_data

if __name__ == "__main__":
    # Esempio di utilizzo del modulo
    input_folder = "input_data"  # Specifica il percorso della cartella di input
    data = read_excel_files(input_folder)
    # Puoi ora lavorare con i dati DataFrame restituiti
