import gradio as gr
import time
from dotenv import load_dotenv
# from research_manager import ResearchManager # Your original import

# --- Placeholder for demonstration. You can replace this with your actual ResearchManager.
class ResearchManager:
    """A placeholder class to simulate the streaming research process."""
    async def run(self, query: str):
        report = ""
        # Simulate generating a report in chunks
        yield "## Researching: *{}*\n\n".format(query)
        time.sleep(1)
        for i in range(5):
            chunk = f"### Section {i+1}\n\nThis is a chunk of the generated report. It's part of an ongoing stream of information that is being actively researched and compiled.\n\n"
            report += chunk
            yield report
            time.sleep(0.5)
        yield report + "\n\n**Research complete.**"
# ---

load_dotenv(override=True)


async def run(query: str):
    """The main async generator function that streams the research report."""
    # This function is now cleaner, only focusing on generating the report.
    async for chunk in ResearchManager().run(query):
        yield chunk


def start_research():
    """Updates the UI to a 'running' state when research begins."""
    return {
        run_button: gr.Button(value="Running...", interactive=False),
        query_textbox: gr.Textbox(interactive=False),
        report: gr.Markdown(value="⏳ **Starting research... Please wait.**"),
    }

def end_research():
    """Resets the UI to its original state after research is complete."""
    return {
        run_button: gr.Button(value="Run", interactive=True),
        query_textbox: gr.Textbox(interactive=True),
    }


# Theming and Layout
with gr.Blocks(theme=gr.themes.Soft(primary_hue="sky")) as ui:
    gr.Markdown(
        """
        # 🚀 Deep Research Assistant
        Enter a topic to generate a comprehensive, streaming research report.
        """
    )

    # Improved layout for input controls
    with gr.Row():
        query_textbox = gr.Textbox(
            label="What topic would you like to research?",
            placeholder="e.g., The future of renewable energy",
            scale=4, # Makes the textbox take up more space
        )
        run_button = gr.Button("Run", variant="primary", scale=1)

    # The main output area for the report
    report = gr.Markdown(label="Report")
    
    # --- Event Handling ---
    # Chain events together for a seamless user experience
    
    # 1. When the button is clicked, call `start_research` to update the UI.
    # 2. Then, call the main `run` function to stream the report.
    # 3. Finally, call `end_research` to reset the UI controls.
    run_button.click(
        fn=start_research, 
        outputs=[run_button, query_textbox, report]
    ).then(
        fn=run, 
        inputs=query_textbox, 
        outputs=report
    ).then(
        fn=end_research, 
        outputs=[run_button, query_textbox]
    )

    # Allow submitting with the "Enter" key
    query_textbox.submit(
        fn=start_research, 
        outputs=[run_button, query_textbox, report]
    ).then(
        fn=run, 
        inputs=query_textbox, 
        outputs=report
    ).then(
        fn=end_research, 
        outputs=[run_button, query_textbox]
    )
    
    # Add examples for user guidance
    gr.Examples(
        ["The impact of AI on climate change", "History of the internet", "Benefits of mindfulness"],
        inputs=query_textbox,
        label="Example Topics"
    )

ui.launch(inbrowser=True)