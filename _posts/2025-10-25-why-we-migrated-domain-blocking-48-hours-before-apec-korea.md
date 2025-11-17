---
layout: post
title: "Why We Migrated: Domain Blocking 48 Hours Before APEC Korea (Updated 2025-10-26T04:30:00Z)"
slug: "why-we-migrated-domain-blocking-48-hours-before-apec-korea"
date: 2025-10-25T04:34:00+00:00
modified_date: 2025-10-26T04:30:00+00:00
lang: en
meta_description: "Our custom domain experienced a major traffic spike exactly 48 hours before APEC Leaders' Week in Gyeongju—the third escalation in 18 days. From APEC's suppression of our X.com reply (Oct 7) to Substack blocking (Oct 20) to the traffic incident (Oct 25). Here's why we migrated to GitHub Pages and what it means for censorship resistance."
---

**October 25, 2025** — We noticed that our custom domain `blog.genderwatchdog.org` stopped resolving globally at approximately 12:34 PM KST today. The timing is not coincidental: **48 hours before APEC Economic Leaders' Week begins in Gyeongju, South Korea**—the same city where we documented student exploitation at Dongguk University's WISE campus.

This post documents the censorship attempt, our migration to more resilient infrastructure, and why this makes our work **stronger**, not weaker.

---

## What Happened

### Timeline

**April 2025 onwards**: Published comprehensive documentation of:
- Falsified university partnerships (40% fraud rate with Canadian institutions)
- Sexual violence cover-ups (KWDI 2020: 61.5% of female arts students experience harassment)
- Corporate-academic exploitation (entertainment CEOs appointed as faculty over students)
- Gyeongju campus exploitation (students sharing "housing" with tourists)

**6+ months**: Custom domain operated without any technical issues

**October 25, 2025, ~12:34 AM KST**: Custom domain stopped resolving globally
- DNS records unchanged at registrar (Namecheap)
- No legal requests received according to registrar
- No court orders
- No government notices
- Bear Blog dashboard suddenly shows "DNS not set" despite 6 months of proper operation

**October 27-November 1, 2025**: APEC Economic Leaders' Week in Gyeongju
- Same city where we documented ongoing exploitation
- International scrutiny at peak levels
- Evidence packages prepared for APEC delegations
- Perfect timing for suppression

### Technical Evidence

We immediately documented:
- ✅ DNS records unchanged at Namecheap
- ✅ Registrar confirmation: "No legal actions, court orders, or government requests"
- ✅ Content still accessible at direct URL: `genderwatchdog.bearblog.dev`
- ✅ Global DNS failure (not regional or ISP-specific)
- ✅ No technical explanation for sudden "DNS not set" status

**This is not a technical issue. This is targeted interference.**

#### Evidence Screenshots

**1. Third-party confirmation of outage (00:47 AM KST):**

![Down For Everyone Or Just Me showing blog.genderwatchdog.org is down](/assets/images/down-for-everyone-2025-10-25%2000-47-21.png)
*Independent verification: "It's not just you! blog.genderwatchdog.org is down." - First documented evidence of the outage.*

**2. DNS records properly configured at registrar (01:02 AM KST):**

![Namecheap DNS dashboard showing proper configuration](/assets/images/namecheap-dashboard-2025-10-25%2001-02-46.png)
*Namecheap dashboard showing DNS records unchanged: 4 A records pointing to GitHub Pages IPs, CNAME record intact. No legal requests, no government notices.*

**3. Global DNS propagation failure (01:19 AM KST):**

![DNS Checker showing global DNS failure with red X marks worldwide](/assets/images/dnschecker-blog-all-x-2025-10-25%2001-19-49.png)
*DNSChecker.org showing DNS failure across all global servers: United States, Canada, Russia, South Africa, Netherlands, France, Spain, UK, Germany, Mexico, Brazil, Australia, New Zealand, Singapore, South Korea. Not a regional issue—global suppression.*

**4. Browser connection error (01:58 AM KST):**

![Browser showing ERR_CONNECTION_RESET error for blog.genderwatchdog.org](/assets/images/blog.genderwatchdog-censored-2025-10-25%2001-58-10.png)
*Chrome browser: "This site can't be reached / The connection was reset. / ERR_CONNECTION_RESET"*

