import gradio as gr
import os
from tavily import TavilyClient

def perform_search(query):
    try:
        client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
        result = client.search(query, include_answer=True)
        return result["answer"]
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
interface = gr.Interface(
    fn=perform_search,
    inputs=gr.Textbox(label="Enter your search query", lines=2),
    outputs=gr.Textbox(label="Answer"),
    title="Tavily Search Assistant",
    description="Enter any question to get an AI-powered search response"
)

if __name__ == "__main__":
    interface.launch()
