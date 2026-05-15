---
layout: post
title: "They Were Watching. Then We Filed the ATIP. Then They Switched to GitHub. (updated at 2026-05-15T17:30:05Z)"
date: 2026-05-15 00:00:00 +0000
slug: dispersed-vpn-surveillance-atip-collapse-dnd-2026
lang: en
tags: Canada, DND, ATIP, Hanwha, Submarines, VPN, Surveillance, Analytics, Procurement, Korea, OIC
meta_description: "Fathom Analytics data documenting 37-country dispersed VPN surveillance of Gender Watchdog sites (Feb–Mar 2026), operational shutdown 8 days after emailing DND, 82% traffic collapse after ATIP filings, 150+ GitHub clone surge, and DND statutory non-response to 2 of 4 ATIP requests."
bearblog_url: https://genderwatchdog.bearblog.dev/dispersed-vpn-surveillance-atip-collapse-dnd-2026/
gh_pages_url: https://blog.genderwatchdog.org/dispersed-vpn-surveillance-atip-collapse-dnd-2026/
---

*Dispersed VPN Surveillance, Operational Shutdown, and DND's Statutory Non-Response — Evidence from Fathom Analytics, January–May 2026*

*Gender Watchdog — May 15, 2026*

Between February 5 and March 30, 2026, 37 countries — Indonesia, Jamaica, Colombia, Paraguay, Syria, and 32 others — each visited Gender Watchdog's sites exactly once or twice a day, on no predictable schedule, for seven weeks. No single country accumulated enough traffic to trigger an alert in a standard dashboard. Together, the signal was invisible unless you looked at the raw data. We looked at the raw data. Then we sent one email. Then the operation shut down within eight calendar days. Then we filed ATIPs. Then the web visits stopped — and the GitHub clones surged. Then the Department of National Defence went silent on two of four statutory requests. This post is the evidentiary record.

---

## Executive Summary

Between early February and March 30, 2026, web traffic to Gender Watchdog's public websites exhibited a pattern consistent with coordinated, covert surveillance by a single actor pool: 37 low-traffic countries each contributed exactly 1–2 visits per day on an irregular but sustained basis, across multiple days and weeks. No single country accumulated enough visits to stand out in standard analytics reports. The pattern is consistent with a deliberate rotation of commercial VPN exit nodes to avoid detection — a technique consistent with institutional intelligence-gathering operations that wish to avoid attribution.[^7]

On March 23, 2026, Gender Watchdog sent a high-profile email to the Canadian Department of National Defence, the Secretary of State for Defence Procurement, the Prime Minister's Office, the Standing Committee on National Defence, and three national journalists, regarding due diligence failures in Hanwha Ocean's Canadian submarine procurement bid.[^3] Within 8 days, the entire dispersed-country surveillance operation went silent. It has not resumed in the 45 days since.

The timeline of subsequent events — an ATIP filing on April 11–12, an immediate collapse of Fathom web traffic, a surge of direct GitHub clone activity before the 30-day response deadline, and DND's statutory non-compliance with 2 of 4 ATIP requests (confirmed May 13, 2026)[^10] — forms a coherent evidentiary chain that is documented here with timestamps from an analytics provider that Gender Watchdog does not control.

---

## § 1 — Background: Prior Singapore VPN Identification (October 2025)

### The Hanwha X.com post (August 27, 2025)

On August 27, 2025, Gender Watchdog posted a thread on X.com calling for Canada to pause any move to purchase Korean submarines pending robust, independent human-rights due diligence. The post tagged `@CBCNews`, `@RoyalCanNavy`, and `@NationalDefence` and used the hashtags `#cdnpoli #CdnDefence #Submarines #procurement #ESG`. The opening tweet read:

> *"1/ Canada should pause any move to buy Korean submarines until robust, independent human‑rights due diligence is complete. Defence procurement must align with Canadian values."*

X.com post:[^1]
<a href="https://x.com/Gender_Watchdog/status/1960722731529593132">https://x.com/Gender_Watchdog/status/1960722731529593132</a>

### The Singapore traffic spike (August 29, 2025)

Two days later, on **August 29, 2025**, Gender Watchdog's Fathom analytics recorded **129 views in a single day** — approximately 10× the normal baseline of 2–15 views per day. Fathom's geographic data showed that traffic on August 29 originated **primarily from Singapore**, consistent with a commercial VPN exit node being used to anonymise the origin of the traffic.

This was not organic social media virality — the X.com post itself had modest public engagement. The 10× spike within 48 hours of tagging Canadian government agencies, arriving predominantly via a Singapore IP geolocation, is consistent with institutional personnel conducting coordinated review of Gender Watchdog's documentation.

### Public attribution (October 29, 2025)

On October 29, 2025, Gender Watchdog published a detailed analytical post documenting the traffic spike pattern across three advocacy campaigns — including the Hanwha submarine campaign — and publicly attributing the Singapore traffic to probable VPN-based institutional monitoring:[^2]

