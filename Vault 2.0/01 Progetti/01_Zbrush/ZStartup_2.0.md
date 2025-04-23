# ⚙️ ZStartup 2.0 – Plugin Modulare Personalizzato

Questa nota documenta il funzionamento e lo stato attuale del plugin **ZStartup 2.0**, sviluppato per creare un ambiente di avvio rapido, coerente e personalizzato in ZBrush 2025.2.

---

## ✅ Funzioni attive nel plugin

- **Load Startup Project**
  - Carica un progetto `.zpr` predefinito all’avvio
  - Percorso: `ZStartup_2.0\Load Startup Project.zpr`

- **Set Brush + Material**
  - Imposta automaticamente il pennello `Move` e il materiale `MatCap Gray`

- **Quick Save Tool**
  - Salva rapidamente il tool attivo in formato `.ztl`
  - Percorso: `ZStartup_2.0\Backup_Tool.ztl`

---

## 🗂️ Struttura dei file in `ZPlugs64`

```
ZPlugs64/
├── ZStartup_2.0.txt         ← file sorgente del plugin (modificabile)
├── ZStartup_2.0.zsc         ← file compilato (plugin attivo)
└── ZStartup_2.0/
    ├── Load Startup Project.zpr
    └── Backup_Tool.ztl
```

*I percorsi usati nel codice sono assoluti, ma possono essere resi relativi se spostati nella stessa cartella.*

---

## ⏳ Funzioni previste (fase 2)

- [ ] Toggle Spotlight
- [ ] Toggle Draw Mode (`Z`)
- [ ] Profili creativi preimpostati (es. Sketch / Modeling / Render)
- [ ] Sezione 2.5D Paint
- [ ] Collegamento a PureRef
- [ ] Backup incrementali automatici

---

## 🛠️ Come modificare il plugin

### Esempio: aggiungere un nuovo pulsante
```zscript
[IButton,"ZPlugin:ZStartup 2.0:Nome Pulsante","Descrizione Tooltip",
    [Comando ZScript qui]
]
```

### Ricompilare:
1. Apri `ZBrush`
2. Vai su `ZScript > Load`
3. Seleziona il file `.txt` per generare il `.zsc`

---

## 🧠 Note operative

- I file `.zpr` e `.ztl` inclusi sono personalizzabili liberamente
- Tutte le macro create restano attive e possono essere incluse nel plugin
- Il layout personalizzato (`.cfg`) e i brush sono salvati a parte e non gestiti direttamente dal plugin (ma integrabili)

---

📌 Ultimo aggiornamento: creazione e attivazione del pannello in `ZPlugin > ZStartup 2.0`, con 3 funzioni già operative.

