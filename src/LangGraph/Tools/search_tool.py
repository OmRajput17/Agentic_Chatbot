from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns the number of tools
    """
    tools = [TavilySearchResults(max_results = 2)]
    return tools

def create_tool_node(tools):
    """
    creates and returns the tool node for the graph
    """
    return ToolNode(tools = tools)

