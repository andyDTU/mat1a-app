"""
Mat1A Studieassistent – DTU Matematik 1A
=========================================
En lokal Streamlit-app der hjælper dig med at forstå og mestre pensum.

Kør appen med:
    streamlit run app.py
"""

import streamlit as st
import re
import os
import random
from pathlib import Path

# ──────────────────────────────────────────────
# KONFIGURATION
# ──────────────────────────────────────────────

# Mappen hvor dine Markdown-filer ligger.
# Ændr denne sti, hvis dine filer ligger et andet sted.
DATA_DIR = Path("data")

# Ugenumre og deres emner (fra intro.md)
UGER = {
    1:  "Udsagnslogik",
    2:  "Mængder og funktioner",
    3:  "Komplekse tal",
    4:  "Komplekse tal og polynomier",
    5:  "Polynomier og induktion",
    6:  "Lineære ligningssystemer og Gauss elimination",
    7:  "Matrixalgebra og determinanter",
    8:  "Udspænding, ordnet basis og koordinater",
    9:  "Generelle vektorrum",
    10: "Lineære afbildninger",
    11: "Egenværdiproblemet og diagonalisering",
    12: "Differentialligninger og differentialligningssystemer",
    13: "Andenordens differentialligninger",
}

# Kompendium-mappen
KOMPENDIUM_DIR = Path("kompendium")

# Kompendium-filer pr. uge
KOMPENDIUM_FILER = {
    1:  "uge01_udsagnslogik.md",
    2:  "uge02_maengder_funktioner.md",
    3:  "uge03_komplekse_tal.md",
    4:  "uge04_polar_form_polynomier.md",
    5:  "uge05_polynomier_induktion.md",
    6:  "uge06_lineaere_systemer.md",
    7:  "uge07_matrixalgebra_determinanter.md",
    8:  "uge08_udspaending_basis.md",
    9:  "uge09_generelle_vektorrum.md",
    10: "uge10_lineaere_afbildninger.md",
    11: "uge11_egenvaerdier.md",
    12: "uge12_differentialligninger.md",
    13: "uge13_andenordens_ode.md",
}

# ──────────────────────────────────────────────
# HJÆLPEFUNKTIONER TIL FILINDLÆSNING
# ──────────────────────────────────────────────

def læs_fil(filnavn: str) -> str | None:
    """Læser en fil fra DATA_DIR. Returnerer None hvis filen ikke findes."""
    sti = DATA_DIR / filnavn
    if sti.exists():
        return sti.read_text(encoding="utf-8")
    return None


def fjern_jupytext_header(tekst: str) -> str:
    """Fjerner jupytext YAML-headeren fra MyST markdown-filer."""
    # Headeren starter og slutter med ---
    match = re.match(r"^---\n.*?\n---\n", tekst, re.DOTALL)
    if match:
        return tekst[match.end():]
    return tekst


def fjern_myst_tags(tekst: str) -> str:
    """Fjerner MyST-specifikke tags som (section:...), +++ og kommentarer."""
    # Fjern section labels
    tekst = re.sub(r"\(section:\w+\)=\n?", "", tekst)
    # Fjern +++ separatorer
    tekst = re.sub(r"^\+\+\+\s*$", "", tekst, flags=re.MULTILINE)
    # Fjern ---- separatorer
    tekst = re.sub(r"^-{3,}\s*$", "", tekst, flags=re.MULTILINE)
    # Fjern linjer der starter med % (MyST kommentarer)
    tekst = re.sub(r"^%.*$", "", tekst, flags=re.MULTILINE)
    # Fjern asset-links
    tekst = re.sub(r"\{asset\}`\[(.+?)\]\s*<.+?>`", r"\1", tekst)
    # Fjern tomme linjer i starten
    tekst = tekst.lstrip("\n")
    return tekst


# ──────────────────────────────────────────────
# PARSING AF UGEOVERSIGTER
# ──────────────────────────────────────────────

