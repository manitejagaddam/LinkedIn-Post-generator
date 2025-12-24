import getpass
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = GROQ_API_KEY

llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key= GROQ_API_KEY,
    model_name="openai/gpt-oss-20b"  # Updated to a valid Groq model
)

# Define standard prompts for different LinkedIn post styles
STYLE_PROMPTS = {
    "simple": "Write a simple and straightforward LinkedIn post about {topic}. Keep it concise and easy to understand.",
    "creative": "Create a creative and imaginative LinkedIn post about {topic}. Use storytelling, metaphors, and engaging language to make it stand out.",
    "professional": "Write a professional LinkedIn post about {topic}. Maintain a formal tone, provide valuable insights, and encourage networking or discussion.",
    "genz": "Write a Gen Z style LinkedIn post about {topic}. Use modern slang, emojis, and a casual, relatable vibe to connect with younger audiences.",
    "millennial": "Write a millennial style LinkedIn post about {topic}. Incorporate nostalgia, humor, and personal anecdotes to make it authentic and shareable.",
    "inspirational": "Write an inspirational LinkedIn post about {topic}. Motivate readers with positive messages, quotes, and calls to action.",
    "educational": "Write an educational LinkedIn post about {topic}. Explain key concepts, share facts, and provide learning opportunities.",
}

def generate_linkedin_post(topic, style):
    if style not in STYLE_PROMPTS:
        raise ValueError(f"Invalid style. Choose from: {', '.join(STYLE_PROMPTS.keys())}")
    
    # Get the standard prompt for the selected style and insert the topic
    prompt = STYLE_PROMPTS[style].format(topic=topic)
    
    # Use the LLM to generate the LinkedIn post based on the prompt
    messages = [
        (
            "system",
            "You are a skilled LinkedIn content creator. Generate a high-quality LinkedIn post based on the provided prompt.",
        ),
        ("human", prompt),
    ]
    
    response = llm.invoke(messages)
    linkedin_post = response.content.strip()
    
    return linkedin_post

# Main execution
if __name__ == "__main__":
    topic = input("Enter the topic for your LinkedIn post: ")
    
    print("\nAvailable styles:")
    for key in STYLE_PROMPTS.keys():
        print(f"- {key}")
    
    style = input("Choose a style: ").strip().lower()
    
    try:
        post = generate_linkedin_post(topic, style)
        print(f"\nGenerated LinkedIn Post ({style} style):\n{post}")
    except ValueError as e:
        print(e)