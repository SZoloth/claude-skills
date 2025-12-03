#!/usr/bin/env node

import { spawn } from 'child_process';
import { promises as fs } from 'fs';
import path from 'path';
import os from 'os';

const SESSION_FILE = path.join(os.homedir(), '.config', 'spotify-player', 'claude-session.json');

/**
 * SessionManager - Manage long-running interactive spotify-player sessions
 *
 * Tracks PID, status, and lifecycle of interactive DJ mode
 */
class SessionManager {
  /**
   * Start a new interactive spotify-player session
   */
  async start() {
    // Check if session already running
    const running = await this.isRunning();
    if (running) {
      console.log('⚠️  Interactive session already running');
      console.log('Use "npm run dj:session status" to check status');
      console.log('Use "npm run dj:session stop" to stop current session');
      return;
    }

    console.log('🎧 Launching interactive DJ mode...');
    console.log('');
    console.log('Keyboard Shortcuts:');
    console.log('  Space    Play/Pause');
    console.log('  n        Next track');
    console.log('  p        Previous track');
    console.log('  +/-      Volume up/down');
    console.log('  ?        Show help');
    console.log('  q        Quit');
    console.log('');

    // Launch spotify-player in interactive mode
    const proc = spawn('spotify-player', [], {
      stdio: 'inherit'
    });

    // Save session info
    await this.saveSession(proc.pid);

    proc.on('close', async (code) => {
      await this.cleanup();
      console.log('\n👋 Exited interactive mode');
    });

    proc.on('error', async (error) => {
      console.error('❌ Error launching interactive mode:', error.message);
      await this.cleanup();
      process.exit(1);
    });
  }

  /**
   * Save session metadata to disk
   * @param {number} pid - Process ID
   */
  async saveSession(pid) {
    try {
      await fs.mkdir(path.dirname(SESSION_FILE), { recursive: true });

      const data = {
        pid,
        started: Date.now(),
        startedAt: new Date().toISOString()
      };

      await fs.writeFile(SESSION_FILE, JSON.stringify(data, null, 2), 'utf8');
    } catch (error) {
      console.error('Warning: Could not save session info:', error.message);
    }
  }

  /**
   * Get session metadata from disk
   * @returns {object|null} - Session data or null
   */
  async getSession() {
    try {
      const data = await fs.readFile(SESSION_FILE, 'utf8');
      return JSON.parse(data);
    } catch {
      return null;
    }
  }

  /**
   * Check if session is currently running
   * @returns {boolean} - True if running, false otherwise
   */
  async isRunning() {
    const session = await this.getSession();
    if (!session || !session.pid) {
      return false;
    }

    try {
      // Check if process exists (signal 0 doesn't kill, just checks)
      process.kill(session.pid, 0);
      return true;
    } catch {
      // Process doesn't exist, clean up stale session file
      await this.cleanup();
      return false;
    }
  }

  /**
   * Stop the running session
   */
  async stop() {
    const session = await this.getSession();
    if (!session || !session.pid) {
      console.log('No active session to stop');
      return;
    }

    try {
      process.kill(session.pid, 'SIGTERM');
      await this.cleanup();
      console.log('✅ Session stopped');
    } catch (error) {
      if (error.code === 'ESRCH') {
        // Process doesn't exist
        await this.cleanup();
        console.log('✅ Cleaned up stale session');
      } else {
        console.error('❌ Error stopping session:', error.message);
      }
    }
  }

  /**
   * Show session status
   */
  async status() {
    const session = await this.getSession();
    if (!session) {
      console.log('📊 Session Status: No active session');
      return;
    }

    const running = await this.isRunning();

    console.log('📊 Session Status');
    console.log('');
    console.log(`  Status: ${running ? '✅ Running' : '❌ Not running'}`);
    console.log(`  PID: ${session.pid}`);
    console.log(`  Started: ${session.startedAt || 'Unknown'}`);

    if (session.started) {
      const duration = Date.now() - session.started;
      const minutes = Math.floor(duration / 60000);
      const seconds = Math.floor((duration % 60000) / 1000);
      console.log(`  Duration: ${minutes}m ${seconds}s`);
    }

    if (!running) {
      console.log('');
      console.log('💡 Use "npm run dj:session cleanup" to remove stale session data');
    }
  }

  /**
   * Clean up session file
   */
  async cleanup() {
    try {
      await fs.unlink(SESSION_FILE);
    } catch {
      // File might not exist, that's fine
    }
  }
}

// CLI interface
const manager = new SessionManager();
const command = process.argv[2] || 'help';

switch (command) {
  case 'start':
    await manager.start();
    break;

  case 'stop':
    await manager.stop();
    break;

  case 'status':
    await manager.status();
    break;

  case 'cleanup':
    await manager.cleanup();
    console.log('✅ Session cleaned up');
    break;

  case 'help':
  default:
    console.log('🎵 Session Manager - Manage interactive DJ sessions');
    console.log('');
    console.log('Commands:');
    console.log('  start    Launch interactive DJ mode');
    console.log('  stop     Stop running session');
    console.log('  status   Show session status');
    console.log('  cleanup  Remove session data');
    console.log('  help     Show this help');
    console.log('');
    console.log('Examples:');
    console.log('  npm run dj:session start');
    console.log('  npm run dj:session status');
    console.log('  npm run dj:session stop');
}
