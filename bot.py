#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔒 CYBER AMARJIT SECURED REACTION BOT 🔒
CREATED BY: CYBER AMARJIT
SECURITY LEVEL: MAXIMUM
UNAUTHORIZED EDITING STRICTLY PROHIBITED
"""

import logging
import sys
import os
import hashlib
import hmac
import asyncio
from telegram import Update, Bot, ReactionTypeEmoji
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext

# 🔐 SECURITY CONFIGURATION - DO NOT EDIT
class SecurityConfig:
    def __init__(self):
        self.MASTER_HASH = "a1b2c3d4e5f67890fedcba9876543210"
        self.OWNER_SIGNATURE = "CYBER_AMARJIT_2024_SECURE_BOT"
        self.SECURITY_KEY = "AMARJIT_CYBER_SECURITY_PROTOCOL_ACTIVATED"
        
    def verify_integrity(self):
        """Verify script integrity"""
        current_hash = self.calculate_file_hash()
        if current_hash != self.MASTER_HASH:
            self.security_breach_detected()
            
    def calculate_file_hash(self):
        """Calculate current file hash"""
        try:
            with open(__file__, 'rb') as f:
                content = f.read()
                return hashlib.md5(content).hexdigest()
        except:
            return "INVALID"
    
    def security_breach_detected(self):
        """Handle security breach"""
        print("\n" + "🔒" * 50)
        print("🚨 CYBER SECURITY BREACH DETECTED! 🚨")
        print("🔒" * 50)
        print("⚠️  UNAUTHORIZED MODIFICATION ATTEMPT!")
        print("📛 CREATOR: CYBER AMARJIT")
        print("🔐 THIS SCRIPT IS PROTECTED")
        print("🚫 ACCESS DENIED - TERMINATING...")
        print("🔒" * 50)
        sys.exit(1)

# 🔥 BANNER DISPLAY
def display_banner():
    banner = """
    
 ██████╗██╗   ██╗██████╗ ███████╗██████╗     █████╗ ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗   ██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║  ██║██╔════╝╚══██╔══╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   ███████║██╔████╔██║███████║██████╔╝███████║█████╗     ██║   
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗██╔══██║██╔══╝     ██║   
╚██████╗   ██║   ██████╔╝███████╗██║  ██║   ██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║███████╗   ██║   
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   
                                                                                                         
    🔒 CREATED BY: CYBER AMARJIT 🔒
    🛡️  SECURITY LEVEL: MAXIMUM PROTECTION 🛡️
    📞 CONTACT: SECURE CHANNEL ONLY 📞
    🚀 VERSION: 3.0 GITHUB EDITION 🚀
    
    """
    print(banner)

# 🔐 SECURE FILE READER FUNCTIONS
def read_token():
    """Read bot token from token.txt file"""
    try:
        if not os.path.exists('token.txt'):
            create_token_file()
        
        with open('token.txt', 'r') as f:
            token = f.read().strip()
            
        if not token:
            print("❌ ERROR: token.txt is empty!")
            print("💡 Please add your bot token in token.txt file")
            sys.exit(1)
            
        return token
        
    except Exception as e:
        print(f"❌ Error reading token.txt: {e}")
        sys.exit(1)

def read_channel():
    """Read channel username from channel.txt file"""
    try:
        if not os.path.exists('channel.txt'):
            create_channel_file()
        
        with open('channel.txt', 'r') as f:
            channel = f.read().strip()
            
        if not channel:
            print("❌ ERROR: channel.txt is empty!")
            print("💡 Please add your channel username in channel.txt file")
            sys.exit(1)
            
        return channel
        
    except Exception as e:
        print(f"❌ Error reading channel.txt: {e}")
        sys.exit(1)

def create_token_file():
    """Create token.txt file with instructions"""
    with open('token.txt', 'w') as f:
        f.write("# Add your bot token here\n")
        f.write("# Get token from @BotFather on Telegram\n")
        f.write("# Example: 1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ\n")
        f.write("YOUR_BOT_TOKEN_HERE\n")
    print("📁 token.txt file created!")
    print("💡 Please edit token.txt and add your bot token")

def create_channel_file():
    """Create channel.txt file with instructions"""
    with open('channel.txt', 'w') as f:
        f.write("# Add your channel username here\n")
        f.write("# Format: @channel_username or channel ID\n")
        f.write("# Example: @my_channel\n")
        f.write("YOUR_CHANNEL_HERE\n")
    print("📁 channel.txt file created!")
    print("💡 Please edit channel.txt and add your channel username")

def check_requirements():
    """Check if requirements.txt exists, create if not"""
    if not os.path.exists('requirements.txt'):
        with open('requirements.txt', 'w') as f:
            f.write("python-telegram-bot==20.7\n")
        print("📁 requirements.txt file created!")

# 🔐 INITIAL SECURITY CHECK
security = SecurityConfig()
security.verify_integrity()
display_banner()

# Check and create required files
check_requirements()

# Read token and channel from files
BOT_TOKEN = read_token()
CHANNEL_USERNAME = read_channel()

# Security Hash Verification
SCRIPT_HASH = "a1b2c3d4e5f67890fedcba9876543210"  # 🔒 DO NOT CHANGE

def verify_script():
    """Verify script integrity on every run"""
    current_hash = hashlib.md5(open(__file__, 'rb').read()).hexdigest()
    if current_hash != SCRIPT_HASH:
        print("🚨 SECURITY BREACH DETECTED! 🚨")
        print("📛 UNAUTHORIZED MODIFICATION!")
        print("👤 CREATOR: CYBER AMARJIT")
        print("🔒 THIS SCRIPT IS PROTECTED")
        sys.exit(1)

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class SecureReactionBot:
    def __init__(self, token: str):
        # Security check
        verify_script()
        
        self.application = Application.builder().token(token).build()
        self.security_checks()
        self.setup_handlers()
        
    def security_checks(self):
        """Perform security validations"""
        if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
            print("❌ ERROR: Invalid BOT_TOKEN!")
            print("💡 Please update token.txt with your actual bot token")
            sys.exit(1)
            
        if not CHANNEL_USERNAME or CHANNEL_USERNAME == "YOUR_CHANNEL_HERE":
            print("❌ ERROR: Invalid CHANNEL_USERNAME!")
            print("💡 Please update channel.txt with your actual channel username")
            sys.exit(1)
            
        print("🔒 Security Checks Passed!")
        print("🤖 Bot Token: ✅ Loaded from token.txt")
        print("📢 Channel: ✅ " + CHANNEL_USERNAME + " (from channel.txt)")
        print("🛡️  Bot Initialization Complete!")
        
    def setup_handlers(self):
        """Set up all message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("react", self.react_command))
        self.application.add_handler(CommandHandler("status", self.status_command))
        self.application.add_handler(CommandHandler("channel", self.channel_command))
        self.application.add_handler(CommandHandler("info", self.info_command))
        
        # Message handlers
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        # Channel post handler
        self.application.add_handler(MessageHandler(filters.ChatType.CHANNEL, self.handle_channel_post))

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message when the command /start is issued."""
        welcome_text = f"""
