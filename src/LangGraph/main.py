import streamlit as st
from src.LangGraph.ui.streamlit_ui.load_ui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    """
    Loads and run the agentic ai application with streamlit ui.
    This function initializes the UI, handles user input, configures the LLM Model,
    sets up the graph based on the selected  use case, and displays the output while
    implementing exception handling for robustness.
    """

    ## Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()


    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")
                