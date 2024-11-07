# 🪵 Plank Bot

A Telegram chatbot powered by Claude 3.5 that embodies Plank from Ed, Edd n Eddy. This witty piece of wood responds to mentions with concise, character-accurate messages.

## 🌟 Features

- Responds to @mentions in Telegram groups
- Powered by Claude 3.5 Sonnet for natural conversations
- Authentic Plank personality from Ed, Edd n Eddy
- Concise responses (under 100 characters)
- Wood-related puns and wisdom
- Logging system for debugging

### Configuration

Create a `.env` file in the project root:
```env
TELEGRAM_TOKEN=your_telegram_token

# Choose your AI provider
AI_PROVIDER=claude  # or "openai"

# Add the API key for your chosen provider
ANTHROPIC_API_KEY=your_anthropic_key  # if using Claude
OPENAI_API_KEY=your_openai_key  # if using OpenAI
```

### AI Provider Options

The bot supports two AI providers:
- **Claude** (Anthropic's Claude 3.5 Sonnet)
- **OpenAI** (GPT-4)

Set `AI_PROVIDER` in your `.env` file to choose which one to use.

### Additional Dependencies

If using OpenAI:
```bash
pip install openai
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Telegram Bot Token (from @BotFather)
- Anthropic API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/plank-bot
cd plank-bot

# Install dependencies
pip install python-telegram-bot anthropic
```

### Configuration

Create a `.env` file in the project root:
```env
TELEGRAM_TOKEN=your_telegram_token
ANTHROPIC_API_KEY=your_anthropic_key
```

### Running the Bot

```bash
python main.py
```

## 💬 Usage

1. Add the bot to your Telegram group
2. Mention the bot using @bot_username
3. Add your message after the mention
4. Plank will respond with wisdom (or a pun)

## 🔧 Technical Details

- Built with python-telegram-bot
- Uses Anthropic's Claude 3.5 Sonnet model
- Implements message filtering and mention detection
- Includes comprehensive logging
- Character-limit enforcement

## ⚠️ Security Notes

- Never commit API keys to version control
- Use environment variables for sensitive data
- Keep your dependencies updated

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.
