GUIDA = {
    "slug": "bolle",
    "parola": "BOLLE",
    "titolo": "Dalla foto della bolla alla tabella dei costi del cantiere",
    "titolo_html": "Dalla foto della bolla <em>alla tabella dei costi del cantiere</em>",
    "sottotitolo": "Fotografi il DDT e ChatGPT lo legge: data, fornitore, materiale, quantità e prezzo finiscono in tabella, cantiere per cantiere. Con il prompt preciso da copiare.",
    "descrizione": "Le bolle arrivano in cantiere, nel furgone, su WhatsApp, e il conto vero di ogni cantiere si fa alla fine, quando si ha tempo. In questa guida trovi come impostare ChatGPT una volta sola perché legga ogni foto di bolla e la metta in una tabella per cantiere, come completare i prezzi quando sulla bolla non ci sono, e come farti dire in qualsiasi momento quanto hai speso finora. Con i prompt pronti da copiare.",
    "tema": "cantiere",
    "minuti": 7,
    "serve": "ChatGPT sul telefono, anche gratuito",
    "creata": "2026-10-25T12:00:00Z",
    "ottieni": [
        ("Una tabella per cantiere", "Data, fornitore, numero del DDT, materiale, quantità, unità, prezzo e importo. Una riga per ogni materiale."),
        ("Il conto vero, quando ti serve", "Quanto hai speso finora su quel cantiere, diviso per fornitore e per tipo di materiale. Senza aspettare la fine."),
        ("I dubbi in vista", "Le righe senza prezzo e i numeri che non si leggono bene vengono segnalati, non inventati."),
    ],
    "passi": [
        {
            "titolo": "Un progetto per ogni cantiere",
            "tempo": "2 minuti",
            "intro": "In ChatGPT crea un nuovo **Progetto** e chiamalo con il nome del cantiere. Tutte le bolle di quel cantiere vanno lì dentro: così la tabella cresce bolla dopo bolla e non si mescola con gli altri lavori.",
        },
        {
            "titolo": "Dai le regole una volta sola",
            "tempo": "2 minuti",
            "intro": "Nel progetto apri il menu con i tre puntini, poi **Impostazioni del progetto**, e incolla queste istruzioni. Da quel momento ChatGPT tratta ogni bolla allo stesso modo, senza che tu debba riscrivere niente.",
            "prompt": [("Istruzioni del progetto · Le bolle", """
In questo progetto registriamo le bolle (DDT) del cantiere [NOME DEL CANTIERE].
Ogni volta che ti mando la foto o il PDF di una bolla:
1. Leggi tutte le righe, anche quelle scritte a mano.
2. Per ogni materiale crea una riga con: data, fornitore, numero DDT, materiale (descrizione come sulla bolla), quantità, unità di misura, prezzo unitario, importo.
3. Se sulla bolla il prezzo non c'è, scrivi «da completare»: non inventarlo e non stimarlo.
4. Se una parola o un numero non si legge bene, mettilo con un punto interrogativo e chiedimi di confermarlo.
5. Aggiungi le righe nuove alla tabella delle bolle già registrate in questo progetto e mostrami la tabella aggiornata.
6. Sotto la tabella scrivi il totale speso finora e quante righe sono ancora «da completare».
Rispondi solo con la tabella e i totali.
""")],
        },
        {
            "titolo": "Fotografa la bolla bene",
            "tempo": "10 secondi",
            "intro": "La lettura è buona quanto la foto. Bastano tre attenzioni.",
            "azioni": [
                "Bolla appoggiata in piano, con luce davanti e non dietro.",
                "Tutto il foglio nella foto, anche i bordi: le quantità stanno spesso in fondo.",
                "Una foto per pagina. Se la bolla ti arriva su WhatsApp in PDF, salvala e caricala così com'è.",
            ],
        },
        {
            "titolo": "Mandala nel progetto e controlla la riga",
            "tempo": "30 secondi",
            "intro": "Apri il progetto del cantiere, allega la foto e scrivi solo «Aggiungi questa bolla». Guarda le righe nuove: se un numero è sbagliato, lo correggi con un messaggio («il ferro sono 12 quintali, non 1,2») e la tabella si aggiorna.",
            "nota": ("success", "Fallo il giorno stesso, quando la bolla è ancora in tasca. Trenta secondi adesso valgono più di un pomeriggio a fine mese."),
        },
        {
            "titolo": "Quando il prezzo sulla bolla non c'è",
            "tempo": "1 minuto",
            "intro": "Succede spesso: il DDT accompagna la merce e il prezzo arriva dopo, con la fattura. In quel caso dai a ChatGPT il listino del fornitore, o la fattura quando arriva, e le righe «da completare» si chiudono da sole.",
            "prompt": [("Prompt · Completa i prezzi", """
Ti carico [il listino prezzi / la fattura] di [FORNITORE].
Completa le righe «da completare» di questo fornitore con i prezzi del documento.
Accanto a ogni prezzo scrivi da dove viene: «da listino» o «da fattura».
Se un materiale non si trova nel documento, lascialo «da completare».
""")],
        },
        {
            "titolo": "Fatti dare il conto del cantiere",
            "tempo": "1 minuto",
            "intro": "Quando vuoi sapere a che punto sei, lo chiedi. Se carichi anche il preventivo del cantiere, ChatGPT ti dice dove stai già spendendo più del previsto.",
            "prompt": [("Prompt · Il punto dei costi", """
Fammi il punto dei materiali del cantiere [NOME]:
1. Il totale speso finora.
2. Il totale diviso per fornitore.
3. Il totale diviso per tipo di materiale: cementi e malte, ferro, laterizi, impianti, finiture, altro.
4. Le righe ancora senza prezzo.
[Se c'è il preventivo nel progetto: confronta le quantità acquistate con quelle del preventivo e dimmi dove sono già sopra.]
Poi preparami la tabella completa in un file Excel da scaricare.
""")],
        },
    ],
    "errori": [
        ("Foto storte o tagliate", "Una cifra letta male cambia il conto. Guarda sempre quantità e unità di misura delle righe nuove."),
        ("Accettare un prezzo «stimato»", "Le istruzioni dicono di non inventare i prezzi. Se vedi un prezzo che non viene dalla bolla, dal listino o dalla fattura, cancellalo."),
        ("Tutte le bolle in una chat sola", "Senza un progetto per cantiere, i materiali si mescolano e il conto per cantiere non torna più."),
        ("Aspettare la fine del mese", "Il bello è vedere il conto mentre il lavoro è aperto, quando puoi ancora correggere."),
    ],
    "fonti": [
        ("OpenAI, guida ai Progetti di ChatGPT (file e istruzioni del progetto)", "https://help.openai.com/en/articles/10169521-projects-in-chatgpt"),
    ],
    "cta": ("Lo vuoi collegato ai tuoi cantieri, senza copiare niente?", "Noi di Cantieri Hub costruiamo sistemi di intelligenza artificiale per imprese edili: le bolle lette in automatico, il costo dei materiali per cantiere sempre aggiornato e il confronto con il preventivo."),
}
