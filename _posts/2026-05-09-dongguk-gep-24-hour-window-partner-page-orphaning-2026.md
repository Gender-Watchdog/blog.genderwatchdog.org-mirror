---
layout: post
title: "Caught on Monitor: The 24-Hour GEP Window, CMS Surgery, and Dongguk's Fake Partner Hub (updated at 2026-05-10T01:37:28Z)"
date: 2026-05-09 00:00:00 +0000
slug: dongguk-gep-24-hour-window-partner-page-orphaning-2026
lang: en
tags: Dongguk, GEP, evidence, monitoring, partner-pages, Horizon-Europe
meta_description: "Monitoring software caught Dongguk University's Gender Equality Plan page live for less than 24 hours before being orphaned, and six continental partner page tabs simultaneously switched to a new CMS template — with three Canadian partners failing basic verification."
bearblog_url: https://genderwatchdog.bearblog.dev/dongguk-gep-24-hour-window-partner-page-orphaning-2026/
gh_pages_url: https://blog.genderwatchdog.org/dongguk-gep-24-hour-window-partner-page-orphaning-2026/
---

On May 5, 2026, monitoring software flagged that all six of Dongguk University's continental partner page tabs — Africa, America, Asia SE/Central/Middle, Chinese-speaking Region, Europe, Oceania — had switched to a new CMS template simultaneously on May 4. Tab navigation stripped. Breadcrumbs gone. The year removed from the copyright notice. The old partner lists orphaned at their original URLs, with no site-level navigation path left to reach them.

Reviewing those monitoring logs for context revealed a second event the software had already captured six weeks earlier: a Gender Equality Plan link appeared in Dongguk's sitewide navigation on March 18, 2026 at approximately 23:17 KST — and was gone within 24 hours.[^1] A Megalodon archive taken inside that window is the only externally timestamped evidence the page was ever publicly accessible.[^2]

This post documents both events and their 72-hour correlation with the May 4 redesign.

---

## Dongguk Does Not Delete. It Orphans.

Since 2025, Dongguk's response to institutional pressure has followed two related but distinct patterns. The first is direct deletion: in January 2026, UBC disappeared from the America partners list on page/554 with no announcement, no correction, no apology — caught mid-act by monitoring software.[^4] The second is more forensically interesting: surgical CMS orphaning, applied twice since March 2026. Strip the page's title, its `<h1>` heading, and its sidebar navigation links. Leave the body content intact at the original URL. Publish a replacement page at a new address if one is needed. The content does not disappear. The institutional pathway to it does.

This is not accidental misconfiguration. It is a documented practice, confirmed on the Gender Equality Plan page `/page/1173` (March 2026) and across six continental partner page tabs (May 2026).[^3] Monitoring software and third-party archives make the architecture visible.

---

## Pillar I — The GEP 24-Hour Window (March 18–19, 2026)

**January 22, 2026 — baseline.** Six partner page URLs are under active monitoring. The `About DU` sitemap footer on all six pages contains no Gender Equality Plan entry.[^1]

**March 18, 2026, approximately 23:17–23:28 KST.** All six partner pages update simultaneously. The footer sitemap now carries `Gender Equality Plan(GEP)` under `About DU`. The change propagated in consistent polling order — page/477 → 553 → 554 → 555 → 556 → 557 — within an 11-minute window.[^1] This is a sitewide nav flush, not an isolated page edit. Six independently monitored URLs confirm the same change, at the same time, in the same sequence.

**March 19, 2026, 12:58 JST.** Megalodon archives `/page/1173` as a fully functional GEP page: title present, `<h1>` present, sidebar navigation intact, contact block listing the Office of Planning and Budgeting at 02-2260-3064, `About DU` sitemap still carrying the GEP link.[^2] The window is open.

**March 19, 2026, approximately 23:17–23:28 KST.** All six pages update again. The GEP link is gone. Research menu items are reorganized. Six-URL corroboration confirms the removal was sitewide and coordinated — the same propagation signature as the addition the night before.[^1]

Less than 24 hours from publication to removal. Megalodon closes the loop.

---

## Pillar II — The GEP Page Orphaning