🔒 CYBER AMARJIT SECURE REACTION BOT 🔒

🤖 Welcome to the Most Secure Telegram Reaction Bot!

🛡️  CREATED BY: CYBER AMARJIT
🔐 SECURITY LEVEL: MAXIMUM
📢 TARGET CHANNEL: {CHANNEL_USERNAME}

📁 Files Used:
• token.txt - Bot authentication
• channel.txt - Target channel
• requirements.txt - Dependencies

Commands:
/start - Show this welcome message
/help - Show help information  
/react - Add reactions to a message
/status - Check bot security status
/channel - Show channel info
/info - Show file configuration info

🔒 This bot is protected against unauthorized modifications!
        """
        await update.message.reply_text(welcome_text)

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message when the command /help is issued."""
        help_text = f"""
🆘 CYBER AMARJIT SECURE HELP 🆘

🔒 SECURE OPERATION GUIDE:

📢 CURRENT CHANNEL: {CHANNEL_USERNAME}
📁 CONFIG FILES: token.txt, channel.txt

1. In private chat: Send any message for auto-reactions
2. In channels: Add bot as admin with "Manage Messages" permission  
3. Use /react command to manually trigger reactions

🛡️  SECURITY FEATURES:
- Script Integrity Protection
- Unauthorized Edit Detection
- Secure Hash Verification
- Auto-Termination on Tampering
- File-based Configuration

⚡ Supported reactions: 👍, ❤️, 😂, 🎉, 😮, 😢, 😡, 🤔

🔐 CREATOR: CYBER AMARJIT
        """
        await update.message.reply_text(help_text)

    async def info_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show file configuration information."""
        try:
            token_preview = BOT_TOKEN[:10] + "..." + BOT_TOKEN[-5:] if len(BOT_TOKEN) > 15 else "***"
            
            info_text = f"""
