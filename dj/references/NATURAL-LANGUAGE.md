# DJ Skill - Natural Language Patterns

This guide shows how Claude interprets natural language requests and maps them to DJ skill commands. The skill supports conversational, context-aware interactions.

## Simple Commands

### Playback Control

| What You Say | Command Executed | Notes |
|--------------|------------------|-------|
| "play" | `npm run dj play` | Resume playback |
| "pause" | `npm run dj pause` | Pause playback |
| "stop" | `npm run dj pause` | Same as pause |
| "resume" | `npm run dj play` | Same as play |
| "next" | `npm run dj next` | Skip to next track |
| "skip" | `npm run dj next` | Same as next |
| "next song" | `npm run dj next` | Same as next |
| "previous" | `npm run dj previous` | Previous track |
| "back" | `npm run dj previous` | Same as previous |
| "last song" | `npm run dj previous` | Same as previous |

### Volume Control

| What You Say | Command Executed | Notes |
|--------------|------------------|-------|
| "volume up" | `npm run dj volume +5` | Increase by 5% |
| "louder" | `npm run dj volume +5` | Increase by 5% |
| "turn it up" | `npm run dj volume +5` | Increase by 5% |
| "volume down" | `npm run dj volume -5` | Decrease by 5% |
| "quieter" | `npm run dj volume -5` | Decrease by 5% |
| "turn it down" | `npm run dj volume -5` | Decrease by 5% |
| "volume to 50" | `npm run dj volume 50` | Set to 50% |
| "set volume 75" | `npm run dj volume 75` | Set to 75% |

### Shuffle & Repeat

| What You Say | Command Executed | Notes |
|--------------|------------------|-------|
| "shuffle on" | `npm run dj shuffle on` | Enable shuffle |
| "shuffle off" | `npm run dj shuffle off` | Disable shuffle |
| "enable shuffle" | `npm run dj shuffle on` | Enable shuffle |
| "repeat this track" | `npm run dj repeat track` | Repeat current track |
| "repeat on" | `npm run dj repeat context` | Repeat playlist/album |
| "repeat off" | `npm run dj repeat off` | Disable repeat |

---

## Context-Aware Commands

These require conversational context from previous commands.

### Track References

**After searching or showing current track:**

| What You Say | Resolves To | Command | Prerequisites |
|--------------|-------------|---------|---------------|
| "play that again" | Current track URI | `playback play-uri` | Recent `current` |
| "play this" | Current track URI | `playback play-uri` | Recent `current` |
| "like this" | Current track | `npm run dj like` | Track playing |
| "add this to my workout playlist" | Current track + fuzzy matched playlist | `playlist add` | Track + playlists loaded |

**Example conversation:**
```
You: "What's playing?"
DJ: [Shows current track: "So What - Miles Davis"]

You: "Play that again"
DJ: [Replays "So What"]

You: "Add this to my jazz playlist"
DJ: [Adds "So What" to fuzzy-matched "Jazz Favorites" playlist]
```

### Search Result References

**After searching:**

| What You Say | Resolves To | Command | Prerequisites |
|--------------|-------------|---------|---------------|
| "play #1" | 1st search result | `playback play-uri` | Recent search |
| "play #3" | 3rd search result | `playback play-uri` | Recent search |
| "play number 2" | 2nd search result | `playback play-uri` | Recent search |
| "play result 5" | 5th search result | `playback play-uri` | Recent search |

**Example conversation:**
```
You: "Search for Miles Davis"
DJ: 🔍 Search results for "Miles Davis" (track):
    1. So What - Miles Davis
    2. Blue in Green - Miles Davis
    3. Freddie Freeloader - Miles Davis
    ...

You: "Play #2"
DJ: ▶️  Playing: Blue in Green - Miles Davis
```

### Playlist Fuzzy Matching

**After listing playlists:**

| What You Say | Fuzzy Matches | Command | Notes |
|--------------|---------------|---------|-------|
| "workout" | "Workout Mix 2024" | Finds playlist | Partial name match |
| "focus" | "Deep Focus" | Finds playlist | Partial name match |
| "chill" | "Chill Vibes" | Finds playlist | Partial name match |

