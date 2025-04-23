# 🎓 Lezione 01 – Interfaccia Base & Importanza della Modalità Edit

Questa lezione è stata costruita integrando la trascrizione originale del corso con il lavoro già svolto nella nostra versione guidata.  
Include sia nozioni sull’interfaccia che un esercizio pratico (il dado), con riflessioni personali e blocchi di consolidamento.

---

## 🧭 Concetti fondamentali

### 🔹 Interfaccia iniziale
- Disattiva l’apertura automatica della home:
  - `Preferences > Lightbox > Open at Launch` → OFF
  - `Preferences > Config > Store Config`

### 🔹 Lightbox
- Si apre con la virgola `,`
- Permette di accedere a progetti, ZTools, pennelli, materiali ecc.
- Puoi caricare uno ZTool da `Lightbox > Tool` (es. dog.ZTL)

### 🔹 ZProject vs ZTool
- **ZProject**: contiene più oggetti (SubTools)
- **ZTool**: singolo oggetto/scultura (es. un cane, una sfera, ecc.)

### 🔹 Aggiunta e modifica oggetti
1. Apri Lightbox e trascina una ZTool nella scena
2. Attiva subito **Edit** (`T`) altrimenti non puoi scolpire
3. Clic in canvas = aggiunge nuova istanza (ma solo la prima serve)
4. Usa `Ctrl + N` per cancellare la canvas e ripartire

### 🔹 Modalità di navigazione
- Zoom: `Alt + clic + rilascio Alt + trascina`
- Pan: `Alt + clic + trascina`
- Rotate: clic vuoto + trascina
- Frame oggetto: `F`

---

## 🧩 Pannelli e menu personalizzabili

- Puoi trascinare qualsiasi sezione dal menu principale ai pannelli laterali
- Usa il **punto bianco** per rimuoverli
- Premi `Shift` mentre clicchi su un menu per aprirne più di uno

---

# 🧪 Esercizio pratico – “Dado base in Dynamesh”

> **Obiettivo**: creare un semplice cubo suddiviso con fori/simboli, utile per iniziare a scolpire con controllo

### 🔧 Strumenti suggeriti
- Crea un cubo (`Tool > Initialize > Cube`)
- Attiva Dynamesh (`Tool > Geometry > Dynamesh`)
- Scolpisci fori usando:
  - **Standard Brush** in Zsub
  - **DragRect** + alpha circolare

### 🔄 Workflow
1. Importa un cubo o creane uno nuovo
2. Applica **Dynamesh**
3. Cambia lo stroke in `DragRect`
4. Scegli un alpha tondo (già presente nei default)
5. Imposta la modalità ZSub (scava invece che aggiungere)
6. Posiziona i fori su ogni faccia
7. Usa `Ctrl + clic vuoto` per aggiornare il Dynamesh
8. Salva la ZTool come esercizio completato

---

## ❓ Difficoltà riscontrate da te

Hai segnalato:
- Blocchi nel riprodurre l’esercizio
- Difficoltà nell’individuare la sequenza corretta
- Dubbi sull’uso del cubo corretto e sulle fasi di Dynamesh/Sub

Ti guiderò passo passo nella prossima sessione per sbloccare questi nodi.

---

🧠 Ricorda: all’inizio l’importante non è “fare bene”, ma **attivare mani e attenzione insieme**.  
Consolidare lentamente porta a molta più padronanza a lungo termine.

