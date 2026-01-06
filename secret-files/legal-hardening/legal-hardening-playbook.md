# Legal Hardening Playbook for Independent Watchdogs

## Overview
This playbook documents the strategy used to "harden" this project against legal threats, misrepresentation claims, and unauthorized co-optation. It is designed to be replicated for other independent investigative projects.

## 1. Truthful Posture Assessment
**Goal:** eliminate ambiguity about the organization's nature to prevent fraud accusations.

| Status | Description | Risk Level | Mitigation |
| :--- | :--- | :--- | :--- |
| **Project** | Independently funded, no formal incorporation, no tax-exempt status. | Low (if disclosed) | Explicitly state "Not a non-profit/NGO". |
| **Social Enterprise** | Pre-incorporation entity building tools (AI) for social good. | Low | Frame as "Social Entrepreneurship". |
| **NGO/Non-Profit** | Registered legal entity with tax-exempt status. | High (regulatory) | Requires formal compliance, audits, and board. |

**The Strategy:**
We operate as a **Pre-incorporation Social Enterprise**, not an NGO. We frame this as "civic tech" and "AI-assisted whistleblowing".
*   **Do NOT:** Imply we are a charity, ask for donations as a tax-exempt entity, or claim official authority.
*   **DO:** State we are privately funded, independent, and building future tools.

## 2. Dual-License Strategy
Standard open-source licenses (MIT/Apache) are too permissive for *investigative findings*. We use a split model:

### Layer 1: Code (Apache 2.0)
*   **Applies to:** Python scripts, HTML/JS, CSS, build workflows.
*   **Why:** Standard, respected by lawyers, includes patent protection. Allows potential commercial use of the *tooling* (which is fine), but protects us from liability.
*   **File:** `LICENSE`

### Layer 2: Content (CC BY-NC-ND 4.0)
*   **Applies to:** Datasets, investigative reports, screenshots, markdown files.
*   **Why:**
    *   **BY (Attribution):** They must credit us.
    *   **NC (Non-Commercial):** PR firms/Universities cannot sell our data.
    *   **ND (No Derivatives):** Crucial. Prevents bad actors from editing our reports to change the conclusion while keeping our name on it.
*   **File:** `LICENSE-CONTENT`

## 3. Partner Liability Shield (Crucial for EROC/Supporters)
We must protect our institutional supporters from liability for our findings.

**The Clause:**
> "While we acknowledge the moral support of [Partner], this project is operationally independent. Supporters provide no funding, editorial direction, or oversight, and bear no liability for findings."

**Why:**
1.  **Protects Them:** Prevents legal threats against them for *our* work.
2.  **Protects Us:** Prevents claims that we are secretly funded/directed by "competitors."

## 4. Implementation Checklist

- [x] **Assessment:** Confirm you are NOT soliciting donations as a charity.
- [x] **Clean House:** Remove vague "ethical use" licenses.
- [x] **Apply Code License:** Overwrite `LICENSE` with Apache 2.0.
- [x] **Apply Content License:** Create `LICENSE-CONTENT` with CC BY-NC-ND 4.0.
- [x] **Partner Shield:** Add "Institutional Independence" clause to Disclaimer.
- [x] **Footer Audit:** Ensure Legal/Disclaimer links are on *every* page.
- [x] **Update README:** Add the "Legal & Licensing" section with:
    - Truthful Posture Statement (Social Enterprise)
    - Dual-license explanation
    - Disclaimers (Not legal advice/Not official accreditation)

## 5. Response Scripts

### Scenario A: University demands takedown citing incorrect data.
*Response:*
"Thank you for reaching out. This project is an independent investigative initiative. All findings are derived from publicly available data sources, which are cited in the repository. We operate under a strict correction policy: if you provide documented evidence contradicting specific data points, we will review and update the record. We do not remove valid public interest data based on general objections."

### Scenario B: Rankings body asks "Who is behind this?"
*Response:*
"This is an independently funded pre-incorporation social enterprise focused on AI-assisted transparency in university administration. We are not affiliated with any political group or competing educational institution. Our funding is personal and autonomous to ensure objectivity. You can review our full methodology, dual-license structure, and open-source code on our GitHub repository."

## 6. Standard Disclaimer Text
> "This project conducts independent research and analysis using AI-assisted methodology. It does not provide legal advice, victim services, or official accreditation judgments. All findings are based on publicly available information and documented correspondence. Users are encouraged to independently verify all data."
