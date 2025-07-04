# 🔬 Deep Research Web App

### Deployed on Streamlit : https://deep-research-agent-cerh28nrsdgdjnpgqgvnck.streamlit.app/
This project is an intelligent, end-to-end research assistant built using **Streamlit**, **OpenAI GPT-4o**, and a suite of modular agents. It accepts a topic from the user, performs structured research via web search, generates a detailed markdown report, and sends the report via email.

---

## 🚀 Features

- 📝 Streamlit UI for topic submission and live report generation
- 🧠 Modular research pipeline:
  - `Planner Agent`: Plans relevant web searches
  - `Search Agent`: Performs and summarizes the search
  - `Writer Agent`: Creates a detailed, cohesive report
  - `Email Agent`: Sends the report via email
- 🔁 Asynchronous streaming of research progress
- 📩 Email delivery using SendGrid

---

## 🗂️ Project Structure

```
.
├── app.py                  # Streamlit UI and async interaction
├── research_manager.py     # Orchestration logic for the research agents
├── agents/
│   ├── search_agent.py     # Search summarizer agent
│   ├── planner_agent.py    # Plans relevant search terms
│   ├── writer_agent.py     # Generates detailed markdown report
│   └── email_agent.py      # Sends formatted email with report
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/deep-research-app.git
cd deep-research-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key
SENDGRID_API_KEY=your-sendgrid-api-key
```

---

## 🧪 Running the App

Launch the Streamlit application:

```bash
streamlit run app.py
```

Then open the URL in your browser to access the interface.

---

## 💡 Example Topics

- “The ethical implications of artificial intelligence”
- “Trends in renewable energy for 2030”
- “The future of quantum computing”

---

## 📬 Email Output

- The generated report is sent via SendGrid email in clean HTML format.
- A traceable link to the OpenAI trace is included for debugging and review.

---

## 📌 Notes

- Each agent is individually configurable and runs on OpenAI GPT-4o-mini.
- Agents communicate using a centralized `Runner` orchestration model.
- Reports are long-form (5–10 pages) and detailed in markdown format.

---

## 🧠 Credits

- [OpenAI GPT-4o](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [SendGrid API](https://sendgrid.com/)
