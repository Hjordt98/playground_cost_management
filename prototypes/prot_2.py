from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_roles.mathematician import mathematician


load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

# Get the formatted historical data
data = """
    Lav 4 regnestykker med forskellige niveauer af sværhedsgrad.
    forklar regnestykkerne og hvordan man løser dem.
"""

# Use it in your prompt
prompt = (
    f"{mathematician()}\n\n"
    f"{data}\n\n"
    "Estimer følgende projekt: 300 m², træbeklædning, 8 m høj, interiør inkluderet, høj kompleksitet.\n"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)
print(completion.choices[0].message)
