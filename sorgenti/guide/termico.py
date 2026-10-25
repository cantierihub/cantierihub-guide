GUIDA = {
    "slug": "termico",
    "parola": "TERMICO",
    "titolo": "Conto Termico 3.0: come funziona e il prompt per il preventivo al cliente",
    "titolo_html": "Conto Termico 3.0: <em>come funziona e il prompt per il preventivo al cliente</em>",
    "sottotitolo": "Pompe di calore e solare termico: il contributo del GSE fino al 65% delle spese ammissibili, il mandato all'incasso che permette all'impresa di incassarlo, e il prompt per scrivere al cliente quanto paga lui.",
    "descrizione": "Il Conto Termico 3.0 è aperto: per pompe di calore e solare termico il GSE riconosce un contributo fino al 65% delle spese ammissibili, e con il mandato irrevocabile all'incasso il contributo lo può incassare direttamente l'impresa, mentre il cliente paga la parte restante. In questa guida trovi le regole che contano per un'impresa, prese dalle pagine ufficiali del GSE, le scadenze da non sbagliare e il prompt da passare a ChatGPT per preparare in pochi minuti il preventivo con la quota del cliente.",
    "tema": "bonus",
    "minuti": 9,
    "serve": "ChatGPT, anche gratuito, e la scheda tecnica dell'impianto",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("Le regole in una pagina", "Cosa copre il Conto Termico 3.0, chi fa la domanda, entro quando e come arriva il contributo."),
        ("Il preventivo con la quota del cliente", "Totale, contributo stimato e quanto paga il cliente, scritti in modo che li capisca."),
        ("Il messaggio per spiegarlo", "Due righe su WhatsApp per far capire al cliente il vantaggio, senza promettere cifre che non sono sicure."),
    ],
    "contesto": {
        "etichetta": "Come funziona",
        "titolo": "Il Conto Termico 3.0 in breve",
        "blocchi": [
            ("box", "Non è una detrazione: è un contributo", "Il Conto Termico 3.0 non si scarica dalle tasse: è un contributo in denaro che il GSE paga con bonifico, fino a un massimo del 65% delle spese ammissibili. Ogni anno ci sono 900 milioni di euro: 500 per i privati, di cui 150 per le imprese, e 400 per la pubblica amministrazione."),
            ("box", "Pompe di calore e solare termico: il 65% non è della fattura", "Per questi interventi il 65% si applica ai massimali calcolati in base alle caratteristiche tecniche dell'impianto: la producibilità e la prestazione stagionale per le pompe di calore, la superficie dei pannelli per il solare termico. Quindi il contributo dipende dall'impianto, non dal prezzo che fai. Il GSE pubblica anche il catalogo degli apparecchi prequalificati: controlla se l'apparecchio che installi c'è."),
            ("box", "Chi fa la domanda e entro quando", "La domanda la presenta il Soggetto Responsabile, cioè chi sostiene la spesa: di solito il cliente. Per un privato è un accesso diretto, a lavori finiti, entro 90 giorni dalla conclusione dell'intervento: dopo, la domanda non è ammissibile. Il cliente può delegare un altro soggetto per compilare la domanda sul Portaltermico. Le imprese che chiedono il contributo per sé devono invece mandare una richiesta preliminare prima di iniziare i lavori."),
            ("box", "Come e quando arriva il contributo", "Fino a 15.000 euro il GSE paga in un'unica rata; sopra, in rate annuali. Il pagamento arriva entro l'ultimo giorno del mese che segue il bimestre in cui la scheda-contratto viene perfezionata."),
            ("box", "Il mandato irrevocabile all'incasso", "Il cliente può dare all'installatore o al fornitore il mandato a incassare il contributo netto. Le condizioni principali: domanda in accesso diretto; il mandato riguarda tutto il contributo; un solo mandatario; si usa il modello standard del Portaltermico, con il conto corrente dell'impresa. La fattura deve essere pari alle spese ammissibili indicate sul portale, il cliente paga con bonifico la parte restante, e bonifici più contributo netto devono fare esattamente l'importo della fattura."),
            "**Cosa vuol dire per te.** Con il mandato puoi proporre al cliente di pagare solo la sua parte, mentre il contributo lo incassi tu dal GSE. Ricordati che quella parte arriva dopo: mettila nei conti dell'impresa. E prima di proporlo, controlla sul sito del GSE che il portale sia aperto: il 13 aprile 2026 è stato riaperto dopo una sospensione.",
        ],
    },
    "passi": [
        {
            "titolo": "Controlla che l'intervento rientri",
            "tempo": "5 minuti",
            "intro": "Prima di parlare di cifre, guarda la pagina «Tipologie di interventi» del Conto Termico 3.0 sul sito del GSE e verifica il caso del tuo cliente: tipo di edificio, impianto che sostituisci, impianto che installi.",
        },
        {
            "titolo": "Fatti dare il contributo stimato",
            "tempo": "dipende dall'impianto",
            "intro": "Il contributo si calcola con le regole del GSE e i dati tecnici dell'impianto: potenza, prestazione stagionale, superficie dei pannelli, zona climatica. Fattelo calcolare dal tecnico o dal fornitore dell'apparecchio, oppure usa il catalogo del GSE se l'apparecchio è prequalificato.",
            "nota": ("warning", "Non chiedere all'intelligenza artificiale di inventarsi il contributo: le formule hanno troppe variabili. Il numero lo porti tu, lei ti aiuta a scrivere il preventivo e a spiegarlo."),
        },
        {
            "titolo": "Prepara il preventivo con la quota del cliente",
            "tempo": "2 minuti",
            "intro": "Con il totale dei lavori e il contributo stimato, ChatGPT ti scrive il preventivo che il cliente capisce al primo colpo.",
            "prompt": [("Prompt 1 · Il preventivo", """
Prepara il testo di un preventivo per il cliente [Nome Cognome] per [l'installazione di una pompa di calore aria-acqua da ... kW che sostituisce la caldaia a gas], nella casa in [indirizzo, tipo di casa].

Dati:
- Totale dei lavori, IVA inclusa: [€ ...]
- Contributo Conto Termico 3.0 stimato: [€ ...], calcolato da [tecnico / fornitore], da confermare dal GSE
- Mandato irrevocabile all'incasso: sì. L'impresa incassa il contributo dal GSE, il cliente paga con bonifico la parte restante.

Scrivi:
1. Cosa installiamo, in parole semplici, in tre righe.
2. Una tabella: totale dei lavori, contributo stimato, quota del cliente.
3. Come e quando paga il cliente la sua quota.
4. Cosa succede se il GSE riconosce un contributo diverso: [scrivi qui cosa hai deciso tu].
5. I documenti che ci servono dal cliente.
6. La frase: «Il contributo è stimato: l'importo esatto lo conferma il GSE dopo la domanda».
Tono semplice, nessuna parola tecnica senza spiegarla. Non cambiare i numeri che ti ho dato.
""")],
        },
        {
            "titolo": "Spiegalo al cliente in due righe",
            "tempo": "1 minuto",
            "intro": "Prima del PDF, spesso serve un messaggio che faccia capire il vantaggio.",
            "prompt": [("Prompt 2 · Il messaggio WhatsApp", """
Scrivi un messaggio WhatsApp per il cliente [nome], dando del [lei]: in massimo cinque righe spiega che per la sua [pompa di calore] può usare il Conto Termico 3.0, che il contributo stimato è di [€ ...] e che, con il mandato all'incasso, lui paga solo [€ ...] e il resto lo incassiamo noi dal GSE.
Aggiungi che l'importo esatto lo conferma il GSE e proponi di sentirci per i dettagli.
""")],
        },
        {
            "titolo": "Segna le date che non si possono sbagliare",
            "tempo": "1 minuto",
            "intro": "Le pratiche si perdono sulle date, non sui conti.",
            "azioni": [
                "Per il cliente privato: la domanda entro **90 giorni dalla fine dei lavori**. Mettilo in calendario il giorno stesso della fine lavori.",
                "Se la domanda la fa un'impresa per sé: la richiesta preliminare va mandata **prima di iniziare** i lavori.",
                "Conserva i documenti dell'intervento: il GSE li può chiedere per tutta la durata dell'incentivo e per i cinque anni dopo l'ultimo pagamento.",
            ],
        },
    ],
    "errori": [
        ("Chiamarlo detrazione", "Il cliente capisce un'altra cosa. È un contributo che arriva con un bonifico del GSE."),
        ("Promettere il 65% della fattura", "Per pompe di calore e solare termico il contributo dipende dall'impianto. Prometti solo cifre calcolate, e scrivi che sono stime."),
        ("Superare i 90 giorni", "Dopo la fine lavori il tempo corre. Una domanda in ritardo non è ammissibile."),
        ("Una fattura che non torna", "Con il mandato, bonifici del cliente più contributo netto devono fare esattamente la fattura. Se non tornano, la domanda non passa."),
    ],
    "fonti": [
        ("GSE, Conto Termico 3.0: cos'è, dotazione e percentuali", "https://www.gse.it/servizi-per-te/efficienza-energetica/conto-termico-3-0"),
        ("GSE, Conto Termico 3.0: come accedere (accesso diretto entro 90 giorni, richiesta preliminare per le imprese)", "https://www.gse.it/servizi-per-te_site/efficienza-energetica_site/conto-termico-3-0_site/Pagine/Come-accedere.aspx"),
        ("GSE, Conto Termico 3.0: tipologie di interventi", "https://www.gse.it/servizi-per-te_site/efficienza-energetica_site/conto-termico-3-0_site/Pagine/Tipologie-di-interventi.aspx"),
        ("GSE, Conto Termico 3.0: chi può accedere (Soggetto Responsabile)", "https://www.gse.it/servizi-per-te_site/efficienza-energetica_site/conto-termico-3-0_site/Pagine/Chi-puo-accedere.aspx"),
        ("GSE, Conto Termico 3.0: percentuali ed erogazione degli incentivi", "https://www.gse.it/servizi-per-te_site/efficienza-energetica_site/conto-termico-3-0_site/Pagine/PERCENTUALI-ED-EROGAZIONE-DEGLI-INCENTIVI.aspx"),
        ("GSE, Regole applicative del Conto Termico 3.0: erogazione (par. 4.3) e mandato irrevocabile all'incasso (par. 12.3)", "https://www.gse.it/documenti_site/Documenti%20GSE/Servizi%20per%20te/BIOMETANO/Regole%20e%20procedure/Regole_Applicative_CT_3_0.pdf"),
    ],
    "cta": ("Lo vuoi per tutti i tuoi preventivi?", "Noi di Cantieri Hub costruiamo sistemi di intelligenza artificiale per le imprese edili: preventivi con incentivi e quota del cliente pronti in pochi minuti, e la comunicazione con il cliente seguita dall'inizio alla fine."),
}
