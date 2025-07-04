# 🧠 Deep Research Assistant

This is an intelligent, end-to-end research assistant built with **Gradio**, **OpenAI GPT-4o**, and **custom agent orchestration**. It takes a user query and performs structured, streaming research—culminating in a well-formatted report sent via email.

---

## 🚀 Features

- 📥 Accepts user queries for deep research
- 🔍 Uses OpenAI agents to plan, perform web searches, and compile structured research
- ✍️ Generates a markdown research report (5–10 pages)
- 📧 Automatically emails the final report
- 🌐 Web-based Gradio UI with live streaming updates
- ⚙️ Modular, agent-based design (planner, searcher, writer, emailer)

---

## 🗂️ Project Structure

```
.
├── app.py                  # Gradio UI and streaming logic
├── research_manager.py     # Orchestration of all research agents
├── agents/
│   ├── search_agent.py     # Agent for web searching
│   ├── planner_agent.py    # Agent for planning search terms
│   ├── writer_agent.py     # Agent for generating the report
│   └── email_agent.py      # Agent for sending the final report via email
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/deep-research-assistant.git
cd deep-research-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Required packages include: `gradio`, `openai`, `pydantic`, `sendgrid`, `python-dotenv`, `asyncio`, etc.

### 3. Configure Environment Variables

Create a `.env` file and add the following:

```env
OPENAI_API_KEY=your-openai-key
SENDGRID_API_KEY=your-sendgrid-api-key
```

---

## 🧪 Usage

### Run Locally

```bash
python app.py
```

This will launch the Gradio app in your browser. Type a research topic and get a detailed, AI-generated report streamed in real-time and sent to your email.

---

## 💡 Example Topics

- "The future of renewable energy"
- "The impact of AI on mental health"
- "History of quantum computing"

---

## 🧩 Agent Architecture

| Agent         | Purpose                                   |
|---------------|-------------------------------------------|
| `planner_agent` | Plans 3 web search queries based on the input |
| `search_agent`  | Performs and summarizes web searches     |
| `writer_agent`  | Creates a full markdown research report  |
| `email_agent`   | Converts report to HTML and sends email  |

---

## 📬 Output

- **Markdown report** displayed in real time
- **HTML email** sent with the report content
- **Streaming interface** with section-by-section progress

---

## 📌 Notes

- The app is asynchronous and supports real-time output using `asyncio`.
- Make sure your email credentials and API keys are valid.
- You can extend each agent's logic by modifying the `agents/` directory.

---

## 🧠 Credits

Built with 💡 by leveraging:

- [Gradio](https://gradio.app/)
- [OpenAI GPT-4o](https://openai.com/)
- [LangChain Agents-like system]
- [SendGrid Email API](https://sendgrid.com/)

