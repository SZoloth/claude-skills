#!/usr/bin/env tsx

/**
 * Journal Analyzer Agent
 *
 * Analyzes journal entries to identify emotional patterns, track themes over time,
 * and generate personalized edge questions for RO-DBT practice.
 *
 * Hybrid access:
 * - Can auto-read from Obsidian vault: /Users/samuelz/Documents/LLM CONTEXT/
 * - OR accept pasted journal entries as input
 *
 * Usage:
 *   tsx agent.ts --vault recent           # Analyze recent vault entries
 *   tsx agent.ts --vault "2025-11-01:2025-11-30"  # Analyze date range
 *   tsx agent.ts --text "Journal entry text..."   # Analyze pasted text
 */

import Anthropic from '@anthropic-ai/sdk';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const MODEL = 'claude-sonnet-4-5-20250929';
const MAX_TOKENS = 4096;
const VAULT_PATH = '/Users/samuelz/Documents/LLM CONTEXT';

interface JournalAnalysis {
  timestamp: string;
  source: 'vault' | 'pasted';
  entry_count: number;
  patterns: {
    emotional_themes: string[];
    overcontrol_manifestations: string[];
    relationship_patterns: string[];
    progress_indicators: string[];
  };
  emotional_arc: string;
  edge_questions: string[];
  recommended_focus: string;
}

class JournalAnalyzerAgent {
  private client: Anthropic;
  private entries: string[];

  constructor(entries: string[]) {
    this.client = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY
    });
    this.entries = entries;
  }

  async analyze(): Promise<JournalAnalysis> {
    console.log(`\n📖 Analyzing ${this.entries.length} journal entries...\n`);

    const combined = this.entries.join('\n\n---ENTRY BREAK---\n\n');

    const prompt = `Analyze these journal entries from an RO-DBT (Radically Open Dialectical Behavior Therapy) perspective.

JOURNAL ENTRIES:
${combined}

Provide comprehensive analysis:

1. **Emotional Themes**
   - What emotions recur across entries?
   - What triggers emotional responses?
   - Are emotions named and processed, or suppressed?

2. **Overcontrol Manifestations**
   - Evidence of emotional inhibition
   - Low self-disclosure patterns
   - Rigid thinking or perfectionism
   - Detail-focused processing
   - Withdrawal when hurt
   - Strategic avoidance

3. **Relationship Patterns**
   - Patterns with Carter (if mentioned)
   - Work relationship dynamics
   - Social connection or isolation
   - Vulnerability vs curated self-presentation

4. **Progress Indicators**
   - Evidence of increased openness
   - Moments of authentic expression
   - Practicing vulnerability
   - Flexibility in thinking

5. **Emotional Arc**
   - How do emotions evolve across entries?
   - Patterns of escalation or regulation?
   - Cycles of withdrawal and re-engagement?

6. **Edge Questions**
   - Generate 3-5 personalized edge questions based on identified patterns
   - Questions should push against overcontrol
   - Should feel slightly uncomfortable but achievable

7. **Recommended Therapeutic Focus**
   - What patterns need most attention?
   - Which RO-DBT skills would be most beneficial?
   - What experiments to try?

Format response as JSON with this structure:
{
  "emotional_themes": ["theme 1", "theme 2", ...],
  "overcontrol_manifestations": ["pattern 1", "pattern 2", ...],
  "relationship_patterns": ["pattern 1", "pattern 2", ...],
  "progress_indicators": ["indicator 1", "indicator 2", ...],
  "emotional_arc": "narrative description of emotional journey",
  "edge_questions": ["question 1", "question 2", ...],
  "recommended_focus": "therapeutic recommendations"
}`;

    const response = await this.client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{
        role: 'user',
        content: prompt
      }]
    });

    const content = this.extractTextContent(response);

    // Parse JSON response
    const jsonMatch = content.match(/\{[\s\S]*\}/);
    if (!jsonMatch) {
      throw new Error('Failed to extract JSON from response');
    }

    const analysis = JSON.parse(jsonMatch[0]);

    return {
      timestamp: new Date().toISOString(),
      source: 'vault',
      entry_count: this.entries.length,
      patterns: {
        emotional_themes: analysis.emotional_themes || [],
        overcontrol_manifestations: analysis.overcontrol_manifestations || [],
        relationship_patterns: analysis.relationship_patterns || [],
        progress_indicators: analysis.progress_indicators || []
      },
      emotional_arc: analysis.emotional_arc || '',
      edge_questions: analysis.edge_questions || [],
      recommended_focus: analysis.recommended_focus || ''
    };
  }

  private extractTextContent(response: Anthropic.Message): string {
    const textBlocks = response.content.filter(
      block => block.type === 'text'
    ) as Anthropic.TextBlock[];
    return textBlocks.map(block => block.text).join('\n\n');
  }

  async saveAnalysis(analysis: JournalAnalysis): Promise<string> {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const filename = `journal-analysis_${timestamp}.md`;
    const filepath = path.join(__dirname, filename);

    const markdown = this.formatAnalysisAsMarkdown(analysis);
    fs.writeFileSync(filepath, markdown, 'utf-8');

    console.log(`\n✅ Analysis saved to: ${filename}\n`);
    return filepath;
  }

  private formatAnalysisAsMarkdown(analysis: JournalAnalysis): string {
    return `# Journal Analysis - RO-DBT Perspective

**Generated:** ${new Date(analysis.timestamp).toLocaleString()}
**Entries analyzed:** ${analysis.entry_count}
**Source:** ${analysis.source}

---

## Emotional Themes

${analysis.patterns.emotional_themes.map(theme => `- ${theme}`).join('\n')}

---

## Overcontrol Manifestations

${analysis.patterns.overcontrol_manifestations.map(pattern => `- ${pattern}`).join('\n')}

---

## Relationship Patterns

${analysis.patterns.relationship_patterns.map(pattern => `- ${pattern}`).join('\n')}

---

## Progress Indicators

${analysis.patterns.progress_indicators.length > 0 
  ? analysis.patterns.progress_indicators.map(indicator => `- ${indicator}`).join('\n')
  : '*No specific progress indicators identified in this set of entries*'}

---

## Emotional Arc

${analysis.emotional_arc}

---

## Edge Questions for Practice

${analysis.edge_questions.map((q, i) => `${i + 1}. ${q}`).join('\n')}

**How to use edge questions:**
- Choose one to explore this week
- Notice the discomfort (it's information, not danger)
- Experiment with small brave steps
- Observe outcomes without judgment

---

## Recommended Therapeutic Focus

${analysis.recommended_focus}

---

*Generated by journal-analyzer agent*
*Next steps: Practice one edge question, log insights to rodbt-progress.json*
`;
  }
}

