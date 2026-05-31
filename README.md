# AI Financial Intelligence Platform

An AI-powered financial analytics platform built using PhonePe Pulse transaction data, Google Gemini, and Retrieval-Augmented Generation (RAG).

The platform combines data analytics, interactive dashboards, financial intelligence generation, and AI-powered question answering to help users explore India's digital payments ecosystem.

## Live Demo

https://phonepe-pulse-a6gukgup9ph9bqqxfpvdu8.streamlit.app/

---

## Key Features

### Financial Analytics Dashboard

* Transaction analysis across India
* State-wise transaction insights
* District-level payment activity
* User growth and engagement analysis
* Transaction trend visualization
* Interactive geo-mapping with Plotly

### AI Insights Engine

Automatically generates:

* Financial summaries
* Market observations
* Growth analysis
* User behavior insights
* Business recommendations

### AI Financial Copilot

Natural language financial assistant capable of answering questions such as:

* Which states are growing fastest?
* Which transaction categories dominate?
* What business opportunities exist in Q1 2024?
* Which districts have the highest transaction activity?
* What trends are emerging in digital payments?

### RBI Knowledge Assistant (RAG)

Built using:

* RBI Annual Reports
* PDF Processing
* Sentence Embeddings
* ChromaDB Vector Database
* Semantic Search
* Google Gemini

Example Questions:

* What does RBI say about digital payments?
* What initiatives support financial inclusion?
* How is RBI promoting digital payment adoption?

---

## Architecture

PhonePe Pulse Data

↓

SQLite Database

↓

Analytics Layer

↓

AI Insights Engine

↓

Financial Copilot

↓

RAG Pipeline

↓

RBI Knowledge Base

---

## Tech Stack

### Data & Analytics

* Python
* Pandas
* SQLite

### Visualization

* Streamlit
* Plotly

### AI & LLM

* Google Gemini 2.5 Flash
* Prompt Engineering

### RAG Stack

* PyPDF
* Sentence Transformers
* ChromaDB
* Vector Embeddings
* Semantic Search

### Deployment

* GitHub
* Streamlit Community Cloud

---

## AI Pipeline

### Analytics Copilot

User Question

↓

Intent Detection

↓

Data Retrieval

↓

Prompt Construction

↓

Gemini

↓

Financial Insight

### RAG Pipeline

User Question

↓

Embedding Generation

↓

ChromaDB Retrieval

↓

Relevant RBI Chunks

↓

Gemini

↓

Grounded Response

---

## Example Questions

### Analytics

* Which states are growing fastest?
* Which transaction categories dominate?
* What business opportunities exist in Q1 2024?
* Which districts process the highest transaction volume?

### RBI Knowledge Base

* What does RBI say about digital payments?
* What initiatives support financial inclusion?
* What are RBI's priorities for the future of payments?

---

## How to Run

### Clone Repository

```bash
git clone <repository-url>
cd PhonePe-Pulse
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## Project Highlights

* Built an end-to-end AI-powered financial intelligence platform.
* Integrated Google Gemini for financial reasoning and insight generation.
* Implemented Retrieval-Augmented Generation (RAG) using RBI reports.
* Developed a vector search pipeline using ChromaDB and sentence embeddings.
* Designed a financial copilot capable of answering analytics and knowledge-based questions.
* Deployed the complete application to Streamlit Cloud.

---

## Future Improvements

* Multi-document RAG
* Real-time financial news integration
* Agentic AI workflows
* Automated report generation
* Forecasting and predictive analytics
* LangGraph-based financial agents

---

## Author

Akash Ravuru

Aspiring AI Engineer | Data Analyst | Musician

Building real-world AI systems through hands-on projects.
