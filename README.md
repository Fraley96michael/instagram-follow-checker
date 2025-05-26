# Instagram Follow Checker 🕵️‍♂️

A simple Python script to find out who you follow on Instagram that doesn't follow you back — using your official data export.

## 🔧 How It Works
1. Request your Instagram data at [https://www.instagram.com/download/request/](https://www.instagram.com/download/request/)
2. Choose **JSON** format and download your data when ready.
3. Place `following.json` and all `followers_*.json` files in the same folder as this script.
4. Run:

```bash
python3 ghost_follows_checker.py
