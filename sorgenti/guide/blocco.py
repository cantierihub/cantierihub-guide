GUIDA = {
    "slug": "blocco",
    "parola": "BLOCCO",
    "titolo": "Quando il materiale non arriva: rifare il programma con l'intelligenza artificiale",
    "titolo_html": "Quando il materiale non arriva: <em>rifare il programma con l'intelligenza artificiale</em>",
    "sottotitolo": "Il blocco dei tir al Sud ha messo a rischio le consegne nei cantieri. Con l'intelligenza artificiale rimetti in fila le lavorazioni in pochi minuti, avvisi chi entra dopo e scrivi al committente. Le richieste da copiare.",
    "descrizione": "Quando il materiale non arriva in cantiere non salta solo quel giorno: salta il programma di tutte le lavorazioni che vengono dopo. In questa guida trovi come usare l'intelligenza artificiale in ufficio e in cantiere per rifare il programma delle prossime settimane in pochi minuti, anche con due ipotesi di consegna, preparare gli avvisi per chi deve entrare dopo e scrivere al committente un messaggio chiaro. Con i prompt pronti da copiare.",
    "tema": "cantiere",
    "minuti": 7,
    "serve": "ChatGPT o un'altra intelligenza artificiale, anche gratuita",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("Il programma rifatto", "Le prossime settimane rimesse in fila in pochi minuti, anche con due ipotesi di consegna."),
        ("Gli avvisi per chi entra dopo", "Squadre, subappaltatori e fornitori: un messaggio per ognuno, già scritto."),
        ("Il messaggio al committente", "Chiaro e corretto: cosa è successo, cosa cambia e cosa stai facendo."),
    ],
    "contesto": {
        "etichetta": "Cosa è successo",
        "titolo": "Il blocco dei tir e i cantieri",
        "blocchi": [
            "A metà ottobre 2026 la protesta di autotrasportatori e agricoltori contro il caro gasolio è partita da **Puglia e Calabria** e si è allargata a **Sicilia, Campania e Basilicata**, con blocchi stradali e camion fermi nei porti. Alla base, il prezzo del gasolio tornato a salire dopo la fine, il 6 ottobre, dello sconto sulle accise.",
            "Le imprese edili lo hanno sentito subito: in Sicilia l'ANCE di Trapani ha parlato di cantieri edili a rischio. E il decreto di aiuti approvato il 22 ottobre riguarda autotrasporto, agricoltura e pesca.",
            ("box", "Il punto, per chi ha un cantiere", "Quando il materiale non arriva, il problema non è solo il giorno stesso. Salta la programmazione di tutte le lavorazioni che vengono dopo, e qualcuno la deve rifare in fretta. Qui l'intelligenza artificiale ti fa risparmiare ore."),
        ],
    },
    "passi": [
        {
            "titolo": "Metti il cantiere in un progetto",
            "tempo": "3 minuti, una volta sola",
            "intro": "In ChatGPT crea un **Progetto** con il nome del cantiere e caricaci il cronoprogramma che hai, in Excel o in PDF. Se non ce l'hai, scrivi l'elenco delle lavorazioni delle prossime tre settimane: chi le fa, quanto durano, cosa deve essere finito prima.",
            "nota": ("info", "Il cronoprogramma da zero lo costruisci con la nostra guida RITARDO: [cantierihub.com/guide/ritardo](https://cantierihub.com/guide/ritardo)."),
        },
        {
            "titolo": "Rifai il programma, con due ipotesi",
            "tempo": "2 minuti",
            "intro": "Quando il fornitore non sa dirti quando arriva il materiale, chiedi due versioni del programma: una se arriva presto, una se arriva tardi. Così decidi con i numeri davanti.",
            "prompt": [("Prompt 1 · Il programma nuovo", """
Non è arrivato [il ferro per il solaio], che era previsto per [martedì 14].
Il fornitore dice che arriva [giovedì 16, ma non è sicuro].

Rifai il programma delle prossime [3] settimane del cantiere [NOME]:
1. Sposta le lavorazioni che dipendono da questo materiale.
2. Proponimi le lavorazioni che si possono anticipare senza questo materiale: me le indichi e io confermo.
3. Fammi due versioni: se il materiale arriva [giovedì 16] e se arriva [lunedì 20].

Per ogni versione dimmi: cosa cambia per ogni squadra, la nuova data di fine delle lavorazioni coinvolte e chi devo avvisare.
Non inventare durate: se te ne manca una, chiedimela.
""")],
        },
        {
            "titolo": "Avvisa chi deve entrare dopo",
            "tempo": "1 minuto",
            "intro": "Scelta la versione, ti fai preparare i messaggi. Non dimenticare i fornitori che hanno una consegna programmata: calcestruzzo, pompa, noleggi.",
            "prompt": [("Prompt 2 · Gli avvisi", """
Teniamo la versione [1 / 2].
Prepara i messaggi WhatsApp per:
- le squadre e i subappaltatori che cambiano data,
- i fornitori e i noleggi con una consegna o un ritiro da spostare.
Uno per persona, brevi e cortesi. In ognuno: il cantiere, cosa cambia, la data nuova, e la richiesta di confermare.
Firma: [Nome, Impresa].
""")],
        },
        {
            "titolo": "Scrivi al committente",
            "tempo": "1 minuto",
            "intro": "Il committente non vuole sapere tutto: vuole sapere cosa è successo, cosa cambia per lui e che hai la situazione in mano.",
            "prompt": [("Prompt 3 · Il messaggio al committente", """
Prepara un messaggio per il committente del cantiere [NOME], dando del [lei].
- Cosa è successo: il materiale [ferro per il solaio] non è arrivato per il blocco dei trasporti al Sud, che non dipende da noi.
- Cosa cambia: [la nuova data della lavorazione e, se cambia, la nuova data di fine lavori].
- Cosa stiamo facendo: [abbiamo anticipato le lavorazioni possibili e siamo in contatto ogni giorno con il fornitore].
- Una proposta: una telefonata se vuole parlarne.
Tono calmo e chiaro, massimo sei righe, senza promettere date che dipendono dal fornitore.
""")],
            "nota": ("warning", "Non promettere al committente una data che il fornitore non ti ha confermato. E tieni per iscritto le comunicazioni del fornitore sul ritardo: possono servirti."),
        },
        {
            "titolo": "Il venerdì, il piano B prima che serva",
            "tempo": "2 minuti a settimana",
            "intro": "Finché la situazione dei trasporti non torna normale, una domanda a settimana ti evita la sorpresa del lunedì.",
            "prompt": [("Prompt 4 · Il controllo del venerdì", """
Guarda le lavorazioni della prossima settimana sul cantiere [NOME].
Quali materiali servono e quali arrivano su camion da fuori regione?
Per ognuno dimmi: cosa succede se arriva con tre giorni di ritardo, e cosa posso fare adesso (ordinare prima, cercare un fornitore più vicino, anticipare un'altra lavorazione).
""")],
        },
    ],
    "errori": [
        ("Non dire cosa dipende da cosa", "Se l'intelligenza artificiale non sa quali lavorazioni hanno bisogno di quel materiale, il programma nuovo è sbagliato."),
        ("Promettere date senza conferma", "La data giusta da dare al committente è quella che il fornitore ti mette per iscritto."),
        ("Avvisare solo le squadre", "Se dimentichi la consegna del calcestruzzo o il noleggio, il problema si sposta solo di un giorno."),
        ("Rifare tutto a mano la sera", "Con il programma già nel progetto, la versione nuova è questione di minuti. Il tempo che risparmi lo usi al telefono con chi conta."),
    ],
    "fonti": [
        ("L'Indipendente, 18 ottobre 2026: lo sciopero degli autotrasportatori che blocca il Sud", "https://www.lindipendente.online/2026/10/18/lo-sciopero-degli-autotrasportatori-sta-bloccando-il-sud-italia/"),
        ("TrapaniOggi, 22 ottobre 2026: ANCE Trapani, caro gasolio e protesta dei tir, cantieri edili a rischio in Sicilia", "https://trapanioggi.it/caro-gasolio-e-protesta-dei-tir-cantieri-edili-a-rischio-in-sicilia/"),
        ("Sky TG24, 22 ottobre 2026: il decreto di aiuti per autotrasporto, agricoltura e pesca", "https://tg24.sky.it/cronaca/2026/10/22/sciopero-autotrasportatori-proteste-italia-diretta"),
    ],
    "cta": ("Lo vuoi pronto sui tuoi cantieri?", "Noi di Cantieri Hub creiamo strumenti di intelligenza artificiale per le imprese edili: il programma che si rifà quando qualcosa non arriva, gli avvisi automatici a chi deve entrare dopo e il messaggio al committente già pronto."),
}
