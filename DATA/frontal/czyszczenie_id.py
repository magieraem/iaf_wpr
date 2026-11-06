import pandas as pd
import os
from collections import Counter


dir_path_list = ["LST", "TAO"]
csv_path = r'/mnt/data/ociepka_idUJ/BDF/OB_Mich_UTF8.csv'

if not os.path.exists(csv_path):
        print("CSV file not found!")
        exit()

df = pd.read_csv(csv_path, sep=';')
ID_kolumna = df['ID'].tolist()

for folder in dir_path_list:
    print(f"\n-----{folder}-----")
    dir_path =f'/mnt/data/ociepka_idUJ/BEH_z_laptopa/IDUJ_Michala/{folder}/results'

    #/mnt/data/ociepka_idUJ/BDF/{folder}
    #/home/magiera/BDF_e/BDF/3_WPR

    #/mnt/data/ociepka_idUJ/BDF/OB_Mich_UTF8.csv
    #/home/magiera/OB_Mich_UTF8.csv
    
    if not os.path.exists(dir_path):
        print(f"[MISSING FOLDER] {dir_path}")
        continue

    #csv
    file_list_raw = os.listdir(dir_path)
    
    file_list = [
        f.split('_')[1]
        for f in file_list_raw
        if f.endswith('.csv') and len(f.split('_')) > 1
    ]
    print(file_list)

    #robic?
    #ID_kolumna = [i.strip().upper() for i in ID_kolumna_raw]

    #takie same ID 
    common_ID = set(file_list).intersection(ID_kolumna)
    #w pliku ale nie excelu/na odwrot
    missing_excel = set(file_list) - set(ID_kolumna)
    missing_file = set(ID_kolumna) - set(file_list)

    versions = {
        ID: count
        for ID, count in Counter(file_list).items()
        if count > 1
    }
    
    print(f"\nWspólne ID: {common_ID}")
    print(f"\nWersje plików (ID występujące wielokrotnie): {versions}")
    print(f"\nMissing in Excel (pliki bez ID w Excelu): {missing_excel}")
    print(f"\nMissing file (ID w Excelu bez pliku): {missing_file}")