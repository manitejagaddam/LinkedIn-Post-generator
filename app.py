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

def generate_linkedin_post(topic):
    # Step 1: Generate a prompt based on the topic
    prompt_generation_messages = [
        (
            "system",
            "You are an expert at creating effective prompts for generating engaging LinkedIn posts. Create a detailed, professional prompt that instructs an AI to write a LinkedIn post about the given topic.",
        ),
        ("human", f"Create a prompt for generating a LinkedIn post about: {topic}"),
    ]
    
    generated_prompt_response = llm.invoke(prompt_generation_messages)
    generated_prompt = generated_prompt_response.content.strip()
    
    print(f"Generated Prompt: {generated_prompt}\n")
    
    # Step 2: Use the generated prompt to create the LinkedIn post
    post_generation_messages = [
        (
            "system",
            "You are a professional content creator specializing in LinkedIn posts. Write an engaging, professional LinkedIn post based on the provided prompt.",
        ),
        ("human", generated_prompt),
    ]
    
    post_response = llm.invoke(post_generation_messages)
    linkedin_post = post_response.content.strip()
    
    return linkedin_post

# Main execution
if __name__ == "__main__":
    topic = input("Enter the topic for your LinkedIn post: ")
    post = generate_linkedin_post(topic)
    print(f"\nGenerated LinkedIn Post:\n{post}")