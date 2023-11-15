import pandas as pd

def write_excel_file(output_filename, dataframes):
    """
    Scrive un file Excel con i dati riorganizzati.

    :param output_filename: Il nome del file Excel di output.
    :param dataframes: Un dizionario con i DataFrame pandas riorganizzati.
    """
    #writer = pd.ExcelWriter(output_filename, engine='openpyxl')

    # Scrivi ogni DataFrame in una scheda separata del file Excel
    for _, df in dataframes.items():
        df.to_excel(output_filename, index=False)

    #writer.save()

if __name__ == "__main__":
    # Esempio di utilizzo del modulo
    # Dataframes è un dizionario con i nomi dei file Excel e i rispettivi DataFrame riorganizzati
    dataframes = {
        "file1.xlsx": reorganized_data1,  # Sostituire con i dati riorganizzati effettivi
        "file2.xlsx": reorganized_data2  # Sostituire con i dati riorganizzati effettivi
    }

    output_filename = "output.xlsx"  # Specifica il nome del file Excel di output
    write_excel_file(output_filename, dataframes)  # Scrivi il file Excel di output
