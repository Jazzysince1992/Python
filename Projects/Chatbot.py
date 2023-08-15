from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('EducationalBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English language corpus data
trainer.train('chatterbot.corpus.english')

# You can also add custom training data if needed
# trainer.train('path_to_custom_data.yml')

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)
