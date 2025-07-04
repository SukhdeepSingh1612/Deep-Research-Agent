import streamlit as st
from dotenv import load_dotenv
from research_manager import ResearchManager
import asyncio

# Load environment variables from your .env file
load_dotenv(override=True)

# Define the asynchronous function that streams the research report
async def run(query: str):
    """
    Asynchronously runs the research manager and yields the output chunks.
    """
    async for chunk in ResearchManager().run(query):
        yield chunk

# --- Streamlit UI Implementation ---

# Set the title of the web app
st.title("Deep Research 🔬")

# Create a form to contain the user input and the run button
with st.form(key='research_form'):
    # Create a text input field for the research topic
    query_textbox = st.text_input("What topic would you like to research?")
    
    # Create a submit button for the form
    run_button = st.form_submit_button("Run", type="primary")

# This block executes only when the form's 'Run' button is clicked
if run_button:
    if query_textbox:
        st.markdown("---") # Add a horizontal rule for visual separation
        # Add a subheader for the report section
        st.markdown("### Report")
        
        # st.write_stream is the ideal way to handle and display streams of data
        st.write_stream(run(query_textbox))
    else:
        # Show a warning if the user clicks 'Run' without entering a topic
        st.warning("Please enter a topic to research.")