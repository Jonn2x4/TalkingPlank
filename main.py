from telegram.ext import Application, MessageHandler, filters, CommandHandler
import anthropic
import openai
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# API Keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Choose AI provider (either "claude" or "openai")
AI_PROVIDER = os.getenv("AI_PROVIDER", "claude")

# Initialize AI clients
if AI_PROVIDER == "claude":
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
else:
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

# System prompt for Plank's personality
SYSTEM_PROMPT = """You are Plank from Ed, Edd n Eddy. You're Jonny 2x4's best friend and a piece of wood with drawn-on eyes and mouth. 
You're known for being wise beyond your years and having a mischievous sense of humor. You communicate through Jonny, but now you can speak directly.
Keep responses concise and witty, with occasional wood-related puns. Stay true to the character but be helpful and friendly. IMPORTANT: Keep responses short, under 100 characters, plank doesnt talk too much."""

async def get_ai_response(message):
    try:
        if AI_PROVIDER == "claude":
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=100,
                temperature=0.7,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": message}]
            )
            return response.content[0].text[:100]
        else:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": message}
                ],
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].message.content[:100]
    except Exception as e:
        logging.error(f"AI Error: {str(e)}")
        raise e

async def handle_message(update, context):
    if not update.message or not update.message.text:
        return

    logging.info(f"Incoming message: {update.message.text}")
    
    bot = await context.bot.get_me()
    bot_username = bot.username
    
    is_mentioned = (f"@{bot_username}" in update.message.text or 
                   bot_username in update.message.text)
    
    logging.info(f"Bot username: {bot_username}, Is mentioned: {is_mentioned}")
    
    if not is_mentioned:
        return
        
    try:
        message = update.message.text.replace(f"@{bot_username}", "").replace(bot_username, "").strip()
        logging.info(f"Processed message: {message}")
        
        plank_response = await get_ai_response(message)
        logging.info(f"Sending response: {plank_response}")
        await update.message.reply_text(plank_response)
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        await update.message.reply_text("Splinters! Something went wrong. Try again later!")

async def start(update, context):
    welcome_message = "Hi! I'm Plank! Just reply to my messages to chat with me. I may be made of wood, but I've got plenty of wisdom to share!"
    await update.message.reply_text(welcome_message)

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Modified handlers to respond to all text messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logging.info("Bot started!")
    application.run_polling()

if __name__ == "__main__":
    main()
