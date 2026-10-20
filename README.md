# AI Lab Assignment: Scaffolding a Robust API Integration

## Overview
This task demonstrates the application of Contextual Prompting to refactor an existing Python sentiment analysis tool (`sentiment_analyzer.py`). The refactoring adds secure environment variable authentication scaffolding and robust exception handling for external HTTP calls.

## Files Included
- `initial_code/sentiment_analyzer.py`: The original script before refactoring.
- `refactored_code/sentiment_analyzer.py`: The updated script incorporating secure API key retrieval from environment variables, Bearer token header injection, explicit timeout limits, and refined exception handling (`Timeout`, `ConnectionError`).
- `README.md`: Task documentation and operational guide.

## AI Tool Used
- **AI Engine**: Gemini 1.5 Pro / Advanced Contextual Prompting Assistant
- **Technique**: Single-turn Contextual Prompting with complete codebase embedding and strict non-functional requirement specification.

## Execution Instructions
1. Navigate to the `refactored_code` directory:
   ```bash
   cd "refactored_code"