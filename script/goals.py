import os
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
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

