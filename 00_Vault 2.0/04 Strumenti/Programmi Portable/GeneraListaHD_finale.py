
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def count_items(path, extensions=None, exclude_dirs=None, only_dirs=False):
    total_files = 0
    total_dirs = 0
    for root, dirs, files in os.walk(path):
        if exclude_dirs and any(skip.lower() in root.lower() for skip in exclude_dirs):
            continue
        total_dirs += len(dirs)
        if only_dirs:
            continue
        if extensions:
            files = [f for f in files if os.path.splitext(f)[1].lower() in extensions]
        total_files += len(files)
    return total_dirs, total_files

def generate_tree(path, output_txt, output_md, log_file, extensions=None, exclude_dirs=None, only_dirs=False):
    with open(output_txt, "w", encoding="utf-8") as txt, open(output_md, "w", encoding="utf-8") as md, open(log_file, "w", encoding="utf-8") as log:
        for root, dirs, files in os.walk(path):
            if exclude_dirs and any(skip.lower() in root.lower() for skip in exclude_dirs):
                continue
            level = root.replace(path, '').count(os.sep)
            indent = '    ' * level
            folder_name = os.path.basename(root)
            txt.write(f"{indent}📁 {folder_name}\n")
            md.write(f"{'#' * (level+1)} {folder_name}\n")
            log.write(f"{root}\n")

            if not only_dirs:
                subindent = '    ' * (level + 1)
                if extensions:
                    files = [f for f in files if os.path.splitext(f)[1].lower() in extensions]
                for file in files:
                    txt.write(f"{subindent}- {file}\n")
                    md.write(f"- {file}\n")
                    log.write(f"  {file}\n")

        total_dirs, total_files = count_items(path, extensions, exclude_dirs, only_dirs)
        summary = f"\n-----\nTotale cartelle: {total_dirs}\nTotale file: {total_files}\n"
        txt.write(summary)
        md.write(f"\n## Statistiche finali\n- Totale cartelle: {total_dirs}\n- Totale file: {total_files}\n")
        log.write(summary)

def browse_source():
    path = filedialog.askdirectory()
    if path:
        entry_source.delete(0, tk.END)
        entry_source.insert(0, path)

def browse_save():
    path = filedialog.askdirectory()
    if path:
        entry_save.delete(0, tk.END)
        entry_save.insert(0, path)

def generate():
    source_path = entry_source.get().strip()
    save_path = entry_save.get().strip()
    extensions = entry_ext.get().strip()
    exclude_dirs = entry_excl.get().strip()
    only_dirs = var_only_dirs.get()
    auto_open = var_open.get()

    if not os.path.exists(source_path):
        messagebox.showerror("Errore", "Il percorso da analizzare non esiste.")
        return
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    exts = [e.strip().lower() if e.strip().startswith('.') else '.' + e.strip().lower() for e in extensions.split(',')] if extensions else None
    excl = [e.strip() for e in exclude_dirs.split(',')] if exclude_dirs else None

    folder_name = os.path.basename(os.path.normpath(source_path)) or "Drive"
    today = datetime.now().strftime("%Y-%m-%d")
    base_filename = f"{today} - {folder_name}"
    output_txt = os.path.join(save_path, base_filename + ".txt")
    output_md = os.path.join(save_path, base_filename + ".md")
    log_file = os.path.join(save_path, base_filename + "_log.txt")

    generate_tree(source_path, output_txt, output_md, log_file, exts, excl, only_dirs)

    messagebox.showinfo("Completato", f"File generati:\n\nTXT: {output_txt}\nMD: {output_md}\n\nLog: {log_file}")

    if auto_open:
        os.startfile(save_path)

# GUI setup
root = tk.Tk()
root.title("Genera Lista HD - Struttura ad Albero")
root.geometry("600x400")

tk.Label(root, text="📁 Cartella da analizzare:").pack()
entry_source = tk.Entry(root, width=80)
entry_source.pack()
tk.Button(root, text="Sfoglia", command=browse_source).pack()

tk.Label(root, text="\n💾 Cartella di destinazione:").pack()
entry_save = tk.Entry(root, width=80)
entry_save.pack()
tk.Button(root, text="Sfoglia", command=browse_save).pack()

tk.Label(root, text="\n📦 Estensioni da includere (es: .jpg,.pdf):").pack()
entry_ext = tk.Entry(root, width=80)
entry_ext.pack()

tk.Label(root, text="🚫 Cartelle da escludere (es: backup,temp):").pack()
entry_excl = tk.Entry(root, width=80)
entry_excl.pack()

var_only_dirs = tk.BooleanVar()
tk.Checkbutton(root, text="📂 Solo cartelle (non includere i file)", variable=var_only_dirs).pack()

var_open = tk.BooleanVar()
tk.Checkbutton(root, text="📬 Apri cartella al termine", variable=var_open).pack()

tk.Button(root, text="\n🧠 Genera Lista\n", command=generate, bg="#4CAF50", fg="white").pack()

root.mainloop()