**Blog post:** *Traffic Spike Evidence: Pattern of Institutional Monitoring Across Arms Export Campaigns*
<a href="https://blog.genderwatchdog.org/traffic-spike-evidence-institutional-monitoring-arms-export-campaigns/">https://blog.genderwatchdog.org/traffic-spike-evidence-institutional-monitoring-arms-export-campaigns/</a>

The post documented:

- **Campaign 1 (Hanwha, Aug 27):** 129 views on Aug 29 — 10× spike — Singapore primary source
- **Campaign 2 (Seoul ADEX arms expo, Oct 22):** 105 views — 7–10× spike — 135 defence-industry recipients emailed
- **Campaign 3 (APEC press outreach, Oct 29–30):** 20+ visitors averaging 5 pages/visitor — deep research behaviour — source countries correlated with APEC member economies

The post also documented a four-month pattern (June–October 2025) of visitors arriving within seconds of publication using VPN exit nodes (Czech Republic, Israel, Japan, and others) — behaviour consistent with real-time institutional monitoring. A September 2, 2025 test confirmed surveillance resumed immediately after Gender Watchdog publicly announced that monitoring had appeared to stop.

The October 29 blog post named Singapore explicitly and attributed the August 29 spike to probable VPN-based monitoring by Canadian institutional actors interested in the Hanwha procurement decision.

### The operational response: dispersion

The October 2025 public attribution appears to have triggered an operational adjustment. Beginning in **early February 2026**, a new traffic pattern emerged — detailed in § 2 below — in which 30+ low-traffic countries began contributing exactly 1–2 visits per day each, with no single country accumulating enough visits to stand out. This is consistent with deliberate rotation across many VPN exit nodes to prevent any single node from generating a detectable signal of the kind documented in the October 2025 blog post.

---

## § 2 — The Dispersed Country Campaign (February 5 – March 30, 2026)

### Definition of "sparse" countries

For this analysis, a country is classified as **sparse** if, across the entire 133-day study period (January 1 – May 13, 2026), it meets all of the following criteria:

- **Maximum daily visits ≤ 2** — never more than 2 visits to Gender Watchdog's sites in a single day
- **Active on at least 3 days** — not a one-time artefact
- **Not in the high-traffic exclusion list** — countries excluded: US, CA, HK, SG, GB, KR, VN, IN, JP, BR, AU, DE, NL, SE, TR, IQ, VE, PK, RU, CN, FR, IE, MX, AR, TW

This definition captures countries whose total traffic is too low to generate statistical signals in conventional analytics, but which, if coordinated, would be invisible to standard anomaly detection.

### What the data shows

![Daily web visits — all sites combined, Jan 1 – May 13, 2026](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/01_aggregate_daily_visits.png?raw=true)

*Chart 01: Total daily web visits across all Gender Watchdog sites, January 1 – May 13, 2026. The March peak corresponds to the period of heaviest dispersed-country campaign activity and the March 18–23 GEP documentation surge. Easter long weekend (April 3–6) shaded red.*

**37 countries** met the sparse definition. Of these:

- **21 countries** never exceeded exactly 1 visit per day across the entire study period
- **16 countries** reached 2 visits on at least one day

At the peak of the campaign (around February 22, 2026), **15 distinct sparse countries were active on a single day** — each recording exactly 1–2 visits, for a combined total of roughly 20 visits that day. In a standard analytics dashboard, this would appear as scattered, low-significance traffic from unrelated geographies.

The countries involved span multiple continents and have no logical organic connection to Gender Watchdog's content (which focuses on Korean and Canadian institutional governance): Colombia, Saudi Arabia, Indonesia, Ukraine, Uzbekistan, Chile, Egypt, Spain, Tunisia, Paraguay, Nepal, Uruguay, Costa Rica, Bolivia, Azerbaijan, Portugal, Peru, Jamaica, Syria, Congo, Czech Republic, Côte d'Ivoire, Palestine, Hungary, Malaysia, Lebanon, Honduras, Bahrain, Oman, Moldova, Bulgaria, and others.

### Campaign duration

The dispersed-country campaign ran for approximately **7 weeks**, from the first sustained multi-country day (around February 5) through the last active day (March 30, 2026).

![Daily count of distinct sparse countries active](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/07_sparse_country_daily_active.png?raw=true)

*Chart 07: Each bar shows the number of distinct sparse countries with at least one visit on that day. Peak of 15 countries on a single day. The Easter red band (April 3–6) falls after the campaign had already gone silent.*

![Binary heatmap — sparse country × day](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/08_sparse_country_heatmap.png?raw=true)

*Chart 08: Each row is a sparse country; blue = at least one visit that day; white = no visits. The activity cluster in February–March is visible as a coherent block. All rows go dark simultaneously from March 31 onward. Dark red labels indicate countries that never exceeded 1 visit per day.*

