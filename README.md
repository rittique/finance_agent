# Finance Agent

This is a Streamlit-based application that utilizes a finance-focused AI agent to analyze and compare stock data. The app is built using the `phi` library and integrates tools for retrieving stock prices, analyst recommendations, and stock fundamentals.

---

## Features

- **Analyze Stock Data**: Retrieve stock prices, analyst recommendations, and fundamental data for stocks.
- **Custom Queries**: Enter a query like "Compare TSLA and NVDA" to analyze multiple stocks simultaneously.
- **AI-Driven Insights**: Uses a state-of-the-art AI model, `Groq (llama-3.3-70b-versatile)`, to process and summarize data.
- **Streamlined Output**: Displays results in an easy-to-read Markdown format, including tables for structured data.

---

## Requirements

To run this application, ensure you have the following installed:

- **Python 3.8+**
- **Dependencies**: See `requirements.txt`.
- **API Key**: The app requires an API key for accessing financial data, which is configured using a `.env` file.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/finance-agent.git
   cd finance-agent
