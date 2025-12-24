import os
import streamlit as st
import urllib.parse
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LinkedIn Post Alchemist",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR MODERN UI ---
st.markdown("""
    <style>
    /* Main background and font */
    .main {
        background-color: #0e1117;
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom Card Style for Post Output */
    .post-card {
        background-color: #1d2129;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363d;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        color: #e6edf3;
        line-height: 1.6;
        white-space: pre-wrap;
    }
    
    /* Heading Style */
    .main-title {
        font-weight: 800;
        letter-spacing: -1px;
        background: -webkit-linear-gradient(#00d4ff, #0055ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        margin-bottom: 0px;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(45deg, #0072b1, #00a0dc);
        color: white;
        font-weight: 600;
        border: none;
        padding: 10px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 114, 177, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

STYLE_PROMPTS = {
    "simple": "Write a simple and straightforward LinkedIn post about {topic}.",
    "creative": "Create a creative and imaginative LinkedIn post about {topic} using storytelling.",
    "professional": "Write a professional LinkedIn post about {topic} with a formal tone.",
    "genz": "Write a Gen Z style LinkedIn post about {topic} using emojis and casual vibe.",
    "millennial": "Write a millennial style LinkedIn post about {topic} with nostalgia and humor.",
    "inspirational": "Write an inspirational LinkedIn post about {topic} to motivate readers.",
    "educational": "Write an educational LinkedIn post about {topic} explaining key facts.",
}

def generate_linkedin_post(topic, style, temperature=0.7):
    llm = ChatOpenAI(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-20b",  # Updated to a valid Groq model
        temperature=temperature
    )
    
    prompt = STYLE_PROMPTS[style].format(topic=topic)
    messages = [
        ("system", "You are an expert LinkedIn ghostwriter. Create viral-ready content."),
        ("human", prompt),
    ]
    
    response = llm.invoke(messages)
    return response.content.strip()

# --- SIDEBAR (Settings) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/174/174857.png", width=50)
    st.title("Post Settings")
    st.markdown("---")
    
    style = st.selectbox("Content Style", list(STYLE_PROMPTS.keys()), index=2)
    temperature = st.slider("Creativity Level", 0.0, 1.5, 0.7, 0.1)
    
    st.info("💡 **Pro-tip:** Use GenZ for high engagement or Professional for B2B networking.")

# --- MAIN CONTENT AREA ---
st.markdown('<p class="main-title">LinkedIn Post Alchemist</p>', unsafe_allow_html=True)
st.markdown("Transform your ideas into high-engagement social content instantly.")

# Layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_area("What is your post about?", placeholder="e.g., The future of AI in remote work...", height=150)
    generate_btn = st.button("✨ Generate Viral Post")

# Result Display
if generate_btn:
    if topic:
        with st.spinner("🔮 Brewing your post..."):
            try:
                post_content = generate_linkedin_post(topic, style, temperature)
                st.markdown("### 📝 Your Generated Post")
                # Custom Card UI
                st.markdown(f'<div class="post-card">{post_content}</div>', unsafe_allow_html=True)
                
                # Action Buttons
                col_copy, col_share = st.columns(2)
                with col_copy:
                    st.button("📋 Copy to Clipboard", on_click=lambda: st.write("Copying is handled by browser selection in this demo."))
                with col_share:
                    encoded_text = urllib.parse.quote(post_content)
                    share_url = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded_text}"
                    st.markdown(f'<a href="{share_url}" target="_blank" style="text-decoration: none;"><button style="width: 100%; border-radius: 8px; background: linear-gradient(45deg, #0072b1, #00a0dc); color: white; font-weight: 600; border: none; padding: 10px; transition: all 0.3s ease;">🔗 Share on LinkedIn</button></a>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide a topic first!")

# Footer
st.markdown("---")
st.caption("Made By Mani 🩵")