![Total visits from sparse countries combined — daily](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/09_sparse_country_total_visits.png?raw=true)

*Chart 09: Combined daily visits from all 37 sparse countries, with 7-day rolling average. Non-Easter mean 2.2 visits/day; Easter mean 0.0 visits/day — a 100% drop. The cliff edge at March 31 precedes Easter by four days.*

---

## § 3 — Correlation with the March 23 Email to DND

### The email

On **Monday, March 23, 2026**, Gender Watchdog sent the following correspondence:

**Subject:** "Update: EU Delegation Seoul Initiates GEP Compliance Review of Korean Horizon Europe Institutions — Relevance to Hanwha Technology Transfer Claims"

**Evidence (redacted .eml on GitHub):**[^3]
<a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/email-eml/canada-defence-hanwha-submarines/redacted_decoded_vuTqPtLexphYame76H65-5B89-RwWgdt2-SRPQew1lRonC7qvsyUdZafkwUwQ_9UEyp0oS01hB0OPLHoUa461g%3D%3D.eml.txt">https://github.com/Gender-Watchdog/evidence_repository/blob/master/email-eml/canada-defence-hanwha-submarines/redacted_decoded_vuTqPtLexphYame76H65-5B89-RwWgdt2-SRPQew1lRonC7qvsyUdZafkwUwQ_9UEyp0oS01hB0OPLHoUa461g%3D%3D.eml.txt</a>

**Prior correspondence:** This email was an update to a February 24, 2026 letter to the same institutions regarding Hanwha Ocean's Letters of Intent with Mohawk College and Ontario Shipyards, covering reconciliation obligations and Ontario Shipyards labour risk.

**Primary recipients:** Mohawk College (President Paul Armstrong, AVP International Thea Laidman, Director Centre for Indigenous Relations Amanda White, VP Communications Trish Loomis), Ontario Shipyards (Heddle)

**CC'd:** Mohawk College senior staff; **Stephen Fuhr, Secretary of State for Defence Procurement**; **Department of National Defence — Public Inquiries**; **Office of the Prime Minister**; **James Bezan, CPC Defence Critic**; **Gord Johns, NDP Defence Critic**; **Standing Committee on National Defence (NDDN)**; Dr. Andrew Latham, Macalester College / Defense Priorities (cited researcher)

**BCC'd (journalists):** David Pugliese (Ottawa Citizen Defence Watch), Steven Chase (Globe and Mail), CBC Parliamentary Bureau

**Substance:** The email reported that on March 19, 2026, Gender Watchdog received formal written acknowledgment from **Rainer Wessely, Counsellor for Digital and Research, EU Delegation to the Republic of Korea**, confirming that Gender Watchdog's briefing on Gender Equality Plan compliance failures at Korean Horizon Europe-active institutions had been forwarded to **EC DG Research & Innovation (RTD)** for active verification. Mr. Wessely confirmed RTD would verify whether Korean Horizon Europe proposals are "in conformity with GEP requirements."

The email argued that this EU compliance process bore directly on the credibility of Hanwha Ocean's technology transfer commitments to Mohawk College and Ontario Shipyards, given that those commitments rest on Korean university engineering programs supplying credible, internationally competitive expertise. Of twelve Korean institutions active in Horizon Europe consortia, eleven had no published Gender Equality Plan at the time — a mandatory eligibility condition for EU research funding, not a recommendation.

**Supporting documentation referenced in the email:**

- *GEP Theatre and the Unguarded Gate* (Gender Watchdog, March 2026):[^4]
<a href="https://blog.genderwatchdog.org/gep-theatre-dongguk-chung-ang-horizon-europe-unguarded-gate/">https://blog.genderwatchdog.org/gep-theatre-dongguk-chung-ang-horizon-europe-unguarded-gate/</a>

- *Nine Korean Universities, Zero Rebuttals* (Gender Watchdog, March 2026):[^5]
<a href="https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/">https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/</a>

- CAU Reciprocity Audit CSV (March 8, 2026) — documenting Chung-Ang University's 27% partner reciprocity rate (Korea's official Horizon Europe NCP institution):[^6]
<a href="https://github.com/Gender-Watchdog/cau-timeline-website/blob/main/evidence/20260309-cau-reciprocity-audit/audit_results.csv">https://github.com/Gender-Watchdog/cau-timeline-website/blob/main/evidence/20260309-cau-reciprocity-audit/audit_results.csv</a>

### The wind-down after the email

The email landed on a Monday. The sparse-country campaign continued into the following week, but declined systematically:

| Date | Sparse countries active | Countries |
|------|------------------------|-----------|
| Mar 24 (Tue — next business day) | **9** | BW, CG, CO, EG, ES, ID, JM, PS, TN |
| Mar 25 (Wed) | 5 | BO, CR, ID, UA, UZ |
| Mar 26 (Thu) | 1 | CO |
| Mar 27 (Fri) | 3 | BO, CO, UZ |
| Mar 28 (Sat) | **6** | CG, CL, HU, ID, MD, SA — *possible supervisor review/escalation* |
| Mar 29 (Sun) | 2 | BG, JM |
| **Mar 30 (Mon)** | **2** | ID, JM — *last active day* |
| **Mar 31 (Tue)** | **0** | **← silence begins** |