After the nav link was removed, `/page/1173` did not 404. It was surgically edited.[^3] Six fields stripped: the CMS page title (now blank), the `<h1>` heading (now blank), the sidebar `ul.snb` navigation list (reduced to a single home link), the `change1` CSS class (removed), the social-share canonical URL (now redirects to root domain), and the breadcrumb trail. Everything else — Sections 1–4, the implementation table, the closing signature — is word-for-word identical to the Megalodon capture. Content preserved. Navigation destroyed.

A replacement page was simultaneously published at `/page/1506`: properly titled, fully navigable, searchable via Dongguk's site search. One substantive difference from the original: no contact information. The Office of Planning and Budgeting telephone number that appeared on `/page/1173` does not appear on `/page/1506`.[^3]

The evidence of coordination is embedded in the orphaned page itself: the sitemap inside `/page/1173` already links to `/page/1506`. The transition was planned before the orphaning was executed. This is the same CMS surgery that would be applied to six partner page tabs six weeks later. And it follows the pattern established in January 2026, when UBC was silently deleted from the partners list — caught by monitoring software, documented in our Panic Scrub post.[^4]

---

## Pillar III — The Partner Page Migration and What Triggered It

On March 19, 2026 — the same day EU Delegation Counsellor Rainer Wessely forwarded Gender Watchdog's GEP compliance briefing to European Commission Research and Development units[^5] — the GEP link was pulled from sitewide navigation. Six weeks passed.

Then two Korean-language posts appeared on DC Inside — Korea's dominant internet forum — in the Dongguk University gallery, where the audience is not international observers but current students, domestic faculty, and film industry insiders.

**May 1, 2026:** A post named all five Western government cultural bodies that had withdrawn from JIFF 2026 — Canada, Japan, Australia, France, and a fifth — and connected those withdrawals to Gender Watchdog's formal notification campaign. (Gender Watchdog subsequently corrected this count to six, noting the departure of Spain's AC/E.[^13]) KOFICE, the Korean government's own Hallyu promotion agency, was named as having withdrawn independently. For the first time, the institutional cost was broadcast in Korean, to the Dongguk community, framed as a Korean-government-level judgment — not a foreign one.[^6]

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Correction to this thread: we wrote &quot;five Western governmental cultural bodies&quot; withdrew.<br><br>It&#39;s six.<br><br>AC/E — Acción Cultural Española, Spain&#39;s Ministry of Culture international cultural action agency — is also absent from JIFF 2026.<br><br>The full six:<br>→ Canada (federal wordmark)<br>→… <a href="https://t.co/DrMIa1oztn">https://t.co/DrMIa1oztn</a></p>&mdash; Gender Watchdog (@Gender_Watchdog) <a href="https://twitter.com/Gender_Watchdog/status/2052562415670419487?ref_src=twsrc%5Etfw">May 8, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**May 2, 2026:** A post named the university president's academic background — Korean Literature — as a structural liability for Horizon Europe GEP compliance, while EU RTD units were actively reviewing proposals. The 61.5% sexual violence rate in Korean university arts programs documented in the KWDI 2020 report was cited. The 영상대학원 (Graduate School of Digital Image and Contents) was identified as the highest-risk department.[^7]

International English-language pressure and domestic Korean-language pressure on the same university forum are qualitatively different threat categories. The first is visible to regulators. The second is visible to everyone inside the institution.

**May 4, 2026, approximately 23:28–23:42 KST** — within 72 hours of the May 2 post — monitoring software detected all six continental partner page tabs switching to a new CMS template simultaneously. Same polling order as March: page/477 first, page/557 last.[^1] Tab navigation: gone. Breadcrumb: gone. Language toggle: gone. Copyright year: stripped. The old partner lists survive at their orphaned URLs. Same CMS surgery as `/page/1173`.

---

## Pillar IV — `/page/1543` Carries the Fraud Forward

In place of the six orphaned pages, Dongguk launched `/page/1543`: an interactive world map with clickable regions and a partner table that populates beneath it.[^8] Regional counts: Asia (182), Europe (95), America (71), Africa (4), Oceania (7). Each institution carries a homepage link icon.

