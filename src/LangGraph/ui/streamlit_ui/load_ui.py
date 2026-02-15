import streamlit as st
import os

from src.LangGraph.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 "+ self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False


        with st.sidebar:
            ## Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            ## LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                ## Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API KEY", type="password")

                ## Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your groq api key")
            
            ## UseCase Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web" or self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TABILY_API_KEY"] = st.text_input("Tavily API Key", type="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your tavily api key.")

            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("AI News Explorer")

                with st.sidebar:
                    timeframe = st.selectbox(
                        "Select time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )          
                if st.button("Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = timeframe


        return self.user_controls
    

    
    