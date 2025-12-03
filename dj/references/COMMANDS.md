# DJ Skill - Complete Command Reference

Detailed reference for all DJ skill commands.

## Playback Control

### play
Resume playback.

**Usage:**
```bash
npm run dj play
```

**Output:**
```
▶️  Resumed playback
```

**Errors:**
- No active device → Shows available devices
- Not authenticated → Guide to authentication

---

### pause
Pause playback.

**Usage:**
```bash
npm run dj pause
```

**Output:**
```
⏸  Paused
```

---

### next
Skip to next track.

**Usage:**
```bash
npm run dj next
```

**Output:**
```
⏭  Skipped
```

---

### previous
Go to previous track.

**Usage:**
```bash
npm run dj previous
```

**Output:**
```
⏮  Previous track
```

---

### volume
Adjust volume (0-100% or relative +/-).

**Usage:**
```bash
npm run dj volume 50       # Set to 50%
npm run dj volume +10      # Increase by 10%
npm run dj volume -5       # Decrease by 5%
```

**Arguments:**
- `<level>` - Volume level (0-100) or relative change (+N/-N)

**Output:**
```
🔊 Volume: 50%
🔊 Volume: +10
```

**Examples:**
```bash
npm run dj volume 75       # Set to 75%
npm run dj volume +5       # Louder by 5%
npm run dj volume -10      # Quieter by 10%
```

---

### shuffle
Toggle shuffle mode.

**Usage:**
```bash
npm run dj shuffle         # Turn on
npm run dj shuffle on      # Turn on
npm run dj shuffle off     # Turn off
```

**Arguments:**
- `[on|off]` - Optional, defaults to "on"

**Output:**
```
🔀 Shuffle: ON
🔀 Shuffle: OFF
```

---

### repeat
Set repeat mode.

**Usage:**
```bash
npm run dj repeat          # Cycle through modes
npm run dj repeat track    # Repeat current track
npm run dj repeat context  # Repeat album/playlist
npm run dj repeat off      # Turn off repeat
```

**Arguments:**
- `[mode]` - track, context, off, or cycle (default)

**Output:**
```
🔁 Repeat: TRACK
🔁 Repeat: CONTEXT
🔁 Repeat: OFF
```

---

## Discovery

### current
Show currently playing track with full details.

**Usage:**
```bash
npm run dj current
```

**Output:**
```
🎵 Now Playing:
   So What - Miles Davis
   Album: Kind of Blue
   Duration: 9:22
```

**Returns:** Track object (JSON internally)

---

### search
Search for tracks, albums, artists, or playlists.

**Usage:**
```bash
npm run dj search <type> <query>
```

**Arguments:**
- `<type>` - track, album, artist, or playlist
- `<query>` - Search terms

**Output:**
```
🔍 Search results for "miles davis" (track):

1. So What - Miles Davis
2. Blue in Green - Miles Davis
3. Freddie Freeloader - Miles Davis
4. All Blues - Miles Davis
5. Flamenco Sketches - Miles Davis

💡 Tip: Use "npm run dj search-play track miles davis" to play top result
```

**Examples:**
```bash
npm run dj search track "coltrane"
npm run dj search album "kind of blue"
npm run dj search artist "miles davis"
npm run dj search playlist "jazz essentials"
```

**Returns:** Array of search results (up to 10)

---

### search-play
Search and immediately play the top result.

**Usage:**
```bash
npm run dj search-play <type> <query>
```

**Arguments:**
- `<type>` - track, album, artist, or playlist
- `<query>` - Search terms

**Output:**
```
🔍 Search results for "coltrane" (track):
[... results ...]

▶️  Playing: Giant Steps - John Coltrane
```

**Examples:**
```bash
npm run dj search-play track "giant steps"
npm run dj search-play artist "coltrane"
npm run dj search-play playlist "focus"
```

---

## Library Management

### like
Like the currently playing track.

**Usage:**
```bash
npm run dj like
```

**Output:**
```
❤️  Liked current track
```

---

### unlike
Remove like from current track.

**Usage:**
```bash
npm run dj unlike
```

**Output:**
```
💔 Unliked current track
```

---

### playlists
List all your playlists.

**Usage:**
```bash
npm run dj playlists
```

