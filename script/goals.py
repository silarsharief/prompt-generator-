import os
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="meta-llama/llama-guard-4-12b"
)

def get_goals(goals: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
        You will be given a paragrapgh of text. that will have list of goals in any format. refine a little only if required
         Your job is to return ONLY a python list of goals.
         in the format of:
         - goal1
         - goal2
         - goal3...
         make sure to include all the goals in the list.
         no other text or explanation is required.
        """),
        ("user", "Here are the goals: {goals}"),
    ])
    chain = prompt | llm
    ans = chain.invoke({"goals": goals})
    return ans.content

