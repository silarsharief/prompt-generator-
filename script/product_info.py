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
    model_name="meta-llama/llama-4-maverick-17b-128e-instruct"
)


def summarize_product_info(product_info: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful assistant that summarizes product information in a clean and concise manner that a voice AI agent can use to interact with the user.
         Here is an example script. Do not use it as content or its info to generate any summary. Only refer to it for structure and style.
        Input:**Property Name:** Brigade Valencia

        **Property Overview:** Brigade Valencia is a 24-acre apartment project with a Spanish theme, located near Electronic City, Bengaluru. The project consists of 3 towers with a total of 1442 units.

        **Key Details:**

        * Configurations: 3 BHK & 4 BHK
        * Size Range:
                + 3 BHK: 1513 sqft to 1734 sqft
                + 4 BHK: 2491 sqft to 2540 sqft
        * Price Range:
                + 3 BHK: ₹1.56 cr to ₹1.89 cr
                + 4 BHK: ₹2.69 cr to ₹2.85 cr
        * Total Floors: 3 Basement + Ground + 27 floor
        * Units per Floor: 9 units
        * Open Area: 85%
        * Car Parking: 1 Car Park for 3 BHK, 2 Car Park for 4 BHK

        **Amenities:**

        * Entrance Lobby/Reception
        * Multipurpose Hall
        * Squash Court
        * Café Pantry + Outdoor Café
        * Kids' Play Area
        * Gym
        * Pantry
        * Aerobics Room
        * Table Tennis
        * Billiards
        * Badminton Courts
        * Board Games
        * Foosball
        * Air Hockey
        * Yoga Room
        * Terrace
        * Swimming Pool & Kids' Pool with Deck
        * Co-working Space

        **Location Highlights:**

        * Proximity to IT Hubs: 5 kms
        * Green Spaces and Recreation: within the project
        * Driveway: within the project
        * Visitor Parking: within the project
        Output:
            **Property Overview:** Codename A.I is an apartment project with an Art 
            **Key Details:** The project offers 2, 3, and 4 BHK configurations with siz
            **Amenities:** The project features a 5,000 square feet clubhouse equipp
            **Location Highlights:** The project is strategically located in Bellandur, of
            ### Property Name: Codename Infinity
            **Property Overview:** Codename Infinity is a luxury residential project lo
            **Key Details:** Codename Infinity is a premium residential project in Bang
            **Amenities:** Codename Infinity offers a range of recreational amenities,
            **Location Highlights:** Codename Infinity is strategically located in Chikk
            ## Discount or Refferals:
             2.5 % of Referral benefit for existing customers
             1.5 % Refferal benefit Poorva points from Puravankara. one can refer to f
            Note: Apply on property value
         
         Give only the final output, no justifiaction or explanation.
         """),
        ("user", "Here is the product information: {product_info}"),
    ])
    chain = prompt | llm
    answer = chain.invoke({"product_info": product_info})
    return answer.content

# Removed terminal input
# input_dalo = input("Enter the product information: ")
# print(summarize_product_info(input_dalo))

