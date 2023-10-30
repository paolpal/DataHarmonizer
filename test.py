import pandas as pd
import os
from itertools import combinations

# Percorso della cartella contenente i file Excel
folder_path = "input_data"

# Elenco dei nomi dei file Excel nella cartella
file_names = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]

# Creazione di una lista di DataFrame dai file Excel
dataframes = [pd.read_excel(os.path.join(folder_path, file_name)) for file_name in file_names]

# Unione di tutti i DataFrame in tutte le possibili combinazioni
merged_dataframes = []
for i in range(1, len(dataframes) + 1):
    for combo in combinations(dataframes, i):
        merged_df = combo[0] if len(combo) == 1 else pd.concat(combo, axis=1)
        merged_dataframes.append(merged_df)

# Ora merged_dataframes contiene tutte le possibili combinazioni di DataFrame
# E' possibile eseguire ulteriori operazioni di pulizia, aggregazione o trasformazione sui DataFrame risultanti

# Salva i DataFrame risultanti in file Excel separati
for idx, df in enumerate(merged_dataframes):
    df.to_excel(f"combination/combined_data_{idx+1}.xlsx", index=False)
