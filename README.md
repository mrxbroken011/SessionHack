<h1 align="center">🚀 Session Controller</h1>

<p align="center">
  <b>An advanced Telegram Session Controller Bot</b>
</p>

<p align="center">
  <a href="https://github.com/Mrxbroken011/SessionHack">
    <img src="https://img.shields.io/badge/Repository-SessionHack-blue?style=flat-square" alt="Repository"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Maintained-Yes-success?style=flat-square" alt="Maintained"/>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"/>
  </a>
</p>


##

## ⚡ Overview

Session Controller is a modular Telegram bot that helps you inspect and manage Telegram string sessions programmatically. It combines the strengths of **Pyrogram** and **Telethon** to provide powerful account and group management features while offering a clean interactive UI.

**Intended use:** educational & administrative tools for managing your *own* Telegram sessions. See the Notice below.

##

## ✨ Quick Highlights

* **Dual engine:** Pyrogram + Telethon for compatibility and performance.
* **Session management:** view, terminate, and inspect active sessions.
* **Account tools:** fetch user details, check 2FA, retrieve OTPs (where applicable), delete accounts safely.
* **Group control:** list admined chats, join/leave, ban members, promote/demote.
* **Modular UI:** interactive inline buttons and automatic module loader.

##

## 📚 Notice (Important)

**This project is provided for educational purposes only.** Use it to learn how Telegram sessions and string sessions work, how to recover or re-login accounts you own, and to perform administrative tasks on accounts you control. **Do not use this tool to access, control, or interfere with accounts that you do not own or have explicit permission to manage.** Misuse may violate Telegram's Terms of Service and local laws.

##

## 🧭 Installation & Usage (Recommended)

### 🚀 One-click: Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mrxbroken011/SessionHack)

> Ensure your repository includes a valid `Procfile` or `heroku.yml` and the required environment variables in the Heroku dashboard.

##

### 🖥️ Manual: VPS / Local Linux (Guide)

<details>
<summary><strong>Click to expand detailed setup</strong></summary>

#### Step 1 — Update & install dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl python3-pip python3-venv tmux nano
sudo pip3 install -U pip
```

#### Step 2 — Clone repository

```bash
git clone https://github.com/mrxbroken011/SESSIONHACK 
cd SESSIONHACK
tmux new -s hac
```

#### Step 3 — Create virtualenv & install Python deps

```bash
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

#### Step 4 — Configure environment

```bash
cp sample.env .env
nano .env
```

Fill the `.env` variables (API_ID, API_HASH, BOT_TOKEN, OWNER_ID, etc.). Save (`Ctrl+X`, `Y`, `Enter`).

#### Step 5 — Run the bot

```bash
bash start
```

#### Maintenance

* Stop & remove repo: `rm -rf SessionHack`
* Attach to tmux: `tmux attach-session -t hac`
* Kill tmux session: `tmux kill-session -t hac`

</details>

##

## 🧩 Contributing

Contributions, bug reports, and pull requests are welcome. Please follow these guidelines:

1. Fork the repository and create a feature branch.
2. Keep changes focused and well-documented.
3. Include tests/examples where applicable.
4. Open a pull request describing the change and why it helps.

##

## 📣 Support & Updates

Join the community channels for support and release updates:

<p align="center">
  <a href="https://t.me/BROKENXNETWORK1"><img src="https://img.shields.io/badge/Support%20Chat-0088CC?style=for-the-badge&logo=telegram&logoColor=white" alt="support"/></a>
  <a href="https://t.me/ABOUTBROKENX"><img src="https://img.shields.io/badge/Updates%20Channel-229ED9?style=for-the-badge&logo=telegram&logoColor=white" alt="updates"/></a>
</p>
