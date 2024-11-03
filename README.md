# Multipurpose Discord Bot

## Project Description
A Discord bot built with Python and discord.py library. This bot includes various features such as moderation tools, fun commands, and utility functions.

## Features
- **Moderation**: Kick, ban, unban, and clear messages.
- **Fun**: Random jokes, memes, and more.
- **Utility**: Poll creation, reminders, etc.

## Setup

### Prerequisites
- Python 3.6+
- discord.py library

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/xtreme-mc/discord-bot.git
   cd discord-bot
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your Discord token:
   ```env
   DISCORD_TOKEN=your_token_here
   ```

## Usage
1. **Run the bot**:
   ```sh
   main.py
   ```

2. **Commands**:
   - `!hello`: Greets the user.
   - `!ping`: Checks the bot's latency.
   - `!kick <user>`: Kicks the specified user.
   - `!ban <user>`: Bans the specified user.
   - `!unban <user>`: Unbans the specified user.
   - `!clear`: Clears  a specified number of messages.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
