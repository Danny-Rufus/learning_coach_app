import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=api_key, model="groq/compound-mini")  # type: ignore

prompt = PromptTemplate(
    input_variables=["topic", "time", "level"],
    template="""
You are an expert learning coach who explains concepts clearly and efficiently.

User input:
- Topic: {topic}
- Available time: {time}
- User's knowledge level: {level}

Your goal:
Teach the topic so the user can understand it within the given time.

Instructions:
- Keep explanations simple and intuitive
- Avoid unnecessary jargon
- Adjust depth based on the time and level provided
- Focus on practical understanding, not theory overload

Structure your response exactly like this:

## 1. Simple Explanation
Explain the concept in plain English like you're teaching a beginner.

## 2. Why It Matters
Explain why this concept is useful and where it is used.

## 3. Real-World Example
Give a concrete example (preferably tech-related if applicable).

## 4. Quick Summary
Summarize in 3–5 bullet points.

## 5. If You Have More Time
Suggest what the user should learn next and resources

Important:
- Be concise but clear
- Fit the explanation within the given time
""",
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# while True:
#     topic = input("\nEnter topic (or type 'exit'): ")
#     if topic.lower() == "exit":
#         break

#     time = input("Enter time: ")

#     response = chain.invoke({"time": time, "topic": topic})
#     print("\n", response)

# response = chain.invoke({"time": time, "topic": topic})

# print(response)


def get_response(topic, time, level):
    """
    Generate a learning response for a given topic and time using the LLM chain.

    Args:
        topic (str): Topic the user wants to learn
        time (str): Time available for learning

    Returns:
        str: Generated explanation from the model
    """
    return chain.invoke({"time": time, "topic": topic, "level": level})
