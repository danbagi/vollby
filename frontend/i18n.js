// i18n.js — Internationalization for WOLL.BY (SK / EN)
(function () {
  const TRANSLATIONS = {
    sk: {
      // ── Navigation ──────────────────────────────────────────────
      'nav.overview':     'Prehľad',
      'nav.model':        'Model',
      'nav.methodology':  'Metodológia',

      // ── Common ──────────────────────────────────────────────────
      'filter.all':          'Všetko',
      'filter.agency.all':   'Všetky',
      'footer.source':       'Zdroj dát',
      'status.loading':      'NAČÍTAVAM...',
      'status.error':        'CHYBA: Backend nedostupný — spustite server',
      'data.journalism':     'DATA JOURNALISM',

      // ── index.html hero ─────────────────────────────────────────
      'index.hero.subtitle':    'Vývoj volebných preferencií SR',
      'index.hero.h1':          'VOLEBNÉ<br/>PREFERENCIE',
      'index.hero.lastLabel':   'Posledný prieskum',

      // ── index.html — Trend ──────────────────────────────────────
      'index.trend.title':  'Trend vývoja',
      'index.trend.source': 'Zdroj: AKO / Focus / Ipsos / NMS · Wikipedia',

      // ── index.html — Aktuálny odhad ─────────────────────────────
      'index.estimate.title': 'Aktuálny odhad',
      'index.estimate.last':  'Posledných',
      'index.estimate.polls': 'prieskumov',

      // ── index.html — Prepočet na sedadlá ────────────────────────
      'index.seats.subtitle':    'Projekcia mandátov NRSR',
      'index.seats.title':       'Prepočet na sedadlá',
      'index.seats.method':      'Hagenbach-Bischoff',
      'index.seats.hemi.title':  'Rozdelenie pléna',
      'index.seats.hemi.dot':    '1 bod = 1 poslanec',
      'index.seats.bars.title':  'Distribúcia strán',
      'index.seats.majority76':  '76 MAJORITA',
      'index.seats.loading.svg': 'NAČÍTAVAM...',

      // ── index.html — Majority info (dynamic) ────────────────────
      'majority.gov':       'Vládna:',
      'majority.opp':       'Opozícia:',
      'majority.threshold': 'Väčšina:',
      'majority.has':       '✓ VÄČŠINA',
      'majority.no':        '✗ BEZ VÄČŠINY',

      // ── index.html — Coalition builder ──────────────────────────
      'index.coalition.subtitle': 'Interaktívny kalkulátor',
      'index.coalition.title':    'Koaličná skladba',
      'index.coalition.reset':    '↺ Resetovať',
      'index.coalition.govBar':   'Vládna koalícia',
      'index.coalition.oppBar':   'Opozícia',
      'index.coalition.govZone':  'Vládna koalícia',
      'index.coalition.neutral':  'Nezaradené',
      'index.coalition.oppZone':  'Opozícia',
      'index.coalition.dragHint': 'Preneste strany sem',

      // ── Coalition builder totals (dynamic) ──────────────────────
      'coalition.hasMaj':       '✓ MÁ VÄČŠINU',
      'coalition.noMaj.prefix': '✗ CHÝBA',
      'coalition.noMaj.suffix': 'KRESIEL',

      // ── index.html — Raw Data Ledger ────────────────────────────
      'rawdata.title':   'Raw Data Ledger',
      'table.agency':    'Agentúra',
      'table.date':      'Dátum',

      // ── index.html — Median cards (dynamic) ─────────────────────
      'threshold.above': '▲ NAD PRAHOM',
      'threshold.below': '▼ POD PRAHOM',

      // ── model.html ──────────────────────────────────────────────
      'model.hero.subtitle':      'Volebná predikcia SR 2027',
      'model.hero.h1':            'PREDIKČNÝ<br/>MODEL',
      'model.sidebar.title':      'STRANY:<br/>OČAKÁVANÝ ZISK',
      'model.sidebar.seats':      'Kresiel:',
      'model.sidebar.threshold':  'Prah: 5.0%',
      'model.sidebar.rangeUnit':  'kr.',

      // ── model.html — Simulation distribution ────────────────────
      'model.sim.title':    'DISTRIBÚCIA SIMULÁCIÍ',
      'model.sim.subtitle': '10 000 Monte Carlo simulácií · zvislá čiara = stredná hodnota',
      'model.sim.show':     'Zobraziť:',
      'model.sim.seats':    'KRESIEL',
      'model.sim.sims':     'SIMULÁCIÍ',

      // ── model.html — Modelová logika ────────────────────────────
      'model.logic.label':     'MODELOVÁ LOGIKA:',
      'model.logic.sims':      '10 000 simulácií',
      'model.logic.weighting': 'váhovanie podľa mesiaca',
      'model.logic.house':     'house effect 2023',
      'model.logic.link':      'METODOLÓGIA',

      // ── model.html — Coalition calculator ───────────────────────
      'model.calc.title':    'KOALIČNÁ KALKULAČKA',
      'model.calc.subtitle': 'Zaškrtni strany · prepočet z 10 000 simulácií',
      'model.calc.seatsLbl': 'Suma mandátov',
      'model.calc.total':    '/ 150',
      'model.calc.probLbl':  'Pravdepodobnosť väčšiny',
      'model.calc.maj':      '✓ VÄČŠINA',
      'model.calc.min':      '✗ MENŠINOVÁ',

      // ── metodologia.html ────────────────────────────────────────
      'met.hero.subtitle': 'Dokumentácia predikčného modelu',
      'met.hero.h1':       'METODOLÓGIA',
      'met.hero.desc':     'Ako funguje predikčný model woll.by',

      'met.01.num':      '01',
      'met.01.title':    'ZDROJE<br/>DÁT',
      'met.01.agencies': 'Ipsos · AKO · Focus · NMS',
      'met.01.p1':       'woll.by agreguje verejne dostupné prieskumy volebných preferencií zo stránky Wikipedia – Opinion polling for the next Slovak parliamentary election. Dáta zahŕňajú prieskumy agentúr Ipsos, AKO, Focus a NMS od roku 2023 po súčasnosť.',
      'met.01.p2':       'Prieskumy sú aktualizované manuálne po zverejnení nových výsledkov. Každý prieskum obsahuje: agentúru, klienta, dátum zberu dát a percentuálne preferencie pre sledované strany.',

      'met.02.num':        '02',
      'met.02.title':      'HOUSE<br/>EFFECT',
      'met.02.subtitle':   'Korekcia systematického biasu agentúr',
      'met.02.p1':         'Rôzne agentúry systematicky nadhodnocujú alebo podhodnocujú určité strany. Model aplikuje korekčné koeficienty aby znížil tento bias. Koeficienty boli kalibrované porovnaním posledných predvolebných prieskumov každej agentúry s oficiálnymi výsledkami parlamentných volieb zo 30. septembra 2023.',
      'met.02.th.agency':  'Agentúra',
      'met.02.th.coef':    'Koeficient',
      'met.02.th.mae':     'MAE 2023',
      'met.02.th.note':    'Poznámka',
      'met.02.ako.note':   'referenčná agentúra (najpresnejšia)',
      'met.02.focus.note': 'mierne podhodnocuje',
      'met.02.ipsos.note': 'mierne podhodnocuje',
      'met.02.nms.note':   'väčšia systematická chyba',
      'met.02.footnote':   'MAE = priemerná absolútna chyba oproti výsledku volieb 2023. Koeficient upravuje celkovú váhu prieskumu agentúry v agregáte — nie individuálne hodnoty strán. Kalibrácia vychádza z jediných volieb (2023), čo je štatisticky obmedzená vzorka. Koeficienty budú spresnené po ďalších voľbách.',

      'met.03.num':       '03',
      'met.03.title':     'VÁHOVANIE<br/>PRIESKUMOV',
      'met.03.subtitle':  'Mesačné váhovanie',
      'met.03.p1':        'Agentúry vydávajú prieskumy spravidla raz mesačne. Model preto váhuje prieskumy podľa kalendárneho mesiaca — nie podľa presného počtu dní. Prieskumy z rovnakého mesiaca majú rovnakú váhu bez ohľadu na to, či boli zverejnené na začiatku alebo konci mesiaca.',
      'met.03.th.month':  'Mesiac',
      'met.03.th.weight': 'Váha',
      'met.03.m0':        'Aktuálny',
      'met.03.m1':        'Pred 1 mes.',
      'met.03.m2':        'Pred 2 mes.',
      'met.03.m3':        'Pred 3 mes.',
      'met.03.mOld':      'Staršie',
      'met.03.footnote':  'Prieskumy staršie ako 3 mesiace sú zahrnuté s váhou 0.10 — prispievajú minimálne ale stabilizujú agregát v obdobiach keď je dostupných menej prieskumov. Výsledná váha každého prieskumu je súčin mesačnej váhy a house effect koeficientu príslušnej agentúry.',

      'met.04.num':          '04',
      'met.04.title':        'MONTE<br/>CARLO',
      'met.04.simLabel':     'Simulácií',
      'met.04.p1':           'Predikčný model spúšťa 10 000 simulácií volebného výsledku. V každej simulácii je vážený agregát narušený náhodným šumom ktorý modeluje prieskumnú nepresnosť a volatilitu voličov.',
      'met.04.p2':           'Na rozdiel od jednoduchých modelov, šum nie je rovnaký pre všetky strany — väčšie strany majú väčšiu absolútnu neistotu, menšie strany menšiu. Sigma každej strany sa počíta zo štatistickej chyby merania pre vzorku 1000 respondentov, násobenej koeficientom 2 ktorý zachytáva reálnu volatilitu voličov nad rámec čistej štatistickej chyby:',
      'met.04.formula.lbl':  'Formula',
      'met.04.formula.note': 'minimum σ = 0.8 %&nbsp;&nbsp;·&nbsp;&nbsp;p = podiel strany v agregáte',
      'met.04.p3':           'Príklady: strana s 20% má σ ≈ 2.5%, strana s 5% má σ ≈ 1.4%. Koeficient 2 bol zvolený na základe porovnania predvolebných prieskumov s výsledkami volieb 2023, kde priemerná absolútna chyba agentúr bola 1.1–1.7%.',
      'met.04.p4':           'Pre každú simuláciu sa aplikuje 5% parlamentný prah a Hagenbach-Bischoff metóda prepočtu na 150 kresiel. Simulácie bežia priamo v prehliadači v JavaScripte.',
      'met.04.stat1.lbl':    'Adaptívny šum',
      'met.04.stat2.lbl':    'Parlamentný prah',
      'met.04.stat3.lbl':    'Kresiel v parlamente',

      'met.05.num':        '05',
      'met.05.title':      'OBMEDZE\u00adNIA<br/>&amp;<br/>DISCLAIMER',
      'met.05.subtitle':   'Hobby projekt · nie profesionálna predpoveď',
      'met.05.intro':      'woll.by je hobby projekt a nie profesionálna predpoveď. Model má tieto obmedzenia:',
      'met.05.li1':        'Prieskumy nezachytávajú posledné dni kampane',
      'met.05.li2':        'House effect koeficienty sú kalibrované na jediných voľbách (2023) — štatisticky obmedzená vzorka',
      'met.05.li3':        'Model neuvažuje strategické hlasovanie ani transfer hlasov pri stranách pod prahom',
      'met.05.li4':        'Vzorka prieskumov (~1000 respondentov) má inherentnú štatistickú chybu ±3%',
      'met.05.li5':        'Výsledky sú citlivé na aktuálnosť a počet dostupných prieskumov',
      'met.05.disclaimer': 'Tento model neslúži ako návod na hlasovanie.',

      'met.back':       '← Späť na dashboard',
      'met.footerNote': 'woll.by — hobby projekt | dáta: Wikipedia CC BY-SA',
    },

    en: {
      // ── Navigation ──────────────────────────────────────────────
      'nav.overview':     'Overview',
      'nav.model':        'Model',
      'nav.methodology':  'Methodology',

      // ── Common ──────────────────────────────────────────────────
      'filter.all':          'All',
      'filter.agency.all':   'All',
      'footer.source':       'Data source',
      'status.loading':      'LOADING...',
      'status.error':        'ERROR: Backend unavailable — start the server',
      'data.journalism':     'DATA JOURNALISM',

      // ── index.html hero ─────────────────────────────────────────
      'index.hero.subtitle':  'Slovak electoral polling trends',
      'index.hero.h1':        'POLLING<br/>TRACKER',
      'index.hero.lastLabel': 'Latest poll',

      // ── index.html — Trend ──────────────────────────────────────
      'index.trend.title':  'Trend',
      'index.trend.source': 'Source: AKO / Focus / Ipsos / NMS · Wikipedia',

      // ── index.html — Aktuálny odhad ─────────────────────────────
      'index.estimate.title': 'Current estimate',
      'index.estimate.last':  'Last',
      'index.estimate.polls': 'polls',

      // ── index.html — Prepočet na sedadlá ────────────────────────
      'index.seats.subtitle':    'NRSR seat projection',
      'index.seats.title':       'Seat allocation',
      'index.seats.method':      'Hagenbach-Bischoff',
      'index.seats.hemi.title':  'Hemicycle',
      'index.seats.hemi.dot':    '1 dot = 1 MP',
      'index.seats.bars.title':  'Party distribution',
      'index.seats.majority76':  '76 MAJORITY',
      'index.seats.loading.svg': 'LOADING...',

      // ── index.html — Majority info (dynamic) ────────────────────
      'majority.gov':       'Govt:',
      'majority.opp':       'Opposition:',
      'majority.threshold': 'Majority:',
      'majority.has':       '✓ MAJORITY',
      'majority.no':        '✗ NO MAJORITY',

      // ── index.html — Coalition builder ──────────────────────────
      'index.coalition.subtitle': 'Interactive calculator',
      'index.coalition.title':    'Coalition builder',
      'index.coalition.reset':    '↺ Reset',
      'index.coalition.govBar':   'Government',
      'index.coalition.oppBar':   'Opposition',
      'index.coalition.govZone':  'Government',
      'index.coalition.neutral':  'Unassigned',
      'index.coalition.oppZone':  'Opposition',
      'index.coalition.dragHint': 'Drag parties here',

      // ── Coalition builder totals (dynamic) ──────────────────────
      'coalition.hasMaj':       '✓ HAS MAJORITY',
      'coalition.noMaj.prefix': '✗ NEEDS',
      'coalition.noMaj.suffix': 'SEATS',

      // ── index.html — Raw Data Ledger ────────────────────────────
      'rawdata.title': 'Raw Data Ledger',
      'table.agency':  'Agency',
      'table.date':    'Date',

      // ── index.html — Median cards (dynamic) ─────────────────────
      'threshold.above': '▲ ABOVE THRESHOLD',
      'threshold.below': '▼ BELOW THRESHOLD',

      // ── model.html ──────────────────────────────────────────────
      'model.hero.subtitle':      'Slovak electoral prediction 2027',
      'model.hero.h1':            'PREDICTIVE<br/>MODEL',
      'model.sidebar.title':      'PARTIES:<br/>EXPECTED GAIN',
      'model.sidebar.seats':      'Seats:',
      'model.sidebar.threshold':  'Threshold: 5.0%',
      'model.sidebar.rangeUnit':  'seats',

      // ── model.html — Simulation distribution ────────────────────
      'model.sim.title':    'SIMULATION DISTRIBUTION',
      'model.sim.subtitle': '10,000 Monte Carlo simulations · vertical line = median',
      'model.sim.show':     'Show:',
      'model.sim.seats':    'SEATS',
      'model.sim.sims':     'SIMULATIONS',

      // ── model.html — Modelová logika ────────────────────────────
      'model.logic.label':     'MODEL LOGIC:',
      'model.logic.sims':      '10,000 simulations',
      'model.logic.weighting': 'monthly weighting',
      'model.logic.house':     'house effect 2023',
      'model.logic.link':      'METHODOLOGY',

      // ── model.html — Coalition calculator ───────────────────────
      'model.calc.title':    'COALITION CALCULATOR',
      'model.calc.subtitle': 'Select parties · computed from 10,000 simulations',
      'model.calc.seatsLbl': 'Total seats',
      'model.calc.total':    '/ 150',
      'model.calc.probLbl':  'Majority probability',
      'model.calc.maj':      '✓ MAJORITY',
      'model.calc.min':      '✗ MINORITY',

      // ── metodologia.html ────────────────────────────────────────
      'met.hero.subtitle': 'Predictive model documentation',
      'met.hero.h1':       'METHODOLOGY',
      'met.hero.desc':     'How the woll.by predictive model works',

      'met.01.num':      '01',
      'met.01.title':    'DATA<br/>SOURCES',
      'met.01.agencies': 'Ipsos · AKO · Focus · NMS',
      'met.01.p1':       'woll.by aggregates publicly available polling data from Wikipedia – Opinion polling for the next Slovak parliamentary election. Data includes polls from Ipsos, AKO, Focus and NMS from 2023 to the present.',
      'met.01.p2':       'Polls are updated manually after new results are published. Each poll includes: agency, client, data collection date, and percentage preferences for tracked parties.',

      'met.02.num':        '02',
      'met.02.title':      'HOUSE<br/>EFFECT',
      'met.02.subtitle':   'Correction for systematic agency bias',
      'met.02.p1':         'Different polling agencies systematically over- or underestimate certain parties. The model applies correction coefficients to reduce this bias. Coefficients were calibrated by comparing each agency\'s last pre-election polls with the official results of the parliamentary elections on September 30, 2023.',
      'met.02.th.agency':  'Agency',
      'met.02.th.coef':    'Coefficient',
      'met.02.th.mae':     'MAE 2023',
      'met.02.th.note':    'Note',
      'met.02.ako.note':   'reference agency (most accurate)',
      'met.02.focus.note': 'slight underestimation',
      'met.02.ipsos.note': 'slight underestimation',
      'met.02.nms.note':   'larger systematic error',
      'met.02.footnote':   'MAE = mean absolute error vs. 2023 election results. The coefficient adjusts the overall weight of an agency\'s poll in the aggregate — not individual party values. Calibration is based on a single election (2023), which is a statistically limited sample. Coefficients will be refined after further elections.',

      'met.03.num':       '03',
      'met.03.title':     'POLL<br/>WEIGHTING',
      'met.03.subtitle':  'Monthly weighting',
      'met.03.p1':        'Agencies publish polls roughly once a month. The model therefore weights polls by calendar month — not by the exact number of days. Polls from the same month have the same weight regardless of whether they were published at the start or end of the month.',
      'met.03.th.month':  'Month',
      'met.03.th.weight': 'Weight',
      'met.03.m0':        'Current',
      'met.03.m1':        '1 month ago',
      'met.03.m2':        '2 months ago',
      'met.03.m3':        '3 months ago',
      'met.03.mOld':      'Older',
      'met.03.footnote':  'Polls older than 3 months are included with weight 0.10 — they contribute minimally but stabilize the aggregate during periods when fewer polls are available. The final weight of each poll is the product of the monthly weight and the house effect coefficient of the respective agency.',

      'met.04.num':          '04',
      'met.04.title':        'MONTE<br/>CARLO',
      'met.04.simLabel':     'Simulations',
      'met.04.p1':           'The predictive model runs 10,000 simulations of the election result. In each simulation, the weighted aggregate is perturbed by random noise that models polling inaccuracy and voter volatility.',
      'met.04.p2':           'Unlike simple models, the noise is not the same for all parties — larger parties have greater absolute uncertainty, smaller parties less. Each party\'s sigma is calculated from the statistical measurement error for a sample of 1,000 respondents, multiplied by a coefficient of 2 that captures real voter volatility beyond pure statistical error:',
      'met.04.formula.lbl':  'Formula',
      'met.04.formula.note': 'minimum σ = 0.8 %&nbsp;&nbsp;·&nbsp;&nbsp;p = party share in aggregate',
      'met.04.p3':           'Examples: a party at 20% has σ ≈ 2.5%, a party at 5% has σ ≈ 1.4%. The coefficient of 2 was chosen based on comparison of pre-election polls with the 2023 election results, where the average absolute error of agencies was 1.1–1.7%.',
      'met.04.p4':           'For each simulation, the 5% parliamentary threshold and Hagenbach-Bischoff method for converting to 150 seats is applied. Simulations run directly in the browser in JavaScript.',
      'met.04.stat1.lbl':    'Adaptive noise',
      'met.04.stat2.lbl':    'Parliamentary threshold',
      'met.04.stat3.lbl':    'Seats in parliament',

      'met.05.num':        '05',
      'met.05.title':      'LIMITA\u00adTIONS<br/>&amp;<br/>DISCLAIMER',
      'met.05.subtitle':   'Hobby project · not a professional forecast',
      'met.05.intro':      'woll.by is a hobby project and not a professional forecast. The model has these limitations:',
      'met.05.li1':        'Polls do not capture the last days of the campaign',
      'met.05.li2':        'House effect coefficients are calibrated on a single election (2023) — a statistically limited sample',
      'met.05.li3':        'The model does not consider strategic voting or vote transfer from parties below the threshold',
      'met.05.li4':        'The poll sample (~1,000 respondents) has an inherent statistical error of ±3%',
      'met.05.li5':        'Results are sensitive to the timeliness and number of available polls',
      'met.05.disclaimer': 'This model is not intended as voting advice.',

      'met.back':       '← Back to dashboard',
      'met.footerNote': 'woll.by — hobby project | data: Wikipedia CC BY-SA',
    },
  };

  function getCurrentLang() {
    const stored = localStorage.getItem('wollby_lang');
    if (stored === 'sk' || stored === 'en') return stored;
    return (navigator.language || '').toLowerCase().startsWith('sk') ? 'sk' : 'en';
  }

  function T(key) {
    const lang = getCurrentLang();
    return (TRANSLATIONS[lang] && TRANSLATIONS[lang][key] != null)
      ? TRANSLATIONS[lang][key]
      : (TRANSLATIONS.sk[key] != null ? TRANSLATIONS.sk[key] : key);
  }

  function applyLang(lang) {
    document.documentElement.lang = lang;

    // Update all toggle buttons
    document.querySelectorAll('.lang-toggle').forEach(btn => {
      btn.textContent = lang === 'sk' ? 'EN' : 'SK';
    });

    // textContent translations
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const val = TRANSLATIONS[lang]?.[el.dataset.i18n] ?? TRANSLATIONS.sk[el.dataset.i18n];
      if (val != null) el.textContent = val;
    });

    // innerHTML translations (for elements with <br/>, &amp; etc.)
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const val = TRANSLATIONS[lang]?.[el.dataset.i18nHtml] ?? TRANSLATIONS.sk[el.dataset.i18nHtml];
      if (val != null) el.innerHTML = val;
    });
  }

  function setLang(lang) {
    localStorage.setItem('wollby_lang', lang);
    applyLang(lang);
    if (typeof onLangChange === 'function') onLangChange(lang);
  }

  // Expose globally
  window.T = T;
  window.getCurrentLang = getCurrentLang;
  window.applyLang = applyLang;
  window.setLang = setLang;

  // Auto-apply on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', () => applyLang(getCurrentLang()));
})();
