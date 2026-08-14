# Northstar Support Deflection MVP: Go-Live Readiness Note

**Project**: Support Deflection Chatbot  
**Team**: Pod G29 (Caroline, Victor, Saudah, Meshack, Ian)  
**Date**: August 2026  

---

## 1. Executive Summary
This MVP provides an automated, self-serve chat interface designed to deflect two of Northstar's highest-volume support ticket categories: **Order Status** and **Returns & Refunds**. By routing clear queries directly to automated lookup functions and gracefully handing off complex queries to human agents, this prototype demonstrates a scalable approach to reducing manual ticket handling.

## 2. What Works (Demoable End-to-End)
* **Chat Interface**: A lightweight, responsive web chat widget where users can submit questions.
* **Intent Routing Engine**: Keyword-based parsing successfully categorizes user input into three buckets: `order_status`, `returns`, or `unmatched`.
* **Order Status Lookup**: Simulates database retrieval by fetching mock order statuses (Processing, Shipped, Delivered) using the `orders.json` dataset.
* **Returns Eligibility Engine**: Simulates policy checks based on item categories (Electronics, Accessories, Software) using the `return_policies.json` dataset.
* **Fallback Handoff**: Any query outside the defined scope (or unclear queries) correctly triggers a polite hand-off message, preparing the user for human agent intervention without a system crash.

## 3. What's Known-Broken / Limitations
* **Strict Keyword Dependency**: The intent router currently relies on exact substring matches (e.g., "order", "status", "return"). It does not yet leverage NLP (Natural Language Processing) to handle typos or complex phrasings.
* **Hardcoded Datasets**: The lookup functions query static `.json` files. Real-time connections to Northstar's live inventory and order management systems (OMS) are not yet implemented.
* **Session Persistence**: The chat window loses conversation history upon page refresh.

## 4. Handoff Guide for Northstar Engineering
To pick this up and transition it to a production environment, Northstar's team should execute the following steps:

1. **Environment Setup**: 
   - Pull the repository: `git clone <https://github.com/kiplah/northstar-support-deflection-mvp.git>`
   - Install dependencies: `pip install -r requirements.txt`
   - Run the development server: `python app.py`
2. **Backend Integration**: Replace the JSON reads in `services/order_service.py` and `services/returns_service.py` with API calls to the Northstar OMS database.
3. **NLP Upgrade**: Swap out the keyword matching in `services/intent_router.py` with an NLP provider (e.g., Dialogflow, OpenAI) to improve routing accuracy.
4. **Deploy**: Containerize the Flask application (Docker) and deploy behind a production WSGI server (like Gunicorn) on your preferred cloud provider.
