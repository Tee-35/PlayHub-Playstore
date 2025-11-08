### Document Audit Tool

## Summary:

This Python-based Document Audit Tool automatically tracks changes in text documents across multiple iterations. It is designed to:
Detect modifications, additions, or removals at sentence-level granularity.
Track multiple versions of a document (e.g., _0, _1, _2).
Generate timestamped CSV and JSON reports with:
Word changes
Sentence added/removed
Page number and line number
Counts and text of added/removed lines
Keep the report folder clean by retaining only the most recent reports.
Key Features:
Uses Python standard libraries: pathlib, hashlib, difflib, json, csv, datetime.
Automatically handles multiple iterations per document.
Produces professional, human-readable audit reports.
