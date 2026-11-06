#!/usr/bin/env python3
"""Generates index.html for Idan Cordovi's portfolio. Edit the data below and re-run."""
from html import escape as e
STILLS = [f"images/still-{i:02d}.jpg" for i in range(1, 20)]  # files in images/, shown in this order
HERO = 0
V = "https://i.vimeocdn.com/video/%s-d_640"
def vm(title, vid, thumb, note=""):
    return dict(t=title, note=note, url=f"https://vimeo.com/{vid}", embed=f"https://player.vimeo.com/video/{vid}?title=0&byline=0&portrait=0&autoplay=1",
                thumb=(V % thumb) if thumb else "", host="Vimeo")
def yt(title, vid, note=""):
    return dict(t=title, note=note, url=f"https://www.youtube.com/watch?v={vid}", embed=f"https://www.youtube-nocookie.com/embed/{vid}?autoplay=1",
                thumb=f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", host="YouTube")
def ig(title, code, thumb, note=""):
    return dict(t=title, note=note, url=f"https://www.instagram.com/reel/{code}/", embed=f"https://www.instagram.com/reel/{code}/embed/",
                thumb=thumb, host="Instagram")

# Works are grouped by client or type of production. Each note says what Idan did.
ALLIN_LIVE = [
 yt("Yeremi Kaplan", "DRhnP965je8", "Live session"),
 yt("Jacko Eisenberg", "JXECIKLr3Go", "Live session"),
 yt("Alma Gov", "YZZeJq5Zj84", "Live session"),
 yt("Liam Hachmon", "d3_nm4BfE9U", "Live session"),
]
for i, p in enumerate(ALLIN_LIVE, 1):
    p["thumb"] = f"images/thumbs/live-{i}.jpg"   # studio photos with the shared film grade
ALLIN_PODCAST = [
 yt("Yehonatan Margi", "tZ7jlnNBLqw", "“My home became a question”"),
]
SSA = [
 vm("Making History", 1032761269, "", "Ben Gurion · Cinematography"),
 vm("Our Story", 1003485746, "", "Web series on social skills · Cinematography"),
 vm("Our Story: Green and Red Lights in a Relationship", 1031027561, "", "Web series · Edit & color"),
 vm("At Eye Level with Rotem Sela", 856396361, "", "Bullying · Cinematography"),
 vm("Testimony from October 7th", 936250297, "", "Officer Eden Ram · Cinematography"),
 vm("Savings and Investments", 881594413, "", "Shaul Amsterdamski · Cinematography"),
 vm("All the Way to the Top", 1027190091, "", "Peter Paltchik · Cinematography"),
]
COMMERCIALS = [
 yt("SheCodes", "b63lotRY0d8", "Commercial · Producer"),
 vm("Sibus: Introduction", 966651464, "", "Social media commercial · Producer"),
 vm("Sibus: People", 966651911, "", "Social media commercial · Producer"),
 ig("Mazda with Lior Suchard", "C4ahVAUo0qn", "images/thumbs/mazda-1.jpg", "Instagram reel · Producer"),
 ig("Mazda with Lior Suchard", "C3XbanLISH4", "images/thumbs/mazda-2.jpg", "Second Instagram reel · Producer"),
]
CORPORATE = [
 vm("Foodish Exhibition", 1033131649, "", "Exhibition promo · Cinematography"),
 vm("Tech For Israel", 930612838, "", "Documentary short · Cinematography"),
 vm("EyeClick", 930606476, "", "Corporate video · Cinematography"),
 vm("V-ARMED", 966674304, "", "Corporate video · Cinematography"),
]
FORMATS = [
 yt("The Sofa: Rina Weissman", "UbM-_qiy7bE", "Short interview format · Producer"),
 yt("The Sofa: Moshik Roth", "9f_uoomWbZo", "Short interview format · Producer"),
]
FILMS = [
 yt("Welcome To The Show Biz", "g35L0fLWzKg", "Short film, 2026 · Editor"),
 yt("Water Girl", "-eWBzLyVscw", "02:51 · Edit & color"),
 yt("Children of Dawn", "wqXiXFmjISc", "Daniel Dvir · Cinematography"),
]
# Every other video's thumbnail is images/thumbs/<video id>.jpg
for p in ALLIN_PODCAST + SSA + COMMERCIALS + CORPORATE + FORMATS + FILMS:
    if p["host"] != "Instagram":
        p["thumb"] = f"images/thumbs/{p['url'].rstrip('/').split('v=')[-1].split('/')[-1]}.jpg"

def card(p):
    src = p["thumb"]
    if src.startswith("images/"):  # version local files so browsers fetch updated images
        import os; src += f"?v={int(os.path.getmtime(os.path.join(os.path.dirname(__file__) or '.', src)))}"
    img = f'<img src="{e(src)}" alt="" loading="lazy">' if p["thumb"] else ""
    data = f' data-embed="{e(p["embed"])}" data-title="{e(p["t"])}" data-host="{p["host"]}"' if p["embed"] else ""
    note = f'<span class="note">{e(p["note"])}</span>' if p["note"] else ""
    return f'''<a class="card" href="{e(p["url"])}" target="_blank" rel="noopener"{data}>
<span class="frame">{img}<span class="play" aria-hidden="true"></span></span>
<span class="cap"><span class="ttl">{e(p["t"])}</span>{note}</span></a>'''
def grid(items, cls=""): return f'<div class="grid {cls}">' + "\n".join(card(p) for p in items) + "</div>"
stills = "\n".join(f'<img src="{h}" alt="Still {i+1}" loading="lazy" width="1600" height="670">' for i, h in enumerate(STILLS) if i != HERO)

CSS = r"""
/* Layout: a screening-room reel. Every picture sits in the 2.39:1 or 16:9 frame it was shot for, with viewfinder corners as the one recurring mark. */
:root{
  --ink:#121216; --panel:#1c1c23; --line:#34343f; --paper:#f1eee6; --muted:#a5a3ad; --finder:#ffe94a;
  --display:"Big Shoulders Display","Arial Narrow",Impact,sans-serif;
  --body:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
  color-scheme:dark;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:72px}
body{margin:0;background:var(--ink);color:var(--paper);font:400 17px/1.55 var(--body)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--ink)}
a{color:inherit}
:focus-visible{outline:2px solid var(--finder);outline-offset:3px}
.wrap{max-width:1240px;margin-inline:auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:color-mix(in srgb,var(--ink) 90%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:4px 24px;padding-block:12px}
.brand{font:800 24px/1 var(--display);letter-spacing:.04em;text-transform:uppercase;text-decoration:none}
nav{display:flex;flex-wrap:wrap;gap:4px 20px}
nav a{font:500 12px/1.8 var(--mono);letter-spacing:.06em;text-transform:uppercase;text-decoration:none;color:var(--muted)}
nav a:hover{color:var(--finder)}
.hero{padding-block:32px 0}
h1{margin:0;font:900 clamp(68px,17.2vw,232px)/.84 var(--display);letter-spacing:-.005em;text-transform:uppercase;text-wrap:balance}
.roles{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 24px;margin:20px 0 28px;font:500 13px/1.6 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--finder)}
.scope{position:relative;aspect-ratio:2.39/1;max-width:100%;background:var(--panel);overflow:hidden}
.scope img{display:block;width:100%;height:100%;object-fit:cover}
.scope::before,.scope::after,.frame::before,.frame::after{content:"";position:absolute;width:22px;height:22px;z-index:2;pointer-events:none;border:2px solid var(--finder)}
.scope::before,.frame::before{left:10px;top:10px;border-right:0;border-bottom:0}
.scope::after,.frame::after{right:10px;bottom:10px;border-left:0;border-top:0}
section{padding-block:72px 0}
.head{display:grid;gap:6px;margin-bottom:28px}
.eyebrow{font:500 12px/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--finder)}
h2{margin:0;font:800 clamp(40px,6.4vw,76px)/.95 var(--display);text-transform:uppercase;text-wrap:balance}
h3{margin:44px 0 20px;font:700 clamp(26px,3.4vw,36px)/1.05 var(--display);text-transform:uppercase}
.lede{margin:6px 0 0;color:var(--muted);max-width:65ch}
.credits{display:flex;flex-wrap:wrap;gap:14px 36px;margin:14px 0 0;padding-top:16px;border-top:1px solid var(--line);max-width:100%}
.credits div{display:grid;gap:3px;min-width:0}
.credits dt{font:500 11px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.credits dd{margin:0;font-weight:600;line-height:1.35}
.reel{display:flex;gap:6px;overflow-x:auto;scroll-snap-type:x proximity;padding-bottom:12px;scrollbar-color:var(--line) transparent}
.reel img{flex:0 0 min(82vw,680px);width:min(82vw,680px);height:auto;aspect-ratio:2.39/1;object-fit:cover;scroll-snap-align:start;background:var(--panel)}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:30px 20px}
.grid.two{grid-template-columns:repeat(2,minmax(0,1fr))}
.card{display:grid;gap:10px;text-decoration:none;min-width:0}
.frame{position:relative;display:block;aspect-ratio:16/9;max-width:100%;background:var(--panel);overflow:hidden}
.frame::before,.frame::after{opacity:0;transition:opacity .18s}
.card:hover .frame::before,.card:hover .frame::after,.card:focus-visible .frame::before,.card:focus-visible .frame::after{opacity:1}
.frame img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .35s ease}
.card:hover img{transform:scale(1.03)}
.play{position:absolute;left:50%;top:50%;width:52px;height:52px;margin:-26px 0 0 -26px;border-radius:50%;background:rgb(18 18 22 / .72);border:1px solid var(--paper)}
.play::after{content:"";position:absolute;left:21px;top:16px;border-left:15px solid var(--paper);border-top:10px solid transparent;border-bottom:10px solid transparent}
.card:hover .play{background:var(--finder);border-color:var(--finder)}
.card:hover .play::after{border-left-color:var(--ink)}
.cap{display:grid;gap:2px;min-width:0}
.ttl{font-weight:600;line-height:1.3}
.note{font-size:14px;color:var(--muted)}
.contact{margin-top:88px;padding-block:56px;background:var(--finder);color:var(--ink)}
.contact h2{font-size:clamp(52px,10vw,132px)}
.contact .where{margin:10px 0 28px;font:500 13px/1.6 var(--mono);letter-spacing:.06em;text-transform:uppercase}
.ways{display:flex;flex-wrap:wrap;gap:10px}
.ways a,.ways button{font:600 16px/1 var(--body);padding:14px 18px;border:2px solid var(--ink);background:none;color:var(--ink);text-decoration:none;cursor:pointer;overflow-wrap:anywhere}
.ways a:hover,.ways button:hover{background:var(--ink);color:var(--finder)}
.contact :focus-visible{outline-color:var(--ink)}
footer{padding-block:18px;font:400 12px/1.5 var(--mono);color:var(--muted)}
dialog{width:min(1100px,calc(100vw - 32px));max-width:none;padding:0;border:0;background:var(--ink);color:var(--paper)}
dialog::backdrop{background:rgb(8 8 10 / .92)}
.dhead{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:10px 12px}
.dhead strong{min-width:0;font-weight:600}
.dactions{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:14px;font:500 12px/1.5 var(--mono);text-transform:uppercase;letter-spacing:.05em}
.dactions button{all:unset;cursor:pointer;color:var(--finder)}
.dactions button:focus-visible{outline:2px solid var(--finder)}
.player{aspect-ratio:16/9;max-width:100%;background:#000}
.player iframe{display:block;width:100%;height:100%;border:0}
.player.tall{aspect-ratio:auto;width:min(100%,420px);height:min(78vh,760px);margin-inline:auto;background:#fff}
.fallback{position:relative;display:block;width:100%;height:100%;color:var(--paper)}
.fallback img{display:block;width:100%;height:100%;object-fit:cover;opacity:.55}
.fallback span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);padding:14px 22px;background:var(--finder);color:var(--ink);font:600 17px/1 var(--body);white-space:nowrap}
.fallback:hover span{background:var(--paper)}
@media (max-width:860px){.grid,.grid.two{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.grid,.grid.two{grid-template-columns:minmax(0,1fr)}section{padding-block:56px 0}.roles{display:grid}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.frame img,.frame::before,.frame::after{transition:none}.card:hover img{transform:none}}
"""

JS = r"""
const d=document.getElementById('player'),box=d.querySelector('.player'),t=d.querySelector('strong'),ext=d.querySelector('a');
document.querySelectorAll('.card[data-embed]').forEach(c=>c.addEventListener('click',ev=>{
  if(ev.metaKey||ev.ctrlKey||ev.shiftKey)return;ev.preventDefault();
  t.textContent=c.dataset.title;ext.href=c.href;ext.textContent='Open on '+c.dataset.host;
  const f=document.createElement('iframe');f.src=c.dataset.embed;f.title=c.dataset.title;f.allow='autoplay; fullscreen; picture-in-picture';f.allowFullscreen=true;
  box.classList.toggle('tall',c.dataset.host==='Instagram');
  box.replaceChildren(f);d.showModal();
}));
d.querySelector('button').addEventListener('click',()=>d.close());
d.addEventListener('click',ev=>{if(ev.target===d)d.close()});
d.addEventListener('close',()=>box.replaceChildren());
// Where the page isn't allowed to embed other sites (e.g. a preview), show the thumbnail and a link out instead.
let cur=null,blocked=false;
const fallback=()=>{if(!cur||!d.open)return;box.classList.remove('tall');const a=document.createElement('a');a.className='fallback';a.href=cur.href;a.target='_blank';a.rel='noopener';
  const im=cur.querySelector('img');if(im){const i=new Image();i.src=im.src;i.alt='';a.append(i)}
  const s=document.createElement('span');s.textContent='Watch on '+cur.dataset.host;a.append(s);box.replaceChildren(a)};
document.querySelectorAll('.card[data-embed]').forEach(c=>c.addEventListener('click',()=>{cur=c;if(blocked)fallback()}));
addEventListener('securitypolicyviolation',e=>{if(/frame|child/.test(e.violatedDirective)){blocked=true;fallback()}});
const copy=document.getElementById('copy');
copy.addEventListener('click',async()=>{try{await navigator.clipboard.writeText('cordovi.idan@gmail.com');copy.textContent='Email copied'}catch(_){copy.textContent='cordovi.idan@gmail.com'}});
"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>Idan Cordovi</title>
<meta name="description" content="Idan Cordovi is a cinematographer, producer, editor and colorist based in Tel Aviv, working in documentary, corporate and educational film.">
<meta property="og:title" content="Idan Cordovi">
<meta property="og:description" content="Cinematographer, producer, editor and colorist. Tel Aviv, Israel.">
<meta property="og:image" content="{STILLS[HERO]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Figtree:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<script>addEventListener('error',e=>{{if(e.target.tagName==='IMG')e.target.remove()}},true)</script>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap bar">
<a class="brand" href="#top">Idan Cordovi</a>
<nav aria-label="Main">
<a href="#works">Works</a><a href="#contact">Contact</a>
</nav></div></header>
<main id="top">
<div class="wrap hero">
<h1>Idan Cordovi</h1>
<div class="roles"><span>Cinematographer</span><span>Producer</span><span>Editor &amp; Color</span><span>Tel Aviv, Israel</span></div>
<div class="scope"><img src="{STILLS[HERO]}" alt="Still from the documentary Who Cares?" width="1600" height="670" fetchpriority="high"></div>
</div>

<div id="works">
<section id="all-in"><div class="wrap">
<div class="head"><span class="eyebrow">Studio productions · Camera, edit &amp; color</span><h2>All in Studios</h2></div>
<h3>The Session with Dean Elbaz · Live music</h3>
{grid(ALLIN_LIVE, "two")}
<h3>The Itay Segal Podcast</h3>
{grid(ALLIN_PODCAST, "two")}
</div></section>

<section id="who-cares"><div class="wrap">
<div class="head"><span class="eyebrow">55 min documentary · Cinematography</span><h2>Who Cares?</h2>
<dl class="credits">
<div><dt>Produced by</dt><dd>Duetch &amp; Co</dd></div>
<div><dt>Directed by</dt><dd>Tamar Schwarz</dd></div>
<div><dt>Cinematography</dt><dd>Tamar Schwarz &amp; Idan Cordovi</dd></div>
<div><dt>Editor</dt><dd>Michael Anug</dd></div>
<div><dt>Post-production director</dt><dd>Rotem Gross</dd></div>
</dl></div>
<div class="reel" tabindex="0" aria-label="Stills from Who Cares?, scroll sideways">
{stills}
</div>
</div></section>

<section id="safe-school"><div class="wrap">
<div class="head"><span class="eyebrow">Educational video series</span><h2>Safe School Analytics</h2></div>
{grid(SSA)}
</div></section>

<section id="brands"><div class="wrap">
<div class="head"><span class="eyebrow">Brands and organizations</span><h2>Commercials &amp; Corporate</h2></div>
<h3>Commercials</h3>
{grid(COMMERCIALS)}
<h3>Corporate and organizations</h3>
{grid(CORPORATE, "two")}
</div></section>

<section id="formats"><div class="wrap">
<div class="head"><span class="eyebrow">Interview format</span><h2>The Sofa</h2></div>
{grid(FORMATS, "two")}
</div></section>

<section id="films"><div class="wrap">
<div class="head"><span class="eyebrow">Short films and music</span><h2>Films</h2></div>
{grid(FILMS)}
</div></section>
</div>
</main>

<div class="contact" id="contact"><div class="wrap">
<h2>Contact me</h2>
<p class="where">Tel Aviv, Israel · +972-52-943-4139 · cordovi.idan@gmail.com</p>
<div class="ways">
<a href="https://wa.me/972529434139" target="_blank" rel="noopener">WhatsApp</a>
<a href="mailto:cordovi.idan@gmail.com">Email</a>
<button id="copy" type="button">Copy email</button>
<a href="https://www.linkedin.com/in/idan-cordovi-898a44231/" target="_blank" rel="noopener">LinkedIn</a>
<a href="https://www.instagram.com/idancordovi/" target="_blank" rel="noopener">Instagram</a>
</div></div></div>
<footer><div class="wrap">© Idan Cordovi</div></footer>

<dialog id="player" aria-label="Video player">
<div class="dhead"><strong></strong><div class="dactions"><a href="#" target="_blank" rel="noopener"></a><button type="button">Close</button></div></div>
<div class="player"></div>
</dialog>
<script>{JS}</script>
</body>
</html>
"""
open(__import__("os").path.join(__import__("os").path.dirname(__file__) or ".", "index.html"), "w", encoding="utf-8").write(HTML)
print(len(HTML))
