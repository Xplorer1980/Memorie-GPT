
# 🧰 Guida – Convertire uno script Python `.py` in `.exe` (con Kit Portabile)

Questa guida ti accompagna passo passo nella trasformazione di uno script `.py` in un file eseguibile `.exe`, **senza installare nulla sul PC**.  
È pensata per essere inclusa nel tuo vault Obsidian, con collegamenti diretti e istruzioni **completamente portabili**.

---

## 📦 1. Scarica il Kit Compiler Portatile

📥 **Link per scaricare il kit ZIP** (da posizionare sul tuo cloud personale):  
👉 `[Inserisci qui il link definitivo al tuo Kit_PyCompiler_Portable.zip]`

Il pacchetto contiene:
- ✅ Python portatile (già configurato)
- ✅ PyInstaller preinstallato
- ✅ Un file `.bat` per convertire qualsiasi `.py` in `.exe`
- ✅ Esempi e README

---

## 📁 2. Estrai il Kit dove preferisci

Puoi metterlo su:
- Chiavetta USB
- Cartella locale sul tuo PC
- Cartella sincronizzata in MEGA, Google Drive, Dropbox, ecc.

Non richiede installazione. Tutti i file restano locali e non toccano il sistema.

---

## 🧪 3. Come convertire un file `.py` in `.exe`

1. **Apri la cartella del Kit**
2. Copia all’interno il file `.py` che vuoi convertire (es: `SpostaDuplicati.py`)
3. Fai doppio clic su:  
   ```
   converti.bat
   ```
4. Si aprirà una finestra che ti chiede il nome del file `.py` da compilare (puoi anche trascinarlo dentro la finestra)
5. Attendi la fine del processo
6. Il tuo `.exe` sarà disponibile nella sottocartella:
   ```
   dist/NomeScript.exe
   ```

---

## ⚙️ Opzioni disponibili

Il file `converti.bat` usa internamente:

```
pyinstaller --onefile --windowed %1
```

Puoi modificarlo per includere:
- Un’icona `.ico`
- Librerie specifiche
- File esterni

Esempio avanzato:
```bat
pyinstaller --onefile --windowed --icon=icon.ico SpostaDuplicati.py
```

---

## 🔄 Note importanti

- ✅ I file `.exe` generati sono **standalone**: non richiedono Python installato sul PC dove li usi
- ✅ La cartella `build/` può essere eliminata dopo ogni compilazione
- ✅ Il file `.spec` serve solo se vuoi personalizzare le future build

---

## 📝 Buone pratiche

- Conserva il tuo Kit sempre aggiornato
- Tieni una copia della guida anche nella cartella del kit
- Se usi script grafici (`tkinter`), assicurati di avere `--windowed` nel comando

---

## 📌 Collegamenti utili

- 🔗 [Documentazione PyInstaller](https://pyinstaller.org/en/stable/)
- 🔗 [WinPython (Python portabile ufficiale)](https://winpython.github.io/)
- 🔗 [Guida PyInstaller su StackOverflow](https://stackoverflow.com/questions/41570359/pyinstaller-and-onefile)

---

## 📂 Esempio struttura

```
Kit_PyCompiler_Portable/
│
├── python-embedded/
├── pyinstaller/
├── converti.bat
├── README.txt
├── dist/
└── build/
```

---

## ✅ Sei pronto

Ora puoi convertire tutti gli script `.py` creati nel tuo sistema direttamente in `.exe`, anche su un PC nuovo o appena formattato.

Nessuna installazione. Nessuna dipendenza. Massima portabilità.
