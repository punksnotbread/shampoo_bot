# Shampoo scraper

Mainly does 3 things:
1) Scrapes various local pharmacies
2) Parses the results
3) Sends formatted results to a telegram channel

## Setup
```commandline
poetry install
plawright install
```

```commandline
cp .env.example .env
```
Do not forget to configure the BOT_TOKEN & CHAT_ID for Telegram.

## Running
```commandline
poetry run python -m shampoo_scraper.main
```

## TODOs
- [ ] Tests
- [ ] Make it a running daemon with ability to trigger from chat
- [ ] Save historic results to DB
- [ ] Better logging
- [ ] Containerise
- [ ] Mypy