**Example conversation:**
```
You: "Show my playlists"
DJ: 📚 Your playlists:
    1. Workout Mix 2024 (47 tracks)
    2. Deep Focus (23 tracks)
    3. Chill Vibes (31 tracks)

You: "Play the workout playlist"
DJ: [Fuzzy matches "Workout Mix 2024" and plays it]
```

---

## Search Patterns

### Basic Search

| What You Say | Interpreted As | Command |
|--------------|----------------|---------|
| "search for jazz" | Search tracks | `npm run dj search track "jazz"` |
| "find miles davis" | Search tracks | `npm run dj search track "miles davis"` |
| "search albums coltrane" | Search albums | `npm run dj search album "coltrane"` |
| "search for workout playlist" | Search playlists | `npm run dj search playlist "workout"` |

### Search and Play

| What You Say | Interpreted As | Command |
|--------------|----------------|---------|
| "play some jazz" | Search + play | `npm run dj search-play track "jazz"` |
| "play miles davis" | Search + play | `npm run dj search-play artist "miles davis"` |
| "play kind of blue" | Search + play | `npm run dj search-play album "kind of blue"` |

**Example:**
```
You: "Play some chill music"
DJ: 🔍 Searching for "chill music"...
    ▶️  Playing: Breathe - Télépopmusik
```

---

## Device Switching Patterns

### Fuzzy Device Matching

| What You Say | Fuzzy Matches | Command | Notes |
|--------------|---------------|---------|-------|
| "play on speaker" | "Living Room Speaker" | `npm run dj connect speaker` | Partial match |
| "switch to mac" | "MacBook Pro" | `npm run dj connect mac` | Partial match |
| "connect to phone" | "iPhone" | `npm run dj connect phone` | Partial match |
| "play on living room" | "Living Room Speaker" | `npm run dj connect living room` | Multi-word match |

**Example conversation:**
```
You: "Show available devices"
DJ: 🔌 Available devices:
    ▶️ 1. MacBook Pro (Computer)
       2. Living Room Speaker (Speaker)
       3. iPhone (Smartphone)

You: "Switch to the speaker"
DJ: ✅ Connected to: Living Room Speaker
```

---

## Multi-Step Workflows

### Search → Filter → Play

```
You: "Search for jazz piano"
DJ: 🔍 Search results for "jazz piano" (track):
    1. Take Five - Dave Brubeck Quartet
    2. Blue Rondo à la Turk - Dave Brubeck
    3. Autumn Leaves - Bill Evans Trio
    ...

You: "Play #3"
DJ: ▶️  Playing: Autumn Leaves - Bill Evans Trio

You: "Like this"
DJ: ❤️  Liked current track
```

### Create Playlist → Search → Add

```
You: "Create a playlist called Focus Music"
DJ: ✅ Created playlist: Focus Music

You: "Search for ambient tracks"
DJ: 🔍 Search results for "ambient tracks" (track):
    1. Weightless - Marconi Union
    2. Breathe - Télépopmusik
    ...

You: "Play #1"
DJ: ▶️  Playing: Weightless - Marconi Union

You: "Add this to my focus playlist"
DJ: ✅ Added Weightless to Focus Music
```

### Device Switch → Volume → Play

```
You: "Switch to living room speaker"
DJ: ✅ Connected to: Living Room Speaker

You: "Volume to 30"
DJ: 🔊 Volume: 30%

You: "Play some morning music"
DJ: 🔍 Searching for "morning music"...
    ▶️  Playing: Morning in the Mountains
```

---

## Context Persistence

Context persists across conversations (for 1 hour):

```
Session 1 (10:00 AM):
You: "Search for Miles Davis"
DJ: [Shows results, stores in context]

Session 2 (10:15 AM):
You: "Play #2"
DJ: [Still remembers search results, plays track]
```

Context includes:
- Last 10 search results
- Current playing track
- Last 20 playlists viewed
- Active device info
- Conversation mode state