It looks auditable. It is not.

![Dongguk /page/1543 America tab — partner list with link icons](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/new-partners-page-20260510/dongguk-new-partners-page-america-top-20260510.png?raw=true)
*Dongguk University /page/1543 America tab, May 10, 2026 — 71 listed partners, each with a homepage link icon implying verifiability.*

Three spot-checks against partner institutions' own live databases:

### University of Ottawa — new Canadian listing; zero results in their database

The University of Ottawa appears on `/page/1543` as a Canadian partner — not present in Dongguk's old partner architecture. Filtering U Ottawa's student exchange destination database for "Korea" returns exactly two results: Korea University and Kyung Hee University.[^9] Dongguk does not appear. Searching "dongguk" directly: zero results — "No matching records found" — out of 87 listed destinations.[^9]

![University of Ottawa exchange finder filtered to Korea — Dongguk absent](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/fake-partners-20260510/u-ottawa-korean-partners-no-dongguk.png?raw=true)
*U Ottawa exchange destination database filtered to "Korea" — Korea University and Kyung Hee University returned; Dongguk absent.*

![University of Ottawa exchange database — zero results for dongguk](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/fake-partners-20260510/u-ottawa-search-donggu-zero-results-20260510.png?raw=true)
*U Ottawa search for "dongguk" — 0 of 87 destinations. "No matching records found."*

### Toronto Metropolitan University — listed, but their own link hits a Dongguk 404

TMU does list Dongguk in its exchange opportunities database — but the scope is **Graphic Communications Management (BTech) at The Creative School only**.[^10] A single-faculty arrangement for one undergraduate program. Dongguk lists TMU as a full institutional partner on `/page/1543` with no scope qualification.

The link TMU's own database provides for the Dongguk partnership — `dongguk.edu/mbs/en/subview.jsp?id=en_040601020000` — returns Dongguk's own **"페이지를 찾을 수 없습니다" (Page not found) error page**.[^10] Dongguk cannot maintain the URL its own partner publicly lists.

In January 2026, Dongguk deleted TMU entirely and reverted to the dead name "Ryerson" — the same scrub that removed UBC from the partners list. Caught mid-act. Documented.[^4] TMU is now correctly named on `/page/1543`. The link is broken.

![TMU exchange database — Dongguk University, The Creative School, dead link visible](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/fake-partners-20260510/tmu-dongguk-creative-school-partners-dead-link-20260510.png?raw=true)
*TMU's exchange opportunities database: "Student Exchange - Dongguk University - The Creative School" — the dead dongguk.edu link URL is visible.*

