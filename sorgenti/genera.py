"""Genera le guide di cantierihub.com/guide dalle sorgenti in sorgenti/guide/*.py.

Ogni sorgente definisce GUIDA (dizionario, vedi sotto). Per ognuna escono:
- public/guide/<slug>.html  la guida (si apre dopo la mail sulla pagina cantierihub.com/guide/<slug>)
- public/guide/<slug>.json  la scheda che il sito legge da GitHub (titolo, sottotitolo, descrizione, html_url)

uso: python3 sorgenti/genera.py            (tutte)
     python3 sorgenti/genera.py ritardo    (una sola)

GUIDA = {
  "slug", "parola" (la parola del commento), "titolo", "titolo_html" (con <em> sulla parte arancio), "sottotitolo",
  "descrizione" (la pagina con la mail: «Cosa troverai»), "tema", "minuti", "serve", "creata" (ISO),
  "ottieni": [(titolo, testo)] x3,
  "contesto": {"etichetta", "titolo", "blocchi": [testo | ("box", titolo, testo)]} (facoltativo),
  "passi": [{"titolo", "tempo", "intro", "azioni": [testo], "prompt": [(etichetta, testo)], "nota": (tipo, testo)}],
  "parti": [(titolo della parte, intro, [passi])]   (in alternativa a "passi", per le guide in due parti),
  "errori": [(titolo, testo)],
  "fonti": [(testo, url)],
  "cta": (titolo, testo),
}
Nei testi: niente trattini lunghi, niente punti esclamativi, niente emoji (stesse regole delle altre guide CH)."""
import html
import importlib.util
import json
import sys
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
SORGENTI = RADICE / "sorgenti" / "guide"
USCITA = RADICE / "public" / "guide"
BASE_HTML = "https://guide.cantierihub.com/guide"

