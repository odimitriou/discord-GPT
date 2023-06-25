# **Discord OpenAI Integration** 💻

This project is a Python application that integrates the Discord API and the OpenAI API to enable seamless communication between Discord channels and OpenAI's powerful language model. The Discord API is used to receive prompts from Discord channels, which are then forwarded to the OpenAI API for generating responses. The generated response is subsequently sent back to the respective Discord channel.

# **Prerequisites**

To run this project, you need to have the following:

- Python 3.x installed on your system
- Discord API credentials (token) for your Discord bot
- OpenAI API credentials (API key) for accessing the OpenAI language model

# **Installation**

1. Clone or download this repository to your local machine.

`git clone https://github.com/odimitriou/discord-bot.git`

2. Navigate to the project directory.

`cd discord-bot`

3. Install the required dependencies using:

`pip install -r requirements.txt`

# **Configuration**

- Open the .env file and update the following variables:
DISCORD_TOKEN="your-discord-bot-token"
OPENAI_API_KEY="your-openai-api-key"

# **Usage**
Run the application using the following command:
`python run.py`

The bot will connect to Discord and start listening for messages in the configured channels.

To interact with the bot, simply send messages in the Discord channels using `/chatgpt` heading. The bot will forward your messages to the OpenAI API and respond back with the generated message.

# **Customization**
You can customize the behavior of the bot by modifying the code in app.py. You can add additional event handlers, modify message processing logic, or incorporate additional functionality based on your requirements.

# **Contributing**
Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

# **License**
This project is licensed under the MIT License. Feel free to modify and distribute it according to your needs.

# **Acknowledgments**
This project was inspired by the Discord API and the OpenAI API documentation. Special thanks to the developers and contributors of these platforms.

# **Contact**
If you have any questions, suggestions, or concerns regarding this project, please feel free to contact the maintainer:

Email: dimitriou.or@gmail.com
