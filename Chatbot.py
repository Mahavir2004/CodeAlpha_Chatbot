# Bot-Vir the chatbot for chatting and knowledge
import random
import time


responses = {
    "hi": "Hello, Mahavir! How can I help you today?",
    "hello": "Hi there! How are you doing?",
    "how are you": "I'm just code, but I'm doing great! What about you?",
    "bye": "Take care, Mahavir! Have a great day!",
    "goodbye": "See you soon! Stay safe.",
    "what happened in 1869": "Mahatma Gandhi, the Father of the Nation, was born in 1869.",
    "who made you": "I was created by Mahavir Pandey on June 19, 2025.",
    "what is your name": "I'm ChatBot, your virtual assistant!",
    "what can you do": "I can answer basic questions, help you learn, and chat with you!",
    "thanks": "You're welcome, anytime!",
    "thank you": "Happy to help!",
    "who is mahavir pandey": "Mahavir Pandey is a brilliant mind learning Python, AI, and building cool projects.",
    "what is python": "Python is a powerful, easy-to-learn programming language used in web, data science, and AI.",
    "what is ai": "AI stands for Artificial Intelligence – making machines think like humans.",
    "what is ml": "Machine learning is a part of AI that helps machines learn from data and make decisions.",
    "what is your purpose": "I'm here to assist, answer, and help you learn anything step by step!",
    "what is the time": time.strftime("The current time is %I:%M %p"),
}

jokes = [
    "Teacher: Itni dair se kahan the?\nStudent: Mam, clock ki sui ke peeche daud raha tha… late ho gaya!",

    "Girl: Tum mujhe kitna pyaar karte ho?\nBoy: Jitna aadmi biryani se karta hai… haddi aaye toh bhi pyaar rehta hai!",

    "Pappu: Papa mujhe phone lena hai!\nPapa: Pehle padhaai kar le!\nPappu: Phone le loonga toh Google se padh lunga!",

    "Boss: Tum office late kyun aaye?\nEmployee: Sapne mein bhi kaam kar raha tha sir, thoda rest le raha tha!",

    "Pappu: Mummy mujhe bhook lagi hai!\nMummy: Fridge mein khana hai.\nPappu: Fridge kholte hi bhook khatam ho jaati hai… itna thanda dekh ke!",

    "Boy: Tumhara naam kya hai?\nGirl: Tum guess karo.\nBoy: Network error... naam mil nahi raha!",

    "Doctor: Aapko kya takleef hai?\nPatient: Sir, jab phone silent pe hota hai… toh dil dhadakna band ho jaata hai!"
]
# Here is Bot-Vir

print("🤖 Bot-Vir: Hello! I am your assistant, Ask me anything or type 'q' to quit 🤖")
print("------------------------------------------------------------------------------\n")

while True:
    user_input = input("You: ").lower()

    if user_input == 'q':
        print("🤖 Thanks for chatting. Goodbye!")
        break
    elif user_input == "joke":
        print(f"🤖 Bot-Vir: {random.choice(jokes)}")
    elif user_input == "time":
        print(f"🤖 Bot-Vir: {time.strftime('%I:%M %p')}")
    elif user_input in responses:
        print(f"🤖 Bot-Vir: {responses[user_input]}")
    else:
        print("🤖Bot-Vir: I can't understand ")