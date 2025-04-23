# Tutorial – Come iniziare con GitHub  
_Guida guidata per principianti_  

> [!note] **Scopo del tutorial**  
> Questa guida ti aiuta a:  
> • Usare GitHub per salvare la tua memoria esterna GPT  
> • Gestire file `.md`, `.txt`, `.zip` da condividere con ChatGPT  
> • Automatizzare gli aggiornamenti con script `.bat`

---

## 1. Registrarsi su GitHub

1. Vai su [https://github.com](https://github.com)
2. Clicca su **Sign up**
3. Inserisci email, password, nome utente e conferma email

> [!tip] GitHub è gratuito e non ha pubblicità.  
> Serve solo una mail per iniziare.

---

## 2. Creare il primo repository

1. Una volta loggato, clicca sul simbolo `+` in alto a destra
2. Seleziona **New repository**
3. Inserisci un nome (es. `Memorie-GPT`)
4. Lascia le opzioni su `Public` e deseleziona "Add a README"
5. Clicca su **Create repository**

> [!warning] Il repo dev’essere pubblico  
> ChatGPT può leggere solo file `.md` da repository **pubblici**.

---

## 3. Collegare una cartella del PC al repository GitHub

1. Crea una cartella locale (es. `G:\0_GitHub`)
2. Clic destro dentro → scegli **Git Bash Here**
3. Incolla questo comando (sostituendo TUONOME):
   ```
   git clone https://github.com/TUONOME/Memorie-GPT.git
   ```

> [!info] Così colleghi la cartella del tuo PC al repository online.  
> Ogni modifica alla cartella locale potrà essere inviata online.

---

## 4. Aggiungere o aggiornare file nel repository

1. Sposta nella cartella i file `.md`, `.txt`, `.zip`, ecc.
2. Apri Git Bash dentro la cartella e incolla:
   ```
   git add .
   git commit -m "Aggiornamento file"
   git push
   ```

> [!tip] Puoi automatizzare tutto questo con file `.bat`  
> (Li troverai nel tuo Vault, sotto “Strumenti”)

---

## 5. Trovare il link RAW da dare a ChatGPT

1. Vai su [github.com](https://github.com) > entra nel tuo repo
2. Clicca sul nome del file `.md` che vuoi usare
3. In alto a destra clicca su **Raw**
4. Copia il link nella barra degli indirizzi

> [!example] Esempio di link RAW:  
> `https://raw.githubusercontent.com/TUONOME/Memorie-GPT/main/Memoria.md`

---

## Consigli finali

> [!note] Usa i file `.md` per:  
> - Memorie GPT  
> - Tutorial  
> - Riassunti o promemoria dei tuoi progetti

> [!tip] Ricorda che puoi:
> - Copiare qualsiasi file GPT con `CTRL+A` e `CTRL+C`  
> - Allegare `.zip` del vault come backup secondario

---

## Ora sei pronto!

> [!success]  
> Hai tutto il necessario per:  
> ✅ Salvare la tua memoria esterna GPT  
> ✅ Usare GitHub per collaborare con ChatGPT  
> ✅ Tenere tutto aggiornato senza fatica
