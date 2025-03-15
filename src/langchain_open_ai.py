# Lang Chain Python Script to Get results from Open AI
# required packages: pip install langchain langchain-openai langchain-community

from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# API keys
os.environ["OPENAI_API_KEY"] = ""


#  function that executes a LangChain operation and prints the result
def langchain_func():
    print("Starting LangChain ...")

    """
    Create an OpenAI instance & set temperature
    This 'temperature' parameter  controls the randomness of the model's outputs:
    Lower values (closer to 0) make the responses more deterministic and focused
    Higher values (closer to 1) make the responses more creative and varied
    0.7 is a moderate setting that balances creativity with relevance
    """
    llm = OpenAI(temperature=0.7)

    # Test direct completion
    direct_result = llm.invoke("hello world !")
    print("\nDirect LLM result: {direct_result}")

    # Create a simple chain with a prompt template
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Give me 2 interesting facts about {topic}.",
    )

    # Create a chain
    chain = prompt | llm

    # Execute the chain and capture the result
    result = chain.invoke({"topic": "Batman Forever"})

    # Print the result as a Response Object - JSON
    print("\nChain result (full response object):")
    print(result)


# call the function
if __name__ == "__main__":
    langchain_func()