
# HappyCoding-Riordinator

![Banner](https://r2.fivemanage.com/pub/ss56sn69nw0n.png)

**HappyCoding-Organizer** è uno strumento progettato per organizzare automaticamente i file scaricati nella cartella **Download**, smistandoli in sottocartelle in base alla loro estensione. È possibile creare anche sottocartelle per ogni estensione specifica, mantenendo la cartella **Download** sempre ordinata.

> ⚠️ **Nota**: Il programma è attualmente in versione **beta** ed è tutt'ora in sviluppo. Alcune funzionalità potrebbero cambiare nelle versioni future.

## Caratteristiche principali

- **Smistamento automatico**: Il programma rileva automaticamente nuovi file scaricati e li sposta nelle cartelle appropriate (Immagini, Video, Documenti, Comprimibili, ecc.).
- **Sottocartelle per estensione**: Puoi scegliere di creare automaticamente sottocartelle basate sull'estensione del file all'interno delle cartelle principali (ad esempio, `png`, `jpg` nella cartella Immagini).
- **Notifiche raggruppate**: Per evitare spam di notifiche, il programma invia una notifica raggruppata quando vengono spostati più file contemporaneamente.
- **Interfaccia grafica semplice**: La GUI è stata progettata per essere facile da usare e intuitiva.

## Requisiti

- **Python 3.7 o superiore**
- **Plyer** per le notifiche desktop:
  ```bash
  pip install plyer
  ```
- **Tkinter** (di solito già incluso con Python)

## Installazione

1. **Clona la repository**:
   ```bash
   git clone https://github.com/emkeyhell/HappyCoding-Riordinator.git
   ```

2. **Installa le dipendenze**:
   Assicurati di avere installato `plyer` per le notifiche desktop:
   ```bash
   pip install plyer
   ```

3. **Esegui il programma**:
   Esegui il file Python `organizer.py` per avviare il programma:
   ```bash
   python organizer.py
   ```

## Utilizzo

### Passaggi principali:

1. **Seleziona una cartella**: All'avvio, seleziona la cartella **Download** o un'altra cartella che desideri monitorare.
2. **Avvia il monitoraggio**: Premi il pulsante `Avvia Monitoraggio` per iniziare a ordinare automaticamente i file scaricati.
3. **Crea sottocartelle per estensione** *(opzionale)*: Spunta l'opzione `Crea sottocartelle per estensione` se desideri che vengano create sottocartelle specifiche per ogni estensione di file.
4. **Monitora e ferma il processo**: Usa il pulsante `Ferma Monitoraggio` per interrompere il monitoraggio in qualsiasi momento.

### Esempio di utilizzo:

Se scarichi un file **.png** e un file **.mp4**, HappyCoding-Organizer li sposterà automaticamente nelle cartelle `images` e `videos`. Se l'opzione delle sottocartelle è attiva, il file **.png** verrà spostato in `images/png` e il file **.mp4** in `videos/mp4`.

### Notifiche raggruppate:

Se più file vengono spostati nello stesso intervallo di tempo, riceverai una singola notifica che ti informa del numero di file spostati e delle cartelle di destinazione.

## Contributi

Siccome il progetto è attualmente in **beta**, ogni feedback è ben accetto. Se trovi bug, vuoi suggerire nuove funzionalità o contribuire al codice, sentiti libero di aprire una issue o fare una pull request.

## Funzionalità future (Roadmap)

- **Miglioramento delle performance**: Ottimizzazione dell'elaborazione dei file in tempo reale.
- **Integrazione cloud**: Possibilità di sincronizzare i file direttamente con servizi cloud (Google Drive, Dropbox, ecc.).
- **Supporto per più cartelle di monitoraggio**: Monitoraggio simultaneo di più cartelle.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Consulta il file [LICENSE](LICENSE) per maggiori dettagli.

## Contatti

- **GitHub**: [emkeyhell](https://github.com/emkeyhell)
- **Email**: [emkeyhell@gmail.com](mailto:emkeyhell@gmail.com)
- **Discord**: [Unisciti al server](https://discord.gg/jjsQU2bFBP)
- **Twitch**: [emkeyhell](https://www.twitch.tv/emkeyhell)
- **Instagram**: [emkeyhell](https://www.instagram.com/emkeyhell)
- **Sito Web**: [emkeyhell.bss.design](https://emkeyhell.bss.design)
- **Itch.io**: [emkeyhell](https://emkeyhell.itch.io/)

