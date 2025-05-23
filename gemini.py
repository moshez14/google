import google.generativeai as genai
import sys
import time

# Check for filename argument
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <path-to-video> <question>")
    sys.exit(1)

file_path = sys.argv[1]
video_question = sys.argv[2]
# Configure API key
genai.configure(api_key="AIzaSyDu_8p38ogl6tNtN8Np7KMzGjacmoIGCPE")

# Create the model (use gemini-1.5-flash or gemini-1.5-pro)
model = genai.GenerativeModel("gemini-1.5-flash")

# Upload the video file
uploaded_file = genai.upload_file(f"/var/tmp/{file_path}")
while uploaded_file.state.name != "ACTIVE":
    #print(f"Waiting for file to become ACTIVE... Current state: {uploaded_file.state.name}")
    time.sleep(1)
    uploaded_file = genai.get_file(uploaded_file.name)

# Send the prompt
#print(f"Question:{video_question}")
response = model.generate_content([
    uploaded_file,
    f"{video_question}" 
])

# Print the result
print(response.text)

