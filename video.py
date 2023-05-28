# main.py
import streamlit as st

import requests

import shutil

def download_video(url):

    # Send a request to get the video content

    response = requests.get(url, stream=True)

    # Extract the filename from the URL

    filename = url.split("/")[-1]

    # Open a file for writing

    with open(filename, "wb") as file:

        # Iterate over the response content in chunks

        for chunk in response.iter_content(chunk_size=1024):

            if chunk:

                # Write the chunk to the file

                file.write(chunk)

    return filename

# Streamlit app code

st.title("Video Downloader")

# Input URL

url = st.text_input("Enter the video URL")

# Download button

if st.button("Download"):

    # Check if URL is provided

    if url:

        # Download the video

        filename = download_video(url)

        st.success("Video downloaded successfully!")

        # Create a temporary download link

        with open(filename, "rb") as file:

            # Read the file contents

            video_bytes = file.read()

        # Generate a unique filename for download

        download_filename = f"{filename}"

        st.download_button(

            label="Click here to download the video",

            data=video_bytes,

            file_name=download_filename,

        )

    else:

        st.warning("Please enter a valid video URL.")



