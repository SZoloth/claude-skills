#!/usr/bin/env tsx

/**
 * Company Research Agent
 *
 * Autonomous agent for deep company research in job search context.
 * Performs multi-step research workflow:
 * 1. Company background (funding, size, products, market)
 * 2. Role analysis (requirements, responsibilities)
 * 3. Culture assessment (reviews, blogs, social)
 * 4. Competitive landscape
 * 5. Generate comprehensive research report
 *
 * Usage:
 *   tsx agent.ts "Stripe" "Senior Product Manager"
 *   tsx agent.ts "Figma" "Director of Product"
 */

import Anthropic from '@anthropic-ai/sdk';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const MODEL = 'claude-sonnet-4-5-20250929';
const MAX_TOKENS = 4096;

interface ResearchReport {
  company: string;
  role: string;
  timestamp: string;
  sections: {
    background: string;
    role_analysis: string;
    culture_assessment: string;
    competitive_landscape: string;
    talking_points: string[];
    interview_prep_foundation: string;
  };
}

class CompanyResearchAgent {
  private client: Anthropic;
  private company: string;
  private role: string;

  constructor(company: string, role: string) {
    this.client = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY
    });
    this.company = company;
    this.role = role;
  }

  async research(): Promise<ResearchReport> {
    console.log(`\n🔍 Researching ${this.company} for ${this.role} role...\n`);

    // Step 1: Company Background
    console.log('Step 1/5: Company background research...');
    const background = await this.researchBackground();

    // Step 2: Role Analysis
    console.log('Step 2/5: Role requirements analysis...');
    const roleAnalysis = await this.analyzeRole();

    // Step 3: Culture Assessment
    console.log('Step 3/5: Culture and values assessment...');
    const cultureAssessment = await this.assessCulture();

    // Step 4: Competitive Landscape
    console.log('Step 4/5: Competitive positioning...');
    const competitiveLandscape = await this.researchCompetitors();

    // Step 5: Synthesize Report
    console.log('Step 5/5: Generating comprehensive report...');
    const { talkingPoints, interviewFoundation } = await this.synthesizeReport(
      background,
      roleAnalysis,
      cultureAssessment,
      competitiveLandscape
    );

    return {
      company: this.company,
      role: this.role,
      timestamp: new Date().toISOString(),
      sections: {
        background,
        role_analysis: roleAnalysis,
        culture_assessment: cultureAssessment,
        competitive_landscape: competitiveLandscape,
        talking_points: talkingPoints,
        interview_prep_foundation: interviewFoundation
      }
    };
  }

  private async researchBackground(): Promise<string> {
    const prompt = `Research ${this.company} company background. Provide:

1. Company Overview
   - Founding year, founders, headquarters
   - Company size (employees, if available)
   - Products/services and primary business model

2. Funding & Financial Health
   - Funding rounds, total raised, latest valuation (if available)
   - Revenue/profitability status (if public information)
   - Recent financial news or developments

3. Market Position
   - Industry/sector
   - Target customers and market segments
   - Market share or competitive standing

4. Recent News & Developments
   - Product launches, expansions, partnerships
   - Leadership changes
   - Any significant announcements (last 6 months)

Be concise but comprehensive. Focus on information relevant to a job seeker evaluating this opportunity.`;

    const response = await this.client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{
        role: 'user',
        content: prompt
      }]
    });

    return this.extractTextContent(response);
  }

  private async analyzeRole(): Promise<string> {
    const prompt = `Analyze the typical requirements and responsibilities for a ${this.role} role at ${this.company}.

Based on ${this.company}'s business model, products, and stage, what would a ${this.role} likely be responsible for?

Provide:

1. Typical Responsibilities
   - Strategic vs tactical balance
   - Key focus areas (e.g., growth, platform, core product)
   - Cross-functional partnerships expected

2. Required Skills & Experience
   - Years of experience typically required
   - Technical skills (if applicable)
   - Domain expertise
   - Leadership expectations

3. Success Metrics
   - How would success likely be measured in this role?
   - Key performance indicators

4. Challenges & Opportunities
   - What makes this role challenging?
   - What makes it compelling?

If you can find actual job postings for this role at ${this.company}, incorporate that information. Otherwise, infer based on company context and industry standards for this role.`;

    const response = await this.client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{
        role: 'user',
        content: prompt
      }]
    });

    return this.extractTextContent(response);
  }

  private async assessCulture(): Promise<string> {
    const prompt = `Assess ${this.company}'s culture and values based on available information:

1. Stated Values & Culture
   - Company values (from website, blog, public statements)
   - Work culture (remote/hybrid/office, collaboration style)
   - Mission and purpose

2. Employee Perspectives
   - Common themes from Glassdoor, Blind, LinkedIn reviews
   - Pros and cons frequently mentioned
   - Interview experience feedback

3. Leadership Style
   - CEO/founder background and philosophy
   - Management approach (data-driven, creative, customer-focused, etc.)
   - Decision-making culture

4. Work-Life Balance
   - Expected hours and intensity
   - Flexibility and benefits
   - Burnout concerns or sustainable pace

Provide an honest assessment - include both positive aspects and potential red flags. Focus on information a ${this.role} candidate should know.`;

    const response = await this.client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{
        role: 'user',
        content: prompt
      }]
    });

    return this.extractTextContent(response);
  }

  private async researchCompetitors(): Promise<string> {
    const prompt = `Analyze ${this.company}'s competitive landscape:

1. Direct Competitors
   - Who are ${this.company}'s main competitors?
   - How does ${this.company} differentiate from them?

2. Competitive Positioning
   - What is ${this.company}'s unique value proposition?
   - Market position (leader, challenger, niche player)?
   - Strengths vs competitors
   - Weaknesses or vulnerabilities

3. Industry Trends
   - Key trends affecting this market
   - How is ${this.company} positioned for future growth?
   - Potential threats or opportunities

This helps understand ${this.company}'s strategic context and challenges a ${this.role} would face.`;

    const response = await this.client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{
        role: 'user',
        content: prompt
      }]
    });

    return this.extractTextContent(response);
  }

  private async synthesizeReport(
    background: string,
    roleAnalysis: string,
    culture: string,
    competitive: string
  ): Promise<{ talkingPoints: string[]; interviewFoundation: string }> {
    const prompt = `Based on this comprehensive research about ${this.company}, synthesize:

RESEARCH CONTEXT:
${background}

${roleAnalysis}

${culture}

${competitive}

Now provide:

1. **Top 10 Talking Points** (for interview conversations)
   - Key facts about the company
   - Strategic insights to demonstrate research
   - Thoughtful observations about their business
   - Questions that show understanding

2. **Interview Prep Foundation**
   - 3-5 "Why ${this.company}?" narrative angles
   - Potential concerns to address proactively
   - How to position your background for this opportunity
   - Cultural fit signals to emphasize

Format:
TALKING POINTS:
1. [point]
2. [point]
...

INTERVIEW FOUNDATION:
[2-3 paragraphs with strategic interview guidance]`;

    const response = await this.client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      messages: [{
        role: 'user',
        content: prompt
      }]
    });

    const content = this.extractTextContent(response);

    // Parse talking points and interview foundation
    const sections = content.split('INTERVIEW FOUNDATION:');
    const talkingPointsSection = sections[0].replace('TALKING POINTS:', '').trim();
    const interviewFoundation = sections[1]?.trim() || '';

    // Extract talking points (lines starting with numbers)
    const talkingPoints = talkingPointsSection
      .split('\n')
      .filter(line => /^\d+\./.test(line.trim()))
      .map(line => line.replace(/^\d+\.\s*/, '').trim());

    return { talkingPoints, interviewFoundation };
  }

  private extractTextContent(response: Anthropic.Message): string {
    const textBlocks = response.content.filter(
      block => block.type === 'text'
    ) as Anthropic.TextBlock[];

    return textBlocks.map(block => block.text).join('\n\n');
  }

  async saveReport(report: ResearchReport): Promise<string> {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const filename = `${this.company.toLowerCase().replace(/\s+/g, '-')}_${timestamp}.md`;
    const filepath = path.join(__dirname, filename);

    const markdown = this.formatReportAsMarkdown(report);

    fs.writeFileSync(filepath, markdown, 'utf-8');
    console.log(`\n✅ Research report saved to: ${filename}\n`);

    return filepath;
  }

  private formatReportAsMarkdown(report: ResearchReport): string {
    return `# ${report.company} - Company Research Report
## ${report.role}

**Generated:** ${new Date(report.timestamp).toLocaleString()}

---

## Company Background

${report.sections.background}

---

## Role Analysis: ${report.role}

${report.sections.role_analysis}

---

## Culture & Values Assessment

${report.sections.culture_assessment}

---

## Competitive Landscape

${report.sections.competitive_landscape}

---

## Talking Points for Interviews

${report.sections.talking_points.map((point, i) => `${i + 1}. ${point}`).join('\n')}

---

## Interview Prep Foundation

${report.sections.interview_prep_foundation}

---

*Generated by Company Research Agent*
`;
  }
}

// Main execution
async function main() {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.error('Usage: tsx agent.ts "Company Name" "Role Title"');
    console.error('Example: tsx agent.ts "Stripe" "Senior Product Manager"');
    process.exit(1);
  }

  const [company, role] = args;

  try {
    const agent = new CompanyResearchAgent(company, role);
    const report = await agent.research();
    await agent.saveReport(report);

    console.log('\n' + '='.repeat(60));
    console.log('RESEARCH COMPLETE');
    console.log('='.repeat(60));
    console.log(`\nCompany: ${report.company}`);
    console.log(`Role: ${report.role}`);
    console.log(`\nTalking Points: ${report.sections.talking_points.length}`);
    console.log('\nUse this research to:');
    console.log('- Prepare for interviews');
    console.log('- Tailor your application materials');
    console.log('- Craft thoughtful questions');
    console.log('- Assess strategic fit\n');

  } catch (error) {
    console.error('\n❌ Error during research:', error);
    process.exit(1);
  }
}

main();