CSS = """
    :root {
      --accent:   #D44E12;
      --accent2:  #F97316;
      --bg:       #0A0F1C;
      --navy:     #0A2D72;
      --text:     #FFFFFF;
      --text-mut: rgba(255,255,255,0.70);
    }
    *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
    html { scroll-behavior:smooth; }
    body { font-family:'Poppins','Helvetica Neue',sans-serif; background:var(--bg); color:var(--text); line-height:1.65; min-height:100vh; }
    a { color:var(--accent2); }

    .hero { background:linear-gradient(160deg, #0d1b3e 0%, var(--bg) 60%); border-bottom:1px solid rgba(212,78,18,0.2); padding:48px 24px 56px; text-align:center; }
    .brand-badge { display:inline-flex; align-items:center; gap:10px; background:rgba(212,78,18,0.12); border:1px solid rgba(212,78,18,0.3);
      border-radius:40px; padding:8px 20px; margin-bottom:28px; font-size:13px; font-weight:700; color:var(--accent2); text-transform:uppercase; letter-spacing:2px; }
    .brand-dot { width:8px; height:8px; border-radius:50%; background:var(--accent); }
    .hero h1 { font-size:clamp(1.9rem,5vw,3rem); font-weight:900; color:var(--text); line-height:1.12; margin:0 auto 20px; max-width:860px; }
    .hero h1 em { color:var(--accent2); font-style:normal; }
    .hero .sub { font-size:1.08rem; color:var(--text-mut); max-width:640px; margin:0 auto 32px; }
    .hero-meta { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }
    .meta-pill { background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:24px; padding:8px 18px; font-size:13px; font-weight:600; color:var(--text-mut); }
    .meta-pill span { color:var(--text); }

    .container { max-width:820px; margin:0 auto; padding:0 20px; }
    section { padding:56px 0 0; }
    .section-label { font-size:11px; font-weight:800; color:var(--accent2); text-transform:uppercase; letter-spacing:4px; margin-bottom:12px; }
    .section-title { font-size:clamp(1.4rem,3.5vw,2rem); font-weight:800; color:var(--text); line-height:1.2; margin-bottom:28px; }
    .section-intro { font-size:.98rem; color:var(--text-mut); margin:-12px 0 28px; }

    .output-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:16px; }
    .output-card { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:16px; padding:26px; }
    .output-num { width:34px; height:34px; border-radius:10px; background:rgba(212,78,18,0.15); color:var(--accent2); font-weight:800;
      display:flex; align-items:center; justify-content:center; margin-bottom:14px; }
    .output-card h4 { font-size:1rem; font-weight:700; color:var(--text); margin-bottom:8px; }
    .output-card p { font-size:.92rem; color:var(--text-mut); line-height:1.55; }

    .testo p { font-size:.98rem; color:var(--text-mut); margin-bottom:16px; }
    .testo p strong { color:var(--text); }
    .box { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.10); border-left:4px solid var(--accent); border-radius:14px; padding:20px 22px; margin:0 0 16px; }
    .box h4 { font-size:1rem; font-weight:700; margin-bottom:6px; }
    .box p { font-size:.94rem; color:var(--text-mut); margin:0; }

    .parte-titolo { font-size:clamp(1.25rem,3vw,1.6rem); font-weight:800; margin:48px 0 10px; }
    .parte-titolo:first-child { margin-top:0; }
    .parte-intro { font-size:.98rem; color:var(--text-mut); margin-bottom:24px; }

    .steps-list { display:flex; flex-direction:column; gap:20px; }
    .step-card { background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:20px; padding:28px; }
    .step-header { display:flex; align-items:flex-start; gap:18px; margin-bottom:16px; }
    .step-number { flex-shrink:0; width:52px; height:52px; border-radius:14px; background:var(--accent); color:#fff; font-size:1.2rem; font-weight:900;
      display:flex; align-items:center; justify-content:center; }
    .step-title { font-size:1.12rem; font-weight:700; color:var(--text); margin-bottom:2px; line-height:1.3; }
    .step-time { font-size:.8rem; color:var(--text-mut); font-weight:500; }
    .step-intro { font-size:.95rem; color:var(--text-mut); line-height:1.65; margin-bottom:16px; }
    .action-list { display:flex; flex-direction:column; gap:10px; margin-bottom:16px; }
    .action-item { display:flex; gap:12px; align-items:flex-start; background:rgba(255,255,255,0.03); border-radius:10px; padding:12px 16px; font-size:.92rem; }
    .action-arrow { color:var(--accent2); font-weight:800; flex-shrink:0; }

    .prompt { position:relative; background:#0d1526; border:1px solid rgba(249,115,22,0.35); border-radius:14px; margin:0 0 16px; overflow:hidden; }
    .prompt-head { display:flex; align-items:center; justify-content:space-between; gap:12px; padding:10px 14px 10px 18px;
      background:rgba(249,115,22,0.10); border-bottom:1px solid rgba(249,115,22,0.25); }
    .prompt-label { font-size:12px; font-weight:800; color:var(--accent2); text-transform:uppercase; letter-spacing:1.5px; }
    .copia { font-family:inherit; font-size:13px; font-weight:700; color:#fff; background:var(--accent); border:0; border-radius:8px; padding:7px 14px; cursor:pointer; }
    .copia.fatto { background:#15803d; }
    .prompt pre { white-space:pre-wrap; word-wrap:break-word; font-family:inherit; font-size:.9rem; line-height:1.6; color:#e2e8f0; padding:16px 18px 18px; margin:0; }

    .callout { border-radius:12px; padding:14px 18px; font-size:.9rem; line-height:1.55; margin:0 0 4px; }
    .callout.info    { background:rgba(59,130,246,0.1); border:1px solid rgba(59,130,246,0.25); color:#bfdbfe; }
    .callout.success { background:rgba(22,163,74,0.1);  border:1px solid rgba(22,163,74,0.25);  color:#bbf7d0; }
    .callout.warning { background:rgba(245,158,11,0.1); border:1px solid rgba(245,158,11,0.25); color:#fde68a; }

    .errori-list { display:flex; flex-direction:column; gap:14px; }
    .err-item { background:rgba(239,68,68,0.06); border:1px solid rgba(239,68,68,0.2); border-left:4px solid #ef4444; border-radius:12px; padding:18px 22px; }
    .err-title { font-size:.98rem; font-weight:700; color:#fca5a5; margin-bottom:4px; }
    .err-desc { font-size:.9rem; color:var(--text-mut); line-height:1.55; }

    .fonti { list-style:none; display:flex; flex-direction:column; gap:10px; }
    .fonti li { font-size:.86rem; color:var(--text-mut); background:rgba(255,255,255,0.03); border-radius:10px; padding:12px 16px; }
    .fonti a { word-break:break-word; }

    .cta-block { margin:64px 0 0; background:linear-gradient(135deg, rgba(10,45,114,0.4) 0%, rgba(212,78,18,0.15) 100%);
      border:1px solid rgba(212,78,18,0.3); border-radius:24px; padding:44px 32px; text-align:center; }
    .cta-block h2 { font-size:clamp(1.4rem,4vw,2rem); font-weight:900; color:var(--text); margin-bottom:14px; line-height:1.2; }
    .cta-block p { font-size:.95rem; color:var(--text-mut); max-width:520px; margin:0 auto 28px; }
    .cta-btn { display:inline-block; background:var(--accent); color:#fff; font-size:1rem; font-weight:800; padding:16px 32px; border-radius:12px; text-decoration:none; }
    .cta-btn:hover { background:#b83a0a; }

    .footer { text-align:center; padding:40px 24px; margin-top:56px; border-top:1px solid rgba(255,255,255,0.06); }
    .footer-brand { font-size:1.1rem; font-weight:800; color:var(--accent2); margin-bottom:8px; }
    .footer-sub { font-size:.8rem; color:var(--text-mut); }
    @media (max-width:520px) { .step-card { padding:22px 18px; } .step-number { width:44px; height:44px; font-size:1.05rem; } .cta-block { padding:36px 20px; } }
"""

