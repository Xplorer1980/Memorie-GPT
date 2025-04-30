# 📘 Guida Personalizzazione Callout – Obsidian

> In questa guida trovi istruzioni base per modificare l’aspetto visivo dei callout (`> [!tip]`, `> [!note]`, ecc.)  
> Utile se vuoi cambiare colore, icona o stile dei box evidenziati in Obsidian.

---

## 🧩 1. Cos’è un callout?

Un **callout** è un blocco evidenziato che inizia con:

```
> [!tipo]
> Contenuto del callout
```

Obsidian lo trasforma in un **box colorato con un’icona**, visibile in modalità Anteprima o Live Preview.

---

## 🎨 2. Come personalizzarli visivamente?

Hai due opzioni:

### 🔹 A. Usare un **tema compatibile** (es. Minimal, Blue Topaz)

Se usi un tema avanzato, i callout sono già visivi. Puoi personalizzare i colori direttamente nelle **impostazioni del tema**.

### 🔹 B. Usare uno **snippet CSS personalizzato**

Vai in:  
📁 `.obsidian/snippets/` → crea un file `.css` e incolla un esempio come questo:

```css
.callout[data-callout="tip"] {
  --callout-color: 210, 100%, 80%;
  --callout-icon: lightbulb;
}
.callout[data-callout="warning"] {
  --callout-color: 5, 100%, 85%;
  --callout-icon: alert-triangle;
}
```

> Dopo aver salvato, attiva lo snippet in Obsidian:  
> ⚙️ Impostazioni > Aspetto > Snippets CSS

---

## 🖌️ 3. Cosa puoi modificare

| Cosa             | Come si cambia                      |
|------------------|-------------------------------------|
| Colore sfondo    | `--callout-color:` in HSL           |
| Icona            | `--callout-icon:` (vedi lista icone)|
| Bordo, testo...  | via regole CSS standard             |

---

## 🔍 4. Dove trovare ispirazione

- [Icone Lucide (usate da Obsidian)](https://lucide.dev/icons/)
- [CSS callout su GitHub](https://github.com) – cerca "obsidian callout css"
- Forum Obsidian: tanti esempi pratici e snippet condivisi

---

## ✅ Suggerimento

Puoi anche creare **nuovi tipi di callout personalizzati**, ad esempio:

```markdown
> [!spazio] Momento di respiro
> Mi fermo un attimo. Mi ascolto. Riparto.
```

…e poi dare a `spazio` un tuo stile nel CSS!

---

## 🛠 Prossimi passi

- Esplora un tema come **Minimal** o **ITS Theme**
- Inizia creando **uno snippet semplice**
- Personalizza i tuoi callout come se fossero **tuoi strumenti emotivi**

