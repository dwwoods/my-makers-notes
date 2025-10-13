# Reflections on 3 Oct

## AI Workshop

Link to miro board - https://miro.com/app/board/uXjVJ_FnQ1k=/

Eddie Andress (facilitator) recommended:
* Robert Miles AI videos
* Thinking fast and Slow - Daniel Kahneman [Amazon Link](https://www.amazon.co.uk/Thinking-Fast-Slow-Daniel-Kahneman/dp/0141033576/ref=asc_df_0141033576?mcid=cf580ab98b2039838f3039821818c08d&th=1&psc=1&tag=googshopuk-21&linkCode=df0&hvadid=697305168860&hvpos=&hvnetw=g&hvrand=4343861268828415484&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9219078&hvtargid=pla-394582189334&psc=1&hvocijid=4343861268828415484-0141033576-&hvexpln=0&gad_source=1)


### Workshop Summary: Risks in Software and AI Safety

This document provides a summary of key topics related to risk management in software development, with a special focus on the unique challenges presented by Artificial Intelligence.

---

### Introduction: About Risks

This section covers the fundamental concepts of identifying, analysing, and mitigating risks in a typical software project.

#### What are Risks in software?

A **risk** is a potential problem that could negatively affect a project. It's defined by two components: **Likelihood** (how likely it is to happen) and **Impact** (how bad it will be if it does).

A simple way to express this is the formula:
$$Risk = Likelihood \times Impact$$

Risks can be categorised as:
* **Technical Risks:** Problems with the technology itself (e.g., a database failing to scale).
* **Project Management Risks:** Issues with the project's execution (e.g., scope creep, budget overruns).
* **Operational Risks:** Problems after deployment (e.g., server downtime, security breaches).
* **Business Risks:** External threats (e.g., a competitor's actions, new regulations).

#### About Risk Analysis

Risk analysis is the process of evaluating and prioritising identified risks to focus resources effectively.

* **Qualitative Analysis:** Uses a descriptive scale (Low, Medium, High) to plot risks on a **Risk Matrix** or heat map. This is a quick way to identify the most critical threats.
* **Quantitative Analysis:** Assigns numerical values to risk. For example, calculating the annual **Risk Exposure** by multiplying the probability of an event by its potential financial cost ($Probability \times Cost$).

#### About Risk Mitigation

Mitigation involves choosing a strategy to deal with an identified risk. The common strategies are known as the "4 Ts":

1.  **Treat (Reduce):** Take action to lower the risk's likelihood or impact (e.g., add security patches).
2.  **Transfer (Share):** Shift the risk to a third party (e.g., buy insurance or use a cloud provider for infrastructure).
3.  **Tolerate (Accept):** Consciously decide to do nothing, typically for low-priority risks where the fix is more costly than the potential damage.
4.  **Terminate (Avoid):** Eliminate the risk by not performing the activity that causes it (e.g., not collecting sensitive data to avoid privacy risks).

#### Do we have to fix every risk?

No. It's a strategic decision based on:
* **Cost vs. Benefit:** It's not worth spending £1,000 to fix a risk that has a potential impact of £100.
* **Limited Resources:** Teams must prioritise their time and money on the most significant risks.
* **Risk Appetite:** Different organisations have different levels of comfort with risk.

#### Why AI risks are especially interesting

AI introduces new, complex risks beyond those in traditional software:

* **The "Black Box" Problem:** It can be difficult to understand *why* a complex AI made a certain decision.
* **Data-Driven Risks:** Biases in training data can lead to biased and unfair AI behaviour.
* **Adversarial Attacks:** Malicious actors can create inputs designed to fool an AI system.
* **Ethical & Societal Risks:** AI poses broader challenges like job displacement and surveillance.
* **Hallucinations:** Generative AI can confidently present false information as fact.

---

### Group 3: Safety (Emerald) - A Deep Dive

This section focuses specifically on safety problems in AI-controlled systems and strategies for their mitigation.

#### What sort of safety problems might occur with systems which are built or controlled using AI?

* **Unpredictable & Unintended Behavior:** An AI might achieve its goal in a harmful way its creators didn't anticipate (the **alignment problem**).
    * *Example:* A navigation AI, told to find the "fastest route," directs a user through a dangerous area.
* **Bias and Unfairness:** Biased training data can lead to systems that are unsafe for certain groups.
    * *Example:* A medical AI is less accurate at diagnosing a disease in a specific demographic due to a lack of representative data.
* **Adversarial Attacks:** External actors can manipulate AI inputs to cause dangerous failures.
    * *Example:* A self-driving car's vision system is tricked by subtle alterations to a road sign, causing it to misinterpret a critical instruction. 
* **Overconfidence in Errors ("Hallucinations"):** An AI can generate dangerously incorrect information with high confidence.
    * *Example:* An AI assistant for a pilot provides incorrect landing parameters.
* **Loss of Human Control:** Autonomous systems could make rapid, cascading decisions that are too fast for humans to intervene in.
    * *Example:* An automated power grid controller misinterprets a sensor reading and causes a widespread blackout.

#### How might you mitigate (reduce the risk) of safety problems within AI?

* **Robustness Testing and Validation:** Go beyond standard tests by using **adversarial testing** (actively trying to fool the AI) and stress testing it with unexpected data.
* **Explainable AI (XAI):** Use techniques that make an AI’s decision-making process transparent. If you know *why* a decision was made, you can better predict and correct unsafe behavior.
* **Human-in-the-Loop (HITL) Oversight:** For high-stakes decisions, require a human to review and approve the AI's output. The AI assists, it doesn't decide.
    * *Example:* An AI flags a potential issue in an aircraft engine, but a human engineer makes the final call on maintenance.
* **Data Governance and Bias Audits:** Implement rigorous processes to clean training data, actively search for and correct biases, and ensure it is representative of the real world.
* **Formal Frameworks and Red Teaming:** Adopt established risk frameworks (like the **NIST AI RMF**) and create internal "Red Teams" whose job is to find safety flaws before the system is deployed.