from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

web_agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo],
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools= [YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals = True,
        company_info=True
    )],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use tables to display data."]
    )

agent_team = Agent(
    team=[web_agent, finance_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("""
    Summarize and compare analyst recommendations and 
                     fundamentals for TSLA and NVDA.
                     """, stream=True)


