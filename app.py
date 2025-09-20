import streamlit as st
import pandas as pd
import random

# --------------------------
# Load music data
# --------------------------
# Example CSV format: mood,song
# happy,Happy - Pharrell Williams
# sad,Someone Like You - Adele
try:
    music_df = pd.read_csv('music_data.csv')
except FileNotFoundError:
    # fallback sample data
    music_df = pd.DataFrame({
        'mood': ['happy', 'sad', 'relaxed', 'angry'],
        'song': ['Happy - Pharrell', 'Someone Like You - Adele', 'Weightless - Marconi', 'Break Stuff - Limp Bizkit']
    })

# --------------------------
# Streamlit UI
# --------------------------
st.title("🎵 Mood to Music App")
st.write("Select your mood, and we'll recommend a song for you!")

mood = st.selectbox("What's your current mood?", music_df['mood'].unique())

if st.button("Get Song Recommendation"):
    filtered_songs = music_df[music_df['mood'] == mood]['song'].tolist()
    if filtered_songs:
        song = random.choice(filtered_songs)
        st.success(f"🎶 Recommended song: **{song}**")
    else:
        st.warning("No songs found for this mood!")