**5. Bear Blog dashboard claiming "DNS not set" (04:51 AM KST):**

![Bear Blog dashboard showing DNS not set error](/assets/images/bearblog-dns-records-not-set-%202025-10-25%2004-51-27.png)
*Bear Blog dashboard suddenly showing "The DNS records for blog.genderwatchdog.org have not been set" despite 6+ months of proper operation and unchanged DNS records at registrar.*

#### Registrar Confirmation: No Legal Basis for Blocking

**Namecheap Support Response (06:15 UTC, Ticket NC-HIV-0055):**

We contacted our domain registrar (Namecheap) during the outage to investigate potential legal action. Their response confirms:

> "We confirm that there are currently no legal actions, court orders, or government requests associated with your domain."
> 
> "DNS record modifications can only be made either by you (the domain owner) through your Namecheap account or by our team upon receipt of a confirmation code provided during verified support interactions."
>
> "Upon checking the DNS settings, the CNAME record for the 'blog' subdomain is currently propagating correctly."
>
> "This indicates that the subdomain name is resolving properly on the DNS level."
>
> "When attempting to access blog.genderwatchdog.org, the error message 'This site can't be reached. blog.genderwatchdog.org refused to connect' appears. **This suggests that the issue is likely on the hosting provider's side**, rather than with the domain or DNS configuration."

**What this proves:**

1. ✅ **No legal basis** for service disruption - no court orders, government requests, or legal actions
2. ✅ **DNS configuration intact** - registrar confirms CNAME propagating correctly
3. ✅ **Registrar-level security** - DNS changes require owner authorization or verified support interaction
4. ✅ **Issue at hosting provider** - Namecheap confirms problem is on Bear Blog's side, not DNS
5. ✅ **Timing remains suspicious** - Technical failure exactly 48 hours before APEC is implausible

**[Download full email evidence (EML format)](/assets/eml-files/emails/decoded/namecheap-support-confirmation-2025-10-25.eml)**

This registrar confirmation eliminates any legitimate legal explanation for the blocking, pointing to interference at the hosting provider level during the most politically sensitive window possible.

#### The AWS Explanation Doesn't Fit

**Update (October 26, 2025):** Our hosting provider (Bear Blog) initially suggested: "suspect this is a knock-on effect of the aws-east-1 outage. I'll be investigating."

However, **AWS service status records show this explanation is impossible:**

![AWS us-east-1 status showing no recent outages](/assets/images/aws-east-outages-10202025/aws-east-1-2025-10-25%2011-47-09.png)
*AWS Health Dashboard for us-east-1 region showing last incidents were October 20 (5 days before our traffic spike)*

**Why the AWS explanation doesn't work:**

1. ✅ **Last AWS us-east-1 incident**: October 20, 2025 (widespread, covered in mainstream news)
2. ✅ **Our traffic spike**: October 25, 2025, ~1:30 PM KST (5 days later)
3. ✅ **AWS status**: No incidents reported between October 20-26
4. ✅ **Hosting provider uncertainty**: Bear Blog representative said "I'll be investigating"—not confirming AWS as the cause, just speculating

**Technical timeline mismatch:**
- **October 20 AWS outage**: Widespread us-east-1 incident affecting many services
- **October 25 traffic spike**: Only `blog.genderwatchdog.org` affected; Bear Blog's own dashboard and other sites operational
- **5-day gap**: If this were AWS-related, why did it manifest 5 days after the AWS incident was resolved?

**Unanswered questions:**

1. Why did DNS records stop propagating from Namecheap's authoritative servers?
2. What changed between October 20-25 to make DNS propagation fail?
3. How did Bear Blog "rectify" an issue with DNS propagation he doesn't control (DNS is at registrar level, not hosting provider)?
4. Why did this occur **exactly** 48 hours before APEC, not during the actual AWS outage on October 20?

We have requested DNS server logs from Namecheap to understand the root cause.

#### **Update (October 28, 2025): Technical Cause Identified**