JS = """
  <script>
    document.querySelectorAll('.copia').forEach(function (b) {
      b.addEventListener('click', function () {
        var testo = b.closest('.prompt').querySelector('pre').innerText;
        var fatto = function () { b.textContent = 'Copiato'; b.classList.add('fatto'); setTimeout(function () { b.textContent = 'Copia'; b.classList.remove('fatto'); }, 2000); };
        var vecchio = function () { var t = document.createElement('textarea'); t.value = testo; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
          document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (err) {} t.remove(); fatto(); };
        if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText(testo).then(fatto, vecchio); } else { vecchio(); }
      });
    });
  </script>"""

e = html.escape


def ricco(testo):
    """Testo con **grassetto** e [link](url): l'unico markup ammesso nelle sorgenti."""
    import re
    t = e(testo)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[(.+?)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t


def passo_html(n, p):
    out = [f'<div class="step-card"><div class="step-header"><div class="step-number">{n:02d}</div><div>'
           f'<h3 class="step-title">{ricco(p["titolo"])}</h3>']
    if p.get("tempo"):
        out.append(f'<div class="step-time">{e(p["tempo"])}</div>')
    out.append("</div></div>")
    if p.get("intro"):
        out.append(f'<p class="step-intro">{ricco(p["intro"])}</p>')
    if p.get("azioni"):
        out.append('<div class="action-list">' + "".join(
            f'<div class="action-item"><span class="action-arrow">&rarr;</span><span>{ricco(a)}</span></div>' for a in p["azioni"]) + "</div>")
    for etichetta, testo in p.get("prompt", []):
        out.append(f'<div class="prompt"><div class="prompt-head"><span class="prompt-label">{e(etichetta)}</span>'
                   f'<button class="copia" type="button">Copia</button></div><pre>{e(testo.strip())}</pre></div>')
    if p.get("nota"):
        tipo, testo = p["nota"]
        out.append(f'<div class="callout {tipo}">{ricco(testo)}</div>')
    out.append("</div>")
    return "".join(out)


def guida_html(g):
    slug = g["slug"]
    corpo = []
    corpo.append(f"""
  <div class="hero">
    <div class="brand-badge"><div class="brand-dot"></div>Cantieri Hub · Guida gratuita</div>
    <h1>{g["titolo_html"]}</h1>
    <p class="sub">{ricco(g["sottotitolo"])}</p>
    <div class="hero-meta">
      <div class="meta-pill">Tempo: <span>{g["minuti"]} minuti</span></div>
      <div class="meta-pill">Ti serve: <span>{e(g["serve"])}</span></div>
      <div class="meta-pill">Per: <span>imprese edili e studi tecnici</span></div>
    </div>
  </div>
  <div class="container">""")
    corpo.append('<section><div class="section-label">Cosa ottieni</div><h2 class="section-title">Alla fine di questa guida</h2><div class="output-grid">'
                 + "".join(f'<div class="output-card"><div class="output-num">{i}</div><h4>{ricco(t)}</h4><p>{ricco(d)}</p></div>'
                           for i, (t, d) in enumerate(g["ottieni"], 1)) + "</div></section>")
    if g.get("contesto"):
        c = g["contesto"]
        pezzi = []
        for b in c["blocchi"]:
            if isinstance(b, tuple) and b[0] == "box":
                pezzi.append(f'<div class="box"><h4>{ricco(b[1])}</h4><p>{ricco(b[2])}</p></div>')
            else:
                pezzi.append(f"<p>{ricco(b)}</p>")
        corpo.append(f'<section><div class="section-label">{e(c["etichetta"])}</div><h2 class="section-title">{ricco(c["titolo"])}</h2>'
                     f'<div class="testo">{"".join(pezzi)}</div></section>')
    if g.get("parti"):
        n = 0
        blocchi = []
        for titolo, intro, passi in g["parti"]:
            blocchi.append(f'<h3 class="parte-titolo">{ricco(titolo)}</h3><p class="parte-intro">{ricco(intro)}</p><div class="steps-list">')
            for p in passi:
                n += 1
                blocchi.append(passo_html(n, p))
            blocchi.append("</div>")
        corpo.append('<section><div class="section-label">La guida</div><h2 class="section-title">Come si fa, passo per passo</h2>'
                     + "".join(blocchi) + "</section>")
    else:
        corpo.append('<section><div class="section-label">La guida</div><h2 class="section-title">Come si fa, passo per passo</h2><div class="steps-list">'
                     + "".join(passo_html(i, p) for i, p in enumerate(g["passi"], 1)) + "</div></section>")
    corpo.append('<section><div class="section-label">Attenzione</div><h2 class="section-title">Gli errori da evitare</h2><div class="errori-list">'
                 + "".join(f'<div class="err-item"><div class="err-title">{ricco(t)}</div><div class="err-desc">{ricco(d)}</div></div>'
                           for t, d in g["errori"]) + "</div></section>")
    if g.get("fonti"):
        corpo.append('<section><div class="section-label">Fonti</div><h2 class="section-title">Dove abbiamo preso le informazioni</h2><ul class="fonti">'
                     + "".join(f'<li>{ricco(t)}<br><a href="{e(u)}" target="_blank" rel="noopener">{e(u)}</a></li>' for t, u in g["fonti"])
                     + "</ul></section>")
    titolo_cta, testo_cta = g["cta"]
    link = f"https://cantierihub.com/demo?utm_source=guida&utm_medium=guida&utm_campaign=guida-{slug}"
    corpo.append(f"""
    <div class="cta-block">
      <h2>{ricco(titolo_cta)}</h2>
      <p>{ricco(testo_cta)}</p>
      <a class="cta-btn" href="{link}" target="_blank" rel="noopener">Prenota una consulenza gratuita</a>
    </div>
  </div>
  <div class="footer">
    <div class="footer-brand">Cantieri Hub</div>
    <div class="footer-sub">Sistemi di intelligenza artificiale per imprese edili e studi tecnici · <a href="https://cantierihub.com">cantierihub.com</a></div>
  </div>""")
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, follow" />
  <title>{e(g["titolo"])} · Cantieri Hub</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>{CSS}  </style>
</head>
<body>
{"".join(corpo)}
{JS}
</body>
</html>
"""


def scheda(g):
    return {
        "slug": g["slug"],
        "title": g["titolo"],
        "subtitle": g["sottotitolo"].replace("**", ""),
        "description": g["descrizione"],
        "topic": g["tema"],
        "cover_image": "",
        "html_url": f"{BASE_HTML}/{g['slug']}.html",
        "created_at": g["creata"],
        "published": True,
    }


def carica(percorso):
    spec = importlib.util.spec_from_file_location(percorso.stem, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.GUIDA


VIETATI = ["—", "–", "!"]


def controlla(g):
    """Le regole di scrittura delle guide CH: niente trattini lunghi, punti esclamativi ed emoji."""
    import re
    testo = json.dumps(g, ensure_ascii=False)
    errori = [f"«{v}»" for v in VIETATI if v in testo]
    if re.search("[\U0001F300-\U0001FAFF☀-➿]", testo):
        errori.append("emoji")
    return errori


def main():
    scelte = set(sys.argv[1:])
    USCITA.mkdir(parents=True, exist_ok=True)
    for p in sorted(SORGENTI.glob("*.py")):
        g = carica(p)
        if scelte and g["slug"] not in scelte:
            continue
        errori = controlla(g)
        if errori:
            sys.exit(f"{g['slug']}: {', '.join(errori)}")
        (USCITA / f"{g['slug']}.html").write_text(guida_html(g), encoding="utf-8")
        (USCITA / f"{g['slug']}.json").write_text(json.dumps(scheda(g), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("ok", g["slug"])


if __name__ == "__main__":
    main()
