---
layout: post
title: "Pusan National University Deletes Its Partner Page — After We Documented a Fake Harvard Partnership (updated at 2026-03-25T04:57:17Z)"
date: 2026-03-25 00:00:00 +0000
slug: pusan-national-university-deletes-harvard-partner-page
lang: en
tags: partner-fraud, korea-universities, pusan-national-university, harvard, evidence-burial, governance, ieqas, national-university
meta_description: "Pusan National University deleted its international partners page 77 days after Gender Watchdog documented a false Harvard University partnership claim. PNU is the eleventh Korean university in this pattern."
bearblog_url: https://genderwatchdog.bearblog.dev/pusan-national-university-deletes-its-partner-page-after-we-documented-a-fake-harvard-partnership/
gh_pages_url: https://blog.genderwatchdog.org/pusan-national-university-deletes-harvard-partner-page/
---

# Pusan National University Deletes Its Partner Page — After We Documented a Fake Harvard Partnership

*March 25, 2026 — Gender Watchdog*

On March 25, 2026, Pusan National University's official international partners page stopped existing — not because of a server failure, but because someone logged into PNU's content management system and deleted the menu entry for it.

We know this because the page didn't return a standard 404 error or a generic gateway timeout. It returned PNU's own CMS interface — bearing the university's institutional logo — with the message: **메뉴이(가) 존재 하지 않습니다.** "This menu does not exist."

![Pusan National University international partners page returning CMS error message — "메뉴이(가) 존재 하지 않습니다." (This menu does not exist.) — captured March 25, 2026 KST](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/pusan-natl-offline-20260325-kst.png?raw=true)
*Pusan National University's own CMS confirms the partners page menu entry was deleted. Captured March 25, 2026 KST.*

A CMS navigation deletion is a deliberate administrative act. It requires a logged-in administrator to manually remove the entry from the site's menu structure. This was not an outage. This was not maintenance. It was a decision.

---

## What Was There Before They Deleted It

On January 7, 2026 — **77 days before the deletion** — we published documentation that PNU's international partners page listed **Harvard University** as a partner institution.[^1]

<div style="display:flex; justify-content:center; margin: 1.5em 0;">
<blockquote class="twitter-tweet"><p lang="ko" dir="ltr">🇰🇷 **부산대의 &#39;하버드 파트너&#39; 주장, 왜 위험할까요? (Ranking Gaming)**<br><br>단순한 허위 기재가 아닙니다. 이는 정교한 **랭킹 조작(Ranking Gaming)** 시도입니다.<br><br>1️⃣ **레버리지(Leverage):** &#39;가짜 파트너십&#39;을 미끼로 해외 연구진에게 접근, 실제 공동 연구(Collaboration)를 따냅니다.<br>2️⃣ **랭킹… <a href="https://t.co/UPPhDU5XRD">pic.twitter.com/UPPhDU5XRD</a></p>&mdash; Gender Watchdog (@Gender_Watchdog) <a href="https://twitter.com/Gender_Watchdog/status/2008768256530915552?ref_src=twsrc%5Etfw">January 7, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

Our .wacz capture from January 1, 2026 — archived at the time of our initial audit of 28 Korean universities — shows Harvard University explicitly listed in the North America / United States section of PNU's partner table.[^1a]

