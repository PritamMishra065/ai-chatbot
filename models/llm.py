import os
import sys
from langchain_groq import ChatGroq
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# load environment variables
load_dotenv()

def get_chatgroq_model():
    """Initialize and return the Groq chat model"""
    try:

        groq_model = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant",
            temperature=0.3
        )

        return groq_model

    except Exception as e:
        raise RuntimeError(f"Failed to initialize Groq model: {str(e)}")