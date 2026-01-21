from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-flash-latest")


class GraphState(TypedDict):
    synopsis: str
    genre: str
    story_score: float
    character_score: float
    final_score: float
    reasoning: str


def genre_classifier(state: GraphState) -> GraphState:
    prompt = f"""
Classify the genre of the following movie synopsis into one of:
Drama, Thriller, Comedy.

Synopsis:
{state['synopsis']}

Respond with only the genre name.
"""
    response = model.generate_content(prompt)
    genre = response.text.strip()

    return {**state, "genre": genre}


def drama_evaluator(state: GraphState) -> GraphState:
    return {**state, "story_score": 8.4, "character_score": 8.0}


def thriller_evaluator(state: GraphState) -> GraphState:
    return {**state, "story_score": 8.2, "character_score": 7.6}


def comedy_evaluator(state: GraphState) -> GraphState:
    return {**state, "story_score": 7.5, "character_score": 7.8}


def aggregator(state: GraphState) -> GraphState:
    final_score = round(
        (state["story_score"] + state["character_score"]) / 2, 1
    )

    prompt = f"""
You are a professional movie critic.

Movie genre: {state['genre']}
Story score: {state['story_score']}
Character score: {state['character_score']}

Write a short, professional reasoning explaining the final evaluation.
"""
    response = model.generate_content(prompt)
    reasoning = response.text.strip()

    return {
        **state,
        "final_score": final_score,
        "reasoning": reasoning
    }


def route_by_genre(state: GraphState) -> Literal[
    "drama_evaluator", "thriller_evaluator", "comedy_evaluator"
]:
    genre = state["genre"].lower()
    if "thriller" in genre:
        return "thriller_evaluator"
    if "comedy" in genre:
        return "comedy_evaluator"
    return "drama_evaluator"


builder = StateGraph(GraphState)

builder.add_node("genre_classifier", genre_classifier)
builder.add_node("drama_evaluator", drama_evaluator)
builder.add_node("thriller_evaluator", thriller_evaluator)
builder.add_node("comedy_evaluator", comedy_evaluator)
builder.add_node("aggregator", aggregator)

builder.set_entry_point("genre_classifier")

builder.add_conditional_edges(
    "genre_classifier",
    route_by_genre
)

builder.add_edge("drama_evaluator", "aggregator")
builder.add_edge("thriller_evaluator", "aggregator")
builder.add_edge("comedy_evaluator", "aggregator")
builder.add_edge("aggregator", END)

graph = builder.compile()


if __name__ == "__main__":
    result = graph.invoke({
        "synopsis": (
            "A grieving father uncovers a hidden conspiracy after his daughter "
            "goes missing in a small coastal town."
        ),
        "genre": "",
        "story_score": 0.0,
        "character_score": 0.0,
        "final_score": 0.0,
        "reasoning": ""
    })

    print("\nFINAL OUTPUT")
    print("=" * 60)
    print(f"Genre: {result['genre']}")
    print(f"Story Score: {result['story_score']}")
    print(f"Character Score: {result['character_score']}")
    print(f"Final Score: {result['final_score']}")
    print("\nReasoning:")
    print(result["reasoning"])
    print("=" * 60)