Bear Blog's developer confirmed the root cause: **bot traffic spike crashed the reverse proxy server** (affecting all custom domains globally, not just ours).

**Developer's statement:** "So while I can't entirely rule out foul play, I'm quite certain that this is just terrible timing."

**What this means:**
- ✅ Technical cause confirmed: Bot traffic overload
- ⚠️ Intentionality remains ambiguous ("can't entirely rule out foul play")
- 🌐 Part of larger AI scraping crisis affecting internet infrastructure globally

**The bigger story:** Whether natural or malicious, the bot spike revealed a global crisis of AI companies' ruthless data scraping crashing infrastructure—and Korea's $100 trillion bet to become a "top three AI nation" by 2027 raises urgent governance questions about institutional integrity, ethical data collection, and AI safety oversight.

**📊 [Full Analysis: Bot Traffic, AI Governance, and Korea's $100 Trillion Gambit →](/bot-traffic-ai-governance-korea/)**

---

## The Escalating Censorship Pattern: Three Attempts in 18 Days

**Update (October 26, 2025):** The traffic spike on October 25 was not the first incident—it was the **third escalation** in 18 days, each targeting our APEC-related documentation with increasing aggression.

**📊 [View Complete 6-Month Surveillance & Censorship Timeline →](/surveillance-censorship-timeline.html)**  
*Interactive timeline documenting systematic suppression from June through October 2025, with evidence links and pattern analysis.*

### October 7: APEC Engagement → Suppression → Evidence Cleanup

**The first incident** occurred when APEC Secretariat directly engaged with our content, then immediately suppressed it:

**Timeline:**
- **October 7, 2025**: APEC Secretariat **liked** our reply to their announcement of APEC Economic Leaders' Week in Gyeongju
- **23 minutes later**: Our reply **disappeared from under APEC's post** (became invisible as a reply while remaining accessible via direct URL)
- **Between Oct 7-10**: APEC **unliked** our post (evidence cleanup—the like notification was completely removed)

**What we documented:**

Our reply raised governance transparency and student safety concerns during Korea's hosting of APEC Leaders' Week in Gyeongju—the same city where we documented Dongguk WISE campus exploitation.

**The suppression pattern:**
1. ✅ **APEC officially engaged** - Liked our reply raising governance concerns
2. ❌ **Immediate suppression** - Reply became invisible under APEC's post within 23 minutes
3. ❌ **Evidence cleanup** - APEC removed their like, erasing notification
4. ✅ **Content still accessible** - Direct URL worked, only the reply connection was severed

**X.com documentation:** [Full thread with evidence →](https://x.com/Gender_Watchdog/status/1975429913491743188)

**Blog post:** [Institutional Capture in Korea (mentions APEC suppression) →](/institutional-capture-in-korea-exploitation-economy-governance-failures/)

**What this proved:** When our APEC-critical content received diplomatic validation (APEC's like), it was immediately disconnected from APEC's post—showing ability to censor even diplomatically-engaged content without deleting the original post.

---

### October 20: Substack Platform Censorship (Failed When Exposed)

**The second incident** escalated from social media suppression to platform-level content blocking.

**What Happened:**

**October 20, 2025, ~3:30 AM EST (12:30 PM KST):**

Both of our key Substack investigations became inaccessible, returning error pages:

1. **"APEC Leaders Will Meet in the Same City Where Students Are Forced to Share Dorms with Tourists"**
   - Documented Dongguk WISE exploitation in Gyeongju (APEC host city)
   - Same content as our blog post: [APEC Leaders Gather in Gyeongju](/apec-leaders-gather-in-gyeongjuwhere-dongguk-university-students-share-dorms-with-random-tourists/)

2. **"How Korea Herald Failed to Cover Court-Confirmed Hate Crimes"**
   - Documented systematic erasure of violence against non-Koreans in English-language press
   - Same content as our blog post: [The Two-Tier System](/the-two-tier-system-how-korean-english-language-press-erases-violence-against-non-koreans/)

**The Evidence:**

![Substack error page for APEC post showing "technical problems" message](/assets/images/substack-censorship-10202025/apec-leader-will-meet-in-same-gyeongju-2025-10-20%2003-31-18.png)
*Substack error page: "Substack is experiencing technical problems" for APEC Gyeongju post (October 20, 3:31 AM EST)*

![Substack error page for Korea Herald post showing "technical problems" message](/assets/images/substack-censorship-10202025/how-kh-failed-to-cover-hate-crimes-2025-10-20%2003-30-52.png)
*Substack error page: "Substack is experiencing technical problems" for Korea Herald coverage post (October 20, 3:30 AM EST)*

![Substack status page showing All Systems Operational](/assets/images/substack-censorship-10202025/substack-all-systems-operational-2025-10-20%2003-30-21.png)
*Substack's status page showing "All Systems Operational" at the exact same time (October 20, 3:30 AM EST)*

### The Technical Impossibility

**What made this suspicious:**

1. ✅ **Substack status page**: "All Systems Operational" with 100% uptime
2. ✅ **Only these two posts affected**: Our other Substack content remained accessible
3. ✅ **Confirmed across multiple devices**: 2 laptops, Android tablet with Substack app, multiple browsers
4. ✅ **Both posts about Korea**: APEC exploitation + systematic press failures
5. ✅ **Timing**: 7 days before APEC Economic Leaders' Week begins

### Public Documentation = Immediate Restoration

**Timeline:**

- **3:30 AM EST**: Posts become inaccessible
- **~5:30-5:45 AM EST**: We document the censorship publicly on X.com: [Thread Link](https://x.com/Gender_Watchdog/status/1980185668321218776)
- **~5:56 AM EST**: Posts suddenly accessible again (noticed at 6:06 AM)

**Total censorship duration:** ~2.5 hours  
**Time from public documentation to restoration:** 10-25 minutes

### What This Proved

The rapid restoration after public documentation proved:

1. **NOT a technical glitch** - Status showed "operational" entire time, other Substack posts worked
2. **Active monitoring** - Someone was monitoring X.com (either our account or @Substack mentions) at 5:30-6:00 AM on a Sunday morning
3. **Immediate authority** - Whoever was monitoring had authority to restore posts within minutes
4. **Intentional censorship reversed when exposed** - Restoration correlated with our public X.com thread, not with any platform status change

### Substack's Non-Response

We sent a detailed email to Substack requesting transparency on October 20:

> "Were these posts flagged or reported? If so, by whom and on what grounds? Did Substack receive any government requests (from South Korea or any other jurisdiction) regarding these posts?"

**[Read full email →](/assets/eml-files/emails/decoded/decoded_Request%20for%20Transparency_%20Posts%20Censored%20Then%20Restored%20Within%2015%20Minutes%20of%20Public%20Documentation%202025-10-20T07_00_03-04_00.eml)**

**Substack never responded.**

---

### October 25: Major Traffic Spike (AI Bot Activity)

**The third incident** involved a major traffic spike (most likely AI scrape bots, though Bear Blog admin notes foul play cannot be ruled out) when platform-level censorship failed.

This is the traffic incident documented throughout this post—occurring **exactly 48 hours before APEC** begins.

---

### The Three-Stage Escalation Pattern

**October 7** (20 days before APEC):
- ❌ Social media reply suppression (X.com context removal)
- ❌ Evidence cleanup (APEC unliked)
- ✅ **Content still accessible** via direct URL
- ✅ **Method**: Context disconnection (reply became invisible under APEC's post)

**October 20** (7 days before APEC):
- ❌ Platform content blocking (Substack posts inaccessible)
- ✅ Reversed when we documented it publicly (10-25 minutes)
- ✅ **Censorship failed** - content remained accessible after exposure
- ✅ **Method**: Platform-level blocking (but reversible when exposed)

**October 25** (48 hours before APEC):
- ❌ Major traffic spike (most likely AI scrape bots)
- ❌ **More aggressive** - caused service disruption at infrastructure level
- ❌ **Harder to address** - required migration to more resilient infrastructure
- ✅ **Method**: Traffic-based disruption (Bear Blog admin notes foul play cannot be ruled out)

**The escalation:** Each method failed or wasn't aggressive enough → escalated to next level as APEC approached.

### The October 20 Coincidence

**A suspicious detail:** Both the **Substack censorship** (3:30 AM EST) and the **AWS us-east-1 outage** happened on the same day: **October 20, 2025**.

- **Morning (3:30 AM EST)**: Our Substack posts blocked
- **Same day**: AWS us-east-1 widespread outage (covered in mainstream news)
- **6:00 AM EST**: Our Substack posts restored after public documentation
- **5 days later (October 25)**: Our Bear Blog experienced traffic spike, hosting provider cites "AWS knock-on effect"

**The timing raises questions:**

1. Why did Substack posts get blocked during an AWS outage day, then restored within hours?
2. Why did our Bear Blog domain fail 5 days *after* the AWS outage was resolved?
3. Could the October 20 AWS outage have provided cover for testing censorship methods?
4. Was the Substack blocking a trial run that failed (due to our immediate public documentation)?

**What we know:** When the October 20 Substack censorship was exposed publicly, it was reversed within minutes. When the October 25 traffic spike occurred, the hosting provider's explanation (AWS) pointed back to October 20—but AWS incidents don't manifest 5 days later, and our hosting provider is still investigating.

---

## Why the Timing Matters

### The APEC Connection

**What is APEC?**
- Asia-Pacific Economic Cooperation forum
- 21 member economies representing 60% of global GDP
- Leaders' Week is the year's most important diplomatic event for host country

**Why Gyeongju?**
- Official APEC Leaders' Week location: October 27-November 1, 2025
- Our documented exploitation: Dongguk WISE campus in **same city**
- Our evidence: Students forced to share "student housing" with tourists
- Our documentation: Campus president under criminal prosecution

**What we prepared:**
- Evidence packages for APEC delegations
- On-site verification information
- Documentation of ongoing exploitation
- Timeline showing 190+ days of institutional silence

**When domain was blocked:**
- **48 hours before APEC begins**
- Exactly when international delegations arrive in Gyeongju
- Perfect timing to suppress information about local institutional failures
- Surgical suppression during peak international scrutiny

### The Pattern

This isn't isolated—it's an **escalating series** of censorship attempts:

1. **April 2025**: We publish documentation → Institutions remain silent
2. **May 2025**: Sidus FNH (entertainment company) sends legal threats → We document and continue
3. **190+ days**: Canadian embassy, Korean government, university maintain silence
4. **October 7, 2025**: **First censorship attempt** - APEC Secretariat likes our reply raising governance concerns → 23 minutes later: reply becomes invisible under APEC's post → Sometime later: APEC unlikes (evidence cleanup)
5. **October 14, 2025**: Publish Dongguk WISE exploitation + Korea Herald coverage failure on Substack
6. **October 19-20, 2025**: Send evidence packages to APEC delegations, international press, Korean authorities
7. **October 20, 2025, 3:30 AM EST**: **Second censorship attempt** - Both Substack posts become inaccessible (7 days before APEC)
8. **October 20, 2025, ~6:00 AM EST**: Posts restored within 10-25 minutes after public documentation → **Censorship attempt failed**
9. **October 23, 2025**: APEC delegations begin arriving in Gyeongju
10. **October 25, 2025, ~1:30 PM KST**: **Third incident** - Major traffic spike at infrastructure level (most likely AI scrape bots, 48 hours before APEC)
11. **October 27, 2025**: APEC officially begins with international media present

**The three-stage escalation pattern:**
- **October 7**: Social media context suppression (reply disconnection) → Content still accessible via direct URL
- **October 20**: Platform content blocking (Substack) → Failed when publicly documented
- **October 25**: Major traffic spike (most likely AI bots) → Required migration to more resilient infrastructure

Each censorship method failed or wasn't aggressive enough → escalated to next level as APEC approached.

The suppression attempts correlate **exactly** with APEC timing and evidence distribution to APEC delegations—showing systematic targeting of documentation about institutional failures in the APEC host city.

---

## Why We Chose GitHub Pages

### The Censorship Resistance Hierarchy

**Bear Blog (Small indie hosting):**
- ✅ Excellent for starting out
- ✅ Simple, clean, fast
- ❌ Small scale = easy to pressure quietly
- ❌ Small team (Bear Blog) has limited resources to investigate or fight back
- ❌ No PR risk for suppressing one site

**GitHub Pages (Microsoft infrastructure):**
- ✅ $2+ trillion company with 100+ million users
- ✅ Any censorship becomes tech news instantly
- ✅ Public legal process required (DMCA transparency)
- ✅ Counter-notification rights protected
- ✅ Geopolitical leverage
- ✅ Streisand effect: Takedowns amplify the story

### What Censors Now Face

**Before (Bear Blog):**
- Quiet pressure possible
- No public record required
- Limited visibility
- Easy suppression

**Now (GitHub Pages):**
- Must pressure **Microsoft**, not individual developer
- Requires **public legal process** (GitHub transparency reports)
- Triggers **tech community response** (Hacker News, Reddit, tech press)
- Creates **international news**: "Microsoft pressured to censor sexual violence documentation"
- **Proves systematic censorship attempts** through public legal process
- Becomes **more expensive** politically than ignoring us

### The Microsoft Factor

GitHub is owned by Microsoft. Censoring content on GitHub Pages means:
- Targeting a US company with massive geopolitical leverage
- Creating precedent that affects thousands of projects globally
- Generating immediate tech industry backlash
- Confirming censorship allegations in most visible way possible

**Any takedown attempt now requires:**
1. Valid legal basis (not just "we don't like this")
2. Public documentation via GitHub transparency reports
3. International legal process (US courts, not just Korean)
4. Consequences for false DMCA claims
5. Counter-notification process

**This is exactly what censors wanted to avoid.**

---

## What This Migration Proves

### Censorship Attempt = Evidence

The migration itself documents:

1. **Institutional panic**: Why else block a domain 48 hours before APEC?
2. **Coordination**: Timing this precise requires planning
3. **Intent**: Suppressing information during diplomatic event
4. **Confirmation**: Everything we documented about institutional capture is validated

**The censorship attempt is now part of the evidence.**

### Strategic Strength

**Before:**
- "We document institutional failures in Korea"

**Now:**
- "We document institutional failures in Korea **AND survived targeted censorship 48 hours before APEC**"

**We just got stronger, not weaker.**

### Multiple Mirrors = Resilience

We now maintain:
1. **Primary**: `blog.genderwatchdog.org` (GitHub Pages) ← **You are here**
2. **Mirror**: `genderwatchdog.bearblog.dev` (Bear Blog)
3. **Timeline**: `genderwatchdog.org` (GitHub)
4. **Evidence**: `github.com/Gender-Watchdog/genderwatchdog_metookorea2025`

If they take down GitHub, that requires:
- Public legal process
- International news coverage
- Confirmation of censorship
- Proof of institutional panic

**Each suppression attempt makes the story bigger.**

---

## What We're Doing Now

### Documentation

1. **This post**: Public record of censorship attempt
2. **Technical logs**: DNS records, registrar confirmations, timestamps
3. **Screenshots**: Working site → blocked domain → restored on GitHub
4. **Timeline**: Correlation analysis with APEC schedule
5. **Correspondence**: Letters to EFF, RSF, press freedom organizations

### Notifications

Sent evidence packages to:
- Electronic Frontier Foundation (EFF)
- Reporters Without Borders (RSF)
- Tech press contacts
- Press freedom organizations
- Academic freedom advocates
- International student safety organizations

### Transparency

All documentation:
- Posted publicly on this site
- Archived in evidence repository
- Shared with press freedom organizations
- Made available to journalists
- Preserved for potential litigation

**We're not hiding. We're documenting.**

---

## Why Censorship Failed

### The Streisand Effect

By blocking our domain, they:
1. Confirmed our documentation is accurate (why else suppress?)
2. Created news story: Censorship attempt itself
3. Generated international interest: APEC timing too obvious
4. Forced migration to more resilient infrastructure
5. Made suppression more expensive going forward

**Quiet suppression is now impossible.**

### Tech Community Support

Response from tech community:
- DNS propagation monitoring
- Archive.org backups
- Mirror hosting offers
- Legal resource referrals
- Documentation assistance

**We're not alone.**

### Institutional Validation

The censorship attempt validates:
- Our methodology (they fear accurate documentation)
- Our timing (APEC correlation proves sensitivity)
- Our impact (wouldn't suppress if ineffective)
- Our concerns (institutional capture confirmed by behavior)

**Actions speak louder than denials.**

---

## What This Means for Survivors

### Silencing Pattern

**What they wanted:**
- Quiet suppression during APEC
- No international scrutiny in Gyeongju
- Victims' testimonies disappear
- Documentation becomes inaccessible
- Institutional failures hidden from delegations

**What they got:**
- Public censorship documentation
- International press freedom advocacy
- More resilient infrastructure
- Confirmation of institutional panic
- Amplified visibility

### Protection Through Transparency

**Survivors who shared testimonies on our platform:**

You are not silenced. Your stories are:
- Preserved in multiple archives
- Documented publicly
- Shared with advocacy organizations
- Protected by censorship-resistant infrastructure
- Validated by institutional reaction

**The censorship attempt proves your stories matter.**

### Continued Documentation

We continue to document:
- Sexual violence in Korean universities
- Institutional cover-ups
- Falsified partnerships
- Corporate-academic exploitation
- Government complicity
- Press failures
- Diplomatic silence

**Now from infrastructure they can't quietly suppress.**

---

## Technical Details of Migration

### DNS Configuration

**Old setup (Bear Blog):**
```
blog.genderwatchdog.org → domain-proxy.bearblog.dev
```

**New setup (GitHub Pages):**
```
blog.genderwatchdog.org → gender-watchdog.github.io
```

### Features Maintained

- ✅ All 205 blog posts migrated
- ✅ 6 language archives (en, ko, ja, zh-cn, zh-tw, other)
- ✅ SEO optimization (meta tags, structured data)
- ✅ Multi-language support (CJK fonts, hreflang tags)
- ✅ Privacy-focused analytics (Fathom, GDPR compliant)
- ✅ Custom domain (blog.genderwatchdog.org)
- ✅ HTTPS enforcement (Let's Encrypt)
- ✅ Responsive design
- ✅ Archive functionality

### Features Enhanced

- ✅ **Censorship resistance**: GitHub transparency requirements
- ✅ **Legal protection**: Counter-notification rights
- ✅ **Geopolitical leverage**: Microsoft backing
- ✅ **Public record**: Any takedown becomes news
- ✅ **Tech community oversight**: Immediate visibility of suppression attempts

---

## Lessons for Other Activists

### Infrastructure Matters

**Don't wait for censorship to start:**
1. Use censorship-resistant infrastructure from day one
2. Maintain multiple mirrors automatically
3. Document everything publicly
4. Build relationships with press freedom orgs
5. Understand legal protections in different jurisdictions

**GitHub Pages advantages:**
- Free hosting
- Custom domains supported
- HTTPS automatic
- Public legal process required for takedowns
- Tech community monitoring
- Geopolitical complexity for censors

### Documentation Protects

**What saved us:**
- Immediate technical documentation
- Public transparency about suppression
- Evidence preservation
- Press freedom organization contacts
- Community support networks

**What makes censorship expensive:**
- Public record of attempts
- Technical proof of interference
- Timing analysis showing coordination
- International advocacy connections
- Platform transparency requirements

### The Paradox of Suppression

**Every censorship attempt:**
- Validates the documentation
- Amplifies the message
- Expands the audience
- Proves institutional guilt
- Creates news stories
- Builds solidarity

**Censorship is evidence.**

---

## Message to Institutions

### You Made It Worse

**Before the censorship attempt:**
- We were documenting institutional failures
- Reaching existing audience
- Operating quietly and methodically
- Building evidence systematically

**After the censorship attempt:**
- We're documenting institutional failures **AND censorship**
- Reaching press freedom organizations globally
- Operating on infrastructure you can't quietly suppress
- With evidence that includes your suppression attempt

**You validated everything we documented.**

### The Inevitable Documentation

Every action you take is documented:
- Legal threats → Archived and published
- Traffic spikes → Technical logs preserved
- APEC timing → Correlation analysis public
- Government silence → 190+ days documented
- Press complicity → Coverage gaps tracked

**You can't suppress what's already preserved in multiple locations.**

### What Accountability Looks Like

We're not going anywhere. This site now operates on:
- ✅ Microsoft infrastructure (harder target)
- ✅ With public legal oversight (transparency required)
- ✅ International press freedom backing (advocacy support)
- ✅ Tech community monitoring (suppression becomes news)
- ✅ Multiple mirrors (resilience built-in)

**Accountability is now censorship-resistant.**

---

## Moving Forward

### What Hasn't Changed

- Documentation continues
- Evidence preservation ongoing
- Survivor support maintained
- International advocacy active
- Multiple mirrors operational

### What Has Changed

- **Infrastructure**: More resilient
- **Visibility**: Higher (censorship attempt is news)
- **Support**: Expanded (press freedom orgs engaged)
- **Protection**: Stronger (legal oversight required)
- **Validation**: Confirmed (institutional panic proves accuracy)

### What's Next

1. **Continue documentation** of institutional failures
2. **Expand evidence** packages for APEC delegations (now with censorship docs)
3. **Collaborate** with press freedom organizations
4. **Support survivors** sharing testimonies
5. **Document** any additional censorship attempts
6. **Build** more resilient infrastructure for activist journalism

---

## Conclusion: Censorship as Validation

**They tried to silence us 48 hours before APEC.**

**Instead, they:**
- Confirmed our documentation is accurate
- Created an international censorship story
- Forced us onto more resilient infrastructure
- Validated institutional panic
- Proved systematic suppression

**The censorship attempt is now part of the evidence.**

We're now on infrastructure that requires public legal process for any takedown. We have press freedom organizations monitoring. We have tech community support. We have multiple mirrors.

**Every suppression attempt from here requires:**
- Public documentation
- International legal process
- Geopolitical consequences
- Tech industry scrutiny
- Confirmation of everything we've documented

**You made us stronger.**

---

## Resources & Links

**This Site:**
- [English Posts](/en/)
- [All Languages](/) (en, ko, ja, zh-cn, zh-tw, other)
- [6-Month Surveillance & Censorship Timeline](/surveillance-censorship-timeline.html) ← **New**
- [About Gender Watchdog](/about/)
- [Contact Us](/contact/)

**Evidence Archive:**
- [GitHub Repository](https://github.com/Gender-Watchdog/genderwatchdog_metookorea2025)
- [Timeline Website](https://genderwatchdog.org)
- [Bear Blog Mirror](https://genderwatchdog.bearblog.dev)

**Support:**
- [End Rape On Campus (EROC)](https://twitter.com/EndRapeOnCampus)

**Press Freedom:**
- [Electronic Frontier Foundation](https://www.eff.org)
- [Reporters Without Borders](https://rsf.org)

---

**Built with Jekyll • Hosted on GitHub Pages • Censorship-Resistant by Design**

*"They tried to silence us before APEC. We migrated to infrastructure that makes silence impossible."*

*"Transparency protects survivors. Censorship protects perpetrators."*

*"The migration itself is evidence."*

© 2025 Gender Watchdog Research Collective. All rights reserved.

---

**Update Log:**
- **October 25, 2025, ~1:30 PM KST**: Major traffic spike detected (service disruption)
- **October 25, 2025, 8:00 PM KST**: Site successfully migrated to GitHub Pages
- **October 25, 2025, 8:30 PM KST**: DNS propagated globally
- **October 25, 2025, 9:00 PM KST**: All 205 posts verified accessible
- **October 25, 2025, 9:30 PM KST**: Press freedom organizations notified
- **October 26, 2025, 4:30 AM UTC**: Post updated with three-stage escalation pattern documentation: October 7 APEC X.com suppression, October 20 Substack censorship, October 25 traffic spike. Added AWS explanation analysis.
- **October 27-November 1, 2025**: APEC Leaders' Week proceeds with our documentation now censorship-resistant
- **October 28, 2025, 10:00 AM UTC**: Post updated with technical investigation results: Bot traffic spike crashed reverse proxy server. Developer: "Can't entirely rule out foul play" but "terrible timing." Added link to AI governance analysis.

**The work continues.**

