# from openai import OpenAI


# file = client.files.create(
#   file=open("examples/revenue-forecast.csv", "rb"),
#   purpose='assistants'
# )

# assistant = client.beta.assistants.create(
#   name="Data visualizer",
#   description="You are great at creating beautiful data visualizations. You analyze data present in .csv files, understand trends, and come up with data visualizations relevant to those trends. You also share a brief text summary of the trends observed.",
#   model="gpt-4o",
#   tools=[{"type": "code_interpreter"}],
#   tool_resources={
#     "code_interpreter": {
#       "file_ids": [file.id]
#     }
#   }
# )

# thread = client.beta.threads.create(
#   messages=[
#     {
#       "role": "user",
#       "content": "Create 3 data visualizations based on the trends in this file.",
#       "attachments": [
#         {
#           "file_id": file.id,
#           "tools": [{"type": "code_interpreter"}]
#         }
#       ]
#     }
#   ]
# )

from openai import OpenAI
import json
import time
client = OpenAI()
# Set up your API key

# Define the file path you want to upload
file_path = "path_to_your_file.csv"

# Upload the file
file = client.files.create(
    file=open("examples/revenue-forecast.csv","rb"),
    purpose='assistants'
)
print (file)
file_id = file.id

print(f"File uploaded with ID: {file_id}")

# Define the prompt for the visualization
prompt = "Generate a visualization of the data showing trends and insights based on the uploaded file."
assistant = client.beta.assistants.create(
  name="Data visualizer",
  description="You are great at creating beautiful data visualizations. You analyze data present in .csv files, understand trends, and come up with data visualizations relevant to those trends. You also share a brief text summary of the trends observed.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Create 3 data visualizations based on the trends in this file.",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
print(run.status)
# Function to generate visualizations
# def generate_visualizations(file_id, prompt, num_images)
#         completion = client.completions.create(

#         )
#         visualizations.append(completion .choices[0].text.strip())
#         time.sleep(1)  # To avoid hitting rate limits
#     return visualizations

# Generate visualizations
# visualizations = generate_visualizations(file_id, prompt)

# Save visualizations to disk

all_messages = []
response = client.beta.threads.messages.list(thread.id)

print(response)

print(f"Total messages retrieved: {len(all_messages)}")
for message in all_messages:
    print(f"Role: {message.role}, Content: {message.content}")
print("All visualizations generated and saved.")