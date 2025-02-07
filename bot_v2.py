from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot Token
BOT_TOKEN = "7769273030:AAGqOauxerdgrm8o6sfyd79lZUW2P1uda6M"

# /start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hello, {update.effective_user.first_name}! 🌟\n"
        "Welcome to your Video & Audio Downloader Bot. 🎥🎵\n"
        "Send me the name or a link, and I'll assist you!"
    )

# /help command function
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot and get a welcome message\n"
        "/help - Show this help message\n\n"
        "Send a link or video name, and I'll download it for you!"
    )

# Bot setup
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Run the bot
    print("🚀 Bot is running...")
    app.run_polling()

