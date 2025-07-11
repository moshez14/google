import sys
from google import genai
from google.genai import types
import time
import os

# Check for arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <path-to-video> <question>")
    sys.exit(1)

filename = sys.argv[1]

if not filename.endswith(".mp4"):
    filename += ".mp4"
file_path = f"/var/tmp/{filename}"
video_question = sys.argv[2]

# Initialize client with API key
client = genai.Client(api_key="AIzaSyDu_8p38ogl6tNtN8Np7KMzGjacmoIGCPE")

# Upload video file
uploaded_file = client.files.upload(file=file_path)

while uploaded_file.state.name != "ACTIVE":
    #print(f"Waiting for file to become ACTIVE... Current state: {uploaded_file.state.name}")
    time.sleep(1)
    uploaded_file = client.files.get(name=uploaded_file.name)

# Use Gemini model to analyze the video
response = client.models.generate_content(
    model="models/gemini-1.5-pro",  # or "gemini-2.0-pro" when available
    contents=[
        uploaded_file,
        {"text": video_question},
        "video/mp4"
    ]
)

# Output the model's response
print(response.text)