![Dongguk 404 error page at the URL listed in TMU's own database](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/fake-partners-20260510/tmu-link-lands-on-dongguk-error-page.png?raw=true)
*Dongguk's "페이지를 찾을 수 없습니다" error page at the URL Toronto Metropolitan University's own database publicly lists for the partnership.*

### University of Manitoba — listed on `/page/1543`; absent from their own database

U Manitoba's international cooperative partnerships database, filtered for "Korea, Republic of," returns nine agreements across five institutions: Chung-Ang University, Dankook University, Hallym University, Korea University, Pusan National University.[^11] Dongguk University does not appear.

![University of Manitoba Korea partnerships — top of list, Dongguk absent](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/fake-partners-20260510/umanitoba-no-dongguk-20260510-top.png?raw=true)
*U Manitoba international partnerships, Korea, Republic of — top of results. Dongguk absent.*

![University of Manitoba Korea partnerships — bottom of list, Dongguk absent](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/dongguk/partner-pages/fake-partners-20260510/umanitoba-no-dongguk-20260510-bottom.png?raw=true)
*U Manitoba international partnerships, Korea, Republic of — bottom of results. Nine agreements across five institutions. Dongguk absent from all.*

U Manitoba was previously documented as holding only an MOU with Dongguk — a non-binding statement of intent with no obligation to maintain exchange programming.[^12] An MOU requires no formal action to dissolve. Their database now reflects a reality that Dongguk's website does not.

**Three spot-checks. Three failures.** One false listing newly added in the scramble (U Ottawa), one inflated from single-faculty to institutional scope (TMU), one quietly dropped from the partner institution's own database (U Manitoba). The interactive world map is window dressing.

---

## The Playbook: Eight Acts. Twelve Months. Zero Investigations.

Dongguk's documented response to institutional pressure takes two forms. The first is direct deletion: remove the entry from the list, issue no statement, and hope no one was watching. The second — applied twice since March 2026 — is CMS orphaning: strip navigation from the page, preserve the body content at the original URL, publish a replacement at a new address. Both techniques produce the same outcome: the institutional record is altered without acknowledgment.

Two applications of the orphaning technique since March 2026: the GEP page `/page/1173`, and six continental partner page tabs simultaneously. Each time: navigation stripped, body content preserved, new page published at a fresh URL. The effect is deniability-by-architecture — the content isn't gone, it's just unreachable without the direct URL.

Monitoring software and third-party archives make that architecture visible. The evidence is now logged in six CSVs, three HTML captures, and one Megalodon archive. None of it can be retroactively altered.

<div style="border: 2px solid #cc0000; padding: 16px; margin: 20px 0; background: #fff8f8; color: #000;">
<strong style="color: #cc0000; font-size: 1.05em;">EIGHT ACTS. TWELVE MONTHS. ZERO INVESTIGATIONS.</strong>
<div style="color: #000; margin-top: 12px; overflow-x: auto;">

| Date | Act |
|---|---|
| May 27, 2025 | Sidus FNH legal threat demanding retraction of Gender Watchdog's sexual violence documentation |
| July 24, 2025 | Female faculty profile (이정현) silently edited on department website — caught by Visual Ping as real-time tokenism |
| After Jul 25, 2025 | 차승재 (Tcha Seung-jai) removed from Korean-language DIC faculty page — present in the July 25 Wayback archive, confirmed absent by September 23, 2025 |
| December 2025 | GEP page itself confirms: "Dongguk established a GEP Task Force (TFT) under the Planning and Budget Office" — timed with GW's 34-partner fraud exposé[^2][^12] |
| January 19, 2026 | "Panic Scrub" — UBC deleted, Toronto Metropolitan University reverted to dead name "Ryerson" — caught mid-act |
| March 18, 2026 | GEP page (`/page/1173`) published on Dongguk website; Gender Watchdog briefs EU Delegation |
| March 18, 2026 (23:17 KST) | GEP link appears in sitewide `About DU` nav — monitoring software confirms simultaneous change across all 6 partner pages |
| March 19, 2026 | EU Delegation Counsellor Wessely forwards GEP compliance briefing to RTD units |
| March 19, 2026 (12:58 JST) | Megalodon archives `/page/1173` — only externally timestamped capture inside the 24-hour window |
| March 19, 2026 (23:17 KST) | GEP link removed from all 6 partner pages; `/page/1173` orphaned; `/page/1506` published with contact info removed |
| March 24, 2026 | EU-Korea Research and Innovation Day, Four Seasons Hotel Seoul |
| April 1, 2026 | Two female research faculty removed; BK21 credential dropped; senior male film professor transitioned to 명예교수 with all contact stripped — eight days after the summit |
| May 1, 2026 | DC Inside (Dongguk gallery): JIFF Western government withdrawals published in Korean — domestic broadcast of institutional cost |
| May 2, 2026 | DC Inside (Dongguk gallery): University president named as Horizon Europe compliance liability in Korean — audience: students, faculty, senate |
| May 4, 2026 (23:28 KST) | All 6 partner page tabs replaced with new CMS; `/page/1543` operational — old partner lists orphaned |
| **May 5, 2026** | **Gender Watchdog discovers GEP 24-hour window and partner page orphaning; `/page/1543` spot-checked: U Ottawa (0 results), TMU dead link, U Manitoba absent from own database** |

</div>
</div>

No investigation has been initiated. No statement has been issued.

*This post extends the timeline documented in Gender Watchdog's April 1, 2026 faculty purge report: <a href="https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026/">https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026/</a>[^5]*

## Sources

[^1]: Gender Watchdog, monitoring logs (changedetection.io), six URLs, January 22 – May 4, 2026. <a href="https://github.com/Gender-Watchdog/evidence_repository/tree/master/logs/changes-detected/dongguk/20260122-to-20260504/partners-webpages-migrations">https://github.com/Gender-Watchdog/evidence_repository/tree/master/logs/changes-detected/dongguk/20260122-to-20260504/partners-webpages-migrations</a>
[^2]: Megalodon, archive of Dongguk University `/page/1173`, March 19, 2026, 12:58 JST. <a href="https://megalodon.jp/2026-0319-1258-12/https://www.dongguk.edu:443/eng/page/1173">https://megalodon.jp/2026-0319-1258-12/https://www.dongguk.edu:443/eng/page/1173</a>
[^3]: Gender Watchdog, HTML capture comparison — three stages: Megalodon capture (March 19, 2026), orphaned live state, replacement `/page/1506`. <a href="https://github.com/Gender-Watchdog/evidence_repository/tree/master/html/dongguk/20260318-to20260510/gep-page-migration">https://github.com/Gender-Watchdog/evidence_repository/tree/master/html/dongguk/20260318-to20260510/gep-page-migration</a>
[^4]: Gender Watchdog, "Panic Scrub: Dongguk Deletes UBC, Reverts to Dead Names" (January 2026). <a href="https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names/">https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names/</a>
[^5]: Gender Watchdog, "Two Profiles, Two Cleanup Tracks" (April 1, 2026) — documents Wessely email of March 19, 2026. <a href="https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026/">https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026/</a>
[^6]: DC Inside, Dongguk University gallery, post no. 129505, May 1, 2026. Archived: <a href="https://megalodon.jp/2026-0501-1152-17/https://gall.dcinside.com:443/board/view/?id=dongguk&no=129505">https://megalodon.jp/2026-0501-1152-17/https://gall.dcinside.com:443/board/view/?id=dongguk&no=129505</a>
[^7]: DC Inside, Dongguk University gallery, post no. 129509, May 2, 2026. Archived: <a href="https://ghostarchive.org/archive/ttysv">https://ghostarchive.org/archive/ttysv</a> — Mirror: <a href="https://megalodon.jp/2026-0502-1248-39/https://gall.dcinside.com:443/board/view/?id=dongguk&no=129509">https://megalodon.jp/2026-0502-1248-39/https://gall.dcinside.com:443/board/view/?id=dongguk&no=129509</a>
[^8]: Dongguk University, `/page/1543` partner hub. Live: <a href="https://www.dongguk.edu/eng/page/1543">https://www.dongguk.edu/eng/page/1543</a> — Archive: <a href="https://archive.md/KR7qu">https://archive.md/KR7qu</a>
[^9]: University of Ottawa, student exchange destination finder. <a href="https://uottawa.ca/study/international-experience/student-exchange-program/find-destination">https://uottawa.ca/study/international-experience/student-exchange-program/find-destination</a>
[^10]: Toronto Metropolitan University, exchange opportunities database. <a href="https://torontomu.adv-pub.moveonca.com/report-page-1732/">https://torontomu.adv-pub.moveonca.com/report-page-1732/</a>
[^11]: University of Manitoba, international cooperative partnerships database. <a href="https://umanitoba.adv-pub.moveonca.com/report-page-1660/">https://umanitoba.adv-pub.moveonca.com/report-page-1660/</a>
[^12]: Gender Watchdog, "Semantic Fraud: How Dongguk University's Global Network Collapsed (34 Fake Partners Exposed)" (December 2025). <a href="https://blog.genderwatchdog.org/semantic-fraud-how-dongguk-universitys-global-network-collapsed-34-fake-partners-exposed/">https://blog.genderwatchdog.org/semantic-fraud-how-dongguk-universitys-global-network-collapsed-34-fake-partners-exposed/</a>
[^13]: Gender Watchdog, correction tweet, May 8, 2026. <a href="https://x.com/Gender_Watchdog/status/2052562415670419487">https://x.com/Gender_Watchdog/status/2052562415670419487</a>