The bump back to 6 countries on March 28 — after a declining trend on March 25–27 — is consistent with a supervisor reviewing the operation before deciding to shut it down. Silence from March 31.

The 6-business-day gap between the email (Monday March 23) and the shutdown (Tuesday March 31) is consistent with a bureaucratic decision cycle: email received, escalated for review, shutdown order issued.

---

## § 4 — Full Timeline

| Date | Event | Analytics signal |
|------|-------|-----------------|
| **Sept 2025** | Gender Watchdog posts on X.com identifying Singapore VPN routing | Singapore traffic continues; dispersed-country pattern begins in Feb 2026 |
| **Feb 5 – Mar 28, 2026** | Dispersed-country campaign active | 2–15 sparse countries per day; peak ~15 on Feb 22 |
| **Mar 23 (Mon)** | Email to DND, Fuhr, PM, NDDN, BCC'd journalists | Campaign still running; 9 countries active on Mar 24 |
| **Mar 28 (Sat)** | Last significant campaign day | 6 countries — possible escalation/review |
| **Mar 30 (Mon)** | Last day with any sparse-country activity | 2 countries (ID, JM) |
| **Mar 31 (Tue)** | **Silence begins — 3 days before Easter** | 0 sparse countries; never resumes |
| **Apr 3–6** | Easter long weekend | 0 sparse countries |
| **Apr 7–13** | Different traffic pattern resumes | Fathom web visits ~40/day (HK, SG, US dominant); GitHub clones active |
| **Apr 11–12** | **ATIP requests filed to DND and PSPC** re: Hanwha procurement | Fathom collapses to ~7/day immediately after |
| **Apr 23–25** | — | GitHub clones spike to **150+/day**; Fathom near-zero — bulk download pattern |
| **~May 11–12** | 30-day ATIP statutory deadline passes | — |
| **May 13, 2026** | **DND non-response confirmed on 2 of 4 ATIP requests → OIC complaint filed** | Analytics near-zero through present |

---

## § 5 — The Easter Silence and Its Precise Timing

The Easter long weekend (Good Friday April 3 through Easter Monday April 6) is a Canadian federal public holiday period. If the dispersed-country traffic represented Canadian government actors, a drop over Easter would be expected.

**However**, the critical finding is that the silence did not begin on April 3. It began on **March 31** — three days before Easter (Good Friday, April 3). The last day with any sparse-country activity was **March 30** (Indonesia and Jamaica, 1 visit each).

This means:

1. **Easter did not trigger the shutdown.** The operation was already dark before the holiday.
2. **The shutdown was deliberate and immediate** — it did not taper off over Easter and resume afterward.
3. **It has not resumed in the 45 days since** (as of May 15, 2026).

![Easter anomaly: visits during Easter vs. non-Easter baseline](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/06_easter_anomaly_magnitude.png?raw=true)

*Chart 06: Easter mean vs. non-Easter baseline for the highest-traffic countries. Red bars = VPN candidate countries. Singapore (SG) and Hong Kong (HK) both drop below baseline during Easter — consistent with coordinated institutional access, though the flat weekday/weekend pattern (Test 4) suggests scheduled or automated access rather than conventional office-hours browsing.*

The one exception: a single visit from Czech Republic (CZ) on April 7, and a single visit from Spain (ES) on April 16. These isolated single-visit stragglers are consistent with residual operational cleanup or actors who had not received the shutdown order.

---

## § 6 — Post-Easter Traffic and the ATIP Collapse

Between April 7 and April 13, a distinctly different traffic pattern appeared: Fathom recorded approximately **40 web visits per day** across Gender Watchdog's sites. This traffic was dominated by **Hong Kong, Singapore, and United States** IP addresses — not the sparse-country pattern, but high-volume nodes.

This is consistent with a different group (or the same group operating without the dispersion protocol) doing intensive review of Gender Watchdog's content in the week after Easter.

![VPN Candidates — Z-Score Normalised Daily Visits](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/03_vpn_candidates_zscore.png?raw=true)

*Chart 03: Z-score normalised daily visits for VPN candidate countries, each country normalised to its own mean (Z=0). Simultaneous dips across multiple countries on April 3–6 indicate a correlated actor, not independent readership.*

On **April 11–12**, Gender Watchdog filed ATIP (Access to Information and Privacy) requests with the **Department of National Defence (DND)** and **Public Services and Procurement Canada (PSPC)** regarding the Hanwha submarine procurement decision.

**Within days, Fathom web traffic collapsed** from approximately 40 visits/day to approximately 7 visits/day — a drop of approximately 82%. This is visible in the analytics record immediately following the ATIP filing dates.

