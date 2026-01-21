# LangGraph Movie Synopsis Evaluator

This project implements a LangGraph-based multi-agent workflow to evaluate a movie synopsis using a Large Language Model (Google Gemini).

The system classifies the genre of a movie synopsis and conditionally routes the execution to a genre-specific evaluator. Each evaluator scores the synopsis based on story quality and character depth, and a final aggregator computes the overall score with reasoning.

---

## Architecture Overview

1. Genre Classification  
2. Conditional Routing  
3. Genre-Specific Evaluation  
4. Score Aggregation  
5. Final Output Generation  

The workflow is modeled as a stateful graph using LangGraph.

---

## Technologies Used

- Python
- LangGraph
- Google Gemini (LLM)
- python-dotenv

---

## Project Structure

langgraph-movie-evaluator/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── venv/


---

## Setup Instructions

1. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\Activate.ps1


2. Install dependencies:
pip install -r requirements.txt


3. Create a `.env` file and add your API key:
GOOGLE_API_KEY=your_api_key_here


4. Run the application:
python main.py


---

## Output

The program prints:
- Detected genre
- Story score
- Character score
- Final aggregated score
- Reasoning behind the evaluation

---

## Key Concepts Demonstrated

- Stateful graph-based orchestration
- Conditional routing using LangGraph
- Multi-agent evaluation pattern
- Deterministic aggregation logic
- Clean separation of responsibilities

---

## Notes

- The `.env` file and virtual environment are excluded from version control.
<<<<<<< HEAD
- The implementation strictly follows the provided task document.
=======
- The implementation strictly follows the provided task document.
>>>>>>> 43449b2 (Finalize LangGraph movie evaluator with conditional routing and aggregation)
