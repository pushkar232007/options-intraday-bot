#!/usr/bin/env python3
"""Send a Telegram notification via the official Bot API.

Setup (one-time, by the human, not the agent):
1. In Telegram, message @BotFather -> /newbot -> follow the prompts to name your bot.
   BotFather replies with a token like 123456789:ABCdefGhIJKlmNoPQRstuVwxyz
2. Open a chat with your new bot (search its @username) and send it any message
   (e.g. "hi") so it's allowed to message you back.
3. Fetch your chat ID by visiting this URL in a browser (replace <TOKEN>):
   https://api.telegram.org/bot<TOKEN>/getUpdates
   Find "chat":{"id": NUMBER, ...} in the response — that NUMBER is your chat ID.
4. Set env vars in the Claude Code routine's cloud environment:
       TELEGRAM_BOT_TOKEN
       TELEGRAM_CHAT_ID

Usage:
    python3 scripts/telegram.py "EOD square-off done. Today's P&L +1,240."
"""
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def _env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(
            f"Missing required environment variable: {name}\n"
            "Set it in the Claude Code routine's cloud environment, not in a .env file."
        )
    return value


def send(message: str) -> str:
    token = _env("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode(
        {"chat_id": _env("TELEGRAM_CHAT_ID"), "text": f"[Theta - Options Bot] {message}"}
    ).encode()
    try:
        with urllib.request.urlopen(url, data=data) as resp:
            return resp.read().decode()
    except urllib.error.HTTPError as e:
        sys.exit(f"Telegram API error {e.code}: {e.read().decode()}")


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 scripts/telegram.py "<message>"')
    print(send(sys.argv[1]))


if __name__ == "__main__":
    main()