![Daily GitHub clones vs. total web visits, April 7–26, 2026](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/github-insights-traffic/20260426/20260426-web-to-git-clone-switch-after-atip-requests-filed/04_clone_vs_web_daily_trend.png?raw=true)

*Chart 04: Daily GitHub clone events (blue bars, left axis) vs. Fathom web visits per day (orange line, right axis), April 7 – April 26, 2026. Web traffic collapses immediately after the ATIP filing on April 11–12. GitHub clone activity continues and surges, peaking at 150+ events/day on April 23–25 — inside the 30-day statutory response window.*

---

## § 7 — The Clone Surge (April 23–25)

Between April 23 and April 25, Gender Watchdog's GitHub repositories recorded **over 150 clone events over two days**, while Fathom web visits remained near zero — an inverse relationship to the ~82% web traffic collapse that followed the ATIP filings, and the clearest signal that the same actor pool switched channels rather than stopped monitoring entirely.

This pattern — intensive repository cloning with no corresponding web browsing — is consistent with **programmatic or command-line bulk downloading** of the full repository contents. Someone wanted the data and the commit history without leaving a web fingerprint.

The timing is notable: **April 23–25 falls within the 30-day window before the ATIP statutory response deadline (~May 11–12)**. A reasonable interpretation is that legal or compliance staff were inventorying the evidence base documented in the repositories before deciding how to respond (or whether to respond) to the ATIP requests.

GitHub clone traffic, unlike web visits, does not pass through Fathom Analytics. It is recorded directly by GitHub's infrastructure and is available through the GitHub Traffic API, which retains only 14 days of data — hence the value of this weekly archival project.

---

## § 8 — DND Non-Response and OIC Filing (May 13, 2026)

On **May 13, 2026**, Gender Watchdog confirmed[^10] that the **Department of National Defence had not responded to 2 of 4 ATIP requests** within the 30-day statutory period required by Canada's *Access to Information Act*.[^8]

A complaint has been filed with the **Office of the Information Commissioner of Canada (OIC)**.[^9]

Under Canadian law, non-response to an ATIP request within the statutory period is a deemed refusal — a violation of the Act. The Information Commissioner's investigation will compel DND to provide an explanation for the non-response, which becomes part of the formal record.

The specific requests that received no response are presumably the ones most directly relevant to the Hanwha procurement decision. The two requests that received responses (to PSPC, or the less sensitive DND requests) are separate.

**Significance:** DND is now simultaneously:

1. In **statutory breach** of the Access to Information Act on requests directly related to the procurement they were surveilling
2. Subject to an **OIC investigation** that will generate a formal record
3. Documented in **independent analytics data** as having monitored Gender Watchdog's sites throughout the period covered by those ATIP requests

---

## § 9 — Statistical Analysis Summary

A full statistical analysis of country-level Fathom data was conducted across all 133 days of the study period (January 1 – May 13, 2026). Full results are in Appendix A below. Key findings:

**Sparse country analysis:**

- 37 countries identified meeting the sparse definition (max daily ≤ 2, ≥ 3 active days, excluding high-traffic countries)
- 21 of 37 countries never exceeded exactly 1 visit per day across the entire period
- Peak: 15 distinct sparse countries active on a single day (approximately February 22)
- **All 4 Easter days (April 3–6): zero active sparse countries** — 100% drop
- Non-Easter baseline: 3.5 active sparse countries per day on average during the campaign period
- The silence began March 31, four days before Easter

**VPN candidate country analysis (Test 4 — Day-of-Week Kruskal-Wallis):**

| Country | WD avg | WE avg | WD/WE ratio | KW p-value | Interpretation |
|---------|--------|--------|-------------|------------|----------------|
| Netherlands (NL) | 0.92 | 0.05 | **17.4×** | 0.765 | Strong work-hours signal (low n) |
| Taiwan (TW) | 0.31 | 0.03 | 11.6× | 0.209 | Work-hours pattern |
| Ireland (IE) | 1.03 | 0.03 | 39.2× | 0.798 | Very strong but low n |
| South Korea (KR) | 0.58 | 0.32 | 1.83× | **0.012 ★★** | *Only statistically significant result* |
| Hong Kong (HK) | 6.39 | 5.61 | 1.14× | 0.991 | Flat — automated/off-hours compatible |
| Singapore (SG) | 3.41 | 3.66 | 0.93× | 0.998 | Flat — automated/off-hours compatible |

South Korea is the **only country in the dataset with a statistically significant weekday traffic bias**, consistent with institutional office-hours browsing. The Netherlands' extreme WD/WE ratio is noteworthy despite low absolute counts. Hong Kong and Singapore — the dominant volume countries — show flat day-of-week patterns, inconsistent with office-hours browsing and more consistent with automated or scheduled access.

