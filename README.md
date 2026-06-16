# GitHub Profile Analyzer

A beginner-friendly backend project built with Python, FastAPI, and the GitHub API.

This project fetches GitHub user profile information and analyzes repositories to provide useful insights such as:

* Followers count
* Public repositories
* Total stars
* Most used languages

## Features

* Fetch GitHub user profile data
* Fetch repository information
* Analyze repository statistics
* Count programming languages used
* REST API built using FastAPI
* Clean modular project structure

## Tech Stack

* Python
* FastAPI
* Requests
* Git & GitHub

## Project Structure

```text
github-profile-analyzer/
│
├── app/
│   ├── main.py
│   ├── github_api.py
│   ├── analyzer.py
│   ├── config.py
│   └── test.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git https://github.com/mohanv2005/github-profile-analyzer
```

Move into project folder:

```bash
cd github-profile-analyzer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

## API Endpoint

### Get GitHub Profile Analysis

```text
GET /github/{username}
```

Example:

```text
http://127.0.0.1:8000/github/octocat
```

