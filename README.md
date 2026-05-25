# AI Technical Support Assistant

## Project Overview
AI-powered technical support assistant designed to automate customer support workflows using NLP, sentiment analysis, escalation logic, and KPI analytics.

## Features

- AI-assisted support query retrieval using TF-IDF and cosine similarity
- Query enrichment and text normalization workflow
- Knowledge-base response matching for customer support queries
- Escalation workflow handling for uncertain or unmatched queries
- Support ticket preprocessing and operational workflow analysis
- KPI dashboard for customer support operations analytics
- Ticket priority, status, and unresolved workload analysis
- Customer satisfaction and support channel analysis

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Matplotlib
- Seaborn

## Repository Structure

notebooks/
├── eda.ipynb
├── kb_retrieval_system.ipynb
├── support_kpi_dashboard.ipynb

data/
├── model_ready_kb.csv
├── support_df_sample.csv

README.md

## Future Improvements

- Workflow simulation and escalation automation
- Semantic search using embeddings
- Streamlit deployment
- Real-time support analytics dashboard
- Automated ticket routing
- LLM-assisted support response generation

## Project Status
Currently in development.

## Current Progress

- Performed exploratory data analysis (EDA) on customer support ticket datasets
- Built NLP preprocessing pipeline including text cleaning and normalization
- Evaluated baseline ticket classification model and identified dataset label inconsistencies
- Shifted project architecture toward knowledge-base retrieval and support workflow automation
- Implemented TF-IDF and cosine similarity based knowledge-base retrieval
- Added query enrichment workflow to improve indirect customer query matching
- Implemented escalation handling for uncertain support queries
- Developed operational KPI dashboard for support workflow analytics
- Performed ticket status, priority, unresolved workload, and customer satisfaction analysis
- Added operational insight reporting and KPI summary analytics