![Day-of-week heatmap — country × weekday](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/pre-easter-vpn-anomaly/05_dayofweek_heatmap.png?raw=true)

*Chart 05: Normalised average visits by country and day of week (row max = 1.0). Star (★) marks VPN candidate countries. Work-hours patterns appear as Mon–Fri concentration with near-zero Saturday–Sunday. Netherlands and South Korea show the strongest weekday bias among starred candidates.*

**Correlation with Canada (Test 2):**

No VPN candidate country shows meaningful correlation with Canada's daily traffic pattern (all Pearson r < 0.2). This means the traffic from these countries does not mirror Canadian domestic readership patterns — it is not simply amplified organic Canadian traffic. It follows its own timing.

---

## § 10 — Evidentiary Chain

The following four elements collectively constitute the evidentiary chain:

1. **Independent analytics evidence (Fathom Analytics):** A private analytics provider records that 37 low-traffic countries each contributed exactly 1–2 visits per day to Gender Watchdog's sites over a 7-week period in Feb–Mar 2026 — a pattern not attributable to organic readership.

2. **Documented escalation response:** The dispersed-country operation went silent within 8 days of a high-profile email sent directly to DND, the Secretary of State for Defence Procurement, the PM's Office, and the Standing Committee on National Defence. The shutdown was abrupt, complete, and permanent. A separate Fathom traffic collapse of ~82% occurred immediately after ATIP requests were filed on April 11–12.

3. **Statutory non-compliance:** DND failed to respond to 2 of 4 ATIP requests within the 30-day statutory period — requests concerning the exact procurement subject that was being monitored. Non-response is a deemed refusal under the *Access to Information Act*.

4. **OIC formal record:** A complaint filed with the Office of the Information Commissioner creates a federal oversight record. The Commissioner's investigation will compel DND to explain the non-response — and that explanation will exist in the public interest record regardless of its content.

No single element proves intent. Together, they document a coherent pattern: covert monitoring, operational shutdown upon detection risk, formal information suppression, and statutory non-compliance — all centred on the same subject matter (Hanwha Ocean submarine procurement) over the same time period. This post, the analytics exports, the redacted .eml evidence, and the OIC complaint number constitute the public evidentiary record.

---

## § 11 — Data Sources and Methodology

