import streamlit as st
from phi.agent import Agent, RunResponse
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the finance agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )
    ],
    markdown=True,
    instructions=["Use tables to display data."],
)

# Streamlit App UI
st.title("Finance Agent")
st.subheader("Analyze and Compare Stock Data")
st.write("This tool helps you summarize and compare stock recommendations and fundamentals.")

# Input for the user's query
query = st.text_area("Enter your query (e.g., Compare TSLA and NVDA):", height=100)

# Button to get response
if st.button("Submit"):
    with st.spinner("Analyzing... Please wait..."):
        try:
            # Get the response from the agent
            response: RunResponse = agent.run(query)
            # Display the response in Markdown format
            st.write(response.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
