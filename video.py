import streamlit as st

import requests

import os

def download_reel(reel_url):

  """Downloads an Instagram reel video from the given URL.

  Args:

    reel_url: The URL of the Instagram reel video to download.

  Returns:

    The path to the downloaded video file.

  """

  # Get the video ID from the URL.

  video_id = reel_url.split("/")[-1]

  # Make a request to the Instagram API to get the video data.

  response = requests.get(f"https://graph.instagram.com/reels/{video_id}/?fields=media_url,taken_at")

  # Check if the request was successful.

  if response.status_code != 200:

    raise Exception(f"Error downloading reel: {response.status_code}")

  # Get the video URL and the timestamp of the video.

  video_url = response.json()["media_url"]

  timestamp = response.json()["taken_at"]

  # Create a directory to store the downloaded video.

  download_dir = os.path.join(os.getcwd(), "downloads")

  if not os.path.exists(download_dir):

    os.mkdir(download_dir)

  # Download the video.

  response = requests.get(video_url)

  with open(os.path.join(download_dir, f"{video_id}.mp4"), "wb") as f:

    f.write(response.content)

  # Return the path to the downloaded video file.

  return os.path.join(download_dir, f"{video_id}.mp4")

# Create a Streamlit app.

app = st.empty()

# Get the Instagram reel URL from the user.

reel_url = st.text_input("Enter the Instagram reel URL:")

# If the user enters a valid URL, download the video.

if reel_url:

  video_path = download_reel(reel_url)

  st.success(f"Downloaded video to {video_path}")

# Otherwise, show an error message.

else:

  st.error("Please enter a valid Instagram reel URL.")



    
    
        