def parse_ugeoversigt(uge_nr: int) -> dict:
    """Parser en Uge*.md fil og returnerer strukturerede data."""
    indhold = læs_fil(f"Uge{uge_nr}.md")
    if not indhold:
        return {
            "emne": UGER.get(uge_nr, "Ukendt emne"),
            "beskrivelse": "",
            "nøglebegreber": "",
            "pensum": "",
        }

    indhold = fjern_jupytext_header(indhold)
    indhold = fjern_myst_tags(indhold)

    # Find nøglebegreber
    nøgle_match = re.search(
        r"##\s*Ugens nøglebegreber\s*\n(.*?)(?=\n##|\Z)",
        indhold, re.DOTALL
    )
    nøglebegreber = nøgle_match.group(1).strip() if nøgle_match else ""

    # Find pensum
    pensum_match = re.search(
        r"##\s*Forberedelse og pensum\s*\n(.*?)(?=\n##|\Z)",
        indhold, re.DOTALL
    )
    pensum = pensum_match.group(1).strip() if pensum_match else ""

    # Find beskrivelse (tekst mellem første ## og næste ##)
    beskrivelse = ""
    sektioner = re.split(r"\n##\s", indhold)
    if len(sektioner) > 1:
        # Første sektion efter overskriften
        første = sektioner[1] if len(sektioner) > 1 else ""
        # Tag kun teksten, ikke overskriften
        linjer = første.split("\n", 1)
        if len(linjer) > 1:
            beskrivelse = linjer[1].strip()

    return {
        "emne": UGER.get(uge_nr, "Ukendt emne"),
        "beskrivelse": beskrivelse,
        "nøglebegreber": nøglebegreber,
        "pensum": pensum,
    }


# ──────────────────────────────────────────────
# PARSING AF OPGAVEFILER
# ──────────────────────────────────────────────

def udtræk_blokke(tekst: str, bloktype: str) -> list[str]:
    """
    Udtrækker indholdet af MyST directive-blokke.
    bloktype er f.eks. 'hint' eller 'admonition'.
    """
    blokke = []
    # Match ```{bloktype} ... ``` (med mulige argumenter)
    pattern = re.compile(
        r"```\{" + bloktype + r"[^}]*\}[^\n]*\n"
        r"(?::class:\s*\w+\s*\n)?"
        r"(.*?)"
        r"\n```",
        re.DOTALL
    )
    for match in pattern.finditer(tekst):
        blokke.append(match.group(1).strip())
    return blokke


def parse_opgavefil(filnavn: str) -> list[dict]:
    """
    Parser en opgavefil (SD/LD) og returnerer en liste af opgaver.
    Hver opgave har: titel, spørgsmål (med tekst, hints, svar).
    """
    indhold = læs_fil(filnavn)
    if not indhold:
        return []

    indhold = fjern_jupytext_header(indhold)
    indhold = fjern_myst_tags(indhold)

    opgaver = []

    # Split på opgave-overskrifter (## Opgave eller ### Opgave)
    opgave_splits = re.split(r"\n(?=#{2,3}\s+Opgave\s+\d+)", indhold)

    for del_tekst in opgave_splits:
        # Find opgavetitel
        titel_match = re.match(r"#{2,3}\s+(Opgave\s+\d+[^#\n]*)", del_tekst)
        if not titel_match:
            continue

        opgave_titel = titel_match.group(1).strip().rstrip(":")
        opgave_tekst_efter_titel = del_tekst[titel_match.end():]

        # Hent eventuel intro-tekst til opgaven (tekst før første spørgsmål)
        intro_match = re.match(
            r"(.*?)(?=#{3,4}\s+Spørgsmål|\Z)",
            opgave_tekst_efter_titel,
            re.DOTALL
        )
        opgave_intro = intro_match.group(1).strip() if intro_match else ""

        # Split på spørgsmål
        spørgsmål_splits = re.split(
            r"\n(?=#{3,4}\s+Spørgsmål\s+\w+)", opgave_tekst_efter_titel
        )

        spørgsmål_liste = []
        for sp_tekst in spørgsmål_splits:
            sp_match = re.match(r"#{3,4}\s+(Spørgsmål\s+\w+)", sp_tekst)
            if not sp_match:
                continue

            sp_titel = sp_match.group(1).strip()
            sp_indhold = sp_tekst[sp_match.end():]

            # Udtræk hints og svar fra dette spørgsmål
            hints = udtræk_blokke(sp_indhold, "hint")
            svar = udtræk_blokke(sp_indhold, "admonition")

            # Fjern hint/svar-blokkene for at få selve spørgsmålsteksten
            ren_tekst = re.sub(
                r"```\{(hint|admonition)[^}]*\}[^\n]*\n.*?```",
                "", sp_indhold, flags=re.DOTALL
            ).strip()

            spørgsmål_liste.append({
                "titel": sp_titel,
                "tekst": ren_tekst,
                "hints": hints,
                "svar": svar,
            })

        # Hvis der ingen spørgsmål er, behandl hele opgaven som ét spørgsmål
        if not spørgsmål_liste and opgave_intro:
            hints = udtræk_blokke(opgave_tekst_efter_titel, "hint")
            svar = udtræk_blokke(opgave_tekst_efter_titel, "admonition")
            ren_intro = re.sub(
                r"```\{(hint|admonition)[^}]*\}[^\n]*\n.*?```",
                "", opgave_intro, flags=re.DOTALL
            ).strip()
            spørgsmål_liste.append({
                "titel": "Spørgsmål",
                "tekst": ren_intro,
                "hints": hints,
                "svar": svar,
            })

        opgaver.append({
            "titel": opgave_titel,
            "intro": opgave_intro,
            "spørgsmål": spørgsmål_liste,
        })

    return opgaver


