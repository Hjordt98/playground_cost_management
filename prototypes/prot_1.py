from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_roles.estimator import estimator


load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

# Get the formatted historical data
data = """
    "projekt_id": 2001,
    "type": "Naturlegeplads",
    "areal_m2": 320,
    "højde_m": 2.8,
    "materiale": "Robinie",
    "kompleksitet": "Høj",
    "arbejdstimer": 580,
    "materiale_omkostninger": 195000,
    "total_pris": 470500,
    "afsluttet_dato": "2023-03-15"
"""

# Use it in your prompt
prompt = (
    f"{estimator()}\n\n"
    f"{data}\n\n"
    "Med ovenstående data som reference, estimer prisen og forventede mandskabstimer for en ny legeplads"
    "med et overfladeareal på 300 m², træbeklædning, 8 m høj, interiør, og høj kompleksitet."
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)
print(completion.choices[0].message)
