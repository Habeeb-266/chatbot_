import gradio
from groq import Groq

client = Groq(
    api_key="key",
)

def initialize_messages():
    return [{"role": "system",
             "content": """providing parenting support and information to adults or implementing safety and content restrictions for children."""}]

messages_prmt = initialize_messages()
print(messages_prmt)

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.1-8b-instant",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to parenthood"),
                     title="Parenting ChatBot",
                     description="Chat bot for Parenting",
                     theme="soft",
                     examples=["hi","What is parenthood", "how acquire"]
                     )

iface.launch(share=True)