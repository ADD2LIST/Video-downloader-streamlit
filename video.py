# main.py

import streamlit as st

import requests

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

# Streamlit app code

st.title("Video Downloader")

# Input URL

url = st.text_input("Enter the video URL")

# Download button

if st.button("Download"):

    # Check if URL is provided

    if url:

        # Download the video

        download_video(url)

        st.success("Video downloaded successfully!")

    else:

        st.warning("Please enter a valid video URL.")

