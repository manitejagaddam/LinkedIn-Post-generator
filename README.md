# ✍️ LinkedIn Post Alchemist

**LinkedIn Post Alchemist** is a modern, developer-friendly Streamlit web application that turns raw ideas into **high‑engagement, viral‑ready LinkedIn posts**.

It leverages **large language models via Groq** to generate content tailored to different personas — from polished B2B professionals to casual, high‑energy Gen Z creators — all within a sleek, dark‑mode UI.

---

## ✨ Key Features

### 🎭 Content Personas (7 Styles)

Choose the exact tone you want for your post:

* Simple
* Creative
* Professional
* Gen Z
* Millennial
* Inspirational
* Educational

### 🎛️ Creativity Control

Fine‑tune output behavior using a **Temperature Slider**:

* Low temperature → safe, structured, predictable content
* High temperature → creative, bold, experimental posts

### 🌙 Modern Dark UI

* Glassmorphism‑inspired post cards
* Neon gradient accents
* Custom typography for a premium, social‑media‑native feel

### ⚡ Instant Generation

Powered by **Groq’s ultra‑fast inference**, content is generated almost instantly — no waiting, no lag.

---

## 🛠️ Tech Stack

| Layer                  | Technology                             |
| ---------------------- | -------------------------------------- |
| Frontend               | Streamlit                              |
| LLM Orchestration      | LangChain                              |
| LLM Provider           | Groq (ChatOpenAI‑compatible interface) |
| Environment Management | python‑dotenv                          |

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Ensure the following are installed:

* Python **3.8+**
* A valid **Groq API Key** (available from the Groq console)

---

### 2️⃣ Installation

Clone the repository and move into the project directory:

```bash
git clone https://github.com/manitejagaddam/LinkedIn-Post-generator.git
cd LinkedIn-Post-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Environment Setup

Create a `.env` file in the root directory and add your API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

### 4️⃣ Run the Application

Launch the Streamlit server:

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 📂 Project Structure

```plaintext
├── app.py              # Main Streamlit application & UI logic
├── .env                # Environment variables (ignored by git)
├── main.py             # python application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🎨 UI Customization Details

The app overrides default Streamlit styling using **custom CSS injection**:

* **Fonts**: Inter — clean, modern, and readable
* **Gradients**: Linear neon gradients for headings and CTAs
* **Post Cards**: Dedicated `.post-card` class for a LinkedIn‑style reading experience

This makes the app feel closer to a **real social media product** than a typical Streamlit demo.

---

## 📝 Model Configuration (Important)

The project currently uses a placeholder model name:

```
openai/gpt-oss-20b
```

You **must replace this** inside `generate_linkedin_post()` with a valid Groq‑supported model, such as:

* `llama3-70b-8192`
* `mixtral-8x7b-32768`

Using a proper Groq model is critical for **quality and performance**.

---

## 🤝 Contributing

Contributions are welcome!

You can:

* Fork the repository
* Submit pull requests
* Propose new content personas or UI enhancements

If you’re experimenting with creator tooling, this is a solid base to build on.

---

## 💙 Mani

**Made with passion by Mani**
Building tools that blend AI, design, and real‑world usability.

---

> If you want help adding analytics, post‑performance scoring, or scheduling automation — this project is perfectly positioned for it.
