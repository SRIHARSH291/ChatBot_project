import nltk
nltk.download('punkt')

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hello|hey there",
        ["Hello, how can I help you today?",]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot, nice to meet you",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am a virtual being, I exist in the world of bits and bytes',]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi! I am a chatbot. You can start talking to me. Type quit to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
