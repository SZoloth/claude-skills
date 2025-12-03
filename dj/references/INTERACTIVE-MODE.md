# DJ Skill - Interactive Mode Reference

Interactive mode launches the full `spotify-player` CLI interface for extended DJ sessions with keyboard controls and visual feedback.

## Launching Interactive Mode

### Via npm script:
```bash
npm run dj interactive
```

### Via session manager (with tracking):
```bash
npm run dj:session start
```

## When to Use Interactive Mode

**Use interactive mode when:**
- You want visual feedback (progress bars, album art if supported)
- You're browsing through your library
- You want real-time keyboard control
- You're DJing or need quick access to many features
- You want to see the queue and lyrics
- You prefer a visual interface over CLI commands

**Use CLI commands when:**
- Quick single operations (play, pause, skip)
- Scripting or automation
- Integration with other tools
- Remote control from Claude
- You prefer minimal output

## Keyboard Shortcuts

### Playback Control
- `Space` - Play/pause toggle
- `n` - Next track
- `p` - Previous track
- `.` - Play random track from current context

### Volume & Seek
- `+` - Increase volume (5% by default)
- `-` - Decrease volume (5% by default)
- `_` (underscore) - Mute toggle
- `<` - Seek backward (5s by default)
- `>` - Seek forward (5s by default)

### Modes
- `C-r` (Ctrl+R) - Cycle repeat modes
- `M-r` (Alt+R) - Toggle fake track repeat
- `C-s` (Ctrl+S) - Toggle shuffle mode

### Navigation
- `j` or `Down` - Select next / scroll down
- `k` or `Up` - Select previous / scroll up
- `C-n` (Ctrl+N) - Next (vim-style)
- `C-p` (Ctrl+P) - Previous (vim-style)

**Vim-count support:**
- `5j` - Move down 5 items
- `10k` - Move up 10 items

### Device & View
- `d` - Switch devices
- `esc` - Close popups
- `?` - Show help
- `q` or `C-c` - Quit

### Mouse Support
- Click on progress bar to seek to position

## Visual Features

### Progress Bar
Shows playback position with seekable timeline.

### Album Art
Displayed if your terminal supports images (iTerm2, kitty, etc.).

### Current Track Info
- Track name
- Artist(s)
- Album
- Duration and current position
- Like status (if liked)

### Queue View
See upcoming tracks in the queue.

### Lyrics
View lyrics for current track (if available from Spotify).

### Device List
Visual list of available Spotify Connect devices with active indicator.

## Configuration

Interactive mode uses `spotify-player` configuration from:
```
~/.config/spotify-player/app.toml
```

You can customize:
- Theme colors
- Key bindings
- Progress bar format
- Lyrics display
- Mouse support
- And more...

See spotify-player documentation for full config options.

## Session Management

### Start with tracking:
```bash
npm run dj:session start
```

### Check session status:
```bash
npm run dj:session status
```

Output:
```
📊 Session Status

  Status: ✅ Running
  PID: 12345
  Started: 2025-01-27T10:30:00Z
  Duration: 15m 32s
```

### Stop session:
```bash
npm run dj:session stop
```

### Clean up stale session:
```bash
npm run dj:session cleanup
```

## Tips for Interactive Mode

### Quick Start
1. Launch: `npm run dj:session start`
2. Use `?` to see all shortcuts
3. Navigate with `j`/`k`
4. Play with `Space`
5. Quit with `q`

### Keyboard Flow
- `j`/`k` to browse tracks
- `Space` to play selected
- `+`/`-` for volume
- `.` for random shuffle
- `d` to switch devices

### Combining with CLI
You can use CLI commands while interactive mode is running in another terminal:

**Terminal 1:**
```bash
npm run dj:session start  # Interactive mode running
```

**Terminal 2:**
```bash
npm run dj volume +10     # Adjust volume via CLI
npm run dj like           # Like track via CLI
```

## Troubleshooting Interactive Mode

### Terminal rendering issues
Some terminals render better than others:
- **Best:** iTerm2, kitty, Alacritty
- **Good:** macOS Terminal, GNOME Terminal
- **Limited:** Basic shells without color support

### Mouse not working
Enable mouse support in spotify-player config:
```toml
[behavior]
mouse_support = true
```

### Album art not showing
Requires terminal with image protocol support:
- iTerm2 (macOS)
- kitty
- WezTerm

### Keyboard shortcuts conflict
Check if your terminal or shell is intercepting keys:
- Ctrl+S might trigger terminal flow control (disable with `stty -ixon`)
- Some keys might be bound by tmux/screen

### Session not stopping
```bash
# Check if running
npm run dj:session status

# Force cleanup
npm run dj:session cleanup

# Kill process manually
ps aux | grep spotify-player
kill <PID>
```

## Advanced Interactive Features

### Fuzzy Search
If `fzf` feature is enabled in spotify-player:
- Super fast fuzzy finding
- Type to filter
- Navigate with arrow keys

### Queue Management
- View queue
- Reorder tracks (if enabled)
- Clear queue

### Playlist Editing
- Browse playlists
- Add/remove tracks (if editing enabled)
- Create new playlists

### Context Switching
- Switch between:
  - Album view
  - Artist view
  - Playlist view
  - Search results

## Comparing Interactive vs CLI

| Feature | Interactive Mode | CLI Mode |
|---------|-----------------|----------|
| **Browsing** | ✅ Rich visual | ❌ Text-based |
| **Speed** | ⚡ Real-time keys | ⚡ Fast commands |
| **Scripting** | ❌ Manual control | ✅ Automatable |
| **Feedback** | ✅ Visual progress | 📝 Text output |
| **Multi-task** | ⚠️  Full screen | ✅ Background |
| **Context** | ✅ Built-in state | 📝 Manual tracking |
| **Queue** | ✅ Visual | ❌ Not visible |
| **Lyrics** | ✅ If available | ❌ Not shown |

## Best Practices

### When to Stay in Interactive
- Long listening sessions
- Exploring new music
- DJ-style control
- Want visual feedback

### When to Drop to CLI
- Quick operations while working
- Scripting/automation
- Integration with other tools
- Want minimal distraction

### Hybrid Workflow
1. Use CLI for quick controls during work
2. Drop to interactive when browsing/exploring
3. Return to CLI for focused tasks

## Resources

**spotify-player Documentation:**
- GitHub: https://github.com/aome510/spotify-player
- Key bindings: `spotify-player --help`
- Config reference: Check repo docs

**Configuration File:**
```
~/.config/spotify-player/app.toml
```

**Session Files:**
- Session tracking: `~/.config/spotify-player/claude-session.json`
- Context data: `~/.config/spotify-player/claude-context.json`

## Summary

Interactive mode provides:
✅ Real-time keyboard control
✅ Visual feedback (progress, art, lyrics)
✅ Queue management
✅ Browsing interface
✅ Session tracking
✅ Mouse support

For command-line control, see `COMMANDS.md`.
For natural language patterns, see `NATURAL-LANGUAGE.md`.
