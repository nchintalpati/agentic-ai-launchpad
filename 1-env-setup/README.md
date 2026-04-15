# Environment Setup

This module covers setting up your development environment for Agentic AI development.

## Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) installed
- Google AI Studio API key ([Get one here](https://aistudio.google.com/api-keys))

## Setup Instructions

### 1. Create and activate the Conda environment

```bash
conda create --prefix ./my_env python=3.11 -y
conda activate ./my_env
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in this directory with your API key:

```
GOOGLE_API_KEY=your_api_key_here
```

### 4. Test the setup

```bash
python setup-test.py
```

This will test your connection to Google's Gemini model.

## Files

| File | Description |
|------|-------------|
| `setup-test.py` | Tests the Gemini API connection |
| `requirements.txt` | Python dependencies |
| `.github/workflows/` | GitHub Actions CI/CD workflows |