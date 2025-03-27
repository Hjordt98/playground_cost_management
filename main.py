from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
