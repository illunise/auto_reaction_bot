# 🤖 Telegram Auto-Reaction Bot  

A lightweight **Telegram bot** that automatically reacts to messages in groups and channels with random emojis.  
Supports **multiple bot tokens** running in parallel with customizable random delays and emoji sets.  

---

## ✨ Features  
- 🔹 **Auto-reacts** to every new message in groups/channels.  
- 🔹 Supports **multiple bots** at the same time (via multiprocessing).  
- 🔹 **Random delay** before reacting (to look natural).  
- 🔹 Configurable **emoji list** (choose which emojis to use).  
- 🔹 **50% skip chance** to mimic human-like behavior.  
- 🔹 Simple **/start command** with invite buttons for groups/channels.  

---

## 📦 Installation  

1. **Clone this repo**  
   ```bash
   git clone https://github.com/yourusername/telegram-auto-reaction-bot.git
   cd telegram-auto-reaction-bot
   ```

2. **Create and activate a virtual environment (recommended)**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root and add your bot tokens & settings:  
   ```ini
   # Comma-separated list of bot tokens
   BOT_TOKENS=123456:ABC-XYZ,654321:DEF-UVW

   # Emojis to use for reactions (comma separated)
   EMOJI_LIST=👍,😂,🔥,❤️,😎

   # Maximum random delay in seconds before reacting
   RANDOM_LEVEL=5
   ```

---

## 🚀 Usage  

Run the bot with:  
```bash
python main.py
```

- Each token will spawn its own bot process.  
- Bots will automatically react in channels/groups where they are added as admins (with **Add Reactions** permission).  

---

## ⚙️ Configuration  

| Variable       | Description |
|----------------|-------------|
| `BOT_TOKENS`   | Comma-separated list of bot tokens (from [BotFather](https://t.me/BotFather)) |
| `EMOJI_LIST`   | Comma-separated list of emojis for reactions |
| `RANDOM_LEVEL` | Max random delay in seconds before reacting (default: 5) |

---

## 📜 Example Behavior  
- A new message arrives in a group.  
- Bot waits **1–5 seconds** randomly.  
- Chooses a random emoji from `EMOJI_LIST`.  
- Reacts to the message.  
- Sometimes **skips reacting** to look natural.  

---

## 🛠️ Requirements  
- Python **3.9+**  
- Dependencies listed in `requirements.txt`:  
  - `python-telegram-bot` (v20+)  
  - `python-dotenv`  

---

## 📌 Notes  
- Ensure bots have **Message Reactions** permission in groups/channels.  
- Multiple bots can be added to the same chat to create **multi-reaction effect**.  
- Works best when emojis are **fun & varied** (not just 👍).  

---

## 📄 License  
MIT License.  
