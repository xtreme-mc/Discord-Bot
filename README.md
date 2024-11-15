# Multipurpose Discord Bot

## Description
A Discord bot built with Python and discord.py library. This bot is still under development.

## Features
soon...

## Setup

### Prerequisites
- Python 3.6+
- discord.py library

> [!IMPORTANT]

> Make sure you have Python 3.6 or higher installed. Using an older version may result in compatibility issues.

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

> [!WARNING]
> Activating the virtual environment is crucial for isolating package installations. Skipping this step can cause conflicts with other Python projects.

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your Discord token:
   ```env
   DISCORD_TOKEN=your_token_here
   ```

> [!CAUTION]
> Keep your .env file secure and never share your Discord token publicly.

## Usage
1. **Run the bot**:
   ```sh
   main.py
   ```

> [!NOTE]

> Ensure your .env file is properly configured before running the bot.

2. **Commands**:
   - `!clear`: Clears  a specified number of messages.

   ...and more soon.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