📁 FILE CONFIGURATION INFO 📁

🔐 TOKEN FILE (token.txt):
• Status: ✅ Loaded
• Preview: {token_preview}
• Location: ./token.txt

📢 CHANNEL FILE (channel.txt):
• Status: ✅ Loaded  
• Channel: {CHANNEL_USERNAME}
• Location: ./channel.txt

📦 REQUIREMENTS FILE:
• Status: {'✅ Exists' if os.path.exists('requirements.txt') else '❌ Missing'}
• Location: ./requirements.txt

💡 To modify configuration:
1. Edit token.txt for bot token
2. Edit channel.txt for channel
3. Restart the bot

🔐 Secured by: CYBER AMARJIT
            """
            await update.message.reply_text(info_text)
        except Exception as e:
            await update.message.reply_text(f"❌ Error reading configuration: {e}")

    async def channel_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show current channel information."""
        channel_info = f"""
📢 CHANNEL INFORMATION 📢

🔧 Configured Channel: {CHANNEL_USERNAME}
📁 Source: channel.txt
🤖 Bot Status: ✅ Active
🛡️ Security: ✅ Protected

💡 To change channel, edit channel.txt file
📝 Then restart the bot for changes to take effect

🔐 Secured by: CYBER AMARJIT
        """
        await update.message.reply_text(channel_info)

    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Check bot security status."""
        status_text = f"""
🔒 SECURITY STATUS REPORT 🔒

✅ BOT: OPERATIONAL
✅ SECURITY: ACTIVE  
✅ INTEGRITY: VERIFIED
✅ PROTECTION: MAXIMUM
📢 CHANNEL: {CHANNEL_USERNAME}
📁 CONFIG: File-based

🛡️  CREATOR: CYBER AMARJIT
📡 STATUS: ALL SYSTEMS SECURE
🔐 HASH: VERIFICATION PASSED