async function readVaultEntries(dateRange: string): Promise<string[]> {
  // For now, return instructions to paste entries
  // In future, could read actual Obsidian vault files
  console.log('\n⚠️  Vault auto-read not yet implemented.');
  console.log('Please use --text mode and paste journal entries.\n');
  return [];
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Usage:');
    console.log('  tsx agent.ts --vault recent');
    console.log('  tsx agent.ts --vault "2025-11-01:2025-11-30"');
    console.log('  tsx agent.ts --text "Journal entry text..."');
    process.exit(1);
  }

  let entries: string[] = [];

  if (args[0] === '--vault') {
    const dateRange = args[1] || 'recent';
    entries = await readVaultEntries(dateRange);
    if (entries.length === 0) {
      console.error('No entries found. Use --text mode instead.');
      process.exit(1);
    }
  } else if (args[0] === '--text') {
    const text = args.slice(1).join(' ');
    if (!text) {
      console.error('Please provide journal entry text after --text');
      process.exit(1);
    }
    entries = [text];
  } else {
    console.error('Unknown option. Use --vault or --text');
    process.exit(1);
  }

  try {
    const agent = new JournalAnalyzerAgent(entries);
    const analysis = await agent.analyze();
    await agent.saveAnalysis(analysis);

    console.log('=' + '='.repeat(60));
    console.log('ANALYSIS COMPLETE');
    console.log('=' + '='.repeat(60));
    console.log(`\nEmotional themes: ${analysis.patterns.emotional_themes.length}`);
    console.log(`Overcontrol patterns: ${analysis.patterns.overcontrol_manifestations.length}`);
    console.log(`Edge questions: ${analysis.edge_questions.length}`);
    console.log('\nUse this analysis to:');
    console.log('- Recognize recurring patterns');
    console.log('- Practice edge questions');
    console.log('- Track therapeutic progress');
    console.log('- Focus RO-DBT work\n');

  } catch (error) {
    console.error('\n❌ Error during analysis:', error);
    process.exit(1);
  }
}

main();
