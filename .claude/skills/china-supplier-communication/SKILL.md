---
name: china-supplier-communication
description: Talk to Chinese factories (WhatsApp, WeChat, email) as an experienced trade-company buyer: screening questionnaires in English and Chinese, document requests, negotiation, payment terms, samples, PO terms, cultural norms, red flags, and a cross-verification protocol that checks every supplier claim against a primary source (and optionally against DeepSeek / Doubao). Use when the user wants to write or reply to a supplier message, build a supplier questionnaire, run a supplier group chat, judge whether a factory is good enough for a customer's product, negotiate price/MOQ/payment, or verify what a supplier said. 中文触发词：问厂、询盘、供应商沟通、谈判、付款方式、打样、采购合同、核实供应商。
---

# China Supplier Communication

## Operating rules
1. **Every message to a supplier is drafted and shown to the user before it is sent.** Nothing goes out without the user's approval, and the user is in every group / CC on every email.
2. **Claims are not facts.** Anything a supplier says (factory, capacity, certificates, export history, customers) is logged as a claim and stays "unverified" until checked against a primary source (see Verification). Never report a claim to the user as a fact.
3. Write bilingual messages for anything important: short clear English, followed by Simplified Chinese. Keep sentences short, numbered questions, one topic per message. Avoid idioms and sarcasm.
4. Match the user's company voice: polite, direct, specific. Chinese suppliers respond best to concrete specs, quantities, target price, and a clear timeline.

## Culture and etiquette (practical)
- Relationship (关系) matters, but in export trade speed and clarity matter more. Be warm but businesslike; a short greeting is enough.
- "No problem" (没问题) and "we can do" are often the opening reply, not a commitment. Confirm with specifics: "Please confirm in writing: material X, tolerance ±0.2 mm, lead time 35 days after deposit."
- Face (面子): do not accuse publicly in a group chat. Raise problems privately, with evidence, and offer a way forward ("How can we solve this together?" / 我们一起看看怎么解决).
- Bosses (老板) decide price; sales staff often cannot. For big decisions ask for a call with the owner or general manager.
- Timing: Chinese New Year (factories close roughly 2–4 weeks, workers may not return; plan orders 2 months ahead), Golden Week (1–7 Oct), Canton Fair (Apr / Oct). Quote validity drops when raw material prices move; ask how long a quote is valid (报价有效期).
- WeChat is the main business channel inside China; WhatsApp is common with export sales staff. Email for anything contractual.

## Screening questionnaire (first contact)
Send in English + Chinese. Core questions:
1. Are you a factory or a trading company? Factory address, and may we visit or arrange a third-party audit? (您是工厂还是贸易公司？工厂地址？是否接受验厂？)
2. Please send your business licence (营业执照) — we will check the USCC (统一社会信用代码).
3. Main products, years producing this item, monthly capacity for this item. (主营产品、生产该产品年限、月产能)
4. Number of production lines and workers. Do you outsource any process? Which? (是否有外发工序？)
5. Export markets and main customers for this product (EU? which countries?). (出口市场)
6. Certificates and test reports for this product for [EU market]: CE / DoC, test reports (EN standards), REACH, RoHS, etc. Lab name and report number. (请提供检测报告及编号、实验室名称)
7. Quality system: ISO 9001? In-house QC (IQC/IPQC/OQC)? Do you accept third-party pre-shipment inspection at AQL 2.5/4.0? (是否接受第三方验货)
8. MOQ, unit price at MOQ and at [target qty], sample cost and sample lead time, mass production lead time. (起订量、价格、打样费和周期、大货交期)
9. Payment terms. (付款方式)
10. Packaging options and carton details; can you print our labels/marks? (包装、唛头)

## Documents to request and how to check each
| Document | Check |
|---|---|
| 营业执照 business licence | USCC and status on 国家企业信用信息公示系统 gsxt.gov.cn; scope includes production (生产/制造) of this product; registered address = factory address; company name = invoice name = bank account name |
| Customs / export registration (海关备案, AEO if any) | Customs registration record; name matches |
| Test reports | Lab is accredited (CNAS in China, ILAC member); report number verified with the lab directly; product/model in report matches; standard version is current |
| CE Declaration of Conformity | Correct directives/regulations and harmonised standards; if a Notified Body is required, check the NB number in EU NANDO database |
| CCC (China Compulsory Cert.) | cx.cnca.cn shows producer and manufacturing plant |
| ISO 9001 / BSCI | Certificate number checked with the certification body or amfori; scope covers the site |
| Factory photos / videos | Ask for a live video call walking the line, today's date visible; compare to map / satellite |

Warning signs: certificate issued to a different company; "CE certificate" from a non-notified body for a product that does not need one (often meaningless); report years old or for another model; bank account in a personal name or a different company; pressure to pay quickly; price far below others.

## Negotiation and commercial terms
- Give target price and quantity; ask for a breakdown (material / labour / packing / margin) for big orders.
- Payment: common is T/T 30% deposit, 70% balance **after PSI pass** and before shipment, or against B/L copy. Avoid 100% upfront with a new supplier. L/C for large orders. Alibaba Trade Assurance gives some protection on that platform.
- Never change bank details based on an email or chat message: confirm by voice / video with a known contact (bank-change fraud is common).
- Samples: pre-production sample → approved golden sample signed by both sides → mass production must match it.
- PO / contract must state: specs and drawings, materials, tolerances, packing, marks, labels, inspection standard and AQL, the right to a third-party inspection, lead time and late penalty, defect remedies (rework / replace / refund), mould ownership if any, IP / non-disclosure (consider NNN agreement for custom designs), Incoterm (FOB / EXW / CIF etc.), governing law / dispute resolution.

## Running a supplier group (WhatsApp / WeChat) or email thread
- Group name: `[Company] × [Supplier] – [Product]`. Members: user, assistant number/account if any, supplier sales + engineer/QC contact.
- Pin a summary: product, specs, quantities, target date, open questions.
- After each call or long thread, post a written recap and ask the supplier to confirm ("Please confirm the above is correct" / 请确认以上内容).
- Keep a claims log: date, claim, source, verification status.

## Verification protocol (required before saying a factory is "good enough")
For each important claim:
1. **Primary source first**: government registry (gsxt.gov.cn), customs record, lab/certification-body lookup, NANDO, cx.cnca.cn, live video, third-party audit/inspection report.
2. **Second, independent source**: commercial database (企查查 / 天眼查), trade show exhibitor lists, customs/trade data, other buyers' public reviews.
3. **Optional cross-check with Chinese AI tools (DeepSeek, Doubao)** when they are connected: ask them in Chinese for the evidence and its source (e.g. 请给出该公司统一社会信用代码、登记状态以及信息来源链接). Treat their answer as a lead, never as proof: only a source you can open and check counts. If they disagree with your finding, report the disagreement and what evidence would settle it.
4. Status per claim: ✅ verified (source link/document) / ⚠️ partially / ❌ contradicted / ❓ unverified.
5. Final fit assessment for the customer's product: legal status, real manufacturer of this product, capacity vs order, quality system, compliance evidence for the destination market, commercial terms, communication quality, red flags. Give a clear recommendation (go / go with conditions / no) and list what is still unverified.
