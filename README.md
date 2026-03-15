# 📐 Mat1A Studieassistent

En lokal studieassistent-app til DTU's kursus **Matematik 1A** (01001).

Appen hjælper dig med at forstå og mestre pensum gennem fire tilstande:

- **📖 Forelæsning** – Få overblik over ugens emne, nøglebegreber og pensum
- **✏️ Opgavetutor** – Arbejd med opgaver trin-for-trin med hints og svar gemt bag fold-ud-sektioner
- **🧠 Quiz** – Test dig selv med tilfældige spørgsmål fra udvalgte uger
- **🔍 Begrebsopslag** – Søg efter begreber og find ud af, hvor i kurset de hører til

---

## Opsætning (5 minutter)

### 1. Installer Streamlit

Åbn din terminal (eller kommandoprompt) og kør:

```bash
pip install streamlit
```

### 2. Opret projektmappen

Opret en mappe til appen og en `data/`-undermappe:

```
mat1a-studieassistent/
├── app.py          ← Hovedfilen (denne fil)
├── README.md       ← Denne guide
└── data/           ← Dine kursusfiler
    ├── intro.md
    ├── Uge1.md
    ├── Uge1SD.md
    ├── Uge1LD.md
    ├── Uge2.md
    ├── Uge2SD.md
    ├── Uge2LD.md
    ├── ...osv. for alle uger
    └── Uge13SD.md
```

### 3. Kopiér dine filer

Kopiér alle dine `.md`-filer (Uge1.md, Uge1SD.md, Uge1LD.md osv.) ind i `data/`-mappen.

### 4. Kør appen

Naviger til projektmappen i din terminal og kør:

```bash
cd mat1a-studieassistent
streamlit run app.py
```

Appen åbner automatisk i din browser på adressen `http://localhost:8501`.

---

## Sådan bruger du appen

### 📖 Forelæsningstilstand
Start her! Vælg en uge i sidebaren og læs op på emnet, nøglebegreberne og pensum. Prøv at forklare hvert begreb med dine egne ord, inden du går videre.

### ✏️ Opgavetutor
Vælg en uge og en opgave. Læs spørgsmålet og **prøv selv først!** Brug hints hvis du sidder fast, og kig først på svaret som sidste udvej.

### 🧠 Quiz
Vælg de uger du vil testes i, og sæt antal spørgsmål. Prøv at besvare hvert spørgsmål i hovedet (eller på papir), før du afslører svaret. Vurdér dig selv ærligt!

### 🔍 Begrebsopslag
Søg på et begreb for at finde ud af, hvilken uge det dukker op i, og hvad det tilhørende pensum er.

---

## Fejlfinding

| Problem | Løsning |
|---------|---------|
| `pip install streamlit` fejler | Prøv `pip3 install streamlit` eller `python -m pip install streamlit` |
| Appen viser "Ingen filer fundet" | Tjek at dine `.md`-filer ligger i `data/`-mappen |
| LaTeX vises ikke korrekt | Sørg for at du bruger en nyere version af Streamlit (`pip install --upgrade streamlit`) |
| Appen åbner ikke i browseren | Gå manuelt til `http://localhost:8501` |

---

## Om appen

Denne app er designet som et læringsværktøj – **ikke** som en erstatning for lærebogen eller undervisningen. Den bedste måde at bruge den på er:

1. Læs det relevante kapitel i lærebogen
2. Brug **Forelæsningstilstanden** til at få overblik
3. Løs opgaverne med **Opgavetutoren** (prøv selv først!)
4. Test dig selv med **Quiz-tilstanden** op til eksamen

God fornøjelse med Matematik 1A! 🎓
