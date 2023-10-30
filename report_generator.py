import os
import pandas as pd

def generate_text_report(dataframe, report_folder, filename):
    """
    Genera un report testuale in formato .txt con informazioni dettagliate sui dati nel DataFrame pandas.

    :param dataframe: Il DataFrame pandas da cui generare il report.
    :param report_folder: La cartella in cui salvare il report.
    :param filename: Il nome del file di report.
    """
    report_path = os.path.join(report_folder, filename)

    with open(report_path, "w") as file:
        file.write("Report sui dati nel DataFrame:\n")

        # Sezione 1: Contenuto dei dati
        file.write("\nSezione 1: Contenuto dei dati\n")
        for column in dataframe.columns:
            unique_values = dataframe[column].unique()
            file.write(f"Colonna: {column}\n")
            file.write(f"Valori unici presenti: {', '.join(map(str, unique_values))}\n")

        # Sezione 2: Statistiche sui dati
        file.write("\nSezione 2: Statistiche sui dati\n")
        file.write(f"Numero di righe totali: {len(dataframe)}\n")

        # Sezione 3: Dati Mancanti
        file.write("\nSezione 3: Dati Mancanti\n")
        missing_data = dataframe.isnull().sum()
        for column, count in missing_data.iteritems():
            if count > 0:
                file.write(f"Colonna con dati mancanti: {column}\n")
                file.write(f"Numero di dati mancanti: {count}\n")


def generate_report(dataframe, report_folder, filename):
    """
    Genera un report da un DataFrame pandas e lo salva nella cartella "reports".

    :param dataframe: Il DataFrame pandas da cui generare il report.
    :param report_folder: La cartella in cui salvare il report.
    :param filename: Il nome del file di report.
    """
    report = {}

    # Numero di colonne
    report["Numero di colonne"] = len(dataframe.columns)

    # Statistiche per ciascuna colonna
    for column in dataframe.columns:
        report[f"Colonna: {column}"] = {
            "Numero di celle mancanti": dataframe[column].isna().sum(),
            "Tipi di dati": dataframe[column].dtype,
            "Statistiche descrittive": dataframe[column].describe()
        }

    # Crea il percorso completo per il file di report nella cartella "reports"
    report_path = os.path.join(report_folder, filename)

    # Salva il report in un file di testo
    with open(report_path, "w") as file:
        for key, value in report.items():
            file.write(f"{key}:\n")
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    file.write(f"  {sub_key}: {sub_value}\n")
            else:
                file.write(f"  {value}\n")

def generate_small_text_report(dataframe, report_folder, filename):
    """
    Genera un report testuale in formato .txt con informazioni dettagliate sui dati nel DataFrame pandas.

    :param dataframe: Il DataFrame pandas da cui generare il report.
    :param report_folder: La cartella in cui salvare il report.
    :param filename: Il nome del file di report.
    """
    report_path = os.path.join(report_folder, filename)

    with open(report_path, "w") as file:
        file.write(f"Report dal file Excel: {filename}\n")
        file.write(f"Numero totale di righe: {len(dataframe)}\n")
        file.write(f"Numero totale di colonne: {len(dataframe.columns)}\n")
        file.write("Elenco delle colonne:\n")
        for column in dataframe.columns:
            file.write(f"- {column}\n")

        file.write("\nCelle vuote per colonna:\n")
        empty_cells = dataframe.isna().sum()
        for column, count in empty_cells.items():
            file.write(f"{column:<10} {count}\n")



if __name__ == "__main__":
    # Esempio di utilizzo del modulo
    excel_file_path = "esempio.xlsx"  # Specifica il percorso del file Excel da analizzare
    report_folder = "reports"  # Specifica la cartella dei report
    report_file = "report.txt"  # Specifica il nome del file di report
    data = pd.read_excel(excel_file_path)  # Leggi il file Excel
    generate_report(data, report_folder, report_file)  # Genera e salva il report testuale

    # Esempio di utilizzo del modulo
    excel_file_path = "esempio.xlsx"  # Specifica il percorso del file Excel da analizzare
    report_folder = "reports"  # Specifica la cartella dei report
    report_filename = "report.txt"  # Specifica il nome del file di report
    data = pd.read_excel(excel_file_path)  # Leggi il file Excel
    generate_text_report(data, report_folder, report_filename)  # Genera e salva il report testuale

