# =====================================================================
# PARQUET → CSV CONVERSION TOOL
# Autore: Gennaro (Studente di Informatica L-31)
# Ambiente: Python 3.x (Anaconda / Jupyter Notebook)
# Descrizione:
#   Questo notebook consente di leggere uno o più file .parquet da una
#   cartella locale, ispezionarli e convertirli in formato .csv.
# =====================================================================

# -------------------------------------------------------
# 📦 1. Importazione librerie necessarie
# -------------------------------------------------------
import pandas as pd
import os
from pathlib import Path

# -------------------------------------------------------
# ⚙️ 2. Impostazioni di base
# -------------------------------------------------------
# Inserisci qui il percorso della cartella dove si trovano i file .parquet
# Esempio: r"C:\Users\Gennaro\Documents\Dataset"
cartella_input = input("Inserisci il percorso della cartella contenente i file .parquet: ").strip()

# Cartella di output (dove salvare i CSV)
cartella_output = os.path.join(cartella_input, "csv_output")
os.makedirs(cartella_output, exist_ok=True)

# -------------------------------------------------------
# 🔍 3. Ricerca file Parquet nella cartella
# -------------------------------------------------------
file_parquet = list(Path(cartella_input).rglob("*.parquet"))

if not file_parquet:
    print("⚠️ Nessun file .parquet trovato nella cartella indicata.")
else:
    print(f"✅ Trovati {len(file_parquet)} file .parquet.\n")

# -------------------------------------------------------
# 🧠 4. Conversione file Parquet → CSV
# -------------------------------------------------------
for file_path in file_parquet:
    try:
        print(f"Elaboro: {file_path.name}")
        
        # Legge il file Parquet
        df = pd.read_parquet(file_path)
        
        # Mostra info sintetiche
        print(f"  → Righe: {len(df)}, Colonne: {len(df.columns)}")
        print(f"  → Colonne: {list(df.columns)[:10]}{'...' if len(df.columns) > 10 else ''}")
        
        # Crea nome file CSV di output
        csv_path = os.path.join(cartella_output, file_path.stem + ".csv")
        
        # Salva in CSV
        df.to_csv(csv_path, index=False)
        print(f"  ✅ Salvato: {csv_path}\n")

    except Exception as e:
        print(f"  ❌ Errore con {file_path.name}: {e}\n")

# -------------------------------------------------------
# 📊 5. Riepilogo finale
# -------------------------------------------------------
print("-------------------------------------------------------")
print(f"Conversione completata. File CSV salvati in: {cartella_output}")
print("-------------------------------------------------------")