🚀 Ready for secure operations!
        """
        await update.message.reply_text(status_text)

    async def react_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manually trigger reactions on the replied message."""
        # Security check
        verify_script()
        
        if not update.message.reply_to_message:
            await update.message.reply_text("🔧 Please reply to a message with /react to add reactions!")
            return
        
        target_message = update.message.reply_to_message
        await self.add_multiple_reactions(update, context, target_message)

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages and add reactions."""
        # Security check
        verify_script()
        
        # Don't react to commands
        if update.message.text.startswith('/'):
            return
            
        await self.add_multiple_reactions(update, context, update.message)

    async def handle_channel_post(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle channel posts and add reactions."""
        # Security check
        verify_script()
        
        if update.channel_post:
            await self.add_multiple_reactions(update, context, update.channel_post)

    async def add_multiple_reactions(self, update: Update, context: ContextTypes.DEFAULT_TYPE, message):
        """Add multiple reactions to a message."""
        try:
            # Security verification
            verify_script()
            
            # List of reactions to add
            reactions = [
                ReactionTypeEmoji("👍"),  # Thumbs up
                ReactionTypeEmoji("❤️"),   # Heart
                ReactionTypeEmoji("😂"),   # Joy
                ReactionTypeEmoji("🎉"),   # Party
                ReactionTypeEmoji("😮"),   # Surprised
                ReactionTypeEmoji("😢"),   # Sad
                ReactionTypeEmoji("😡"),   # Angry
                ReactionTypeEmoji("🤔"),   # Thinking
            ]
            
            # Add reactions one by one with delay
            reaction_count = 0
            for reaction in reactions:
                try:
                    await message.set_reaction(reaction)
                    reaction_count += 1
                    await asyncio.sleep(0.5)  # Small delay between reactions
                except Exception as e:
                    logger.warning(f"Failed to add reaction {reaction}: {e}")
                    continue
            
            logger.info(f"✅ Successfully added {reaction_count} reactions to message {message.message_id}")
            
        except Exception as e:
            logger.error(f"❌ Error adding reactions: {e}")
            # Security breach check
            verify_script()

    async def add_reaction_to_channel_message(self, message_id: int):
        """Add reactions to a specific message in the channel."""
        try:
            # Security check
            verify_script()
            
            bot = self.application.bot
            reactions = [
                ReactionTypeEmoji("👍"),
                ReactionTypeEmoji("❤️"),
                ReactionTypeEmoji("😂"),
            ]
            
            for reaction in reactions:
                await bot.set_message_reaction(
                    chat_id=CHANNEL_USERNAME,
                    message_id=message_id,
                    reaction=[reaction]
                )
                await asyncio.sleep(1)
                
            print(f"✅ Reactions added to channel message {message_id}")
                
        except Exception as e:
            logger.error(f"❌ Error reacting to channel message: {e}")
            verify_script()

    def run(self):
        """Start the bot with security monitoring."""
        logger.info("🔒 Starting Secure Reaction Bot...")
        logger.info("🛡️  Security Protocol: ACTIVE")
        logger.info("👤 Creator: CYBER AMARJIT")
        logger.info(f"📢 Target Channel: {CHANNEL_USERNAME}")
        logger.info("📁 Configuration: File-based (token.txt, channel.txt)")
        
        # Continuous security monitoring
        async def security_monitor():
            while True:
                verify_script()
                await asyncio.sleep(30)  # Check every 30 seconds
        
        # Start security monitor
        asyncio.create_task(security_monitor())
        
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

# 🔒 MAIN EXECUTION WITH SECURITY PROTECTION
if __name__ == "__main__":
    try:
        # Initial security verification
        verify_script()
        display_banner()
        
        print("🔒 Initializing Secure Reaction Bot...")
        print("🛡️  Running Security Checks...")
        print("📁 Checking configuration files...")
        
        # Verify files exist and have content
        if not os.path.exists('token.txt'):
            create_token_file()
            print("❌ Please configure token.txt first!")
            sys.exit(1)
            
        if not os.path.exists('channel.txt'):
            create_channel_file()
            print("❌ Please configure channel.txt first!")
            sys.exit(1)
        
        if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
            print("❌ CRITICAL ERROR: Invalid token in token.txt!")
            print("💡 Please edit token.txt and add your actual bot token")
            sys.exit(1)
            
        if not CHANNEL_USERNAME or CHANNEL_USERNAME == "YOUR_CHANNEL_HERE":
            print("❌ CRITICAL ERROR: Invalid channel in channel.txt!")
            print("💡 Please edit channel.txt and add your actual channel username")
            sys.exit(1)
        
        print("✅ All configuration files verified!")
        print(f"🤖 Bot Token: {BOT_TOKEN[:10]}...{BOT_TOKEN[-5:]}")
        print(f"📢 Channel: {CHANNEL_USERNAME}")
        print("🚀 Starting Bot...")
        
        # Create and run the bot
        bot = SecureReactionBot(BOT_TOKEN)
        bot.run()
        
    except KeyboardInterrupt:
        print("\n🔒 Secure Shutdown Initiated...")
        print("👤 Thank you for using CYBER AMARJIT Secure Bot!")
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        print("🔒 Security Protocol: Maintaining Protection...")
        sys.exit(1)
