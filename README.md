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
- Identified dataset inconsistencies and shifted project direction from pure ticket classification toward retrieval-based support automation
- Built NLP preprocessing pipeline including text cleaning, normalization, stopword handling, and query enrichment
- Implemented TF-IDF vectorization and cosine similarity based knowledge-base retrieval system
- Developed confidence-based workflow routing for automated response handling and escalation simulation
- Added query enrichment logic to improve indirect intent matching and account/login related retrieval accuracy
- Built workflow simulation engine for AI-assisted customer support operations
- Generated augmented customer query datasets to simulate realistic operational support traffic
- Developed workflow logging system to capture query behavior, confidence scores, routing decisions, and retrieval outcomes
- Performed workflow analytics on 650 simulated support interactions
- Implemented operational KPI tracking including AI resolution rate, escalation rate, and similarity score monitoring
- Built workflow visualizations for decision distribution and confidence score analysis
- Conducted escalation analysis to identify support categories with high uncertainty and escalation frequency
- Developed support KPI analytics dashboard covering ticket status, priority distribution, unresolved workload, and customer satisfaction trends
- Added operational findings, workflow limitations, and future system improvement recommendations
- Established foundational architecture for an AI-assisted support operations platform combining retrieval systems, workflow automation, escalation handling, and operational analytics
  


