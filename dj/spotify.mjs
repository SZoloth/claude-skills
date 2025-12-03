#!/usr/bin/env node

import { spawn, execSync } from 'child_process';
import { promises as fs } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Check if spotify-player is installed
function checkInstalled() {
  try {
    execSync('which spotify-player', { stdio: 'pipe' });
    return true;
  } catch {
    console.error('❌ Error: spotify-player not installed');
    console.error('');
    console.error('Install with: cargo install spotify_player');
    console.error('Then authenticate: spotify-player authenticate');
    process.exit(1);
  }
}

// Execute spotify-player CLI command
async function runCommand(args, options = {}) {
  return new Promise((resolve, reject) => {
    const proc = spawn('spotify-player', args, {
      stdio: ['inherit', 'pipe', 'pipe'],
      ...options
    });

    let stdout = '';
    let stderr = '';

    proc.stdout.on('data', (data) => stdout += data);
    proc.stderr.on('data', (data) => stderr += data);

    proc.on('close', (code) => {
      if (code === 0) {
        resolve(stdout.trim());
      } else {
        reject(new Error(stderr || `Exit code: ${code}`));
      }
    });
  });
}

// Helper: Format duration from milliseconds to mm:ss
function formatDuration(ms) {
  const mins = Math.floor(ms / 60000);
  const secs = Math.floor((ms % 60000) / 1000);
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}

// Helper: Format search result based on type
function formatSearchResult(item, type) {
  switch (type) {
    case 'track':
      return `${item.name} - ${item.artists?.join(', ') || item.artist || 'Unknown'}`;
    case 'album':
      return `${item.name} by ${item.artists?.join(', ') || item.artist || 'Unknown'}`;
    case 'artist':
      return item.name;
    case 'playlist':
      return `${item.name} (${item.tracks?.total || item.track_count || 0} tracks)`;
    default:
      return item.name || JSON.stringify(item);
  }
}

// Helper: Format track info with contextual detail level
function formatTrackInfo(track, detailed = false) {
  const basic = `🎵 ${track.name || 'Unknown'} - ${track.artists?.join(', ') || track.artist || 'Unknown'}`;

  if (!detailed) {
    return basic;
  }

  let output = `🎵 Now Playing:\n`;
  output += `   ${track.name || 'Unknown'} - ${track.artists?.join(', ') || track.artist || 'Unknown'}\n`;
  if (track.album) {
    output += `   Album: ${track.album}\n`;
  }
  if (track.duration_ms) {
    output += `   Duration: ${formatDuration(track.duration_ms)}\n`;
  }
  return output;
}

