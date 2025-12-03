---
name: dj
description: Control Spotify playback, search music, manage playlists, switch devices, and handle likes via spotify-player CLI. Use when user mentions Spotify, music control, playing songs, creating playlists, or DJ features. Supports conversational context-aware requests.
---

# DJ - Spotify Control via CLI

Control your Spotify playback, discover music, manage playlists, and switch devices through natural language commands powered by `spotify-player` CLI.

## When to Use

This skill triggers when the user:
- Mentions Spotify, music, songs, albums, artists, or playlists
- Wants playback control (play, pause, skip, volume, shuffle, repeat)
- Searches for music or asks about the current track
- Manages playlists (create, add tracks, remove)
- Switches playback devices
- Likes/unlikes tracks or albums
- Asks for DJ features or music recommendations

## Prerequisites

- `spotify-player` must be installed (`cargo install spotify_player`)
- Must be authenticated with Spotify (`spotify-player authenticate`)
- Spotify Premium account required for full functionality

## Available Operations

### Playback Control
- **Play/Pause**: Resume or pause playback
- **Skip**: Next or previous track
- **Volume**: Adjust volume (set to level or increase/decrease)
- **Shuffle**: Toggle shuffle mode on/off
- **Repeat**: Cycle through repeat modes (track, context, off)
- **Current Track**: Display currently playing track information

### Search & Discovery
- **Search**: Find tracks, albums, artists, or playlists
- **Search and Play**: Search and immediately play top result
- **Current**: Get detailed information about what's playing

### Playlist Management
- **List Playlists**: View all your playlists
- **Create Playlist**: Make a new playlist
- **Add to Playlist**: Add tracks to existing playlists (supports fuzzy playlist name matching)

### Device Management
- **List Devices**: See all available Spotify Connect devices
- **Connect**: Switch playback to a different device (supports fuzzy device name matching)

### Library Management
- **Like**: Like the currently playing track
- **Unlike**: Remove like from current track

### Interactive Mode
- **DJ Mode**: Launch full interactive spotify-player session for extended browsing and control

## Best Practices

### CLI vs Interactive Mode Decision Tree

**Use CLI commands when:**
- Quick single operations (play, pause, skip, volume)
- Specific search with immediate action needed
- Device switching
- Like/unlike tracks
- Creating or listing playlists

**Use Interactive Mode when:**
- Extended browsing through library
- Real-time visual feedback desired
- DJ-style session with keyboard shortcuts
- Exploring multiple albums or artists
- Queue management and visual progress tracking

## Example Workflows

### Quick Playback Control
```
User: "Play some music"
DJ: ▶️  Playback resumed
```

### Search and Play
```
User: "Play Miles Davis"
DJ: 🔍 Searching for "Miles Davis"...
    ▶️  Playing: So What - Miles Davis
```

### Conversational Context
```
User: "Search for jazz piano"
DJ: 🔍 Search results for "jazz piano":
    1. Take Five - Dave Brubeck Quartet
    2. Blue Rondo à la Turk - Dave Brubeck
    ...

User: "Play #2"
DJ: ▶️  Playing: Blue Rondo à la Turk - Dave Brubeck

User: "Add this to my focus playlist"
DJ: ✅ Added Blue Rondo à la Turk to "Focus Music"
```

### Device Switching
```
User: "Play on living room speaker"
DJ: 🔌 Switching to device...
    ✅ Connected to: Living Room Speaker
```

### Playlist Creation
```
User: "Create a workout playlist"
DJ: ✅ Created playlist: Workout

User: "Search for high energy tracks"
DJ: 🔍 Search results...

User: "Add #1, #3, and #5 to workout"
DJ: ✅ Added 3 tracks to Workout playlist
```

## Natural Language Support

The DJ skill understands conversational requests:

**Playback:**
- "play", "pause", "stop", "resume"
- "next song", "skip", "previous track"
- "turn it up", "louder", "volume to 50"
- "shuffle on", "shuffle off"

**Context-aware:**
- "play that again" (replays current/last track)
- "add this to my X playlist" (adds current track)
- "play #3" (plays numbered search result)
- "what's playing" (shows current track)

**Search:**
- "play some jazz"
- "search for Miles Davis"
- "find workout music"

**Devices:**
- "play on speaker"
- "switch to macbook"
- "connect to my phone"

## Troubleshooting

### Not Authenticated
```
❌ Error: Not authenticated with Spotify

To fix:
1. Run: spotify-player authenticate
2. Follow the browser prompts to authorize
3. Try your command again

Note: Spotify Premium required for full functionality
```

### No Active Device
```
⚠️  No active playback device found

Available devices:
1. MacBook Pro
2. Living Room Speaker

Try: "connect to MacBook Pro"
```

### Empty Search Results
```
🔍 No results found for your search

Suggestions:
- Check spelling
- Try broader search terms
- Search by artist name instead
```

### Command Not Found
```
❌ Error: spotify-player not installed

Install with: cargo install spotify_player
Then authenticate: spotify-player authenticate
```

## Integration with Other Skills

**Morning Kickstart:**
Start your day with energizing music automatically

**Executive Assistant:**
Play ambient background music before meetings, chill music after work

**Focus Mode:**
Auto-start focus playlists when entering deep work sessions

## Advanced Features

### Fuzzy Matching
Device and playlist names support partial matching:
- "speaker" matches "Living Room Speaker"
- "workout" matches "Workout Mix 2024"

### Context Persistence
The DJ skill remembers:
- Recent search results
- Last played track
- Recently viewed playlists
- Current device

This enables conversational interactions across multiple requests.

### Session Management
Interactive mode sessions are tracked, allowing you to check status and manage long-running DJ sessions.

## Extending the Skill

To add new commands:
1. Add command to `spotify.mjs` commands registry
2. Follow the command pattern (async function with args and context)
3. Update context manager if needed for conversational support
4. Add documentation to references/COMMANDS.md

## Resources

- spotify-player CLI documentation: Use `spotify-player --help`
- Command reference: See `references/COMMANDS.md`
- Natural language patterns: See `references/NATURAL-LANGUAGE.md`
- Interactive mode guide: See `references/INTERACTIVE-MODE.md`