**Output:**
```
📚 Your playlists:

1. Workout Mix (47 tracks)
2. Focus Music (23 tracks)
3. Chill Vibes (31 tracks)
...
```

**Returns:** Array of playlist objects

---

### create-playlist
Create a new playlist.

**Usage:**
```bash
npm run dj create-playlist <name>
```

**Arguments:**
- `<name>` - Playlist name (can include spaces)

**Output:**
```
✅ Created playlist: Workout Mix
```

**Examples:**
```bash
npm run dj create-playlist "Morning Routine"
npm run dj create-playlist Favorites
```

---

## Device Management

### devices
List all available Spotify Connect devices.

**Usage:**
```bash
npm run dj devices
```

**Output:**
```
🔌 Available devices:

▶️ 1. MacBook Pro (Computer)
   2. Living Room Speaker (Speaker)
   3. iPhone (Smartphone)
```

**Note:** ▶️ indicates currently active device

**Returns:** Array of device objects

---

### connect
Switch playback to a different device.

**Usage:**
```bash
npm run dj connect <device-name>
```

**Arguments:**
- `<device-name>` - Full or partial device name (fuzzy matched)

**Output:**
```
✅ Connected to: Living Room Speaker
```

**Fuzzy Matching Examples:**
```bash
npm run dj connect speaker       # Matches "Living Room Speaker"
npm run dj connect mac           # Matches "MacBook Pro"
npm run dj connect phone         # Matches "iPhone"
```

**Errors:**
```
❌ Device "xyz" not found

Available devices:
  1. MacBook Pro
  2. Living Room Speaker
```

---

## Interactive Mode

### interactive
Launch full interactive spotify-player session.

**Usage:**
```bash
npm run dj interactive
```

**Output:**
```
🎧 Launching interactive DJ mode...
Press ? for help, q to quit

[Interactive interface opens]
```

**Keyboard Shortcuts in Interactive Mode:**
- `Space` - Play/pause
- `n` - Next track
- `p` - Previous track
- `+`/`-` - Volume up/down
- `<`/`>` - Seek backward/forward
- `?` - Help
- `q` - Quit

---

## Session Management

### session start
Start interactive session with tracking.

**Usage:**
```bash
npm run dj:session start
```

**Output:**
```
🎧 Launching interactive DJ mode...

Keyboard Shortcuts:
  Space    Play/Pause
  n        Next track
  ...
```

---

### session status
Check if interactive session is running.

**Usage:**
```bash
npm run dj:session status
```

**Output:**
```
📊 Session Status

  Status: ✅ Running
  PID: 12345
  Started: 2025-01-27T10:30:00Z
  Duration: 15m 32s
```

---

### session stop
Stop running interactive session.

**Usage:**
```bash
npm run dj:session stop
```

**Output:**
```
✅ Session stopped
```

---

### session cleanup
Remove stale session data.

**Usage:**
```bash
npm run dj:session cleanup
```

**Output:**
```
✅ Session cleaned up
```

---

## Utility

### help
Show command reference.

**Usage:**
```bash
npm run dj help
npm run dj  # (same as help)
```

**Output:**
```
🎵 Spotify DJ - Control Spotify via CLI

[Command listing with examples]
```

---

## Error Handling

All commands implement consistent error handling:

### Authentication Error
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

Try: npm run dj connect "MacBook Pro"
```

### Search No Results
```
🔍 No results found for "xyz123impossible"

Suggestions:
- Check spelling
- Try broader search terms
- Search by artist name instead
```

### Invalid Arguments
```
Usage: volume <0-100|+N|-N>
Examples:
  npm run dj volume 50      # Set to 50%
  npm run dj volume +10     # Increase by 10%
  npm run dj volume -5      # Decrease by 5%
```

---

## Return Values

Commands that return data (for programmatic use):

- `current` - Returns track object
- `search` - Returns array of search results
- `playlists` - Returns array of playlist objects
- `devices` - Returns array of device objects

All other commands return void (exit code 0 on success, 1 on error).

---

## Context Integration

Some commands automatically update conversational context:

- `search` - Stores results for "play #N" references
- `current` - Stores track for "this track" references
- `playlists` - Stores list for fuzzy playlist matching
- `devices` - Stores active device info

See `references/NATURAL-LANGUAGE.md` for context-aware usage patterns.
