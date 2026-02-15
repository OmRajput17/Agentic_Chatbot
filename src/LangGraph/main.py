import streamlit as st
from src.LangGraph.ui.streamlit_ui.load_ui import LoadStreamlitUI
from src.LangGraph.LLMs.GroqLLM import GroqLLM
from src.LangGraph.Graphs.Graph_builder import GraphBuilder
from src.LangGraph.ui.streamlit_ui.display_result import DisplayResultStreamlit


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
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message : ")

    if user_message:
        try:
            ## Configure the LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_models()

            if not model:
                st.error("ERROR: LLM model could not be initialized.")
                return
            
            ## Initialize and set up the graph based on use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error Not use case selected.")
                return
            
            ## Graph Builder

            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(user_message=user_message, graph=graph, usecase=usecase).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup has failed - {e}")
                return 
            
        except Exception as e:
            st.error(f"Error: Graph setup has failed - {e}")
            return 
                