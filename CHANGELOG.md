# Changelog

All notable changes to price-watch.
- move price parsing into items.to_decimal
- load settings from env with sane defaults
- basic product spider with css selectors
- add pre-commit with ruff and black
- randomise user-agent and accept-language per session
- small cleanup
- Prometheus metric for crawl success rate
- handle Set-Cookie on redirect chains
- reuse proxy TLS sessions to cut handshake overhead
