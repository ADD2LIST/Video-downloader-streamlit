 import streamlit as st

import instaloader

def download_instagram_video(url):

    # Create an instance of Instaloader

    loader = instaloader.Instaloader()

    # Download the video

    try:

        loader.download_video(url, filename="downloaded_video")

        st.success("Video downloaded successfully!")

    except Exception as e:

        st.error(f"Failed to download the video. Error: {str(e)}")

def download_instagram_reel(url):

    # Create an instance of Instaloader

    loader = instaloader.Instaloader()

    # Download the reel

    try:

        loader.download_reels(url, filename="downloaded_reel")

        st.success("Reel downloaded successfully!")

    except Exception as e:

        st.error(f"Failed to download the reel. Error: {str(e)}")

# Streamlit app code

st.title("Instagram Video and Reel Downloader")

# Input URL

url = st.text_input("Enter the Instagram video or reel URL")

# Download button

if st.button("Download Video"):

    # Check if URL is provided

    if url:

        # Download the video

        download_instagram_video(url)

    else:

        st.warning("Please enter a valid Instagram video URL")

if st.button("Download Reel"):

    # Check if URL is provided

    if url:

        # Download the reel

        download_instagram_reel(url)

    else:

        st.warning("Please enter a valid Instagram reel URL")


              
