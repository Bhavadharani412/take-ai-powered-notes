# 🧠 AI Notes Generator

Turn raw transcripts, lecture text, course materials, or messy notes into clean, structured study notes using AI.

Built with **Streamlit** + **Groq API** for fast note generation and smooth deployment.

---

## ✨ Features

* Paste transcripts or long-form text
* Automatic chunking for large inputs
* Clean, readable study notes
* Headings, bullets, summaries, key concepts
* Fast responses with Groq LLMs
* Download generated notes
* Simple and clean UI
* Ready for deployment

---

## 🚀 Live Use Cases

Perfect for:

* Online course transcripts
* YouTube lecture notes
* College class notes
* Certification programs
* Self-learning materials
* Revision summaries
* Interview preparation notes

---

## 🛠 Tech Stack

* Python
* Streamlit
* Groq API
* dotenv

---

## 📂 Project Structure

```bash
notes-ai/
│── app.py
│── requirements.txt
│── .env
│── README.md
```

---

## ⚙️ Installation

### 1 Clone Repository

```bash
git clone https://github.com/Bhavadharani412/take-ai-powered-notes
cd take-ai-powered-notes
```

### 2 Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from Groq.

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🤖 Recommended Model

```python
llama-3.3-70b-versatile
```

Fast, reliable, and great for structured note generation.

---

## 📌 How It Works

1. Paste transcript or text
2. Click **Generate Notes**
3. AI processes content in chunks
4. Receive structured notes instantly
5. Copy or download output

---

## 📷 Example Input

```text
Today we are learning about operating systems...
```

## 📘 Example Output

```md
# Operating Systems

## Core Concepts
- Process management
- Memory management
- File systems

## Summary
Operating systems manage hardware and software resources.
```

---

## ☁️ Deploy Options

### Streamlit Cloud

Push repo to GitHub and deploy on Streamlit.

### Render

Deploy Python web app easily.

### Railway

Fast deployment with environment variables support.

---

## 🔒 Security Note

Never expose your `.env` file publicly.

Add this to `.gitignore`:

```gitignore
.env
__pycache__/
venv/
```

---

## 🧠 Future Upgrades

* PDF upload support
* DOCX upload
* Flashcards generation
* Quiz mode
* Ask questions from notes
* Subject wise folders
* Export to Notion
* Dark mode UI

---

## 🤝 Contributing

Pull requests are welcome for improvements and features.

---

## 📄 License

MIT License

---

## ⭐ Support

If this project helped you, give it a star on GitHub.

---

## 👨‍💻 Author

Built for learners who want speed, clarity, and better notes.
