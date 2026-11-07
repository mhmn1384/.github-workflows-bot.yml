name: SE BOT

on:
  schedule:
    - cron: "*/15 * * * *"
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: se-bot
  cancel-in-progress: false

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install numpy requests
      - name: Run bot
        run: python se_bot_gh.py
      - name: Save state
        run: |
          git config user.name "se-bot"
          git config user.email "se-bot@users.noreply.github.com"
          git add state.json trades.log
          git diff --cached --quiet || (git commit -m "update state" && git push)
