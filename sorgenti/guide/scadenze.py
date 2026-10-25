GUIDA = {
    "slug": "scadenze",
    "parola": "SCADENZE",
    "titolo": "Tutte le scadenze dell'impresa in una tabella, con ChatGPT",
    "titolo_html": "Tutte le scadenze dell'impresa <em>in una tabella, con ChatGPT</em>",
    "sottotitolo": "DURC, revisioni, polizze, patenti, attestati: metti i documenti in una cartella, li dai a ChatGPT e ti restituisce la tabella delle scadenze, il calendario e l'avviso un mese prima.",
    "descrizione": "Le scadenze di un'impresa edile sono decine all'anno e nessuno te le ricorda: basta un documento scaduto per tenere fermo un cantiere. In questa guida trovi come raccogliere i documenti, come farli leggere a ChatGPT per avere la tabella di tutte le scadenze in ordine di data, e come metterle nel calendario del telefono con l'avviso un mese prima. Con i prompt pronti da copiare.",
    "tema": "ufficio",
    "minuti": 8,
    "serve": "ChatGPT, anche gratuito, e il calendario del telefono",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("La tabella delle scadenze", "Documento, a chi o a cosa si riferisce, data di scadenza, giorni che mancano. In ordine, dalla più vicina."),
        ("Il calendario con gli avvisi", "Ogni scadenza nel calendario del telefono, con l'avviso un mese prima e una settimana prima."),
        ("Niente cantiere fermo per un foglio", "Le scadenze le vedi arrivare, non quando te le chiedono in cantiere o in gara."),
    ],
    "passi": [
        {
            "titolo": "Raccogli i documenti in una cartella",
            "tempo": "15 minuti, una volta sola",
            "intro": "Metti in una cartella del computer o del telefono i documenti che hanno una data di scadenza. Vanno bene PDF e foto leggibili. Qualche esempio:",
            "azioni": [
                "Il DURC e i documenti dell'impresa che ti chiedono in cantiere o in gara.",
                "Le polizze: responsabilità civile, mezzi, cantiere.",
                "Revisioni, assicurazioni e bolli dei mezzi; patenti e abilitazioni di chi guida.",
                "Gli attestati dei corsi sulla sicurezza dei dipendenti e i giudizi di idoneità del medico.",
                "Contratti di noleggio e manutenzioni periodiche delle attrezzature.",
            ],
            "nota": ("warning", "Per le visite mediche basta il giudizio di idoneità con la data, non la cartella sanitaria. E nelle impostazioni dei dati di ChatGPT puoi scegliere che le tue conversazioni non vengano usate per migliorare i modelli."),
        },
        {
            "titolo": "Crea il progetto «Scadenze impresa» e carica i file",
            "tempo": "3 minuti",
            "intro": "In ChatGPT crea un nuovo **Progetto** chiamato «Scadenze impresa» e carica i documenti. Quanti file puoi caricare dipende dal tuo piano: se sono tanti, caricali a gruppi e chiedi la tabella alla fine.",
        },
        {
            "titolo": "Fatti fare la tabella delle scadenze",
            "tempo": "2 minuti",
            "intro": "Incolla questo prompt nel progetto. ChatGPT apre ogni file, cerca le date di scadenza e ti dà la tabella.",
            "prompt": [("Prompt 1 · La tabella", """
Nei file di questo progetto ci sono i documenti della mia impresa. Oggi è il [GG/MM/AAAA].
Apri ogni file e trova le date di scadenza.

Fammi una tabella con: documento, a chi o a cosa si riferisce (impresa, nome della persona, targa del mezzo), data di scadenza, giorni che mancano da oggi, nome del file.

Regole:
- Ordina dalla scadenza più vicina.
- Scrivi le date nel formato GG/MM/AAAA.
- Non inventare date: se in un documento la scadenza non è scritta, mettilo in fondo con «data non trovata».
- Se una data non si legge bene, mettila con un punto interrogativo.
- Evidenzia le scadenze dei prossimi 60 giorni.
""")],
            "nota": ("success", "Controlla le scadenze più vicine sul documento vero, una per una. È la prima volta che lo fai: vale la pena guardare."),
        },
        {
            "titolo": "Metti tutto nel calendario, con l'avviso un mese prima",
            "tempo": "3 minuti",
            "intro": "Chiedi a ChatGPT un file calendario (si chiama .ics) con tutte le scadenze. Lo apri sul telefono o lo importi in Google Calendar, e gli avvisi arrivano da soli.",
            "prompt": [("Prompt 2 · Il calendario", """
Con la tabella delle scadenze prepara un file calendario .ics da scaricare.
- Un evento per ogni scadenza, il giorno della scadenza, per tutta la giornata.
- Titolo dell'evento: «Scade: [documento], [a chi si riferisce]».
- Nella descrizione: il nome del file e cosa serve per il rinnovo, se è scritto nel documento.
- Due avvisi per ogni evento: 30 giorni prima e 7 giorni prima.
Escludi le righe con «data non trovata».
""")],
            "azioni": [
                "Su iPhone: apri il file .ics e scegli di aggiungere tutti gli eventi al calendario.",
                "Su Google Calendar dal computer: Impostazioni, poi **Importa ed esporta**, scegli il file e il calendario.",
                "Su Android: importa il file in Google Calendar dal computer, poi lo vedi anche sul telefono.",
            ],
        },
        {
            "titolo": "Il promemoria del mese, direttamente da ChatGPT",
            "tempo": "1 minuto, facoltativo",
            "intro": "ChatGPT può anche mandarti un promemoria ricorrente con le **attività pianificate**. Due cose da sapere: un'attività creata dentro un progetto non legge i file del progetto, quindi va creata fuori, con le scadenze scritte nel testo; e con l'account gratuito le attività attive sono al massimo tre, con orari indicativi. Per questo il calendario del passo 4 resta la base.",
            "prompt": [("Prompt 3 · Il promemoria mensile", """
Ogni primo lunedì del mese alle 8 ricordami le scadenze dei 60 giorni successivi, prendendole da questa lista:
[incolla qui la tabella delle scadenze]
""")],
        },
        {
            "titolo": "Ogni volta che rinnovi un documento",
            "tempo": "1 minuto",
            "intro": "Carichi il documento nuovo nel progetto e lo dici in una riga. La tabella si aggiorna e ti fai dare l'evento nuovo per il calendario.",
            "prompt": [("Prompt 4 · Il rinnovo", """
Ho rinnovato [il DURC / la polizza / la revisione del mezzo targa ...]: il documento nuovo è il file [nome del file].
Aggiorna la tabella delle scadenze e preparami il file .ics solo per questa scadenza nuova, con gli stessi avvisi.
""")],
        },
    ],
    "errori": [
        ("Scansioni illeggibili", "Se il documento non si legge, anche l'intelligenza artificiale sbaglia la data. Rifai la foto o scarica il PDF originale."),
        ("Fidarsi senza guardare la prima volta", "La prima tabella si controlla sui documenti veri, almeno per le scadenze dei prossimi mesi."),
        ("Caricare dati sanitari", "Per le visite mediche basta il giudizio di idoneità con la data. Il resto non serve e non va caricato."),
        ("Dimenticare i rinnovi", "Se rinnovi e non aggiorni, il calendario continua a suonare per la data vecchia. Un minuto, ogni volta."),
    ],
    "fonti": [
        ("OpenAI, guida ai Progetti di ChatGPT", "https://help.openai.com/en/articles/10169521-projects-in-chatgpt"),
        ("OpenAI, guida alle attività pianificate di ChatGPT (limiti per piano, attività nei progetti)", "https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt"),
    ],
    "cta": ("Lo vuoi che controlli da solo le scadenze dell'impresa?", "Noi di Cantieri Hub costruiamo sistemi di intelligenza artificiale per imprese edili: i documenti letti appena arrivano, le scadenze sempre aggiornate e l'avviso a chi deve rinnovare, prima che il cantiere si fermi."),
}
