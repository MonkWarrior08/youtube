# YouTube Transcript Note Generator

This application extracts transcripts from YouTube videos and uses OpenAI to generate concise bullet-point notes.

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the application using:
```
python main.py
```

Enter a YouTube URL when prompted, and the application will:
1. Extract the transcript from the video
2. Generate bullet-point notes using OpenAI
3. Display the notes for you to copy

## Requirements

- Python 3.8+
- An OpenAI API key 