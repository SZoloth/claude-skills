---
name: warelay
description: Turn Claude into a proactive WhatsApp assistant via Twilio or WhatsApp Web. This skill should be used when setting up WhatsApp relay, troubleshooting WhatsApp integration, managing warelay processes, or configuring Twilio sandbox. Triggers on "WhatsApp", "warelay", "Twilio relay", or "message relay".
---

# warelay - WhatsApp AI Assistant

Turn Claude into a proactive WhatsApp assistant.

## Providers

- **Twilio** (recommended): Polls Twilio API for messages
- **Web**: Uses WhatsApp Web via Baileys (requires QR login, has limitations)

## Start/Stop Commands

```bash
# Start Twilio relay in tmux (recommended)
cd ~/.warelay && tmux new-session -d -s warelay "source .env && warelay relay --provider twilio --interval 5 --lookback 5 --verbose 2>&1 | tee /tmp/warelay/relay.log"

# Check status
tmux ls | grep warelay
tail -f /tmp/warelay/relay.log

# Stop relay
tmux kill-session -t warelay

# Web provider (alternative)
warelay login --verbose  # Scan QR
warelay relay --provider web --verbose
```

## Config Files

| File | Purpose |
|------|---------|
| `~/.warelay/warelay.json` | Main config (Claude command, allowFrom list) |
| `~/.warelay/.env` | Twilio credentials |
| `~/.warelay/sessions.json` | Session state |

## Twilio Sandbox Setup

1. Go to https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
2. Send "join <code>" to +1 415 523 8886 from WhatsApp
3. Start relay with `--provider twilio`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Multiple replies | Ensure only ONE relay runs (`pgrep -fl warelay`) |
| Web won't receive self-messages | Use a different contact; Baileys only triggers on inbound |
| Relay respawns after kill | Check `~/Library/LaunchAgents/*warelay*`, rename to `.disabled` |
| Twilio messages not arriving | Verify sandbox join and `allowFrom` includes your number |

**Logs:** `/tmp/warelay/relay.log` and `/tmp/warelay/warelay.log`