// Command registry
const commands = {
  // ========== Playback Control ==========

  async play(args) {
    try {
      await runCommand(['playback', 'play']);
      console.log('▶️  Resumed playback');
    } catch (error) {
      console.error('❌ Error:', error.message);
      if (error.message.includes('No active device')) {
        console.error('\n⚠️  No active playback device found');
        console.error('Try: npm run dj devices');
      }
      process.exit(1);
    }
  },

  async pause(args) {
    try {
      await runCommand(['playback', 'pause']);
      console.log('⏸  Paused');
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async next(args) {
    try {
      await runCommand(['playback', 'next']);
      console.log('⏭  Skipped');
      // Optionally show new track
      // await commands.current([]);
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async previous(args) {
    try {
      await runCommand(['playback', 'previous']);
      console.log('⏮  Previous track');
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async volume(args) {
    const level = args[0];
    if (!level) {
      console.error('Usage: volume <0-100|+N|-N>');
      console.error('Examples:');
      console.error('  npm run dj volume 50      # Set to 50%');
      console.error('  npm run dj volume +10     # Increase by 10%');
      console.error('  npm run dj volume -5      # Decrease by 5%');
      process.exit(1);
    }

    try {
      await runCommand(['playback', 'volume', level]);
      const display = level.startsWith('+') || level.startsWith('-') ? level : `${level}%`;
      console.log(`🔊 Volume: ${display}`);
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async shuffle(args) {
    const state = args[0] === 'off' ? 'false' : 'true';
    try {
      await runCommand(['playback', 'shuffle', state]);
      console.log(`🔀 Shuffle: ${state === 'true' ? 'ON' : 'OFF'}`);
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async repeat(args) {
    const mode = args[0] || 'cycle'; // track, context, off, cycle
    try {
      await runCommand(['playback', 'repeat', mode]);
      console.log(`🔁 Repeat: ${mode.toUpperCase()}`);
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  // ========== Discovery ==========

  async current(args) {
    try {
      const result = await runCommand(['get', 'item', '--format', 'json']);
      const track = JSON.parse(result);
      console.log(formatTrackInfo(track, true));
      return track;
    } catch (error) {
      console.error('❌ Error getting current track:', error.message);
      process.exit(1);
    }
  },

  async search(args) {
    const [type, ...query] = args;
    const searchQuery = query.join(' ');

    if (!type || !searchQuery) {
      console.error('Usage: search <track|album|artist|playlist> <query>');
      console.error('Examples:');
      console.error('  npm run dj search track "miles davis"');
      console.error('  npm run dj search album "kind of blue"');
      process.exit(1);
    }

    try {
      const result = await runCommand(['search', type, searchQuery, '--format', 'json', '--limit', '10']);

      // Parse JSON output
      let results;
      try {
        results = JSON.parse(result);
      } catch (parseError) {
        console.error('❌ Error parsing search results');
        console.error(result);
        process.exit(1);
      }

      console.log(`🔍 Search results for "${searchQuery}" (${type}):\n`);

      if (results.length === 0) {
        console.log('No results found');
        console.log('\nSuggestions:');
        console.log('- Check spelling');
        console.log('- Try broader search terms');
        console.log('- Search by artist name instead');
        return [];
      }

      results.slice(0, 5).forEach((item, i) => {
        console.log(`${i + 1}. ${formatSearchResult(item, type)}`);
      });

      console.log(`\n💡 Tip: Use "npm run dj search-play ${type} ${searchQuery}" to play top result`);

      return results;
    } catch (error) {
      console.error('❌ Error searching:', error.message);
      process.exit(1);
    }
  },

  async 'search-play'(args) {
    const results = await commands.search(args);

    if (results.length > 0) {
      const topResult = results[0];
      try {
        await runCommand(['playback', 'play-uri', topResult.uri]);
        console.log(`\n▶️  Playing: ${formatSearchResult(topResult, args[0])}`);
      } catch (error) {
        console.error('❌ Error playing track:', error.message);
        process.exit(1);
      }
    }
  },

  // ========== Library Management ==========

  async like(args) {
    try {
      await runCommand(['like']);
      console.log('❤️  Liked current track');
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async unlike(args) {
    try {
      await runCommand(['like', '--unlike']);
      console.log('💔 Unliked current track');
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  },

  async playlists(args) {
    try {
      const result = await runCommand(['get', 'playlists', '--format', 'json']);
      const playlists = JSON.parse(result);

      console.log('📚 Your playlists:\n');
      playlists.forEach((pl, i) => {
        const trackCount = pl.tracks?.total || pl.track_count || 0;
        console.log(`${i + 1}. ${pl.name} (${trackCount} tracks)`);
      });

      return playlists;
    } catch (error) {
      console.error('❌ Error fetching playlists:', error.message);
      process.exit(1);
    }
  },

  async 'create-playlist'(args) {
    const name = args.join(' ');
    if (!name) {
      console.error('Usage: create-playlist <name>');
      console.error('Example: npm run dj create-playlist "Workout Mix"');
      process.exit(1);
    }

    try {
      await runCommand(['playlist', 'create', name]);
      console.log(`✅ Created playlist: ${name}`);
    } catch (error) {
      console.error('❌ Error creating playlist:', error.message);
      process.exit(1);
    }
  },

  // ========== Device Management ==========

  async devices(args) {
    try {
      const result = await runCommand(['connect', '--list', '--format', 'json']);
      const devices = JSON.parse(result);

      console.log('🔌 Available devices:\n');
      devices.forEach((device, i) => {
        const active = device.is_active ? '▶️ ' : '   ';
        console.log(`${active}${i + 1}. ${device.name} (${device.type})`);
      });

      return devices;
    } catch (error) {
      console.error('❌ Error fetching devices:', error.message);
      process.exit(1);
    }
  },

  async connect(args) {
    const deviceName = args.join(' ');

    if (!deviceName) {
      // Just list devices if no name provided
      return commands.devices([]);
    }

    try {
      // Get devices for fuzzy matching
      const result = await runCommand(['connect', '--list', '--format', 'json']);
      const devices = JSON.parse(result);

      // Fuzzy match device name
      const match = devices.find(d =>
        d.name.toLowerCase().includes(deviceName.toLowerCase())
      );

      if (match) {
        await runCommand(['connect', '--device-id', match.id]);
        console.log(`✅ Connected to: ${match.name}`);
      } else {
        console.error(`❌ Device "${deviceName}" not found`);
        console.error('\nAvailable devices:');
        devices.forEach((d, i) => {
          console.error(`  ${i + 1}. ${d.name}`);
        });
        process.exit(1);
      }
    } catch (error) {
      console.error('❌ Error switching device:', error.message);
      process.exit(1);
    }
  },

  // ========== Interactive Mode ==========

  async interactive(args) {
    console.log('🎧 Launching interactive DJ mode...');
    console.log('Press ? for help, q to quit\n');

    const proc = spawn('spotify-player', [], {
      stdio: 'inherit'
    });

    proc.on('close', (code) => {
      console.log('\n👋 Exited interactive mode');
    });
  },

  // ========== Utility ==========

  async help(args) {
    console.log('🎵 Spotify DJ - Control Spotify via CLI\n');
    console.log('Playback:');
    console.log('  play                    Resume playback');
    console.log('  pause                   Pause playback');
    console.log('  next                    Next track');
    console.log('  previous                Previous track');
    console.log('  current                 Show current track');
    console.log('  volume <0-100|+N|-N>    Set or adjust volume');
    console.log('  shuffle [on|off]        Toggle shuffle');
    console.log('  repeat [track|context|off|cycle]  Set repeat mode\n');
    console.log('Search & Discovery:');
    console.log('  search <type> <query>   Search (type: track, album, artist, playlist)');
    console.log('  search-play <type> <q>  Search and play top result\n');
    console.log('Library:');
    console.log('  like                    Like current track');
    console.log('  unlike                  Unlike current track');
    console.log('  playlists               List your playlists');
    console.log('  create-playlist <name>  Create new playlist\n');
    console.log('Devices:');
    console.log('  devices                 List available devices');
    console.log('  connect <device-name>   Switch playback device\n');
    console.log('Interactive:');
    console.log('  interactive             Launch full interactive mode');
    console.log('  help                    Show this help\n');
    console.log('Examples:');
    console.log('  npm run dj play');
    console.log('  npm run dj search track "miles davis"');
    console.log('  npm run dj volume +10');
    console.log('  npm run dj connect speaker');
  }
};

// Main execution
checkInstalled();

const command = process.argv[2] || 'help';
const args = process.argv.slice(3);

if (!commands[command]) {
  console.error(`❌ Unknown command: ${command}`);
  console.error('Run "npm run dj help" for available commands');
  process.exit(1);
}

try {
  await commands[command](args);
} catch (error) {
  console.error('❌ Unexpected error:', error.message);
  process.exit(1);
}
