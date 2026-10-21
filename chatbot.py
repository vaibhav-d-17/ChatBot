from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatMistralAI(model="ministral-3b-latest")

chat_history = [
    SystemMessage(content="you are helpful ai assistant for me")
]

if __name__ == "__main__":
    while True:
        user_input = input('You : ')
        chat_history.append(HumanMessage(content=user_input))
        if user_input == 'exit' :
            break;
        result = llm.invoke(chat_history)
        print('AI : ',result.content)