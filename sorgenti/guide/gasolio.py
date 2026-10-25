GUIDA = {
    "slug": "gasolio",
    "parola": "GASOLIO",
    "titolo": "Quanto gasolio consuma ogni cantiere: la tabella fatta con l'intelligenza artificiale",
    "titolo_html": "Quanto gasolio consuma ogni cantiere: <em>la tabella fatta con l'intelligenza artificiale</em>",
    "sottotitolo": "Il prompt da passare a ChatGPT, o a qualsiasi intelligenza artificiale, per tenere in una tabella i mezzi, il gasolio, i noleggi e le consegne, cantiere per cantiere. Così vedi dove il margine si stringe.",
    "descrizione": "Il gasolio sta dentro tutto quello che si muove in cantiere: il furgone, l'escavatore, i noleggi, le consegne. Se non lo misuri per cantiere, il margine cala senza che nessuno se ne accorga. In questa guida trovi come raccogliere i dati che servono, il prompt per far costruire all'intelligenza artificiale la tabella dei mezzi e dei consumi, e come leggere ogni mese quanto costa il gasolio su ogni lavoro.",
    "tema": "costi",
    "minuti": 8,
    "serve": "ChatGPT o un'altra intelligenza artificiale, anche gratuita",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("La tabella dei mezzi", "Ogni rifornimento e ogni giornata di lavoro di ogni mezzo, in un posto solo."),
        ("Il gasolio di ogni cantiere", "Quanto costano carburante, noleggi e consegne su ogni lavoro, mese per mese."),
        ("Dove guadagni di più", "Quale cantiere ti rende e quale si mangia il margine, con i numeri davanti."),
    ],
    "contesto": {
        "etichetta": "Prima di cominciare",
        "titolo": "Gli aiuti sul gasolio e i mezzi di cantiere",
        "blocchi": [
            "Il 22 ottobre 2026 il Consiglio dei ministri ha approvato un decreto di aiuti per **autotrasporto, agricoltura e pesca**, con altre risorse per il credito d'imposta sul gasolio dell'autotrasporto. Per i mezzi di cantiere non è previsto un aiuto simile.",
            "Il gasolio però entra in tutto quello che si muove in cantiere. Se non sai quanto ne consuma ogni mezzo e su quale lavoro, il conto lo scopri solo a fine anno. La buona notizia è che per saperlo non serve un gestionale: bastano i dati che hai già e una tabella tenuta dall'intelligenza artificiale.",
        ],
    },
    "passi": [
        {
            "titolo": "Raccogli i pezzi che hai già",
            "tempo": "10 minuti",
            "intro": "Non devi inventarti niente: i dati sono già nelle tue fatture e nella testa dei tuoi capisquadra.",
            "azioni": [
                "Le fatture del carburante, o il resoconto della carta carburante se la usi: di solito ha già targa, litri e importo.",
                "L'elenco dei mezzi: targa o matricola e tipo (furgone, escavatore, camion, gruppo elettrogeno).",
                "I noleggi e le consegne con il costo del trasporto.",
                "Il dato che manca quasi sempre: **dove ha lavorato ogni mezzo**. Basta una riga al giorno per mezzo: data, mezzo, cantiere, ore di lavoro o chilometri.",
            ],
            "nota": ("info", "La riga del giorno la può mandare il caposquadra in un vocale o in un messaggio: «oggi escavatore piccolo in via Roma, 6 ore». L'intelligenza artificiale la trascrive e la mette in tabella."),
        },
        {
            "titolo": "Crea il progetto «Mezzi e gasolio» e dai le regole",
            "tempo": "3 minuti",
            "intro": "In ChatGPT crea un nuovo **Progetto**. Nelle impostazioni del progetto incolla queste istruzioni: valgono per tutto quello che gli manderai dopo.",
            "prompt": [("Istruzioni del progetto · Mezzi e gasolio", """
In questo progetto teniamo i consumi dei mezzi della mia impresa edile.
Tieni due tabelle:

TABELLA 1, RIFORNIMENTI: data, mezzo (targa o nome), litri, importo, prezzo al litro, da dove viene il dato (fattura, scontrino, carta carburante).
TABELLA 2, LAVORO DEI MEZZI: data, mezzo, cantiere, ore di lavoro o chilometri.

Ogni volta che ti mando foto, PDF, vocali trascritti o messaggi:
1. Metti ogni dato nella tabella giusta e mostrami solo le righe nuove.
2. Non inventare numeri. Se un dato manca o non si legge, scrivi «da completare» e chiedimelo.
3. Se un rifornimento non si può collegare a un mezzo, mettilo «da assegnare».

Quando ti chiedo il riepilogo, dividi il gasolio di ogni mezzo tra i cantieri in proporzione alle ore (o ai chilometri) lavorati in quel periodo, e spiegami in una riga il calcolo che hai fatto.
""")],
        },
        {
            "titolo": "Ogni settimana: le ricevute e le giornate",
            "tempo": "5 minuti a settimana",
            "intro": "Una volta a settimana carichi nel progetto le foto delle ricevute o il PDF della carta carburante, e incolli le righe delle giornate dei mezzi. Se preferisci, lo fai ogni sera dal telefono.",
            "nota": ("success", "Più è fresco il dato, più è giusto. La riga «dove ha lavorato il mezzo» dopo una settimana non se la ricorda nessuno."),
        },
        {
            "titolo": "A fine mese, il riepilogo per cantiere",
            "tempo": "1 minuto",
            "intro": "Con questo prompt hai il costo del gasolio di ogni cantiere, i consumi dei mezzi e quanto pesano gasolio, noleggi e consegne sul lavoro.",
            "prompt": [("Prompt · Il riepilogo del mese", """
Fammi il riepilogo di [mese e anno]:
1. Il costo del gasolio per ogni cantiere, con i litri.
2. Il consumo medio di ogni mezzo: litri all'ora per i mezzi d'opera, litri ogni 100 km per furgoni e camion.
3. I mezzi che questo mese hanno consumato più della loro media.
4. Per ogni cantiere: gasolio, noleggi e consegne, e il totale.
[5. Ti do l'importo dei lavori di ogni cantiere: dimmi quanto pesano questi costi in percentuale sul lavoro.]
Elenca anche le righe ancora «da completare» o «da assegnare».
Poi preparami il riepilogo in un file Excel da scaricare.
""")],
        },
        {
            "titolo": "Leggi i numeri e usali",
            "tempo": "10 minuti al mese",
            "intro": "La tabella serve se cambia qualcosa nel modo in cui lavori. Tre domande da farti ogni mese:",
            "azioni": [
                "Un mezzo consuma più della sua media? Spesso è una manutenzione da fare, o un mezzo usato per il lavoro sbagliato.",
                "Su quale cantiere gasolio e trasporti pesano di più? Il prossimo preventivo per un lavoro simile deve tenerne conto.",
                "Noleggi e consegne si possono raggruppare? Due consegne nella stessa settimana spesso possono diventare una.",
            ],
        },
    ],
    "errori": [
        ("Il gasolio dell'auto personale nel conto", "Tieni fuori quello che non lavora in cantiere, o il costo dei lavori sembra più alto di quello che è."),
        ("Saltare la riga «dove ha lavorato»", "Senza, l'intelligenza artificiale non può dividere il gasolio tra i cantieri: hai solo il totale."),
        ("Prendere i numeri senza guardarli", "Il primo mese controlla due o tre righe sulle fatture vere. Se tornano, poi ti puoi fidare di più."),
        ("Dimenticare il carburante dei noleggi", "Alcuni noleggi lo includono, altri no: scrivi nella tabella quale dei due è."),
    ],
    "fonti": [
        ("Sky TG24, 22 ottobre 2026: il decreto di aiuti per autotrasporto, agricoltura e pesca e il credito d'imposta sul gasolio", "https://tg24.sky.it/cronaca/2026/10/22/sciopero-autotrasportatori-proteste-italia-diretta"),
        ("OpenAI, guida ai Progetti di ChatGPT", "https://help.openai.com/en/articles/10169521-projects-in-chatgpt"),
    ],
    "cta": ("Lo vuoi automatico, senza ricopiare le ricevute?", "Noi di Cantieri Hub costruiamo strumenti di intelligenza artificiale per imprese edili: le fatture del carburante e dei noleggi lette e divise per cantiere, i consumi di ogni mezzo e il margine di ogni lavoro sempre aggiornati."),
}
