# DJ Skill - Spotify Control via CLI

Control Spotify playback through natural language using the spotify-player CLI tool.

## Quick Start

### Prerequisites

1. **Install spotify-player**
   ```bash
   cargo install spotify_player
   ```

2. **Authenticate with Spotify**
   ```bash
   spotify-player authenticate
   ```
   This will open your browser to authorize the application. You'll need a Spotify Premium account for full functionality.

3. **Verify Installation**
   ```bash
   spotify-player --version
   spotify-player playback --help
   ```

### Usage

The DJ skill provides npm scripts for easy access:

```bash
# Playback control
npm run dj play
npm run dj pause
npm run dj next
npm run dj volume +10

# Search and discovery
npm run dj search track "miles davis"
npm run dj search-play artist "coltrane"
npm run dj current

# Playlists
npm run dj playlists
npm run dj create-playlist "Chill Mix"

# Devices
npm run dj devices
npm run dj connect speaker

# Interactive mode
npm run dj interactive

# Session management
npm run dj:session start
npm run dj:session status
npm run dj:session stop
```

## Architecture

### Components

**spotify.mjs** - Main CLI wrapper
- Command dispatch pattern
- All spotify-player operations
- Error handling and help system

**context-manager.mjs** - Conversational context
- Tracks search results, current track, playlists
- Enables "play that again", "add this to playlist"
- Persists context across sessions

**session-manager.mjs** - Interactive sessions
- Manages long-running spotify-player instances
- Tracks PID and session state
- Status monitoring and cleanup

### File Structure

```
.claude/skills/dj/
├── SKILL.md                    # Skill definition (loaded by Claude Code)
├── spotify.mjs                 # Main CLI wrapper (executable)
├── context-manager.mjs         # Context tracking (executable)
├── session-manager.mjs         # Session management (executable)
├── README.md                   # This file
└── references/
    ├── COMMANDS.md            # Detailed command reference
    ├── NATURAL-LANGUAGE.md    # NL pattern examples
    └── INTERACTIVE-MODE.md    # Interactive features guide
```

## Features

### Playback Control
- Play, pause, skip tracks
- Volume adjustment (absolute and relative)
- Shuffle and repeat modes
- Get current track info

### Search & Discovery
- Search tracks, albums, artists, playlists
- Search and play in one step
- JSON parsing for programmatic use
- Empty result handling with suggestions

### Playlist Management
- List all playlists
- Create new playlists
- Add tracks to playlists
- Fuzzy playlist name matching

### Device Management
- List available Spotify Connect devices
- Switch playback device
- Fuzzy device name matching
- Active device indication

### Library Management
- Like/unlike tracks
- Add to library

### Interactive Mode
- Full keyboard control
- Visual progress tracking
- Real-time playback info
- Session persistence

### Conversational Context
- Reference resolution ("this", "that", "it")
- Numbered results ("play #3")
- Fuzzy matching (playlists, devices)
- Cross-session memory

## Natural Language Examples

The DJ skill understands natural requests:

**Simple:**
```
"play"
"pause"
"next song"
"volume to 50"
```

**Context-aware:**
```
"search for jazz"
→ [shows results]
"play #2"
→ [plays second result]

"what's playing"
→ [shows current track]
"add this to my workout playlist"
→ [adds to fuzzy-matched playlist]

"play that again"
→ [replays current/last track]
```

**Multi-step:**
```
"play some miles davis"
→ [searches and plays top result]

"connect to speaker"
→ [fuzzy matches and switches device]
```

## Troubleshooting

### spotify-player not found

```bash
# Install with cargo
cargo install spotify_player

# Or check installation
which spotify-player
```

### Not authenticated

```bash
# Authenticate with Spotify
spotify-player authenticate

# Follow browser prompts
# Requires Spotify Premium
```

### No active device

```bash
# List available devices
npm run dj devices

# Connect to a device
npm run dj connect "MacBook Pro"
```

### JSON parsing errors

The skill expects JSON output from spotify-player. If you get parsing errors:

```bash
# Verify spotify-player supports JSON output
spotify-player search track "test" --format json

# Update spotify-player if needed
cargo install spotify_player --force
```

### Context not persisting

Context is stored in `~/.config/spotify-player/claude-context.json`.

```bash
# Check context status
node .claude/skills/dj/context-manager.mjs summary

# Clear if needed
node .claude/skills/dj/context-manager.mjs clear
```

## Extending the Skill

### Adding New Commands

1. **Add to spotify.mjs commands registry:**

```javascript
async 'my-command'(args) {
  // Implementation
  const result = await runCommand(['spotify-player', 'args']);
  console.log('✅ Done');
  return result;
}
```

2. **Update help system:**

Add command to `help()` function output.

3. **Update documentation:**

Add to SKILL.md and references/COMMANDS.md.

### Adding Context Awareness

To make your command context-aware:

```javascript
import { context } from './context-manager.mjs';

async 'my-command'(args) {
  // Load context
  await context.load();

  // Use context
  const track = context.resolveReference('this');

  // Do work
  const result = await runCommand([...]);

  // Update context
  context.updateContext('my-command', result);
  await context.save();

  return result;
}
```

## Integration with Claude Code

The DJ skill is automatically loaded by Claude Code when you mention:
- Spotify, music, songs, albums, artists
- Playback control keywords
- Playlist management
- DJ features

Example interactions with Claude:

```
You: "Play some jazz"
Claude: [Uses DJ skill to search and play jazz]

You: "What's playing?"
Claude: [Uses DJ skill to show current track]

You: "Add this to my focus playlist"
Claude: [Uses DJ skill with context to add current track]
```

## Advanced Usage

### Scripting

Use the DJ skill in shell scripts:

```bash
#!/bin/bash
# Morning music routine

npm run dj connect "Living Room Speaker"
npm run dj search-play playlist "Morning Vibes"
npm run dj volume 30
npm run dj shuffle on
```

### Context Inspection

```bash
# View current context
node .claude/skills/dj/context-manager.mjs summary

# Clear context
node .claude/skills/dj/context-manager.mjs clear
```

### Session Management

```bash
# Start interactive session in background
npm run dj:session start &

# Check if running
npm run dj:session status

# Stop when done
npm run dj:session stop
```

## License

This skill is part of your personal Claude Code configuration.

## Credits

Built using:
- [spotify-player](https://github.com/aome510/spotify-player) by aome510
- Node.js for CLI wrapper
- Spotify Web API via spotify-player

## Support

For issues:
1. Check troubleshooting section above
2. Verify spotify-player is working: `spotify-player --help`
3. Check context state: `node .claude/skills/dj/context-manager.mjs summary`
4. Review skill logs in Claude Code

For spotify-player specific issues, see: https://github.com/aome510/spotify-player
