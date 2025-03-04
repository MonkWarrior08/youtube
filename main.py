import os
import re
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from pytube import YouTube

load_dotenv()

def extract_url(url):
    id_pattern = r'(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))([^?&\n]+)'
    match = re.search(id_pattern, url)
    if match:
        return match.group(1)
    return None

def url_title(url):
    try:
        ytb = YouTube(url)
        return ytb.title
    except Exception as e:
        print("Error: {e}")

def transcript(id):
    try:
        yt_transcript = YouTubeTranscriptApi.get_transcript(id)
        transcript = ' '.join(item['text'] for item in yt_transcript)
        return transcript
    except Exception as e:
        print(f"Error: {e}")

def generate_note(transcript, title):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="o3-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates detailed, structured bullet point notes from video transcripts. Focus on the main ideas, key points, and important details. Organize the notes in a hierarchical structure with categories when appropriate."},
                {"role": "user", "content": f"Please create bullet point notes for this YouTube video titled '{title}'. Here's the transcript:\n\n{transcript}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")

def main():
    url = input("Enter url: ")
    id = extract_url(url)
    if not id:
        return "Invalid URL"
    print("\nProcessing")
    video_title = url_title(url)
    print(f"{video_title}")

    print("get transcript")
    get_transcript = transcript(id)

    print("generate note")
    note = generate_note(get_transcript, video_title)

    print("\n==== Note =====\n")
    print(note)
    print("\n==== Note =====\n")

if __name__ == "__main__":
    main()