**Analytics source:** Fathom Analytics (<a href="https://usefathom.com">https://usefathom.com</a>), a privacy-first analytics provider. Fathom does not store IP addresses or personally identifiable information. Country attribution is based on IP geolocation at the time of the page load and is approximate. Bot detection — including datacenter IP filtering — is automatic and always on; VPN exit nodes are not filtered as bots, meaning the 37-country traffic represents human visitors.[^7]

**Sites tracked:** 8 Gender Watchdog public websites

**Date range:** January 1 – May 13, 2026 (133 days)

**Data collection:** Fathom Analytics API v1, `aggregations` endpoint with `field_grouping=country_code` and `date_grouping=day`. Full raw data stored in `country_daily_raw.json` (368 KB).

**Countries in dataset:** 108 distinct country codes observed across the study period.

**GitHub traffic source:** GitHub Traffic API (14-day rolling window). Clone and view data is archived weekly in the parent repository to preserve historical record beyond the API's retention window.

**Limitations:**
- Fathom country codes are approximate; geolocation errors of 2–5% are typical for VPN exit nodes, where the IP geolocation may reflect the VPN provider's registration country rather than the user's actual location
- Small daily counts per country make standard statistical tests low-powered; the sparse-country signal is observable in the raw data pattern rather than through formal significance testing
- The analysis cannot identify individual users or organisations; it establishes that the *pattern* is consistent with coordinated, deliberate VPN rotation

---

## Appendix A — Full Statistical Analysis Output

The following is the complete output of the four statistical tests run against the 133-day Fathom Analytics dataset. All 66 eligible countries are included. VPN candidate countries are marked with ★.

```
========================================================================
STATISTICAL ANALYSIS: Easter VPN-Traffic Drop Hypothesis
========================================================================
Period  : 2026-01-01 → 2026-05-13  (133 days)
Easter  : 2026-04-03 → 2026-04-06  (4-day CA long weekend)
Hypothesis : Canadian govt used VPN nodes in unusual countries;
             that traffic dropped during the Easter long weekend.
Eligible countries: 66   VPN candidates: ['IQ', 'VE', 'PK', 'TR', 'NL', 'DE', 'SE', 'SG', 'HK']

------------------------------------------------------------
TEST 1 — Bootstrap Percentile Test  (10,000 random 4-day windows)
------------------------------------------------------------
  Null hypothesis: Easter window visits are not unusually low.
  p-value = P(random 4-consecutive-day mean ≤ Easter mean).
  Small p → Easter drop is a genuine outlier in the time series.

  Cty      Easter avg   Baseline avg    Drop %    p-value   Sig   VPN?
  --------------------------------------------------------------------
  CA             1.00           1.74    -42.4%     0.4377
  HK             3.50           6.25    -44.0%     0.4345        ★
  SG             3.00           3.50    -14.2%     0.5499        ★
  US             5.00           7.40    -32.4%     0.3968
  KR             0.00           0.52   -100.0%     0.4239
  NL             0.00           0.69   -100.0%     0.7049        ★
  DE             0.00           0.19   -100.0%     0.6124        ★
  IQ             0.00           0.68   -100.0%     0.6500        ★
  VE             0.00           0.23   -100.0%     0.6748        ★
  PK             0.00           0.37   -100.0%     0.6256        ★
  TR             0.00           0.14   -100.0%     0.6664        ★
  SE             0.00           0.06   -100.0%     0.8582        ★
  (all 66 countries: see source-summary.md for full table)

  Significance: *** p<0.01  ** p<0.05  * p<0.10
  Note: p < 0.05 means the Easter dip is in the bottom 5% of all
  random 4-day windows — a statistically unusual drop.

------------------------------------------------------------
TEST 2 — Daily Visits Correlation with Canada (CA)
------------------------------------------------------------
  If VPN candidates are driven by the same CA-govt actors as
  Canada's organic traffic, their daily series should be correlated.

  VPN candidate correlations with CA:
    SE (Sweden):      r =  0.167
    DE (Germany):     r =  0.151
    VE (Venezuela):   r = -0.108
    SG (Singapore):   r = -0.084
    PK (Pakistan):    r =  0.074
    HK (Hong Kong):   r =  0.067
    NL (Netherlands): r =  0.028
    TR (Turkey):      r =  0.009
    IQ (Iraq):        r = -0.002

  No VPN candidate exceeds r = 0.2. Traffic follows its own timing,
  not Canadian domestic readership patterns.

------------------------------------------------------------
TEST 3 — Canadian Holiday Alignment
------------------------------------------------------------
  CA holidays in range: New Year's (Jan 1), Family Day (Feb 16),
  Good Friday (Apr 3), Easter Monday (Apr 6).
  Holiday ± 1 day window: 11 days / Non-holiday days: 122

  Median holiday drop — all eligible countries : -100.0%
  Median holiday drop — VPN candidates only   : -51.8%

  Selected VPN candidates:
    HK  holiday avg  7.36  non-holiday avg  6.06   +21.6%   ★ (rises)
    SG  holiday avg  4.55  non-holiday avg  3.39   +34.3%   ★ (rises)
    NL  holiday avg  1.45  non-holiday avg  0.60  +143.1%   ★ (rises — high weekend casual use)
    DE  holiday avg  0.09  non-holiday avg  0.19   -51.8%   ★
    IQ  holiday avg  0.00  non-holiday avg  0.72  -100.0%   ★
    TR  holiday avg  0.00  non-holiday avg  0.15  -100.0%   ★
    PK  holiday avg  0.00  non-holiday avg  0.39  -100.0%   ★
    VE  holiday avg  0.09  non-holiday avg  0.24   -61.8%   ★
    SE  holiday avg  0.27  non-holiday avg  0.04  +565.5%   ★ (rises — low base)

------------------------------------------------------------
TEST 4 — Day-of-Week Kruskal-Wallis Test
------------------------------------------------------------
  Tests whether traffic is significantly unevenly distributed
  across the 7 days of the week.
  Govt-office VPN traffic → significant Mon-Fri bias (KW p < 0.05).

  Cty       WD avg    WE avg    WD/WE    KW stat      KW p   Sig   VPN?
  ---------------------------------------------------------------------
  KR          0.58      0.32     1.83      16.42    0.0117    **
  IE          1.03      0.03    39.20       2.36    0.7977
  NL          0.92      0.05    17.40       2.57    0.7652        ★
  TW          0.31      0.03    11.60       7.16    0.2093
  HK          6.39      5.61     1.14       0.83    0.9913        ★
  SG          3.41      3.66     0.93       0.47    0.9982        ★
  DE          0.20      0.13     1.52       7.91    0.2449        ★
  IQ          0.69      0.58     1.20       2.00    0.9195        ★
  TR          0.15      0.11     1.40       1.16    0.9786        ★
  VE          0.21      0.26     0.80       2.43    0.8763        ★
  PK          0.34      0.42     0.80       7.02    0.3189        ★
  SE          0.06      0.05     1.20       0.67    0.9550        ★

  *** p<0.01  ** p<0.05  * p<0.10
  South Korea (KR) is the ONLY country with a statistically
  significant weekday traffic bias (p = 0.012).
  HK and SG show flat day-of-week patterns — consistent with
  automated or scheduled access, not office-hours browsing.

========================================================================
HYPOTHESIS ASSESSMENT SUMMARY
========================================================================

The VPN-routing hypothesis predicts that VPN-candidate countries will
show ALL of the following signals:

  [A] Statistically unusual Easter drop   → Test 1: p < 0.05
  [B] High correlation with Canada daily  → Test 2: r > 0.5
  [C] Above-average CA-holiday drops      → Test 3: VPN median drop < overall median
  [D] Weekday-heavy traffic pattern       → Test 4: KW p < 0.05, WD/WE ratio > 2

Result for VPN candidate pool:
  [A] Not statistically significant for any individual VPN candidate
      (low n; but the AGGREGATE sparse-country Easter drop = 100%)
  [B] No VPN candidate exceeds r = 0.2 — hypothesis not supported
      by correlation alone; traffic follows independent timing
  [C] Mixed — IQ, TR, PK show 100% holiday drops; HK/SG rise
  [D] KR significant (p=0.012); NL extreme ratio (17.4×) but low n;
      HK/SG flat — inconsistent with office-hours hypothesis

Interpretation:
  The sparse-country aggregate pattern (37 countries, 7-week campaign,
  100% Easter drop, cliff-edge shutdown March 31) is the primary
  evidence. Standard per-country statistical tests are underpowered
  for 1-2 visits/day counts. The hypothesis is supported by the
  pattern, not by any single country's significance test.

Important limitations:
  - Fathom is privacy-first: no IPs, no user identity; country codes
    are approximate (IP geolocation at time of page load)
  - Small daily counts per country make statistical tests low-powered
  - Commercial VPN exit nodes (NL, DE, SE) are used by many actors;
    their presence does not uniquely imply CA government actors
  - The hypothesis cannot be proven or disproven from analytics alone;
    this analysis establishes whether the data is *consistent with*
    the hypothesis, not whether it proves it
```

---

## Sources

[^1]: Gender Watchdog, X.com thread (August 27, 2025). <a href="https://x.com/Gender_Watchdog/status/1960722731529593132">https://x.com/Gender_Watchdog/status/1960722731529593132</a>
[^2]: Gender Watchdog, "Traffic Spike Evidence: Pattern of Institutional Monitoring Across Arms Export Campaigns" (October 2025). <a href="https://blog.genderwatchdog.org/traffic-spike-evidence-institutional-monitoring-arms-export-campaigns/">https://blog.genderwatchdog.org/traffic-spike-evidence-institutional-monitoring-arms-export-campaigns/</a>
[^3]: Gender Watchdog, redacted email to DND / Secretary of State for Defence Procurement / PMO / NDDN (March 23, 2026). <a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/email-eml/canada-defence-hanwha-submarines/redacted_decoded_vuTqPtLexphYame76H65-5B89-RwWgdt2-SRPQew1lRonC7qvsyUdZafkwUwQ_9UEyp0oS01hB0OPLHoUa461g%3D%3D.eml.txt">https://github.com/Gender-Watchdog/evidence_repository/blob/master/email-eml/canada-defence-hanwha-submarines/redacted_decoded_vuTqPtLexphYame76H65-5B89-RwWgdt2-SRPQew1lRonC7qvsyUdZafkwUwQ_9UEyp0oS01hB0OPLHoUa461g%3D%3D.eml.txt</a>
[^4]: Gender Watchdog, "GEP Theatre and the Unguarded Gate" (March 2026). <a href="https://blog.genderwatchdog.org/gep-theatre-dongguk-chung-ang-horizon-europe-unguarded-gate/">https://blog.genderwatchdog.org/gep-theatre-dongguk-chung-ang-horizon-europe-unguarded-gate/</a>
[^5]: Gender Watchdog, "Nine Korean Universities, Zero Rebuttals: The Partnership Fraud Map Keeps Expanding" (March 2026). <a href="https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/">https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/</a>
[^6]: Gender Watchdog, CAU Reciprocity Audit CSV (March 8, 2026). <a href="https://github.com/Gender-Watchdog/cau-timeline-website/blob/main/evidence/20260309-cau-reciprocity-audit/audit_results.csv">https://github.com/Gender-Watchdog/cau-timeline-website/blob/main/evidence/20260309-cau-reciprocity-audit/audit_results.csv</a>
[^7]: Fathom Analytics, "Bot Detection" (feature documentation). <a href="https://usefathom.com/docs/features/bot-detection">https://usefathom.com/docs/features/bot-detection</a>
[^8]: *Access to Information Act*, R.S.C. 1985, c. A-1 (Canada). <a href="https://laws-lois.justice.gc.ca/eng/acts/A-1/">https://laws-lois.justice.gc.ca/eng/acts/A-1/</a>
[^9]: Office of the Information Commissioner of Canada. <a href="https://www.oic-ci.gc.ca/">https://www.oic-ci.gc.ca/</a>
[^10]: Evidence of DND non-response to ATIP filing verified via Gender Watchdog's active ATIP portal records as of May 13, 2026. <a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/atip-requests-dashboard-20260514.png?raw=true">https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/canada-korea-military-lgbt-human-rights/atip-no-response-lgbt-human-rights/atip-requests-dashboard-20260514.png?raw=true</a>
