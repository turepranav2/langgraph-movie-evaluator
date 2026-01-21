# Multi-Agent LangGraph Movie Evaluator

This project implements a LangGraph-based multi-agent workflow to evaluate a movie synopsis.

## Workflow
1. The synopsis is classified into a primary genre.
2. Execution is conditionally routed to a genre-specific evaluator.
3. The evaluator scores the synopsis on story and character quality.
4. An aggregator computes the final score and provides reasoning.

## Technologies Used
- LangGraph
- Google Gemini (LLM)

## How to Run

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY=your_api_key_here
python main.py