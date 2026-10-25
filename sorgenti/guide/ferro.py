GUIDA = {
    "slug": "ferro",
    "parola": "FERRO",
    "titolo": "Il prezzo del ferro si decide a Bruxelles: cosa cambia e come aggiornare i preventivi con l'intelligenza artificiale",
    "titolo_html": "Il prezzo del ferro si decide a Bruxelles: <em>cosa cambia e come aggiornare i preventivi</em>",
    "sottotitolo": "Le due regole europee che pesano sull'acciaio che arriva da fuori, spiegate semplici. E come far trovare all'intelligenza artificiale il ferro nei tuoi preventivi e aggiornarlo con il listino nuovo, in un minuto.",
    "descrizione": "Il prezzo del ferro non dipende più solo dal mercato: dal 2026 contano anche due regole europee sull'acciaio importato. In questa guida trovi cosa prevedono, spiegato in modo semplice e con le fonti ufficiali, cosa vuol dire per un'impresa edile, e come usare l'intelligenza artificiale per trovare tutte le voci con il ferro nei preventivi aperti e aggiornarle con il listino nuovo del fornitore. Con i prompt pronti da copiare.",
    "tema": "preventivi",
    "minuti": 8,
    "serve": "ChatGPT o un'altra intelligenza artificiale, il listino del fornitore",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("Le regole in due minuti", "Cosa ha deciso l'Europa sull'acciaio che arriva da fuori, e da quando vale."),
        ("I preventivi aggiornati", "Tutte le voci con il ferro trovate e ricalcolate con il listino nuovo, con il prima e il dopo."),
        ("Il messaggio al cliente", "Come spiegare l'aggiornamento in poche righe, senza perdere la fiducia."),
    ],
    "contesto": {
        "etichetta": "Cosa cambia",
        "titolo": "Le due regole europee sull'acciaio",
        "blocchi": [
            ("box", "Dal 1° luglio 2026: meno acciaio estero senza dazio", "Con il regolamento (UE) 2026/1384 la quantità di acciaio che può entrare in Europa senza dazio scende di circa il 47% rispetto al 2024, e sopra quella quota il dazio sale al 50%. I prodotti coperti sono 30 categorie."),
            ("box", "Dal 1° gennaio 2026: si paga la CO2 contenuta nell'acciaio importato", "Con il CBAM (regolamento (UE) 2023/956) chi importa prodotti come acciaio, cemento e fertilizzanti deve essere autorizzato e paga le emissioni di CO2 contenute nei prodotti, acquistando certificati. L'applicazione è graduale e sarà completa nel 2034."),
            "**Cosa vuol dire per te.** Il prezzo del ferro, e di altri materiali che arrivano da fuori Europa, adesso dipende anche da queste regole. I listini dei fornitori possono cambiare più spesso, e ogni volta i preventivi già fatti vanno riaperti e riadattati. È un lavoro meccanico: lo può fare l'intelligenza artificiale, mentre tu decidi cosa proporre al cliente.",
        ],
    },
    "passi": [
        {
            "titolo": "Fatti dare il listino nuovo",
            "tempo": "5 minuti",
            "intro": "Chiedi al fornitore il listino aggiornato, in Excel o in PDF. Va bene anche la foto della pagina che ti interessa. Senza un prezzo di riferimento scritto, l'aggiornamento non si fa.",
        },
        {
            "titolo": "Metti listino e preventivi in un progetto",
            "tempo": "3 minuti",
            "intro": "In ChatGPT crea un **Progetto** «Preventivi e listini» e carica il listino nuovo e i preventivi ancora aperti, in PDF o in Excel.",
            "nota": ("warning", "Se nei preventivi ci sono dati dei clienti, nelle impostazioni dei dati di ChatGPT puoi scegliere che le conversazioni non vengano usate per migliorare i modelli."),
        },
        {
            "titolo": "Trova il ferro in tutti i preventivi",
            "tempo": "1 minuto",
            "intro": "Il ferro non sta solo nelle voci che si chiamano «ferro»: sta dentro il cemento armato, le reti, i profilati, le staffe, le voci composte. Fallo cercare tutto.",
            "prompt": [("Prompt 1 · Trova il ferro", """
Nei preventivi di questo progetto trova tutte le voci che contengono acciaio o ferro: tondino per cemento armato, rete elettrosaldata, profilati, lamiere, staffe, ferro lavorato, e anche le voci composte dove il ferro è una parte (per esempio un solaio o un pilastro in cemento armato).

Per ogni voce dammi: preventivo, numero della voce, descrizione, quantità, unità di misura, prezzo attuale.
Segnalami le voci composte, dove il ferro è solo una parte del prezzo.
Non modificare niente per adesso.
""")],
        },
        {
            "titolo": "Aggiorna i prezzi con il listino nuovo",
            "tempo": "1 minuto",
            "intro": "Adesso ChatGPT ricalcola solo le voci con il ferro, e ti fa vedere il prima e il dopo.",
            "prompt": [("Prompt 2 · Aggiorna", """
Con il listino nuovo di [FORNITORE], aggiorna le voci che hai trovato.
- Per le voci con solo ferro: usa il prezzo del listino [più il mio ricarico del ...%].
- Per le voci composte: aggiorna solo la parte del ferro e mostrami il calcolo. Se non sai quanto ferro c'è nella voce, chiedimelo: non stimarlo.
- Se un articolo non c'è nel listino, scrivi «non trovato».

Fammi una tabella con: preventivo, voce, prezzo vecchio, prezzo nuovo, differenza.
Poi il totale di ogni preventivo prima e dopo.
Non toccare le altre voci.
""")],
            "nota": ("success", "Quando i numeri ti tornano, chiedi «riscrivimi il preventivo [nome] aggiornato» o «dammelo in Excel»: ti ritrovi il documento pronto da controllare."),
        },
        {
            "titolo": "Decidi tu cosa mandare al cliente",
            "tempo": "2 minuti",
            "intro": "L'intelligenza artificiale ti dà i numeri, la scelta resta tua: aggiornare tutto, assorbire una parte, proporre una variante. Quando hai deciso, il messaggio lo prepara lei.",
            "prompt": [("Prompt 3 · Il messaggio al cliente", """
Prepara un messaggio per il cliente [nome], dando del [lei], sul preventivo [nome del preventivo].
Spiega in modo semplice che il fornitore ha aggiornato il listino dell'acciaio [e il motivo, se te l'ha detto] e che la differenza sul suo lavoro è di [importo].
Proponi [quello che hai deciso] e offri una telefonata per parlarne.
Massimo sei righe, tono cortese e chiaro, niente parole tecniche.
""")],
        },
        {
            "titolo": "Per i prossimi preventivi",
            "tempo": "una volta sola",
            "intro": "Due abitudini che proteggono il margine quando i prezzi si muovono spesso.",
            "azioni": [
                "Scrivi sempre per quanti giorni vale il preventivo.",
                "Valuta con il tuo consulente una clausola di aggiornamento del prezzo per i materiali che cambiano di più.",
            ],
        },
    ],
    "errori": [
        ("Cercare solo la parola «ferro»", "Il ferro sta anche dentro le voci composte. Se non lo cerchi lì, il preventivo resta sotto."),
        ("Lasciare che stimi le quantità", "Se l'intelligenza artificiale non sa quanto ferro c'è in una voce, deve chiederlo a te, non indovinarlo."),
        ("Mandare il preventivo senza rileggerlo", "Controlla almeno le voci più grandi prima di inviare."),
        ("Aspettare che sia il cliente a chiedere", "Spiegare tu l'aggiornamento, presto e con le ragioni, tiene la fiducia. Scoprirlo alla fattura no."),
    ],
    "fonti": [
        ("Commissione europea, Access2Markets, 30 giugno 2026: le nuove misure di salvaguardia sulle importazioni di acciaio (regolamento (UE) 2026/1384)", "https://trade.ec.europa.eu/access-to-markets/en/news/new-eu-safeguards-steel-imports-third-countries"),
        ("Commissione europea, Access2Markets, 28 gennaio 2026: l'inizio del periodo definitivo del CBAM (regolamento (UE) 2023/956)", "https://trade.ec.europa.eu/access-to-markets/en/news/start-definitive-period-cbam-eu"),
    ],
    "cta": ("Lo vuoi sui tuoi preventivi, con i tuoi prezzi e i tuoi listini?", "Noi di Cantieri Hub creiamo strumenti di intelligenza artificiale per le imprese edili: i listini nuovi letti appena arrivano e i preventivi aperti aggiornati da soli, con il prima e il dopo da approvare."),
}
