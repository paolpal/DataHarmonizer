import os
import pandas as pd

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

def tabular_report(df):
    righe = []
    
    for colonna in df.columns:
        #numero_di_celle = len(df[colonna])
        numero_di_celle = (df[colonna].count())
        percentuale_valori_mancanti = df[colonna].isnull().mean() * 100
        percentuale_valori_univoci = df[colonna].nunique() / numero_di_celle * 100
        
        righe.append({
            'Colonna': colonna,
            'Numero di celle': numero_di_celle,
            '% Valori mancanti': percentuale_valori_mancanti,
            '% Valori univoci': percentuale_valori_univoci
        })
    
    # Creare un nuovo DataFrame dalla lista di dizionari
    tabella = pd.DataFrame(righe)
    
    return tabella



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

