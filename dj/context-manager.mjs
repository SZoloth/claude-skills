#!/usr/bin/env node

import { promises as fs } from 'fs';
import path from 'path';
import os from 'os';

const CONTEXT_FILE = path.join(os.homedir(), '.config', 'spotify-player', 'claude-context.json');

/**
 * ContextManager - Track conversation state for conversational DJ interactions
 *
 * Enables natural language patterns like:
 * - "play that again" (references currentTrack)
 * - "add this to my workout playlist" (references current track + playlist fuzzy match)
 * - "play #3" (references searchResults)
 */
export class ContextManager {
  constructor() {
    this.searchResults = [];      // Last search results
    this.currentTrack = null;      // Current playing track
    this.lastPlaylists = [];       // Recently viewed playlists
    this.deviceContext = null;     // Current device info
    this.conversationMode = false; // Multi-turn conversation flag
  }

  /**
   * Resolve references like "this", "that", "it", "current"
   * @param {string} phrase - User input phrase
   * @returns {object|null} - Resolved track or null
   */
  resolveReference(phrase) {
    const lowerPhrase = phrase.toLowerCase();

    // "this", "current", "this song/track"
    if (lowerPhrase.includes('this') || lowerPhrase.includes('current')) {
      return this.currentTrack;
    }

    // "that", "that song/track" - refers to last search result
    if (lowerPhrase.includes('that') && this.searchResults.length > 0) {
      return this.searchResults[0];
    }

    // "it" - context-dependent, default to current
    if (lowerPhrase.includes('it')) {
      return this.currentTrack || (this.searchResults.length > 0 ? this.searchResults[0] : null);
    }

    return null;
  }

