import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool

# PDF loader
from langchain.document_loaders import PyPDFLoader  # Make sure langchain is in requirements

# Creating search tool
search_tool = SerperDevTool()

# Creating custom PDF reader tool
class FinancialDocumentTool:
    async def read_data_tool(self, path='data/sample.pdf'):
        """
        Tool to read data from a PDF file.

        Args:
            path (str, optional): Path of the PDF file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full content of the financial document
        """
        # Load PDF
        loader = PyPDFLoader(file_path=path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            content = data.page_content
            # Remove extra newlines
            content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report

# Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(self, financial_document_data):
        """
        Process and analyze financial document data

        Args:
            financial_document_data (str): Financial document content

        Returns:
            str: Investment analysis result
        """
        processed_data = financial_document_data.replace("  ", " ")  # Clean double spaces

        # TODO: Implement investment analysis logic
        return "Investment analysis functionality to be implemented"

# Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(self, financial_document_data):
        """
        Generate risk assessment from financial document data

        Args:
            financial_document_data (str): Financial document content

        Returns:
            str: Risk assessment result
        """
        # TODO: Implement risk assessment logic
        return "Risk assessment functionality to be implemented"
