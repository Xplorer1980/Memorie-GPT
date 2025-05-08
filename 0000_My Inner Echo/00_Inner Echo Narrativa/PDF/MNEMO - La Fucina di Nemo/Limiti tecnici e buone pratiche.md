### 🪤 Limiti tecnici e buone pratiche (raccolta 2025-05-08)

---

#### 📌 1. Il canvas è una funzione automatica, non disattivabile via prompt
Anche se nel Prompt CORE è vietato, la piattaforma attiva comunque il canvas in certe operazioni (es: aggiornamento file), ignorando le istruzioni personalizzate.  
**Soluzione:** evitare frasi come “scrivimi in block note” per non attivare il canvas per errore. Usare “scrivimi qui sotto in code block, senza canvas”.

---

#### 📌 2. Il canvas tronca testi lunghi e li sostituisce con placeholder
Quando il contenuto supera una certa lunghezza, il canvas sostituisce parti di testo con stringhe tipo `[... truncated ...]`.  
**Rischio:** perdi pezzi di contenuto sia a livello visivo, sia nel backup.  
**Soluzione:** usare file `.md` o code block per contenuti lunghi.

---

#### 📌 3. I code block sono leggibili, compatti e persistenti
- Restano **dentro la chat**, non aprono finestre nuove
- Non spostano la visuale quando si chiudono
- Si copiano con un clic
- Permettono uso di `###`, colori e indentazioni
- Sono pienamente compatibili con Obsidian e Markdown
- **Non vengono mai troncati**

---

#### 📌 4. I code block sono salvati integralmente nei file `.json`
A differenza dei canvas, i code block appaiono come **testo puro e continuo** nell’export.  
**Questo li rende leggibili e ricercabili anche fuori da ChatGPT.**

---

#### 📌 5. Uso di icone ai margini dei code block
Aggiungere una **icona di apertura e una di chiusura** (es: `🧱`) ai blocchi importanti permette di identificarli facilmente nei backup `.json`.  
**Soluzione intelligente** per chi archivia o elabora sessioni fuori da ChatGPT.

---

#### 📌 6. Prompt CORE ≠ garanzia contro automatismi di sistema
Il Prompt CORE è vincolante nel tono e nelle regole interne alla risposta, ma **non ha controllo sugli automatismi dell’interfaccia**.  
**Serve come bussola narrativa, non come freno tecnico.**

---
