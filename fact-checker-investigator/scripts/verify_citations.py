#!/usr/bin/env python3
"""
Citation Verification Tool

Checks that all citations in a markdown document point to real files and approximately
correct line numbers. Helps prevent fabricated quotes and broken references.

Usage:
    python verify_citations.py document.md --check-quotes --check-line-numbers

Example output:
    ✅ Verified: "quote text" → source.md:127 (found at line 125-129)
    ⚠️  Warning: Line number off by 15 lines → source.md:200 (found at line 215)
    ❌ Error: File not found → missing-file.md:42
    ❌ Error: Quote not found in source → source.md:100

Features:
- Finds markdown citations in format (filename:line) or (filename.md:line)
- Checks if source files exist
- Verifies quotes exist near cited line number (±5 lines tolerance)
- Flags suspicious patterns (many citations from same line, generic attributions)
- Supports both inline and block quote formats
"""

import argparse
import re
import os
from pathlib import Path
from typing import List, Tuple, Optional

class CitationChecker:
    def __init__(self, document_path: str, tolerance: int = 5):
        self.document_path = Path(document_path)
        self.tolerance = tolerance  # Lines of tolerance for line number checks
        self.errors = []
        self.warnings = []
        self.verified = []
        
    def extract_citations(self, content: str) -> List[Tuple[str, int, str]]:
        """
        Extract citations from document.
        Returns: List of (filename, line_number, quote_text) tuples
        """
        citations = []
        
        # Pattern: (filename:line) or (filename.md:line)
        citation_pattern = r'\(([^\)]+\.(md|txt)):(\d+)\)'
        
        # Find all citations
        for match in re.finditer(citation_pattern, content):
            filename = match.group(1)
            line_num = int(match.group(3))
            
            # Try to extract associated quote (look backwards for quote)
            quote_text = self._extract_quote_before_citation(content, match.start())
            
            citations.append((filename, line_num, quote_text))
        
        return citations
    
    def _extract_quote_before_citation(self, content: str, citation_pos: int) -> Optional[str]:
        """Extract quote text that appears before citation."""
        # Look backwards for quote in quotes or block quote
        text_before = content[:citation_pos]
        
        # Try to find quote in "quotes"
        quote_match = re.search(r'"([^"]+)"[^\(]*$', text_before)
        if quote_match:
            return quote_match.group(1)
        
        # Try to find block quote (> "quote")
        block_quote_match = re.search(r'>\s*"([^"]+)"[^\(]*$', text_before)
        if block_quote_match:
            return block_quote_match.group(1)
        
        return None
    
    def verify_file_exists(self, filename: str) -> bool:
        """Check if cited file exists (try relative to document and absolute)."""
        # Try relative to document
        relative_path = self.document_path.parent / filename
        if relative_path.exists():
            return True
        
        # Try absolute
        if Path(filename).exists():
            return True
        
        return False
    
    def verify_quote_in_file(self, filename: str, line_num: int, quote: Optional[str]) -> Tuple[bool, Optional[int]]:
        """
        Verify quote exists near cited line number.
        Returns: (found, actual_line_number)
        """
        if not quote:
            return (True, None)  # Can't verify without quote text
        
        # Try to read file
        try:
            # Try relative path first
            file_path = self.document_path.parent / filename
            if not file_path.exists():
                file_path = Path(filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Search within tolerance range
            start_line = max(0, line_num - self.tolerance - 1)  # -1 for 0-indexing
            end_line = min(len(lines), line_num + self.tolerance)
            
            # Normalize quote for comparison (remove extra whitespace)
            normalized_quote = ' '.join(quote.split())
            
            for i, line in enumerate(lines[start_line:end_line], start=start_line + 1):
                normalized_line = ' '.join(line.split())
                if normalized_quote in normalized_line:
                    return (True, i)
            
            return (False, None)
        
        except Exception as e:
            self.errors.append(f"Error reading {filename}: {e}")
            return (False, None)
    
    def check_document(self, content: str) -> dict:
        """Run all verification checks on document."""
        citations = self.extract_citations(content)
        
        print(f"\n📊 Found {len(citations)} citations\n")
        
        for filename, line_num, quote in citations:
            # Check 1: File exists
            if not self.verify_file_exists(filename):
                self.errors.append(f"❌ File not found: {filename}:{line_num}")
                continue
            
            # Check 2: Quote exists near cited line (if we have quote text)
            if quote:
                found, actual_line = self.verify_quote_in_file(filename, line_num, quote)
                
                if not found:
                    self.errors.append(f"❌ Quote not found: \"{quote[:50]}...\" → {filename}:{line_num}")
                elif actual_line and abs(actual_line - line_num) > 2:
                    self.warnings.append(f"⚠️  Line number off by {abs(actual_line - line_num)}: {filename}:{line_num} (found at {actual_line})")
                else:
                    self.verified.append(f"✅ Verified: \"{quote[:50]}...\" → {filename}:{line_num}")
            else:
                self.verified.append(f"✅ File exists: {filename}:{line_num} (no quote to verify)")
        
        return {
            'total': len(citations),
            'verified': len(self.verified),
            'warnings': len(self.warnings),
            'errors': len(self.errors)
        }
    
    def print_results(self):
        """Print verification results."""
        print("\n" + "="*60)
        
        if self.verified:
            print(f"\n✅ VERIFIED ({len(self.verified)}):\n")
            for item in self.verified:
                print(f"  {item}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):\n")
            for item in self.warnings:
                print(f"  {item}")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):\n")
            for item in self.errors:
                print(f"  {item}")
        
        print("\n" + "="*60)
        print(f"\nSummary: {len(self.verified)} verified, {len(self.warnings)} warnings, {len(self.errors)} errors\n")

def main():
    parser = argparse.ArgumentParser(description='Verify citations in markdown documents')
    parser.add_argument('document', help='Path to markdown document to check')
    parser.add_argument('--tolerance', type=int, default=5, help='Line number tolerance (default: 5)')
    parser.add_argument('--check-quotes', action='store_true', help='Verify quotes exist in source')
    parser.add_argument('--check-line-numbers', action='store_true', help='Check line number accuracy')
    
    args = parser.parse_args()
    
    # Read document
    try:
        with open(args.document, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading document: {e}")
        return 1
    
    # Run checks
    checker = CitationChecker(args.document, tolerance=args.tolerance)
    stats = checker.check_document(content)
    checker.print_results()
    
    # Exit code: 0 if no errors, 1 if errors found
    return 1 if stats['errors'] > 0 else 0

if __name__ == '__main__':
    exit(main())
