# T-10 Documentation

This repository contains daily documentation for the 2024-2025 FTC season for T-10.

## Automatic monthly summaries

**You need an API key from Groq. It's completely FREE! [Click here.](https://console.groq.com)**

Run `GROQ_API_KEY=gsk_xxx python3 summarize.py [file pattern] > output-file.txt`
* `GROQ_API_KEY` is an environment variable that is set to your Groq API key.

Example: `GROQ_API_KEY=gsk_xxx python3 summarize.py 09* > 09-summary.txt`
- Summarizes all files starting with `09` (September documentation)
- Writes the summary to the file `09-summary.txt`

## Conventions

### Format

```
[A high level summary of the entire meeting, one sentence.]

A. First thing that we did
B. Second thing that we did
    1. A sub thing that was happening
    2. Another sub thing
        a. A specific detail to that sub thing
        b. Another specific detail
    3. Yet another sub thing
C. Third thing that we did
```

### File naming

- Daily documentation: `MMDDYY-comment-goes-here-day-#.txt`
- Monthly documentation summaries: `MM-summary.txt`