![.wacz archive from January 1, 2026 showing PNU's partner page with Harvard University listed — captured from Webrecorder ArchiveWeb.page](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/pnu-20260101-wacz-shows-harvard.png?raw=true)
*PNU's partner page as captured January 1, 2026 — Harvard University visible in the North America / United States partner table.*

**But the claim does not survive institutional-level verification.** Harvard College's own Office of International Education maintains a public, searchable registry of approved semester programs for Harvard students. A Korea search returns exactly three results: Seoul National University, Yonsei University, and Ewha Womans University. Pusan National University does not appear.[^1b]

What PNU does have is a relationship with the **Harvard-Yenching Institute** — an independent, privately endowed institute that is legally and administratively separate from Harvard University. The Harvard-Yenching Institute runs a scholars program under which faculty from partner Asian universities spend time at Harvard. PNU is listed on the Harvard-Yenching Institute's own partner page.[^1c]

![Harvard-Yenching Institute partner institutions page listing Pusan National University under Korea](https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/harvard-yenching-lists-pnu.jpeg?raw=true)
*Harvard-Yenching Institute's partner institutions list includes PNU — but the Harvard-Yenching Institute is not Harvard University. It has its own board, its own endowment, and its own governance. Source: harvard-yenching.org*

This is not fabrication from nothing. It is something more calculated: PNU took a **real but limited scholar exchange relationship** with an independent institute that occupies Harvard's campus, and listed it as an institutional partnership with **Harvard University itself**. This is the same pattern documented at Dongguk University with the University of Southampton — a limited program relationship inflated into a formal institutional partnership claim.

Deliberate brand inflation is harder to defend than outright fabrication precisely because it demonstrates intent to deceive. Compliance functions at universities understand exactly what a Harvard-Yenching scholars program is. They also understand it is not a partnership with Harvard University.

This case differs from previous instances in one important dimension. Dong-A University listed "Western California University" — a sufficiently unfamiliar name that context was needed. Harvard requires none. Every reader anywhere, immediately understands what a false Harvard University partnership claim means.

---

## The Evidentiary Chain

We had been monitoring the specific page element containing PNU's international partners list. When that element failed to load across **six consecutive automated checks**, an alert was triggered.[^2]

The sequence is unbroken and timestamped at every stage:

- **January 7, 2026:** Gender Watchdog X.com thread documents Harvard listed on PNU's official partners page — pre-deletion baseline confirmed[^1]
- **March 24–25, 2026:** Six consecutive monitoring checks find the partner list element absent from the page
- **March 25, 2026 KST:** Manual verification confirms CMS deletion; screenshot captured[^3]
- **March 25, 2026:** .wacz archive locked; Wayback Machine capture completed[^2a]

The .wacz capture taken before deletion shows Harvard listed. The screenshot taken after deletion shows "This menu does not exist." Both are independently verifiable.

---

**Verify the archive yourself.** The pre-deletion state of PNU's partner page is contained in Gender Watchdog's original January 2026 reciprocity audit archive of 28 Korean universities: <a href="https://drive.proton.me/urls/KBJMAPVS3C#O3Y7S38aeLxC">https://drive.proton.me/urls/KBJMAPVS3C#O3Y7S38aeLxC</a>

**How to use:** download the `.wacz` file → go to <a href="https://replayweb.page/">https://replayweb.page/</a> → click "Load Archive" → select the file. You are replaying the capture, not the live site.

---

Six consecutive failed checks rule out a transient server issue. Transient failures resolve. Structural deletions do not. The six-check sequence also narrows the deletion timestamp to within hours of the alert.

PNU cannot credibly claim routine maintenance. Routine maintenance does not delete navigation menu entries. Routine maintenance does not follow, by 77 days, public documentation of a false Harvard partnership claim.

---

## Why PNU Is Categorically Different From Every Previous Case

Every institution documented in this wave until now — Dongguk, Sogang, Chung-Ang, Ajou, Hongik, Dong-A — is a **private university**. Governance at private Korean universities is held by private foundations whose internal accountability structures are opaque.

Pusan National University is a **national university** (국립대학교). It is directly funded and overseen by the Korean Ministry of Education (교육부). This distinction changes the accountability structure entirely.

When PNU falsifies international partnerships:

- Government internationalization funding — tied in part to partnership and collaboration metrics — is directly implicated
- PNU holds **IEQAS accreditation**[^4a], the government credential system that authorizes it to recruit international students; that accreditation was granted partly on institutional credentials that may include fabricated partnerships[^4]
- Research grants partially justified by international collaboration metrics may rest on false foundations
- The Ministry of Education funded, accredited, and failed to audit a national institution falsely claiming Harvard as a partner

**The circular accountability failure is precise:** MOE funds PNU — MOE accredits PNU via IEQAS — MOE's accreditation process does not require reciprocal verification of partnership claims — MOE's own funding system enables the fraud without catching it.

PNU is also located in Busan. Dong-A University — documented as the tenth institution in this wave on March 22, 2026 — is also in Busan, under the same regional education oversight.[^5] Two institutions in the same city, the same regional jurisdiction, the same documented pattern.

---

## The Eleventh Institution

PNU is the **eleventh Korean university** we have documented exhibiting the same behavior: falsified international partnerships, followed by silent removal after public documentation — with no public correction, no statement, and no response to the reciprocity evidence.[^6]

The pattern is now consistent across all eleven cases. Not one institution has issued a public statement. Not one has published a corrected partners list. Not one has addressed the central question: when their claimed partner universities were contacted, did those universities confirm the partnership?

When the same administrative behavior — silent deletion rather than correction — repeats across eleven institutions following public documentation, the explanation is no longer coincidence. It is a recognizable institutional response to exposure.

---

## The Trap

PNU cannot restore its partners page without navigating an impossible set of outcomes:

**If PNU restores the page with Harvard removed:** it confirms the listing was false and the removal was reactive to our documentation.

**If PNU restores the page with Harvard retained:** it confirms the institution is maintaining a false claim under documented, timestamped scrutiny.

**If PNU restores the page with a correction or disclaimer:** it confirms our original documentation was accurate.

The one path not available to PNU is denial — because our X.com post pre-dates the deletion by 77 days, and our archived captures are independently verifiable by any third party.

This is the same trap Dong-A fell into when it attempted a three-stage evidence burial: the existence of pre-deletion documentation renders all subsequent actions self-incriminating.[^5]

---

## The Ministry of Education's Silence Is Now the Story

The Korean government has received our full evidence file since April 10, 2025. In the eleven months since, the government has continued to fund and accredit institutions whose international partnership pages we have documented as fraudulent across eleven cases.

At private institutions, the question was whether those universities had acted in bad faith. At a national university, the question becomes whether the Ministry of Education is functionally complicit — whether a government that funds, accredits, and consistently fails to audit partnership claims is effectively endorsing the fraud.

The world's leading university ranking body has now confirmed this structure in writing. On March 24, 2026, Times Higher Education responded to our documented evidence across eleven institutions — including PNU's Harvard claim — with three sentences. THE's stated position: "inclusion in the rankings is based on the proviso that a university is deemed to be in good standing by its relevant local regulatory body." THE directed us to "the relevant regulatory body." That regulatory body is the Ministry of Education. The Ministry of Education has been formally notified since April 10, 2025 and taken no public action.[^7]

The loop is now documented: THE ranks based on MOE accreditation — MOE's accreditation process does not verify partnership claims — fabricated partnerships inflate THE rankings — THE directs complaints back to MOE.

One specific action is available right now: the Ministry of Education should publicly audit the international partnership claims of IEQAS-accredited institutions against reciprocal verification from the foreign universities listed. Harvard can confirm or deny a PNU partnership in a single email. The Ministry of Education has not sent that email. Neither has THE.

When a private university fabricates partnerships, it misleads students. When a national university does the same thing — and the Ministry of Education says nothing, and the ranking body defers to the Ministry of Education — the fraud becomes infrastructure.

---

*Gender Watchdog is supported by End Rape On Campus (EROC).*

*Follow the evidence: <a href="https://x.com/Gender_Watchdog">https://x.com/Gender_Watchdog</a>*

---

## Footnotes

[^1]: *Gender Watchdog*, X.com (January 7, 2026) — documents PNU listing Harvard University as a partner on its official international partners page, pre-dating the deletion by 77 days: <a href="https://twitter.com/Gender_Watchdog/status/2008768256530915552">https://twitter.com/Gender_Watchdog/status/2008768256530915552</a>

[^1a]: .wacz archive screenshot, January 1, 2026 — PNU partner page with Harvard University listed in the North America / United States section: <a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/pnu-20260101-wacz-shows-harvard.png?raw=true">https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/pnu-20260101-wacz-shows-harvard.png?raw=true</a>

[^1b]: *Harvard College Office of International Education*, "Approved Semester Programs" — Korea search returns Seoul National University, Yonsei University, and Ewha Womans University only; Pusan National University is absent. Source: <a href="https://oie.fas.harvard.edu/approved-programs?search=korea">https://oie.fas.harvard.edu/approved-programs?search=korea</a> | Screenshot: <a href="https://x.com/Gender_Watchdog/status/2008768256530915552/photo/2">https://x.com/Gender_Watchdog/status/2008768256530915552/photo/2</a>

[^1c]: *Harvard-Yenching Institute*, "Partner Institutions in Asia" — lists Pusan National University under Korea. The Harvard-Yenching Institute is an independent, privately endowed institute with its own board, endowment, and governance; legally and administratively separate from Harvard University. Its partner relationships are scholar exchange programs, not institutional partnerships with Harvard University: <a href="https://harvard-yenching.org/partner-institutions-in-asia/">https://harvard-yenching.org/partner-institutions-in-asia/</a> | Screenshot: <a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/harvard-yenching-lists-pnu.jpeg?raw=true">https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/harvard-yenching-lists-pnu.jpeg?raw=true</a>

[^2]: Automated web monitoring alert — six consecutive failed checks on the international partner list element at `https://international.pusan.ac.kr/international/74621/subview.do` triggered an alert on March 24–25, 2026. Six consecutive failures confirm a structural DOM change, not a transient server error.

[^2a]: Pre-deletion .wacz archive of PNU's partner page is contained in Gender Watchdog's original January 2026 reciprocity audit of 28 Korean universities: <a href="https://drive.proton.me/urls/KBJMAPVS3C#O3Y7S38aeLxC">https://drive.proton.me/urls/KBJMAPVS3C#O3Y7S38aeLxC</a>. To replay: download the file → open <a href="https://replayweb.page/">https://replayweb.page/</a> → click "Load Archive" → select the file. You are replaying the capture, not the live site. Wayback Machine archive of the CMS deletion state (March 25, 2026 KST): <a href="https://web.archive.org/web/20260324213735/https://international.pusan.ac.kr/international/74621/subview.do">https://web.archive.org/web/20260324213735/https://international.pusan.ac.kr/international/74621/subview.do</a>

[^3]: Screenshot of `https://international.pusan.ac.kr/international/74621/subview.do` captured March 25, 2026 KST — PNU CMS returns "메뉴이(가) 존재 하지 않습니다." (This menu does not exist.) with institutional logo: <a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/pusan-natl-offline-20260325-kst.png?raw=true">https://github.com/Gender-Watchdog/evidence_repository/blob/master/imgs/scrubs-20260320/pusan-natl-u/pusan-natl-offline-20260325-kst.png?raw=true</a>

[^4]: *Gender Watchdog*, "The Alleged Predatory Appointment and Government Cover-Up: How IEQAS Certification Enables Systematic Corporate-Academic Exploitation at Dongguk University." Documenting how IEQAS certification does not include reciprocal verification of partnership claims: <a href="https://blog.genderwatchdog.org/the-alleged-predatory-appointment-and-government-cover-up-how-ieqas-certification-enables-systematic-corporate-academic-exploitation-at-dongguk-university">https://blog.genderwatchdog.org/the-alleged-predatory-appointment-and-government-cover-up-how-ieqas-certification-enables-systematic-corporate-academic-exploitation-at-dongguk-university</a>

[^4a]: *Pusan National University*, "Admissions For International Student" brochure. Explicitly claims "IEQAS Accreditation – The Best University (International Education Quality Assurance System)." Archived March 18, 2025: <a href="https://web.archive.org/web/20250318170952/https://his.pusan.ac.kr/sites/international/download/brochure/005-Admissons%20For%20International%20Student(English).pdf">https://web.archive.org/web/20250318170952/https://his.pusan.ac.kr/sites/international/download/brochure/005-Admissons%20For%20International%20Student(English).pdf</a>

[^5]: *Gender Watchdog*, "Dong-A University's Three-Stage Evidence Burial: From Ghost Partners to a False 2023 Timestamp" (March 22, 2026): <a href="https://blog.genderwatchdog.org/dong-a-university-partner-fraud-three-stage-burial/">https://blog.genderwatchdog.org/dong-a-university-partner-fraud-three-stage-burial/</a>

[^6]: *Gender Watchdog*, "Nine Korean Universities, Zero Rebuttals: The Partnership Fraud Map Keeps Expanding" (March 11, 2026): <a href="https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/">https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/</a>

[^7]: *Times Higher Education*, response from THE Data Team to Gender Watchdog (March 24, 2026) — three sentences responding to documented evidence across eleven institutions. Archived .eml: <a href="https://github.com/Gender-Watchdog/evidence_repository/blob/master/email-eml/THE-ranking-responses/decoded_Re_%20UPDATE_%20Nine%20Korean%20Universities%2C%20Zero%20Rebuttals%20%E2%80%94%20CAU%20at%2027%25%2C%20Top%201%2C500%20QS%20Partners%20Now%20Being%20Notified%202026-03-24T10_05_04-07_00.eml">https://github.com/Gender-Watchdog/evidence_repository/blob/master/email-eml/THE-ranking-responses/decoded_Re_%20UPDATE_%20Nine%20Korean%20Universities%2C%20Zero%20Rebuttals%20%E2%80%94%20CAU%20at%2027%25%2C%20Top%201%2C500%20QS%20Partners%20Now%20Being%20Notified%202026-03-24T10_05_04-07_00.eml</a>
