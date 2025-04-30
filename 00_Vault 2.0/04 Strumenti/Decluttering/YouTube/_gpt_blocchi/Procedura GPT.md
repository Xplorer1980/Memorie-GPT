# 📘 Procedura GPT – Analisi link scremati da PDF

Questa nota descrive il flusso operativo che GPT segue quando riceve un file `.txt` con i link selezionati manualmente dall'utente.

---

## 📥 INPUT ATTESO

- Formato: file `.txt` o `.md`
- Contenuto:
  - Nome del PDF esattamente come appare nella tua cartella (es. `ZBrush_Creativity_AI.pdf`)
  - Lista dei link (uno per riga)

---

## 🔁 COSA FA GPT

Per ogni blocco ricevuto:

1. **Riconosce il PDF di origine** (senza rinominarlo)
2. **Analizza sommariamente ciascun link**
   - Non guarda il video per intero, ma ne deduce tema e qualità da titolo e anteprima
3. **Classifica il link per categoria**
   - Es. `Creatività`, `Motivazione`, `AI`, `Studio`, `Metodo`, `ZBrush`...
4. **Aggiunge (se utile)**:
   - Breve commento
   - Valutazione da ⭐ a ⭐⭐⭐⭐⭐
   - Suggerimento di un video alternativo (se migliore o più aggiornato)

---

## 📤 OUTPUT RESTITUITO

GPT crea un file `.md` strutturato così:

```markdown
## PDF: NomeOriginale.pdf

### 🎯 Creatività

- ⭐⭐⭐⭐ [Titolo del video](link)
  > Commento GPT

### 🧠 Mindset / Motivazione

- ⭐⭐⭐ [Titolo del video](link)
  > Commento GPT
```

---

## 🧠 ALTRE FUNZIONI ATTIVE

- Riconoscimento link già presenti in blocchi precedenti
- Segnalazione di duplicati
- Inserimento in `/output_gpt/`
- Rispetto della memoria temporanea e delle istruzioni presenti nei file MEGA

---

✍️ Questa guida può essere modificata o evoluta nel tempo se il metodo cambia.