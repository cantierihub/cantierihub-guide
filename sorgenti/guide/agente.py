GUIDA = {
    "slug": "agente",
    "parola": "AGENTE",
    "titolo": "Gli agenti di intelligenza artificiale per la tua impresa: uno per la squadra, uno per i clienti su WhatsApp",
    "titolo_html": "Gli agenti di intelligenza artificiale per la tua impresa: <em>uno per la squadra, uno per i clienti su WhatsApp</em>",
    "sottotitolo": "Come costruire da solo l'agente che risponde alla squadra con i tuoi documenti e le tue regole, e quello che risponde ai clienti su WhatsApp anche nel weekend. Con le istruzioni da copiare.",
    "descrizione": "Se ogni domanda la fanno a te, il cantiere non va avanti senza di te. E se nel weekend su WhatsApp non risponde nessuno, i clienti scrivono a un altro. In questa guida trovi come costruire con ChatGPT, anche gratuito, l'agente che risponde alla tua squadra usando preventivi, cronoprogrammi e schede tecniche, e come far rispondere i clienti su WhatsApp anche il sabato e la domenica, raccogliendo le richieste di preventivo senza dare prezzi. Con le istruzioni pronte da copiare e le cose da non fare per non rischiare il numero.",
    "tema": "agenti",
    "minuti": 12,
    "serve": "ChatGPT, anche gratuito, e WhatsApp Business",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("L'agente della squadra", "Risponde ai tuoi operai con i tuoi documenti: misure, materiali, orari. Quello che non sa, lo gira a te."),
        ("L'agente dei clienti", "Su WhatsApp risponde subito anche nel weekend, raccoglie le richieste di preventivo e non dà prezzi."),
        ("Le regole scritte da te", "Le istruzioni da copiare, con quello che l'agente deve fare e quello che non deve fare mai."),
    ],
    "parti": [
        (
            "Parte 1 · L'agente che risponde alla squadra",
            "La misura del rivestimento, la colla, l'orario del fornitore: le risposte ci sono già, nel preventivo e nel cronoprogramma che hai fatto tu. Il problema è che le sai solo tu. Le metti in un progetto di ChatGPT e lo condividi con la squadra.",
            [
                {
                    "titolo": "Raccogli i documenti del cantiere",
                    "tempo": "10 minuti",
                    "intro": "L'agente sa solo quello che gli dai. Più i documenti sono chiari, più le risposte sono giuste.",
                    "azioni": [
                        "Il preventivo o il computo, con le misure e i materiali.",
                        "Il cronoprogramma, con chi entra e quando.",
                        "Le schede tecniche dei materiali: colle, rivestimenti, impermeabilizzanti.",
                        "Un foglio con le informazioni pratiche: orari di consegna dei fornitori, contatti, dove si scarica, chi chiamare per cosa.",
                        "Le tue regole di cantiere, se le hai scritte.",
                    ],
                },
                {
                    "titolo": "Crea il progetto e caricaci i documenti",
                    "tempo": "3 minuti",
                    "intro": "In ChatGPT crea un nuovo **Progetto**, per esempio «Agente cantiere via Roma», e carica i file. Quanti file puoi caricare dipende dal tuo piano.",
                    "nota": ("info", "Prima si usavano i «GPT personalizzati». Oggi OpenAI non permette più di crearne di nuovi sugli account personali (Free, Go, Plus e Pro): per questo usiamo i Progetti, che fanno lo stesso lavoro e si possono condividere."),
                },
                {
                    "titolo": "Scrivi le istruzioni dell'agente",
                    "tempo": "3 minuti",
                    "intro": "Nel progetto apri il menu con i tre puntini, poi **Impostazioni del progetto**, e incolla queste istruzioni. Sono le regole che l'agente segue con tutti.",
                    "prompt": [("Istruzioni del progetto · L'agente della squadra", """
Sei l'assistente del cantiere [NOME DEL CANTIERE] dell'impresa [NOME IMPRESA]. Rispondi alle domande della squadra.

Come rispondi:
- Usa solo le informazioni dei documenti di questo progetto. Dimmi sempre da quale documento prendi la risposta.
- Risposte brevi e pratiche, come le darebbe un capocantiere: prima la risposta, poi il dettaglio se serve.
- Misure, quantità, prodotti e orari li copi dai documenti. Non li arrotondi e non li stimi.

Quando non sai:
- Se la risposta non è nei documenti, scrivi: «Non lo trovo nei documenti del cantiere. Chiedi a [NOME DEL TITOLARE], [NUMERO DI TELEFONO]».
- Poi scrivi la domanda in una riga, pronta da inoltrare.

Mai:
- Inventare una misura, un prodotto o una data.
- Dare indicazioni sulla sicurezza diverse da quelle dei documenti: per la sicurezza rimanda sempre al piano di sicurezza e al capocantiere.
""")],
                },
                {
                    "titolo": "Condividilo con la squadra",
                    "tempo": "2 minuti",
                    "intro": "Nel progetto premi **Condividi** e invita le persone con la loro email o con un link. La condivisione dei progetti c'è anche nella versione gratuita di ChatGPT: a ognuno basta un account, anche gratuito.",
                    "azioni": [
                        "Dai a tutti l'accesso **Chat**: possono fare domande e vedere file e istruzioni, ma non cambiarli.",
                        "Le chat del progetto le vedono tutti i membri: le risposte restano a disposizione di tutta la squadra.",
                        "Spiega alla squadra in un messaggio come si usa: «Prima di chiamarmi, chiedi all'assistente del cantiere».",
                    ],
                },
                {
                    "titolo": "Tienilo aggiornato",
                    "tempo": "1 minuto ogni cambio",
                    "intro": "Quando cambia qualcosa, cambia il documento nel progetto: una variante, un fornitore nuovo, un orario diverso. Un agente con i documenti vecchi dà risposte vecchie.",
                    "nota": ("info", "Preferisci Claude? Anche lì ci sono i Progetti, pure nella versione gratuita, fino a cinque. Per condividerli con altre persone però serve un piano Team o Enterprise."),
                },
            ],
        ),
        (
            "Parte 2 · L'agente che risponde ai clienti su WhatsApp",
            "Il sabato e la domenica nell'edilizia non risponde quasi nessuno: è lì che puoi battere i concorrenti. Ci sono tre livelli. Il primo lo attivi oggi, gratis, in un quarto d'ora.",
            [
                {
                    "titolo": "Livello 1, oggi e gratis: WhatsApp Business",
                    "tempo": "15 minuti",
                    "intro": "WhatsApp Business è l'app gratuita di WhatsApp per le aziende, su Android e iPhone. Ha già gli strumenti per rispondere subito, anche quando non ci sei.",
                    "azioni": [
                        "**Messaggio di benvenuto**: parte da solo quando un cliente ti scrive per la prima volta.",
                        "**Messaggio di assenza**: lo programmi fuori orario e nel weekend. Dice quando rispondi e cosa ti serve per un preventivo.",
                        "**Risposte rapide**: le domande per il preventivo salvate una volta, che mandi con due tocchi.",
                        "**Etichette**: «Preventivo da fare», «Da richiamare lunedì». Il lunedì mattina trovi tutto in ordine.",
                    ],
                    "prompt": [("Da copiare · Il messaggio di assenza del weekend", """
Grazie per averci scritto, siamo [NOME IMPRESA].
Nel weekend rispondiamo dal lunedì mattina. Intanto, se ti serve un preventivo, scrivici qui:
1. che lavoro devi fare,
2. l'indirizzo del cantiere,
3. le misure indicative o qualche foto,
4. quando vorresti iniziare.
Lunedì ti ricontattiamo noi.
""")],
                },
                {
                    "titolo": "Livello 2, se nella tua app c'è: Meta Business Agent",
                    "tempo": "20 minuti",
                    "intro": "Meta sta portando dentro WhatsApp Business un agente di intelligenza artificiale, **Meta Business Agent**: impara dalle tue chat passate, dal tuo sito e dai listini o cataloghi che carichi, risponde ai clienti a qualsiasi ora e passa a te la conversazione quando serve. Per ora è disponibile per le aziende idonee in alcuni paesi: guarda negli strumenti della tua app se c'è.",
                    "azioni": [
                        "Se c'è, dagli le regole qui sotto: soprattutto che non deve mai dare prezzi.",
                        "Provalo tu prima, da un altro numero, come se fossi un cliente.",
                    ],
                    "prompt": [("Da copiare · Le regole dell'agente dei clienti", """
Rispondi ai clienti dell'impresa edile [NOME IMPRESA] di [CITTÀ].

Cosa fai:
- Rispondi subito e con gentilezza, anche fuori orario.
- Spieghi cosa facciamo: [ristrutturazioni, rifacimento bagni e cucine, cappotti, impianti] nella zona di [ZONA].
- Se il cliente vuole un preventivo, gli chiedi: che lavoro deve fare, l'indirizzo, le misure indicative o delle foto, quando vorrebbe iniziare, il suo nome e un numero di telefono.
- Alla fine dici: «Grazie, il titolare la ricontatta [lunedì mattina / entro un giorno lavorativo]».

Cosa non fai mai:
- Dare prezzi, anche indicativi, o sconti.
- Promettere date di inizio o di fine lavori.
- Rispondere su questioni tecniche o di sicurezza: dici che risponde il titolare.
Se il cliente è arrabbiato o la richiesta è urgente, scrivi che lo ricontattiamo il prima possibile e passa la conversazione a una persona.
""")],
                },
                {
                    "titolo": "Livello 3: un agente tutto tuo, sulla piattaforma ufficiale",
                    "tempo": "da progettare",
                    "intro": "Se vuoi un agente che usa i tuoi documenti, scrive le richieste direttamente nel tuo gestionale e segue le tue regole al dettaglio, la strada è la **piattaforma ufficiale WhatsApp Business**, quella per le aziende che collegano sistemi propri. Serve una configurazione tecnica e ha costi per i messaggi: è il lavoro che facciamo noi di Cantieri Hub.",
                    "nota": ("warning", "Mai collegare il tuo numero ad app o programmi non ufficiali che promettono di mettere l'intelligenza artificiale su WhatsApp. Il centro assistenza di WhatsApp dice che le app non supportate violano i termini di servizio e che l'account può essere bloccato, per un periodo o per sempre."),
                },
            ],
        ),
    ],
    "errori": [
        ("Documenti vecchi nel progetto", "L'agente della squadra risponde con quello che trova. Se il cronoprogramma è cambiato e il file no, sbaglia con sicurezza."),
        ("Lasciargli dare prezzi", "Né alla squadra né ai clienti: i prezzi li dai tu, sempre. Scrivilo nelle regole."),
        ("Le app non ufficiali su WhatsApp", "Rischi di perdere il numero dell'impresa. Usa solo WhatsApp Business e la piattaforma ufficiale."),
        ("Non provarlo prima", "Fai tu dieci domande come se fossi un operaio o un cliente. Quello che risponde male lo correggi nelle istruzioni."),
    ],
    "fonti": [
        ("OpenAI, guida ai Progetti di ChatGPT (condivisione su Free, Go, Plus e Pro; accesso Chat e Modifica)", "https://help.openai.com/en/articles/10169521-projects-in-chatgpt"),
        ("OpenAI, creare un GPT (nuovi GPT non disponibili sugli account personali)", "https://help.openai.com/en/articles/8554397-creating-a-gpt"),
        ("Anthropic, cosa sono i Progetti di Claude (anche gratuiti, condivisione con Team ed Enterprise)", "https://support.claude.com/en/articles/9517075-what-are-projects"),
        ("WhatsApp, informazioni su WhatsApp Business (app gratuita, strumenti di messaggistica)", "https://faq.whatsapp.com/988069844889223/?locale=it_IT"),
        ("WhatsApp Business, Meta Business Agent (disponibile per aziende idonee in alcuni mercati)", "https://business.whatsapp.com/products/business-app-ai-agent/"),
        ("WhatsApp, informazioni sulle app non supportate", "https://faq.whatsapp.com/520312452657376/"),
    ],
    "cta": ("Lo vuoi collegato davvero al tuo WhatsApp e ai tuoi documenti?", "Noi di Cantieri Hub costruiamo agenti di intelligenza artificiale per imprese edili e studi tecnici: quello che risponde alla squadra e quello che risponde ai clienti, collegati ai tuoi cantieri e alle tue regole."),
}
