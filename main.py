import ollama

#load file
with open('gcsf.txt', 'r') as file:
    data = file.read()
print()

#Ensure data loaded
if data:
    print("***File load SUCCESS***")
else:
    print("!!!File load FAILED!!!")
print()

#Set prompt for Agent#1
prompt_01 = f"{data} #### from this text, extract all pertinent information from this insurance medical policy"
# print("<agent_01 Prompt: " + prompt_01)
# print()

print("<agent_01> Generating a response...")
print()

#Get response from Agent#1 - EXTRACTOR(PREVENTS THE END USER FROM GETTING DIRECTLY TO THE INFORMATION)
response01 = ollama.chat(model="llama3", messages=[
    {
        "role": "user",
        "content": prompt_01,
    }
])

# print(response01["message"]["content"])

#Set prompt from Agent #2
prompt_02 = f"{response01["message"]["content"]} #### Explain the policy in a simple, clear and engaging manner"
print("Agent-02 Prompt: " + prompt_02)
print()

print("<Agent-02> Generating a response...")

#Get response from Agent 2 - Teacher
response02 = ollama.chat(model="llama3", messages=[
    {
        "role": "user",
        "content": prompt_02,
    }
])

#Print out results from second agent
print("<Agent2> Response: " + response02["message"]["content"])