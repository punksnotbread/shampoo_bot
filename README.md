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
Do not forget to configure the BOT_TOKEN & CHAT_ID for Telegram. Also, see Configuration

## Running
```commandline
poetry run python -m shampoo_scraper.main
```

## Docker
App can be built as a Docker container.
```commandline
docker build -f infrastructure/app/Dockerfile .
```

And then run
```commandline
docker run CONTAINER_ID
```

## Configuration
Project is configured via .env file. Currently used/supported keys:
* `BOT_TOKEN` - bot token for Telegram.
* `CHAT_ID` - chat ID for Telegram where to post to.
* `ENVIRONMENT` - what environment are we running in. If not `prod`, 
   we do not post messages via the bot. Defaults to `local`.
* `QUERIES` - JSON compatible list of queries. e.g. '["dercos"]'.
* `SEARCH_TYPES` - JSON compatible list of str of what pharmacies to scrape. 
   Defaults to: '["camelia", "eurovaistine", "gintarinevaistine"]'. Supported values:
  * "camelia"
  * "eurovaistine"
  * "gintarinevaistine"
* `PARALEL_JOB_COUNT` - how many jobs to do in parallel. As we're using browsers, we may
  use a lot of resources. Defaults to `3`.

## TODOs
- [ ] Make it a running daemon with ability to trigger from chat
- [ ] Save historic results to DB
- [x] Better logging
- [x] Containerise
- [ ] Mypy
- [ ] Tests