def hent_alle_opgaver(uge_nr: int) -> dict:
    """Henter opgaver for både Store Dag og Lille Dag."""
    return {
        "Store Dag": parse_opgavefil(f"Uge{uge_nr}SD.md"),
        "Lille Dag": parse_opgavefil(f"Uge{uge_nr}LD.md"),
    }


# ──────────────────────────────────────────────
# BEGREBSINDEKS
# ──────────────────────────────────────────────

def byg_begrebsindeks() -> dict[str, list[int]]:
    """
    Bygger et indeks: begreb -> [ugenumre].
    Baseret på 'Ugens nøglebegreber' fra ugeoversigterne.
    """
    indeks = {}
    for uge_nr in UGER:
        oversigt = parse_ugeoversigt(uge_nr)
        nøgle = oversigt["nøglebegreber"]
        if not nøgle:
            continue
        # Split på komma, punktum og "og"
        begreber = re.split(r"[,.]|\bog\b", nøgle)
        for begreb in begreber:
            begreb = begreb.strip().strip(".")
            if len(begreb) > 2:  # Ignorer meget korte fragmenter
                begreb_lower = begreb.lower()
                if begreb_lower not in indeks:
                    indeks[begreb_lower] = {"visningsnavn": begreb, "uger": []}
                indeks[begreb_lower]["uger"].append(uge_nr)
    return indeks


# ──────────────────────────────────────────────
# STREAMLIT UI
# ──────────────────────────────────────────────

