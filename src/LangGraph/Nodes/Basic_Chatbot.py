from src.LangGraph.State.state import State

class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State)->dict:
        """Process the input and generate a chat response"""
        return {"messages":self.llm.invoke(state["messages"])}