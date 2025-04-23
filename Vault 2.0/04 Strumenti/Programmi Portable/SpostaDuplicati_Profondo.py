
import os
import re
import shutil
import hashlib
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def get_base_name(filename):
    return re.sub(r'\s\(\d+\)', '', filename)

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_zip_content_hash(filepath):
    hash_list = []
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            for info in sorted(z.infolist(), key=lambda x: x.filename):
                if not info.is_dir():
                    with z.open(info.filename) as file:
                        content = file.read()
                        file_hash = hashlib.sha256(content).hexdigest()
                        hash_list.append(f"{info.filename}:{file_hash}")
        return hashlib.sha256("".join(hash_list).encode()).hexdigest()
    except Exception as e:
        return f"ERROR:{str(e)}"

def trova_duplicati_contenuto(directory):
    file_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            base = get_base_name(file)
            file_map.setdefault(base, []).append(full_path)
    return file_map

def sposta_duplicati(directory):
    duplicati_dir = os.path.join(directory, "DUPLICATI")
    os.makedirs(duplicati_dir, exist_ok=True)
    log = []

    gruppi = trova_duplicati_contenuto(directory)
    for base, percorsi in gruppi.items():
        if len(percorsi) <= 1:
            continue

        hash_mappa = {}
        for path in percorsi:
            try:
                size = os.path.getsize(path)
                if path.lower().endswith('.zip'):
                    hash_val = get_zip_content_hash(path)
                else:
                    hash_val = get_file_hash(path)
                hash_mappa[path] = (size, hash_val)
            except Exception as e:
                log.append(f"Errore: {path} → {e}")

        # Se c'è una versione "senza numero", preferisci quella
        preferiti = [p for p in percorsi if os.path.basename(p) == base]
        if preferiti and preferiti[0] in hash_mappa:
            file_da_tenere = preferiti[0]
        else:
            # Tieni la versione più recente tra quelle identiche
            gruppi_identici = {}
            for path, (size, h) in hash_mappa.items():
                gruppi_identici.setdefault((size, h), []).append(path)

            gruppo_top = max(gruppi_identici.values(), key=lambda g: max(os.path.getmtime(p) for p in g))
            file_da_tenere = max(gruppo_top, key=os.path.getmtime)

        for path in percorsi:
            if path != file_da_tenere:
                if hash_mappa.get(path) == hash_mappa.get(file_da_tenere):
                    # Sposta mantenendo la struttura
                    rel_path = os.path.relpath(path, directory)
                    dest_path = os.path.join(duplicati_dir, rel_path)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.move(path, dest_path)
                    log.append(f"Spostato: {rel_path}")
                else:
                    log.append(f"Non spostato (diverso): {os.path.relpath(path, directory)}")

    return log

def seleziona_cartella():
    folder = filedialog.askdirectory()
    if not folder:
        return

    log = sposta_duplicati(folder)

    if log:
        log_path = os.path.join(folder, "DUPLICATI", "log_duplicati.txt")
        with open(log_path, "w", encoding="utf-8") as f:
            for line in log:
                f.write(line + "\n")
        messagebox.showinfo("Completato", f"{sum('Spostato:' in l for l in log)} duplicati reali spostati.\nLog in:\n{log_path}")
    else:
        messagebox.showinfo("Completato", "Nessun duplicato reale trovato.")

# GUI
root = tk.Tk()
root.title("Sposta Duplicati – Profonda (SHA256 + ZIP + Ricorsiva)")
root.geometry("500x180")

tk.Label(root, text="📁 Seleziona la cartella da analizzare").pack(pady=20)
tk.Button(root, text="🔍 Scansiona cartella", command=seleziona_cartella, bg="#4CAF50", fg="white").pack(pady=10)

tk.Label(root, text="✔ Analizza anche sottocartelle e contenuto ZIP\n✔ Mantiene solo duplicati reali (SHA-256)").pack(pady=10)

root.mainloop()
