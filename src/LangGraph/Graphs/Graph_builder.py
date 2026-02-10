
from langgraph.graph import StateGraph, START, END
from src.LangGraph.State.state import State
from src.LangGraph.Nodes.Basic_Chatbot import BasicChatbotNode
from src.LangGraph.Tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from src.LangGraph.Nodes.Chatbot_with_Tools import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph using Langgraph.
        The chatbot node is set as both the entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def chatbot_with_tools_build_graph(self):
        """
        Builds an advance chatbot graph with tool integration
        this chatbot node is set as the entry point.
        """
        ## Define the tool with tool nodes
        tools = get_tools()
        tool_node = create_tool_node(tools=tools)

        ## define the LLM
        llm = self.llm

        ## Define the chatbot node
        obj_chatbot_with_tools = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_tools.create_chatbot(tools=tools)
        ## Add nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        ## Define the conditional edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)




    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()