---

## Ambiguity Resolution

### When Multiple Interpretations Exist

**"Play jazz"** could mean:
1. Search track "jazz" and play top result ✅ (chosen by default)
2. Search playlist "jazz" and play
3. Search artist "jazz" and play

**Claude's approach:**
- Default to most common interpretation (track search)
- User can be specific: "play the jazz playlist"

### When Context is Unclear

**"Play that"** when no context:
```
DJ: ❌ No track reference found in context
    Try:
    - "search for [song]" first
    - "what's playing" to set current track
```

---

## Tips for Best Results

### Be Specific When Needed

❌ Vague: "Play it"
✅ Clear: "Play that track again"

❌ Ambiguous: "Switch device"
✅ Specific: "Switch to speaker"

### Use Context Flow

Good conversation flow:
```
1. "Search for coltrane" (sets search context)
2. "Play #3" (uses search context)
3. "Like this" (uses playing context)
4. "Add to my jazz playlist" (uses playing + playlist context)
```

### Fuzzy Matching Works Best with Unique Terms

✅ "workout" → Likely matches "Workout Mix"
⚠️  "music" → May match multiple playlists with "music" in name

### Context Hints

The skill provides hints when context is available:

```
💡 Say "play #N" to play a search result (1-5)
💡 Say "add this to my playlist" to save current track
💡 Say "play that again" to replay
```

---

## Natural Language → Command Mapping Table

Complete mapping of common phrases:

| Category | Natural Language | Command |
|----------|------------------|---------|
| **Playback** | "play" | `play` |
| | "pause", "stop" | `pause` |
| | "next", "skip" | `next` |
| | "previous", "back" | `previous` |
| **Volume** | "louder", "turn it up", "volume up" | `volume +5` |
| | "quieter", "turn it down", "volume down" | `volume -5` |
| | "volume to X" | `volume X` |
| **Current** | "what's playing", "current track", "now playing" | `current` |
| **Search** | "search for X", "find X" | `search track X` |
| | "play some X" | `search-play track X` |
| **Context** | "play #N" | `play search result N` |
| | "play that again" | `play current track` |
| | "add this to my X playlist" | `add current to playlist X` |
| **Devices** | "play on X", "switch to X", "connect to X" | `connect X` |
| | "show devices" | `devices` |
| **Playlists** | "show playlists", "my playlists" | `playlists` |
| | "create playlist X" | `create-playlist X` |
| **Library** | "like this", "like it" | `like` |
| | "unlike this" | `unlike` |
| **Interactive** | "dj mode", "interactive mode" | `interactive` |

---

## Advanced Patterns

### Chained References

```
You: "Search for jazz piano"
[Results shown]

You: "Play #2"
[Blue Rondo à la Turk playing]

You: "Like it"
[Likes Blue Rondo à la Turk]

You: "Play it again"
[Replays Blue Rondo à la Turk]
```

### Cross-Session Memory

```
Morning (9 AM):
You: "Show my playlists"
[Lists playlists, stores in context]

Later (9:30 AM):
You: "Add this track to my workout playlist"
[Still has playlists in context, fuzzy matches "workout"]
```

### Implicit Context

```
You: "What's playing?"
[Shows current track, stores in context]

You: "Like it"
[Knows "it" = current track, likes it]

You: "Play something similar"
[Uses current track as seed for search]
```

---

## Context Manager Commands

For debugging or clearing context:

```bash
# View current context state
node .claude/skills/dj/context-manager.mjs summary

# Clear all context
node .claude/skills/dj/context-manager.mjs clear

# Load context from disk
node .claude/skills/dj/context-manager.mjs load
```

---

## Summary

The DJ skill supports:
✅ Simple command patterns
✅ Context-aware references ("this", "that", "#N")
✅ Fuzzy matching (playlists, devices)
✅ Multi-step workflows
✅ Cross-session context (1 hour)
✅ Natural conversational flow

For exact command syntax, see `COMMANDS.md`.
For interactive mode features, see `INTERACTIVE-MODE.md`.
