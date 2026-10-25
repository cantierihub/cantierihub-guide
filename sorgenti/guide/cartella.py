GUIDA = {
    "slug": "cartella",
    "parola": "CARTELLA",
    "titolo": "Le cartelle del cantiere su Google Drive: il prompt per farle preparare a ChatGPT",
    "titolo_html": "Le cartelle del cantiere su Google Drive: <em>il prompt per farle preparare a ChatGPT</em>",
    "sottotitolo": "Un posto solo per foto, varianti, disegni e documenti, invece della chat di WhatsApp. ChatGPT ti disegna la struttura delle cartelle su misura per la tua impresa e ti aiuta a crearla in pochi minuti.",
    "descrizione": "Un cantiere non si può gestire su WhatsApp: foto, varianti e disegni finiscono in mezzo ai messaggi e quando servono non si trovano. In questa guida trovi il prompt da dare a ChatGPT per avere la struttura delle cartelle su misura per i tuoi lavori, la regola per dare il nome ai file, chi deve vedere cosa, e due modi per crearla su Google Drive senza perdere un pomeriggio.",
    "tema": "ufficio",
    "minuti": 6,
    "serve": "ChatGPT e Google Drive, anche gratuiti",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("La struttura su misura", "Le cartelle giuste per i tuoi lavori, numerate e sempre uguali da un cantiere all'altro."),
        ("La regola dei nomi", "Un modo unico di chiamare i file, così ognuno trova quello che cerca anche senza chiederlo a te."),
        ("Chi vede cosa", "Cosa condividere con la squadra, con il tecnico e con il committente, e con quali permessi."),
    ],
    "passi": [
        {
            "titolo": "Rispondi a cinque domande",
            "tempo": "2 minuti",
            "intro": "La struttura giusta dipende dal tuo lavoro. Prima di aprire ChatGPT, pensa a queste cinque cose: le metti nel prompt.",
            "azioni": [
                "Che lavori fai: ristrutturazioni, nuove costruzioni, impianti, lavori pubblici.",
                "Quanti cantieri hai aperti insieme, di solito.",
                "Chi deve mettere dentro i file: tu, l'ufficio, i capisquadra, il tecnico.",
                "Chi deve solo guardare: il committente, il direttore lavori.",
                "Da dove carichi i file: telefono in cantiere o computer in ufficio.",
            ],
        },
        {
            "titolo": "Fatti disegnare la struttura",
            "tempo": "1 minuto",
            "intro": "Copia il prompt, completa le parti tra parentesi quadre e invialo.",
            "prompt": [("Prompt 1 · La struttura delle cartelle", """
Sono il titolare di un'impresa edile. Voglio smettere di tenere foto, varianti, disegni e documenti nelle chat di WhatsApp e organizzare tutto su Google Drive.

La mia impresa:
- Lavori che facciamo: [ristrutturazioni di appartamenti e villette]
- Cantieri aperti insieme, di solito: [4]
- Chi carica i file: [io, l'ufficio, i due capisquadra dal telefono]
- Chi deve solo guardare: [il committente, il direttore lavori]

Preparami:
1. La struttura di una cartella «modello» da copiare per ogni cantiere: cartelle numerate (01, 02, 03...) con un nome corto e chiaro, e dentro le sottocartelle che servono. Per esempio contratto e preventivi, progetto e disegni, varianti, foto, documenti di cantiere, sicurezza, fornitori e subappalti, contabilità, fine lavori. Togli quello che a un'impresa come la mia non serve.
2. La regola per il nome dei file, con 5 esempi (la data all'inizio, nel formato AAAA-MM-GG).
3. Chi deve avere accesso a quali cartelle e con quale permesso (modifica o solo lettura).
4. Le tre regole da mandare alla squadra su WhatsApp, in un messaggio corto.

Scrivi la struttura come un elenco ad albero, facile da copiare.
""")],
        },
        {
            "titolo": "Creala su Google Drive",
            "tempo": "10 minuti la prima volta",
            "intro": "Su Google Drive dal browser le cartelle non si duplicano con un clic. Hai due strade.",
            "azioni": [
                "**A mano, una volta sola**: crei la cartella «Modello cantiere» con la struttura che ti ha dato ChatGPT. Per ogni cantiere nuovo ricrei le cartelle principali in cinque minuti.",
                "**Con un piccolo script**, se vuoi farlo in un clic ogni volta: lo scrive ChatGPT con il prompt qui sotto, tu lo incolli su script.google.com e lo avvii. La prima volta Google ti chiede il permesso di usare il tuo Drive: è normale, lo script è tuo.",
            ],
            "prompt": [("Prompt 2 · Lo script per creare le cartelle", """
Scrivimi uno script per Google Apps Script che crea su Google Drive una cartella con il nome che gli dico io (il nome del cantiere) e dentro tutta questa struttura di cartelle e sottocartelle:
[incolla qui l'albero delle cartelle]

Poi spiegami passo per passo, per chi non ha mai usato Apps Script:
1. dove incollarlo su script.google.com,
2. dove scrivo il nome del cantiere,
3. come lo avvio e cosa fare quando Google chiede le autorizzazioni.
""")],
            "nota": ("info", "Se usi Google Drive anche sul computer (l'app Google Drive per desktop), puoi duplicare la cartella modello come una cartella qualsiasi, dal Finder o da Esplora file."),
        },
        {
            "titolo": "Condividi con le regole giuste",
            "tempo": "3 minuti per cantiere",
            "intro": "Dalla cartella del cantiere, il tasto **Condividi**. Due regole semplici evitano quasi tutti i problemi.",
            "azioni": [
                "La squadra con permesso di **modifica** solo dove deve caricare: foto e documenti di cantiere.",
                "Il committente con permesso di **visualizzazione**, e solo sulle cartelle che deve vedere.",
                "Manda alla squadra il messaggio con le tre regole che ti ha preparato ChatGPT, e fissalo nel gruppo WhatsApp del cantiere.",
            ],
        },
        {
            "titolo": "Il passo dopo: ritrovare le cose chiedendole",
            "tempo": "facoltativo",
            "intro": "Nei Progetti di ChatGPT, se il tuo piano lo prevede, puoi aggiungere come fonte il link di una cartella di Google Drive: ChatGPT può cercarci dentro quando gli chiedi qualcosa, per esempio le foto del massetto di marzo. Funziona bene proprio perché i file hanno nomi e cartelle ordinate.",
        },
    ],
    "errori": [
        ("Cartelle diverse per ogni cantiere", "Se ogni cantiere ha la sua struttura, nessuno trova niente. Il modello è sempre lo stesso."),
        ("File chiamati «IMG_4471»", "Senza la data e due parole nel nome, la cartella diventa un'altra chat di WhatsApp."),
        ("Tutti possono modificare tutto", "Un file cancellato per sbaglio da un telefono è un problema. Modifica solo dove serve."),
        ("Continuare a mandare tutto anche su WhatsApp", "Il gruppo serve per parlare, non per archiviare: le foto vanno nella cartella, nel gruppo basta dire «caricate»."),
    ],
    "fonti": [
        ("OpenAI, guida ai Progetti di ChatGPT (aggiungere link di Google Drive come fonti)", "https://help.openai.com/en/articles/10169521-projects-in-chatgpt"),
    ],
    "cta": ("Lo vuoi fatto su misura, con l'intelligenza artificiale dentro?", "Noi di Cantieri Hub costruiamo sistemi di intelligenza artificiale per imprese edili e studi tecnici: un posto solo per ogni cantiere, e l'intelligenza artificiale che ti ritrova foto e documenti quando glieli chiedi."),
}