  /**
   * Resolve numbered references like "#1", "#3", "number 2"
   * @param {string} phrase - User input phrase
   * @returns {object|null} - Resolved search result or null
   */
  resolveNumberedResult(phrase) {
    // Match patterns: "#1", "#3", "number 2", "result 5"
    const numberMatch = phrase.match(/#(\d+)|number (\d+)|result (\d+)/i);

    if (numberMatch) {
      const index = parseInt(numberMatch[1] || numberMatch[2] || numberMatch[3]) - 1;
      if (index >= 0 && index < this.searchResults.length) {
        return this.searchResults[index];
      }
    }

    return null;
  }

  /**
   * Resolve playlist names with fuzzy matching
   * @param {string} name - Playlist name or partial name
   * @returns {object|null} - Matched playlist or null
   */
  resolvePlaylist(name) {
    if (!name || this.lastPlaylists.length === 0) {
      return null;
    }

    const lowerName = name.toLowerCase();

    // Exact match first
    let match = this.lastPlaylists.find(pl =>
      pl.name.toLowerCase() === lowerName
    );

    // Fuzzy match if no exact match
    if (!match) {
      match = this.lastPlaylists.find(pl =>
        pl.name.toLowerCase().includes(lowerName) ||
        lowerName.includes(pl.name.toLowerCase())
      );
    }

    return match;
  }

  /**
   * Resolve device names with fuzzy matching
   * @param {string} name - Device name or partial name
   * @param {array} availableDevices - List of available devices
   * @returns {object|null} - Matched device or null
   */
  resolveDevice(name, availableDevices = []) {
    if (!name || availableDevices.length === 0) {
      return null;
    }

    const lowerName = name.toLowerCase();

    // Exact match first
    let match = availableDevices.find(d =>
      d.name.toLowerCase() === lowerName
    );

    // Fuzzy match if no exact match
    if (!match) {
      match = availableDevices.find(d =>
        d.name.toLowerCase().includes(lowerName) ||
        lowerName.includes(d.name.toLowerCase())
      );
    }

    return match;
  }

  /**
   * Update context after command execution
   * @param {string} commandType - Type of command executed
   * @param {any} data - Data returned from command
   */
  updateContext(commandType, data) {
    switch (commandType) {
      case 'search':
        if (Array.isArray(data) && data.length > 0) {
          this.searchResults = data;
          this.conversationMode = true; // Enable conversation mode after search
        }
        break;

      case 'current':
        if (data) {
          this.currentTrack = data;
        }
        break;

      case 'playlists':
        if (Array.isArray(data) && data.length > 0) {
          this.lastPlaylists = data;
        }
        break;

      case 'devices':
        if (Array.isArray(data) && data.length > 0) {
          this.deviceContext = data.find(d => d.is_active) || data[0];
        }
        break;

      case 'play':
      case 'next':
      case 'previous':
        // Track changed, should refresh currentTrack if needed
        // This could trigger an automatic `current` fetch
        break;
    }
  }

  /**
   * Clear search context (e.g., after playing a track)
   */
  clearSearchContext() {
    this.searchResults = [];
    this.conversationMode = false;
  }

  /**
   * Get conversation hints for the user
   * @returns {string} - Helpful hints based on context
   */
  getHints() {
    const hints = [];

    if (this.searchResults.length > 0) {
      hints.push(`💡 Say "play #N" to play a search result (1-${Math.min(5, this.searchResults.length)})`);
    }

    if (this.currentTrack) {
      hints.push('💡 Say "add this to my playlist" to save current track');
      hints.push('💡 Say "play that again" to replay');
    }

    if (this.lastPlaylists.length > 0) {
      hints.push('💡 Playlist names support fuzzy matching');
    }

    return hints.length > 0 ? '\n' + hints.join('\n') : '';
  }

  /**
   * Persist context to disk
   */
  async save() {
    try {
      // Ensure directory exists
      await fs.mkdir(path.dirname(CONTEXT_FILE), { recursive: true });

      const data = {
        searchResults: this.searchResults.slice(0, 10), // Keep last 10
        currentTrack: this.currentTrack,
        lastPlaylists: this.lastPlaylists.slice(0, 20), // Keep last 20
        deviceContext: this.deviceContext,
        conversationMode: this.conversationMode,
        timestamp: Date.now()
      };

      await fs.writeFile(CONTEXT_FILE, JSON.stringify(data, null, 2), 'utf8');
    } catch (error) {
      // Silent fail - context persistence is optional
      // console.error('Warning: Could not save context:', error.message);
    }
  }

  /**
   * Load context from disk
   */
  async load() {
    try {
      const data = await fs.readFile(CONTEXT_FILE, 'utf8');
      const parsed = JSON.parse(data);

      // Only load recent context (within last hour)
      const oneHourAgo = Date.now() - (60 * 60 * 1000);
      if (parsed.timestamp && parsed.timestamp > oneHourAgo) {
        this.searchResults = parsed.searchResults || [];
        this.currentTrack = parsed.currentTrack || null;
        this.lastPlaylists = parsed.lastPlaylists || [];
        this.deviceContext = parsed.deviceContext || null;
        this.conversationMode = parsed.conversationMode || false;
      }
    } catch (error) {
      // Silent fail - no context file is fine
      // Start fresh
    }
  }

  /**
   * Clear all context
   */
  async clear() {
    this.searchResults = [];
    this.currentTrack = null;
    this.lastPlaylists = [];
    this.deviceContext = null;
    this.conversationMode = false;

    try {
      await fs.unlink(CONTEXT_FILE);
    } catch {
      // File might not exist, that's fine
    }
  }

  /**
   * Get a summary of current context (for debugging)
   * @returns {string} - Context summary
   */
  getSummary() {
    let summary = '📊 Context Summary:\n';

    summary += `\nSearch Results: ${this.searchResults.length} items`;
    if (this.searchResults.length > 0) {
      summary += ` (most recent: ${this.searchResults[0].name || 'unknown'})`;
    }

    summary += `\nCurrent Track: ${this.currentTrack ? this.currentTrack.name : 'none'}`;

    summary += `\nPlaylists Cached: ${this.lastPlaylists.length} items`;

    summary += `\nDevice Context: ${this.deviceContext ? this.deviceContext.name : 'none'}`;

    summary += `\nConversation Mode: ${this.conversationMode ? 'ON' : 'OFF'}`;

    return summary;
  }
}

// Export singleton instance for use in spotify.mjs
export const context = new ContextManager();

// CLI interface for debugging
if (import.meta.url === `file://${process.argv[1]}`) {
  const action = process.argv[2];

  switch (action) {
    case 'summary':
      await context.load();
      console.log(context.getSummary());
      break;

    case 'clear':
      await context.clear();
      console.log('✅ Context cleared');
      break;

    case 'load':
      await context.load();
      console.log('✅ Context loaded');
      console.log(context.getSummary());
      break;

    default:
      console.log('Usage: node context-manager.mjs <summary|clear|load>');
      console.log('\nCommands:');
      console.log('  summary  Show current context state');
      console.log('  clear    Clear all context');
      console.log('  load     Load context from disk');
  }
}