def setup_side():
    """Konfigurerer Streamlit-siden."""
    st.set_page_config(
        page_title="Mat1A Studieassistent",
        page_icon="📐",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Lidt tilpasset styling
    st.markdown("""
    <style>
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    .hint-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 4px;
        margin: 0.5rem 0;
    }
    .answer-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 4px;
        margin: 0.5rem 0;
    }
    .concept-tag {
        display: inline-block;
        background-color: #e3f2fd;
        color: #1565c0;
        padding: 0.25rem 0.75rem;
        border-radius: 16px;
        margin: 0.25rem;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)


def vis_sidebar() -> tuple[str, int | None]:
    """Viser sidebar med navigation. Returnerer (valgt_tilstand, valgt_uge)."""
    with st.sidebar:
        st.title("📐 Mat1A")
        st.caption("Din studieassistent til DTU Matematik 1A")
        st.divider()

        tilstand = st.radio(
            "Vælg tilstand:",
            ["📚 Kompendium", "📖 Forelæsning", "✏️ Opgavetutor", "🧠 Quiz", "🔍 Begrebsopslag"],
            index=0,
        )

        valgt_uge = None
        if tilstand in ["📚 Kompendium", "📖 Forelæsning", "✏️ Opgavetutor", "🧠 Quiz"]:
            st.divider()
            if tilstand == "🧠 Quiz":
                valgt_uge = None  # Quiz bruger sit eget valg
            else:
                valgt_uge = st.selectbox(
                    "Vælg uge:",
                    options=list(UGER.keys()),
                    format_func=lambda u: f"Uge {u}: {UGER[u]}",
                )

        st.divider()
        st.markdown(
            "**Tip:** Brug denne app som supplement til "
            "lærebogen – ikke som erstatning! 📚"
        )

    return tilstand, valgt_uge


# ──────────────────────────────────────────────
# SIDE: KOMPENDIUM
# ──────────────────────────────────────────────

def vis_kompendium(uge_nr: int):
    """Viser kompendiet for en given uge med navigation mellem sektioner."""
    oversigt = parse_ugeoversigt(uge_nr)

    st.header(f"📚 Kompendium – Uge {uge_nr}: {oversigt['emne']}")

    # Læs kompendium-fil
    kompendium_fil = KOMPENDIUM_FILER.get(uge_nr)
    if not kompendium_fil:
        st.warning(f"Intet kompendium tilgængeligt for uge {uge_nr}.")
        return

    sti = KOMPENDIUM_DIR / kompendium_fil
    if not sti.exists():
        st.warning(
            f"Kompendium-filen `{kompendium_fil}` blev ikke fundet i "
            f"`{KOMPENDIUM_DIR}/`. Tjek at filen er kopieret korrekt."
        )
        return

    indhold = sti.read_text(encoding="utf-8")

    # Parse sektioner (split på ## overskrifter)
    sektioner = re.split(r"\n(?=## )", indhold)

    # Første sektion er titlen (# overskrift) – vis altid
    titel_sektion = sektioner[0] if sektioner else ""

    # Fjern titel-overskriften (vi har vores egen header)
    titel_sektion = re.sub(r"^#\s+.*\n", "", titel_sektion).strip()

    # Resterende sektioner
    emne_sektioner = sektioner[1:] if len(sektioner) > 1 else []

    # Byg navigation
    emne_titler = []
    for sek in emne_sektioner:
        match = re.match(r"##\s+(.+)", sek)
        if match:
            emne_titler.append(match.group(1).strip())
        else:
            emne_titler.append("Ukendt afsnit")

    if not emne_titler:
        # Ingen sektioner – vis alt
        st.markdown(indhold)
        return

    # Pensum-info
    if oversigt["pensum"]:
        st.info(f"📖 **Pensum:** {oversigt['pensum']}")

    # Vis indholdsfortegnelse
    st.markdown("### 📋 Indholdsfortegnelse")
    for i, titel in enumerate(emne_titler, 1):
        st.markdown(f"{i}. {titel}")

    st.divider()

    # Vis-tilstand: Alt på én gang eller sektion for sektion
    vis_alt = st.toggle("Vis alt på én gang", value=False)

    if vis_alt:
        for sek in emne_sektioner:
            st.markdown(sek)
            st.divider()
    else:
        # Vis én sektion ad gangen
        valgt_sektion = st.selectbox(
            "Vælg afsnit:",
            range(len(emne_titler)),
            format_func=lambda i: f"{i+1}. {emne_titler[i]}",
        )

        st.markdown(emne_sektioner[valgt_sektion])

        # Navigation
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if valgt_sektion > 0:
                if st.button(f"⬅️ {emne_titler[valgt_sektion - 1][:25]}..."):
                    st.session_state["_nav"] = valgt_sektion - 1
                    st.rerun()
        with col3:
            if valgt_sektion < len(emne_titler) - 1:
                if st.button(f"➡️ {emne_titler[valgt_sektion + 1][:25]}..."):
                    st.session_state["_nav"] = valgt_sektion + 1
                    st.rerun()

    # Tip i bunden
    st.divider()
    st.success(
        "💡 **Tip:** Når du har læst kompendiet, skift til **✏️ Opgavetutor** "
        "og prøv at løse opgaverne for denne uge!"
    )


# ──────────────────────────────────────────────
# SIDE: FORELÆSNING
# ──────────────────────────────────────────────

def vis_forelæsning(uge_nr: int):
    """Viser forelæsningstilstand for en given uge."""
    oversigt = parse_ugeoversigt(uge_nr)

    st.header(f"📖 Uge {uge_nr}: {oversigt['emne']}")

    # Trin 1: Introduktion
    st.subheader("1️⃣ Hvad handler denne uge om?")
    if oversigt["beskrivelse"]:
        st.markdown(oversigt["beskrivelse"])
    else:
        st.info(f"Emnet er **{oversigt['emne']}**.")

    # Trin 2: Nøglebegreber
    st.subheader("2️⃣ Ugens nøglebegreber")
    if oversigt["nøglebegreber"]:
        st.markdown(oversigt["nøglebegreber"])
        st.markdown("---")
        st.markdown(
            "💡 *Prøv at forklare hvert begreb med dine egne ord, "
            "inden du går videre til opgaverne.*"
        )
    else:
        st.warning("Ingen nøglebegreber fundet for denne uge.")

    # Trin 3: Pensum
    st.subheader("3️⃣ Forberedelse og pensum")
    if oversigt["pensum"]:
        st.markdown(oversigt["pensum"])
    else:
        st.info("Ingen pensuminfo fundet for denne uge.")

    # Trin 4: Selvtest
    st.subheader("4️⃣ Test dig selv")
    st.markdown(
        "Inden du går i gang med opgaverne, prøv at besvare disse spørgsmål "
        "for dig selv:"
    )

    if oversigt["nøglebegreber"]:
        begreber = re.split(r"[,.]|\bog\b", oversigt["nøglebegreber"])
        begreber = [b.strip() for b in begreber if len(b.strip()) > 2]
        for i, begreb in enumerate(begreber[:5], 1):
            st.markdown(f"- Kan du forklare, hvad **{begreb}** betyder?")

    st.markdown("")
    st.success(
        "Når du føler dig klar, skift til **✏️ Opgavetutor** i sidebaren "
        "og begynd at løse opgaverne!"
    )


# ──────────────────────────────────────────────
# SIDE: OPGAVETUTOR
# ──────────────────────────────────────────────

def vis_opgavetutor(uge_nr: int):
    """Viser opgavetutoren for en given uge."""
    st.header(f"✏️ Opgavetutor – Uge {uge_nr}: {UGER.get(uge_nr, '')}")

    alle_opgaver = hent_alle_opgaver(uge_nr)

    # Vælg dag
    tilgængelige_dage = [
        dag for dag, opg in alle_opgaver.items() if len(opg) > 0
    ]

    if not tilgængelige_dage:
        st.warning(f"Ingen opgavefiler fundet for uge {uge_nr}. "
                   f"Tjek at filerne ligger i mappen `{DATA_DIR}/`.")
        return

    valgt_dag = st.radio(
        "Vælg dag:", tilgængelige_dage, horizontal=True
    )

    opgaver = alle_opgaver[valgt_dag]

    if not opgaver:
        st.info(f"Ingen opgaver fundet for {valgt_dag}.")
        return

    # Vælg opgave
    opgave_titler = [o["titel"] for o in opgaver]
    valgt_idx = st.selectbox(
        "Vælg opgave:",
        range(len(opgave_titler)),
        format_func=lambda i: opgave_titler[i],
    )

    opgave = opgaver[valgt_idx]
    st.divider()

    # Vis opgavens intro
    st.subheader(opgave["titel"])
    if opgave["intro"]:
        st.markdown(opgave["intro"])

    # Vis spørgsmål med progressiv afsløring
    for sp_idx, sp in enumerate(opgave["spørgsmål"]):
        st.markdown(f"#### {sp['titel']}")

        if sp["tekst"]:
            st.markdown(sp["tekst"])

        # Progressiv afsløring: Tænk → Hints → Svar
        col1, col2, col3 = st.columns(3)

        # Unik nøgle til session state
        nøgle = f"uge{uge_nr}_{valgt_dag}_{valgt_idx}_{sp_idx}"

        # Step 1: Tænk selv
        st.markdown(
            "🤔 *Prøv selv at løse spørgsmålet, før du kigger på hints!*"
        )

        # Step 2: Hints
        for h_idx, hint in enumerate(sp["hints"]):
            with st.expander(f"💡 Hint {h_idx + 1}", expanded=False):
                st.markdown(hint)

        # Step 3: Svar
        if sp["svar"]:
            with st.expander("✅ Vis svar", expanded=False):
                for svar in sp["svar"]:
                    st.markdown(svar)

                st.markdown("---")
                st.markdown(
                    "*Forstod du svaret? Hvis ikke, prøv at genlæse "
                    "den relevante del af lærebogen og forsøg igen.*"
                )

        st.markdown("---")


# ──────────────────────────────────────────────
# SIDE: QUIZ
# ──────────────────────────────────────────────

def vis_quiz():
    """Viser quiz-tilstanden."""
    st.header("🧠 Quiz – Test din viden!")
    st.markdown(
        "Vælg hvilke uger du vil testes i, og prøv at besvare "
        "spørgsmålene uden at kigge i bogen."
    )

    # Vælg uger
    valgte_uger = st.multiselect(
        "Vælg uger at inkludere:",
        options=list(UGER.keys()),
        default=[1],
        format_func=lambda u: f"Uge {u}: {UGER[u]}",
    )

    if not valgte_uger:
        st.info("Vælg mindst én uge for at starte quizzen.")
        return

    antal = st.slider("Antal spørgsmål:", min_value=1, max_value=20, value=5)

    # Saml alle spørgsmål fra valgte uger
    alle_sp = []
    for uge_nr in valgte_uger:
        for dag_navn, opgaver in hent_alle_opgaver(uge_nr).items():
            for opgave in opgaver:
                for sp in opgave["spørgsmål"]:
                    if sp["tekst"] and sp["svar"]:
                        alle_sp.append({
                            "uge": uge_nr,
                            "dag": dag_navn,
                            "opgave": opgave["titel"],
                            "intro": opgave["intro"],
                            "spørgsmål": sp,
                        })

    if not alle_sp:
        st.warning("Ingen spørgsmål med svar fundet for de valgte uger.")
        return

    # Generer quiz med session state
    if st.button("🎲 Generer ny quiz", type="primary"):
        udvalgte = random.sample(alle_sp, min(antal, len(alle_sp)))
        st.session_state["quiz_spørgsmål"] = udvalgte
        st.session_state["quiz_score"] = {}

    if "quiz_spørgsmål" not in st.session_state:
        st.info("Tryk på knappen ovenfor for at starte en quiz!")
        return

    quiz = st.session_state["quiz_spørgsmål"]

    st.divider()
    st.markdown(f"**Quiz: {len(quiz)} spørgsmål**")

    for i, item in enumerate(quiz):
        sp = item["spørgsmål"]

        st.markdown(f"### Spørgsmål {i + 1}")
        st.caption(f"Uge {item['uge']} – {item['dag']} – {item['opgave']}")

        if item["intro"]:
            st.markdown(item["intro"])

        st.markdown(sp["tekst"])

        # Svar-afsløring
        with st.expander("🔓 Vis svar", expanded=False):
            for svar in sp["svar"]:
                st.markdown(svar)

            # Selvvurdering
            score_key = f"quiz_score_{i}"
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Jeg havde ret", key=f"ret_{i}"):
                    st.session_state["quiz_score"][i] = True
            with col2:
                if st.button("❌ Jeg havde forkert", key=f"forkert_{i}"):
                    st.session_state["quiz_score"][i] = False

        st.markdown("---")

    # Vis score
    score = st.session_state.get("quiz_score", {})
    if score:
        rigtige = sum(1 for v in score.values() if v)
        total = len(score)
        st.divider()
        st.subheader("📊 Din score")
        st.metric("Rigtige svar", f"{rigtige}/{total}")
        if rigtige == total and total == len(quiz):
            st.balloons()
            st.success("Perfekt score! Du mestrer stoffet! 🎉")
        elif rigtige / max(total, 1) >= 0.7:
            st.success("Godt klaret! Fortsæt det gode arbejde! 💪")
        else:
            st.info(
                "Bliv ikke modløs – gå tilbage til forelæsningstilstanden "
                "og genopfrisk de emner, du havde svært ved."
            )


# ──────────────────────────────────────────────
# SIDE: BEGREBSOPSLAG
# ──────────────────────────────────────────────

def vis_begrebsopslag():
    """Viser begrebsopslagets søgefunktion."""
    st.header("🔍 Begrebsopslag")
    st.markdown(
        "Søg efter et begreb for at finde ud af, hvilken uge det hører til, "
        "og se de tilhørende nøglebegreber."
    )

    indeks = byg_begrebsindeks()

    søgning = st.text_input(
        "Søg efter et begreb:",
        placeholder="f.eks. egenværdi, komplekse tal, matrix..."
    )

    if søgning:
        søgning_lower = søgning.lower()
        resultater = []
        for begreb_lower, info in indeks.items():
            if søgning_lower in begreb_lower or begreb_lower in søgning_lower:
                resultater.append(info)

        if resultater:
            st.success(f"Fandt {len(resultater)} resultat(er):")
            for res in resultater:
                for uge_nr in res["uger"]:
                    oversigt = parse_ugeoversigt(uge_nr)
                    st.markdown(f"### Uge {uge_nr}: {oversigt['emne']}")
                    st.markdown(f"**Begreb:** {res['visningsnavn']}")
                    if oversigt["nøglebegreber"]:
                        st.markdown(
                            f"**Alle nøglebegreber for ugen:** "
                            f"{oversigt['nøglebegreber']}"
                        )
                    if oversigt["pensum"]:
                        st.markdown(f"**Pensum:** {oversigt['pensum']}")
                    st.divider()
        else:
            st.warning(
                f"Ingen resultater for \"{søgning}\". "
                f"Prøv et andet søgeord."
            )
    else:
        # Vis alle begreber som overblik
        st.subheader("📋 Alle nøglebegreber pr. uge")
        for uge_nr in sorted(UGER.keys()):
            oversigt = parse_ugeoversigt(uge_nr)
            if oversigt["nøglebegreber"]:
                with st.expander(
                    f"Uge {uge_nr}: {oversigt['emne']}", expanded=False
                ):
                    st.markdown(oversigt["nøglebegreber"])
                    if oversigt["pensum"]:
                        st.caption(f"Pensum: {oversigt['pensum']}")


# ──────────────────────────────────────────────
# HOVEDPROGRAM
# ──────────────────────────────────────────────

def main():
    setup_side()

    # Tjek om data-mappen findes
    if not DATA_DIR.exists():
        st.error(
            f"⚠️ Mappen `{DATA_DIR}/` blev ikke fundet!\n\n"
            f"Opret mappen og kopier dine Markdown-filer ind i den.\n\n"
            f"Se README.md for instruktioner."
        )
        st.stop()

    # Tjek om der er filer
    md_filer = list(DATA_DIR.glob("*.md"))
    if not md_filer:
        st.error(
            f"⚠️ Ingen .md-filer fundet i `{DATA_DIR}/`.\n\n"
            f"Kopier dine Uge*.md filer ind i mappen."
        )
        st.stop()

    tilstand, valgt_uge = vis_sidebar()

    if tilstand == "📚 Kompendium":
        vis_kompendium(valgt_uge)
    elif tilstand == "📖 Forelæsning":
        vis_forelæsning(valgt_uge)
    elif tilstand == "✏️ Opgavetutor":
        vis_opgavetutor(valgt_uge)
    elif tilstand == "🧠 Quiz":
        vis_quiz()
    elif tilstand == "🔍 Begrebsopslag":
        vis_begrebsopslag()


if __name__ == "__main__":
    main()
