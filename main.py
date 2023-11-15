from file_reader import read_excel_files
from report_generator import generate_small_text_report, tabular_report
#from data_analyzer import analyze_data
from data_reorganizer import reorganize_data_merge, merge_dataframes_ordered
from excel_writer import write_excel_file

def main(input_folder, output_filename):
    # Passo 1: Lettura dei file Excel nella cartella di input
    dataframes = read_excel_files(input_folder)

    # Passo 2: Generazione dei report
    for filename, df in dataframes.items():
        other = set(dataframes)
        other.discard(filename)
        print(other, filename)
        filtered_dict = {key: value for key, value in dataframes.items() if key in other}

        report_filename = f"report_{filename}.txt"
        generate_small_text_report(df, "reports", report_filename)
        rep = tabular_report(df)
        
        #print(rep,end='\n\n')
        missing = rep[rep.columns[2]]
        check = (missing != 0).any()
        # Se il check e' TRUE, c'è una colonna che manca di alcuni dati.
        # E' necessario cercarli nel resto delle tabelle.
        # il resto delle tabelle è il dizionario filtered_dict
        print(check)


    # Passo 3: Analisi dei dati
    """for filename, df in dataframes.items():
        data_info = analyze_data(df)
        print(f"Analisi dei dati in {filename}:")
        for key, value in data_info.items():
            print(f"{key}: {value}")"""

    # Passo 4: Riorganizzazione dei dati
    #reorganized_data = 
    reorganize_data_merge(dataframes)
    #merged = merge_dataframes_ordered(dataframes)
    #print(merged)
    #merged.to_csv('output.csv')

    # Passo 5: Scrittura del file Excel di output
    #write_excel_file(output_filename, reorganized_data)

if __name__ == "__main__":
    input_folder = "input_data"  # Specifica il percorso della cartella di input
    output_filename = "output.xlsx"  # Specifica il nome del file Excel di output
    main(input_folder, output_filename)
