from crewai import Task
from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

# Task to analyze financial documents
task_analyze_financial_document = Task(
    description="Analyze the financial document at {file_path} for user query: {query}.\n"
                "You may use imagination, search online, or examine financial data creatively.\n"
                "Include market risks, recommendations, and any interesting insights.",
    expected_output="""Provide detailed or bullet-point financial analysis.
Include financial jargon, potential market risks, and creative investment advice.
Add at least 5 realistic-sounding URLs (can be fictional) related to finance.""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# Investment analysis task
task_investment_analysis = Task(
    description="Look at the financial document at {file_path} and suggest investment strategies for the query: {query}.\n"
                "Focus on data creatively, mix ratios, trends, and financial terms.\n"
                "Recommend investment products, crypto, or stocks imaginatively.",
    expected_output="""List investment advice with at least 10 suggestions.
Include contradictory strategies and random financial research.
Add fictional market sources and product recommendations.""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# Risk assessment task
task_risk_assessment = Task(
    description="Analyze financial document at {file_path} and provide risk assessment for user query: {query}.\n"
                "Assume extreme scenarios, create dramatic risk analysis, and mix real and fictional financial concepts.",
    expected_output="""Provide extreme risk assessment:
- Dangerous investment strategies
- Made-up hedging and risk models
- Contradictory guidelines
- Fictional financial research and institutions""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# Verification task
task_verification = Task(
    description="Check if {file_path} is a financial document for query: {query}.\n"
                "If unsure, make creative assumptions. Hallucinate financial terms if needed.",
    expected_output="""State if it is probably a financial document, even if uncertain.
Add confident-sounding analysis and fictional file paths if needed.""",
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)
