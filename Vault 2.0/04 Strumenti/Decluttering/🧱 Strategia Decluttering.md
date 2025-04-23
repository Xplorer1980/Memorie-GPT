# 🧱 Strategia Decluttering – Metodo attuale (ibrido)

Questa nota descrive il metodo attuale e condiviso per il decluttering dei materiali salvati da YouTube (e successivamente Pinterest), basato su collaborazione tra scrematura manuale e affiancamento GPT.

---

## 🧭 Principi guida

- 📌 I PDF non vengono più analizzati da GPT in blocco.
- 📂 L’utente seleziona 5 PDF alla volta, estrae i link ritenuti interessanti.
- 🧠 GPT analizza, cataloga, valuta e propone eventualmente contenuti alternativi.

---

## 🔁 Flusso operativo

### 👤 Azioni utente
1. Seleziona un blocco di 5 PDF dal proprio archivio YouTube.
2. Legge i contenuti e seleziona solo i link ritenuti validi.
3. Salva i link in un file `.txt`, formato:

```
Blocco 01 - PDF: NomeOriginale.pdf
https://youtube.com/...
https://youtube.com/...
```

4. Invia il file a GPT per analisi.

---

### 🤖 Azioni GPT
1. Legge i link forniti, **non apre né analizza i PDF**.
2. Classifica ogni link per categoria.
3. Aggiunge (se utile):
   - un breve commento descrittivo
   - una valutazione ⭐ da 1 a 5 (qualità, rilevanza, chiarezza)
   - una proposta di alternativa (se trovata)
4. Raccoglie tutto in un file `.md` elegante, ordinato, salvato in `04 Strumenti/Decluttering/YouTube/_output_gpt/`

---

## 🧠 Criteri attivi
- Nomi originali dei PDF **sempre rispettati**
- Nessuna categorizzazione forzata
- Simboli usati solo dove aiutano la comprensione
- Verifica duplicati man mano che si accumulano i blocchi
- Le regole in `🧠 Memorie Temporanee.md` e nei file MEGA sono da considerarsi **vincolanti**

---

## 📂 Struttura operativa

- `/input_utente/` – file .txt con link da te selezionati
- `/output_gpt/` – file .md restituiti con categorie e valutazioni
- `/gpt_blocchi/` – log PDF già elaborati

---

✍️ Questa nota può essere aggiornata man mano che il processo evolve.