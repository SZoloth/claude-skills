---
name: gmail-manager
description: Manage Gmail emails for job search workflows. Use when the user wants to check recruiting emails, scan for inbound recruiter outreach, send follow-ups, create drafts, search messages, or manage their inbox. Optimized for job search communication.
---

# Gmail Manager

A skill for managing Gmail emails with a focus on job search workflows using the Code Execution pattern for token efficiency.

## When to use this skill

Use this skill whenever the user:
- Wants to check unread emails (especially from recruiters)
- Wants to scan inbox for inbound recruiter outreach
- Needs to respond to recruiter emails
- Needs to send follow-up emails to hiring managers or recruiters
- Wants to search for specific emails (interviews, offers, applications)
- Needs to create email drafts for review
- Wants to organize emails (mark as read, archive, label)
- Mentions "email", "Gmail", "inbox", "recruiter", or specific email tasks

## Prerequisites

This skill requires:
1. Gmail MCP server configured in `.mcp.json` (in `1 - personal/.mcp.json`)
2. Python environment with the MCP client modules
3. Gmail API credentials properly configured in the MCP server

## Available operations

All operations use the Python CLI at `scripts/gmail_cli.py`.

### Check unread emails
```bash
python scripts/gmail_cli.py unread [limit]
```
Shows unread messages. Default limit is 50.

Example:
```bash
python scripts/gmail_cli.py unread 10  # Show 10 most recent unread
```

### Search emails
```bash
python scripts/gmail_cli.py search "query" [limit]
```
Search using Gmail search syntax.

Example:
```bash
python scripts/gmail_cli.py search "from:recruiter@gusto.com"
python scripts/gmail_cli.py search "subject:interview"
python scripts/gmail_cli.py search "is:unread interview OR offer"
```

### Get specific email
```bash
python scripts/gmail_cli.py get <message-id>
```
Get full details of a specific email by ID.

### Send email
```bash
python scripts/gmail_cli.py send <to> <subject> <body>
```
Send a new email.

Example:
```bash
python scripts/gmail_cli.py send "recruiter@example.com" "Follow-up: PM Role" "Thanks for the interview..."
```

### Create draft
```bash
python scripts/gmail_cli.py draft <to> <subject> <body>
```
Create a draft email (doesn't send).

### Reply to email
```bash
python scripts/gmail_cli.py reply <message-id> <body>
```
Reply to an existing email.

### Mark as read
```bash
python scripts/gmail_cli.py mark-read <message-id>
```

### Archive email
```bash
python scripts/gmail_cli.py archive <message-id>
```

### Scan for recruiter emails (NEW)
```bash
python scripts/gmail_cli.py scan-recruiters [days]
```
Automatically detect inbound recruiter emails and add them to the job search hub as "Inbound" opportunities. Default: 14 days.

**Detection signals:**
- Known recruiter domains: linkedin.com, greenhouse.io, lever.co, ashbyhq.com, gem.com
- Email patterns: recruit@, talent@, hiring@, careers@, people@, hr@
- Subject signals: "opportunity", "role at", "position at", "interested in your profile"
- Body signals: "saw your profile", "perfect fit", "compensation", "on behalf of"

**What it does:**
1. Searches Gmail for potential recruiter emails
2. Filters using multi-layer detection (domain, email pattern, subject, body)
3. Extracts company name and role from email content
4. Adds new entries to job search hub with status "Inbound"
5. Skips emails already matched to pipeline entries

Example:
```bash
python scripts/gmail_cli.py scan-recruiters       # last 14 days
python scripts/gmail_cli.py scan-recruiters 30    # last 30 days
```

### Generate recruiter reply template
```bash
python scripts/gmail_cli.py draft-reply <message-id>
```
Generate a response template for a recruiter email with:
- Extracted sender name and company
- Detected role (if found in email)
- Professional response template with key questions
- Instructions for creating the draft in Gmail

Example:
```bash
python scripts/gmail_cli.py draft-reply 19ae1bdf5bb76bed
```

## Job search use cases

### Process Job Alert Emails (Otta, Wellfound, LinkedIn)

**⚠️ IMPORTANT**: Before processing job alerts, invoke the **job-search-specialist** skill which has the Job Alert Processing Protocol. Key points:

1. Job alerts can be stale - verify roles exist on company careers page
2. Don't create Application folders until role is verified active
3. Filter by location: Remote → Denver → Durham/Raleigh

**Search for job alerts:**
```bash
python scripts/gmail_cli.py search "from:otta.com OR from:wellfound.com OR from:linkedin.com job" 20
```

**After extraction**: Follow job-search-specialist's Job Alert Processing Protocol for verification and folder creation.

### Check recruiting emails
```bash
python scripts/gmail_cli.py search "recruiter OR interview OR application" 20
```

### Find emails from specific company
```bash
python scripts/gmail_cli.py search "from:@gusto.com OR from:@davita.com"
```

### Follow-up workflow
1. Search for interview email
2. Get the message ID
3. Create draft reply for review
4. Send after approval

## Best practices

### When checking emails
1. Use specific search queries to filter noise
2. Focus on recruiting-related keywords: recruiter, interview, application, offer, hiring
3. Limit results to avoid overwhelming output

### When sending emails
1. Always create drafts first for important emails
2. Review subject lines for clarity
3. Keep body text concise and professional
4. Use reply-to-message for threading

### Search syntax tips
- `from:domain.com` - from specific domain
- `subject:keyword` - subject contains keyword
- `is:unread` - only unread messages
- `after:2025/11/01` - after specific date
- `has:attachment` - has attachments
- Combine with OR: `interview OR offer`

## Job Search Hub Integration

**Primary Hub**: `.claude/skills/data/job_search_hub.json`

When processing emails, cross-reference with the job search hub for context-aware handling.

### On Email Check: Pipeline Awareness

Before displaying search results, read `hub.pipeline[]` to identify active companies:

```python
import json
from pathlib import Path

hub_path = Path.home() / "Documents/LLM CONTEXT/.claude/skills/data/job_search_hub.json"
hub = json.loads(hub_path.read_text())

# Get active pipeline companies
active_companies = [e['company'].lower() for e in hub['pipeline']
                   if e['status'] not in ['rejected', 'withdrawn', 'stale']]

# When displaying emails, highlight those from pipeline companies
for email in emails:
    sender = email.get('from', '').lower()
    for company in active_companies:
        if company in sender:
            print(f"[PIPELINE] {email['subject']}")  # Highlight as relevant
```

### After Sending Job Email: Offer to Log

When a job-related email is sent, offer to update the hub:

**Prompt**: "Log this as outreach to [Company]?"

If yes:
```bash
python scripts/job_search_hub_sync.py --log-outreach "Company" "Contact Name" email
```

### On Response Received: Offer Status Update

When an email response is received from a pipeline company:

**Prompt**: "Update [Company] status to 'responded'?"

If yes:
```bash
python scripts/job_search_hub_sync.py --update-pipeline company status responded
```

### Relevant Searches for Job Search

| Search | Use Case |
|--------|----------|
| `from:otta.com OR from:wellfound.com` | Job alert processing |
| `subject:interview` | Interview scheduling |
| `subject:offer` | Offer-related communication |
| Companies in hub.pipeline | Active opportunity updates |

## Token efficiency

This skill uses the Code Execution pattern:
- No persistent MCP tools loaded in every conversation
- Python code executes on-demand when skill is invoked
- 95%+ token savings compared to always-on MCP tools
- Clean separation between orchestration (skill) and execution (Python)
