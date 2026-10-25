GUIDA = {
    "slug": "ritardo",
    "parola": "RITARDO",
    "titolo": "Il cronoprogramma che si aggiorna con un messaggio",
    "titolo_html": "Il cronoprogramma che <em>si aggiorna con un messaggio</em>",
    "sottotitolo": "La guida e il prompt da passare a ChatGPT: ti costruisce il cronoprogramma del cantiere e, quando una lavorazione slitta, sposta le date di quelle dopo e ti prepara i messaggi per chi deve entrare.",
    "descrizione": "Un giorno di ritardo in cantiere non è mai solo un giorno: il massetto slitta, il piastrellista può solo la settimana dopo e tutte le date successive si spostano. In questa guida trovi come costruire il cronoprogramma con ChatGPT partendo dal tuo elenco di lavorazioni, come aggiornarlo con una riga quando qualcosa cambia e come farti preparare in un minuto i messaggi per le squadre e per il committente. Con i prompt pronti da copiare.",
    "tema": "cantiere",
    "minuti": 8,
    "serve": "ChatGPT, anche gratuito",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("Il cronoprogramma in tabella", "Lavorazioni, durate, chi le fa e cosa deve finire prima. Lo costruisci in pochi minuti dal tuo elenco."),
        ("Le date che si spostano da sole", "Scrivi «il massetto slitta di un giorno» e tutte le lavorazioni dopo prendono la data nuova."),
        ("I messaggi già scritti", "Per l'idraulico, il piastrellista e il committente: pronti da mandare su WhatsApp il giorno stesso."),
    ],
    "passi": [
        {
            "titolo": "Crea un progetto per il cantiere",
            "tempo": "2 minuti",
            "intro": "In ChatGPT apri il menu a sinistra e crea un nuovo **Progetto**. Chiamalo con il nome del cantiere, per esempio «Via Roma 12». Dentro un progetto ChatGPT tiene insieme le chat, i file e le istruzioni di quel cantiere: quando lo riapri, riparte da lì.",
            "azioni": [
                "Un progetto per ogni cantiere: se li mescoli, le date si confondono.",
                "Se hai già un cronoprogramma in Excel o in PDF, caricalo nel progetto: ChatGPT parte da quello.",
            ],
            "nota": ("info", "Usi un'altra intelligenza artificiale, come Claude o Gemini? Funziona allo stesso modo: cerca i Progetti, o tieni una chat solo per quel cantiere."),
        },
        {
            "titolo": "Prepara l'elenco delle lavorazioni",
            "tempo": "5 minuti",
            "intro": "Il cronoprogramma è giusto solo se sono giusti i dati che gli dai. Ti servono poche cose, e puoi anche dettarle a voce con il microfono di ChatGPT.",
            "azioni": [
                "Le lavorazioni in ordine, con la durata in giorni lavorativi.",
                "Chi fa ogni lavorazione, con il numero di telefono.",
                "Cosa deve essere finito prima: per esempio, i pavimenti dopo il massetto.",
                "La data di inizio e i giorni in cui non si lavora: sabato, domenica, festivi, ferie.",
            ],
        },
        {
            "titolo": "Incolla il prompt e ottieni il cronoprogramma",
            "tempo": "1 minuto",
            "intro": "Copia il prompt, sostituisci le parti tra parentesi quadre con i tuoi dati e invialo nel progetto del cantiere.",
            "prompt": [("Prompt 1 · Il cronoprogramma", """
Sei il mio assistente di cantiere. Costruisci il cronoprogramma dei lavori del cantiere [NOME DEL CANTIERE].

Dati del cantiere:
- Data di inizio lavori: [GG/MM/AAAA]
- Giorni lavorativi: [dal lunedì al venerdì]
- Giorni di chiusura già noti: [festivi, ferie, altro]

Lavorazioni, in ordine (durata in giorni lavorativi, chi la fa, cosa deve essere finito prima):
1. [Demolizioni], [3 giorni], [Ditta Rossi, tel. 333 0000000], prima: nessuna
2. [Impianti sottotraccia], [5 giorni], [Idraulico Bianchi, tel. 333 0000000], prima: 1
3. [Massetto], [2 giorni], [Ditta Verdi, tel. 333 0000000], prima: 2
4. [Pavimenti e rivestimenti], [6 giorni], [Piastrellista Neri, tel. 333 0000000], prima: 3

Regole:
- Una lavorazione inizia solo quando è finita quella indicata in «prima».
- Non mettere due lavorazioni in parallelo se non te lo dico io.
- Se manca un dato non inventarlo: chiedimelo prima di fare la tabella.

Restituiscimi:
1. Una tabella con: numero, lavorazione, chi la fa, inizio, fine, durata, prima.
2. La data di fine lavori.
3. Le lavorazioni critiche: quelle che, se slittano, spostano la fine del cantiere.

Ricorda questo cronoprogramma: nei prossimi messaggi ti dirò cosa cambia.
""")],
            "nota": ("success", "Rileggi la tabella una volta, con calma: se una durata è sbagliata, correggila con un messaggio («le demolizioni durano 4 giorni, non 3») e ChatGPT rifà i conti."),
        },
        {
            "titolo": "Quando qualcosa slitta, scrivilo in una riga",
            "tempo": "30 secondi",
            "intro": "Il massetto finisce un giorno dopo, il piastrellista ti dice che può entrare solo la settimana dopo. Lo scrivi nel progetto, e ChatGPT ricalcola tutto quello che viene dopo.",
            "prompt": [("Prompt 2 · Lo slittamento", """
Aggiornamento del [GG/MM]: [il massetto finisce giovedì invece di mercoledì].
[Il piastrellista può entrare solo da lunedì 10: tieni fermo il suo inizio.]

Ricalcola il cronoprogramma da qui in avanti, con le stesse regole di prima.
Poi dimmi:
1. Quali lavorazioni cambiano data, con la data vecchia e quella nuova.
2. Se cambia la fine lavori e di quanti giorni.
3. Chi devo avvisare, con il suo numero.
Non toccare le lavorazioni già finite.
""")],
        },
        {
            "titolo": "Fatti preparare i messaggi per chi entra dopo",
            "tempo": "1 minuto",
            "intro": "Il problema non è solo la data che cambia: è dirlo a tutti in tempo. Con questo prompt hai i messaggi pronti da copiare su WhatsApp, uno per persona.",
            "prompt": [("Prompt 3 · I messaggi", """
Prepara i messaggi WhatsApp per tutte le persone che hanno cambiato data.
- Uno per persona, brevi e cortesi, dando del [lei / tu].
- In ogni messaggio: il cantiere, la data vecchia, la data nuova, e la richiesta di confermare con un «ok».
- Firma: [Nome Cognome, Nome Impresa].
Poi prepara un messaggio per il committente: in tre righe spiega che c'è stato uno slittamento, la nuova data di fine lavori e che restiamo a disposizione per una telefonata. Senza dare colpe a nessuno.
""")],
            "nota": ("warning", "ChatGPT i messaggi li prepara, ma non li manda da solo sul telefono dell'idraulico: li copi tu su WhatsApp, e ci vuole un minuto. Per farli partire in automatico serve un sistema collegato a WhatsApp Business."),
        },
        {
            "titolo": "Tienilo vivo ogni settimana",
            "tempo": "1 minuto a settimana",
            "intro": "Il venerdì chiedi il punto della settimana dopo. Così chi deve entrare lo sai prima, non quando ti chiama.",
            "prompt": [("Prompt 4 · Il punto del venerdì", """
Fammi il punto della prossima settimana sul cantiere [NOME]: chi entra, in che giorno, cosa deve essere pronto prima che entri, e cosa rischia di slittare.
Se serve, preparami il cronoprogramma aggiornato in un file Excel da scaricare.
""")],
        },
    ],
    "errori": [
        ("Le durate a occhio", "L'intelligenza artificiale fa i conti, non conosce il tuo cantiere. Se le durate sono sbagliate, il cronoprogramma è sbagliato anche se è ordinato."),
        ("Non dire cosa viene prima", "Senza la colonna «prima», ChatGPT può mettere in parallelo lavorazioni che non possono andare insieme."),
        ("Tutti i cantieri nella stessa chat", "Le date si mescolano. Un progetto per cantiere, sempre."),
        ("Mandare i messaggi senza rileggerli", "Controlla date e nomi prima di inviare. Trenta secondi che ti evitano una squadra in cantiere nel giorno sbagliato."),
    ],
    "fonti": [
        ("OpenAI, guida ai Progetti di ChatGPT (file, istruzioni e condivisione)", "https://help.openai.com/en/articles/10169521-projects-in-chatgpt"),
    ],
    "cta": ("Lo vuoi che avvisi da solo le squadre?", "Noi di Cantieri Hub costruiamo sistemi di intelligenza artificiale per imprese edili e studi tecnici: il cronoprogramma che si aggiorna e manda il messaggio a chi deve entrare, il giorno stesso, collegato ai tuoi cantieri."),
}
