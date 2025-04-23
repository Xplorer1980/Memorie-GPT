
import os
import re
import shutil
import hashlib
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

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

def trova_duplicati(paths):
    file_map = {}
    for directory in paths:
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                base = get_base_name(file)
                file_map.setdefault(base, []).append(full_path)
    return file_map

def sposta_duplicati(paths, output_dir, progress_callback=None):
    os.makedirs(output_dir, exist_ok=True)
    log = []

    gruppi = trova_duplicati(paths)
    totale_file = sum(len(f) for f in gruppi.values())
    progress = 0

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

        preferiti = [p for p in percorsi if os.path.basename(p) == base]
        if preferiti and preferiti[0] in hash_mappa:
            file_da_tenere = preferiti[0]
        else:
            gruppi_identici = {}
            for path, (size, h) in hash_mappa.items():
                gruppi_identici.setdefault((size, h), []).append(path)
            gruppo_top = max(gruppi_identici.values(), key=lambda g: max(os.path.getmtime(p) for p in g))
            file_da_tenere = max(gruppo_top, key=os.path.getmtime)

        for path in percorsi:
            if path != file_da_tenere:
                if hash_mappa.get(path) == hash_mappa.get(file_da_tenere):
                    rel_path = os.path.relpath(path, os.path.commonpath(paths))
                    dest_path = os.path.join(output_dir, rel_path)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.move(path, dest_path)
                    log.append(f"Spostato: {rel_path}")
            progress += 1
            if progress_callback:
                progress_callback(progress, totale_file)

    return log

# GUI
class DuplicatiApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sposta Duplicati – Avanzato")
        self.master.geometry("500x300")
        self.paths = []

        tk.Label(master, text="📁 Cartelle da analizzare:").pack()
        self.path_listbox = tk.Listbox(master, height=5)
        self.path_listbox.pack(fill="x", padx=10)

        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="➕ Aggiungi cartella", command=self.aggiungi_cartella).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="❌ Rimuovi selezionata", command=self.rimuovi_cartella).grid(row=0, column=1, padx=5)

        tk.Label(master, text="📂 Dove creare la cartella DUPLICATI:").pack()
        self.output_path = tk.Entry(master, width=60)
        self.output_path.pack(padx=10)
        tk.Button(master, text="🔍 Scegli destinazione", command=self.scegli_destinazione).pack(pady=5)

        self.progress = ttk.Progressbar(master, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        tk.Button(master, text="🚀 Avvia analisi duplicati", command=self.avvia).pack(pady=5)

    def aggiungi_cartella(self):
        folder = filedialog.askdirectory()
        if folder and folder not in self.paths:
            self.paths.append(folder)
            self.path_listbox.insert(tk.END, folder)

    def rimuovi_cartella(self):
        selected = self.path_listbox.curselection()
        for index in reversed(selected):
            self.paths.pop(index)
            self.path_listbox.delete(index)

    def scegli_destinazione(self):
        dest = filedialog.askdirectory()
        if dest:
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, dest)

    def aggiorna_progresso(self, current, total):
        self.progress["value"] = int((current / total) * 100)
        self.master.update_idletasks()

    def avvia(self):
        if not self.paths:
            messagebox.showwarning("Attenzione", "Nessuna cartella selezionata.")
            return
        if not self.output_path.get():
            messagebox.showwarning("Attenzione", "Seleziona una destinazione per DUPLICATI.")
            return

        destinazione = os.path.join(self.output_path.get(), "DUPLICATI")
        log = sposta_duplicati(self.paths, destinazione, self.aggiorna_progresso)

        if log:
            log_path = os.path.join(destinazione, "log_duplicati.txt")
            with open(log_path, "w", encoding="utf-8") as f:
                for line in log:
                    f.write(line + "\n")
            messagebox.showinfo("Completato", f"{len(log)} duplicati spostati.\nLog: {log_path}")
        else:
            messagebox.showinfo("Completato", "Nessun duplicato reale trovato.")
        self.progress["value"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicatiApp(root)
    root.mainloop()
