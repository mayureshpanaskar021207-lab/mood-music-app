import streamlit as st
from textblob import TextBlob
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Page Config
st.set_page_config(page_title="Tune-Aura", page_icon="🎧", layout="centered")

# Custom CSS
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .main { background: transparent; }

    h1, h2, h3, h4 {
        text-align: center;
        color: white;
    }
    
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        border: 2px solid #00eaff;
        background: rgba(255,255,255,0.1);
        color: white;
        font-size: 16px;
    }
    .stTextInput>div>div>input::placeholder {
        color: #bdeaff;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: #bbb;
        font-size: 0.9rem;
    }

    .stButton>button {
        background: linear-gradient(135deg, #ff0080, #7928ca);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 14px 20px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0px 4px 10px rgba(255, 0, 128, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #00ffe1, #00bcd4);
        color: black;
        transform: scale(1.08);
        box-shadow: 0px 4px 20px rgba(0, 255, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎧 Mood-Based Music Recommender")

st.markdown("""
<h3 style='text-align:center; color:#ADD8E6;'>OR</h3>
<h4 style='text-align:center; color:white;'>Choose your mood to explore playlists</h4>
""", unsafe_allow_html=True)

# Playlist URLs
playlists = {
    "Sad": "https://www.youtube.com/playlist?list=PL9khxBZiiQwoKEqdTrb4ip-S_Tov6FkBQ",
    "Romantic": "https://www.youtube.com/playlist?list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK",
    "Motivational": "https://www.youtube.com/playlist?list=PL4taEUw-UM8QZ7NiTUm2mEpzia2ulckpi"
}

# Playlist Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("😢 Sad Vibes"):
        st.markdown(f"<h4 style='text-align:center;'>🎵 <a href='{playlists['Sad']}' target='_blank'>Open Sad Playlist</a></h4>", unsafe_allow_html=True)

with col2:
    if st.button("❤ Romantic Vibes"):
        st.markdown(f"<h4 style='text-align:center;'>🎵 <a href='{playlists['Romantic']}' target='_blank'>Open Romantic Playlist</a></h4>", unsafe_allow_html=True)

with col3:
    if st.button("💪 Motivational Energy"):
        st.markdown(f"<h4 style='text-align:center;'>🎵 <a href='{playlists['Motivational']}' target='_blank'>Open Motivational Playlist</a></h4>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.header("🎧 What's your vibe today?")

# Mood Input
text = st.text_input("", placeholder="Type something like 'I feel lonely' or 'feeling excited'...")

if text:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    if any(w in text_lower for w in ["love", "romantic", "crush", "heart"]):
        mood = "Romantic"
    elif any(w in text_lower for w in ["energetic", "excited", "dance", "power"]):
        mood = "Energetic"
    elif any(w in text_lower for w in ["motivate", "inspired", "goal", "win"]):
        mood = "Motivational"
    elif any(w in text_lower for w in ["alone", "lonely", "missing"]):
        mood = "Lonely"
    elif polarity > 0.2:
        mood = "Happy"
    elif polarity < -0.2:
        mood = "Sad"
    else:
        mood = "Calm"

    emoji_map = {
        "Happy": "😄", "Sad": "😢", "Calm": "😌", "Romantic": "❤",
        "Energetic": "⚡", "Motivational": "💪", "Lonely": "💔"
    }

    emoji = emoji_map.get(mood, "🎧")

    # Song Dictionary
    songs = {
        "Happy": {
            "Phir Se Ud Chala – Mohit Chauhan": "https://www.youtube.com/embed/R09akexWiq4?si=0Rtzjs_or04jPv8Z",
            "Ilahi – Arijit Singh": "https://www.youtube.com/embed/wM4xpaWV5s4?si=Tf-tRJBf35NbbI4A",
            "On Top of the World – Imagine Dragons": "https://www.youtube.com/embed/Xzl416fjUSY?si=qrxj-AOaRpGmYeoC"
        },
        "Sad": {
            "Channa Mereya – Arijit": "https://www.youtube.com/embed/S7tYeUBgGHU?si=bAyREA8HnpO3NaSp",
            "Tujhe Kitna Chahne Lage – Arijit": "https://www.youtube.com/embed/kbh5jqPEjj0?si=zO0zYhnaKNEw-Y39",
            "Fix You – Coldplay": "https://www.youtube.com/embed/bzRMneypG04?si=YJOJS7hjuLz1JSm0"
        },
        "Romantic": {
            "Tum Hi Ho – Arijit": "https://www.youtube.com/embed/LULKYBUvfCQ?si=q46VR1Sc43iHkhy5",
            "Raabta – Arijit": "https://www.youtube.com/embed/vEe-UgJvUHE?si=fnsRZ0CNLKVNHxXW",
            "Pehla Nasha – Udit Narayan": "https://www.youtube.com/embed/Ed1WBWvxnSY?si=mLHfbl-osYWMs7CO"
        },
        "Calm": {
            "Khairiyat – Arijit": "https://www.youtube.com/embed/_RFUvHlW41A?si=sS0l8LQkBIGWMq0J",
            "Let It Be – Beatles": "https://www.youtube.com/embed/5AnNkJ_VK9E?si=6mDgSGdFglI5Zh2-",
            "Perfect – Ed Sheeran": "https://www.youtube.com/embed/kPhpHvnnn0Q?si=afPkQPK1uLxTbSrb"
        },
        "Energetic": {
            "Zinda – Siddharth Mahadevan": "https://www.youtube.com/embed/4IIrghqiEPY?si=T6d5PHhcyor5gtUC",
            "Believer – Imagine Dragons": "https://www.youtube.com/embed/W0DM5lcj6mw?si=GcYh_6BcKQN5BVAV",
            "Lakshya Title Track": "https://www.youtube.com/embed/QWnqk6pDpYI?si=U5VxNZ_sTJkrv1K8"
        },
        "Motivational": {
            "Kar Har Maidaan Fateh": "https://www.youtube.com/embed/pQm8Ifoy-ik?si=ttYrQOX-6EC_gNwP",
            "Aashayein – KK": "https://www.youtube.com/embed/xIob3OjpnFg?si=R_39os80RHyVm1Nz",
            "Hall of Fame – The Script": "https://www.youtube.com/embed/3Kxf2dHlDpQ?si=MKDC3mAwrHUUljz0"
        },
        "Lonely": {
            "Jo Bheji Thi Duaa": "https://www.youtube.com/embed/xtjxlOnzQNg?si=JHHDuX2wtjAh0CFh",
            "Shayad – Arijit": "https://www.youtube.com/embed/muxtRRMmyhc?si=DArExucTqGPcgMqs",
            "Someone Like You – Adele": "https://www.youtube.com/embed/z7GCiVTlv04?si=5LzFj9C1vMoqxK7G"
        }
    }

    st.success(f"*Detected Mood:* {mood} {emoji}")
    st.subheader("🎵 Recommended Songs")

    for s, link in songs[mood].items():
        st.markdown(f"{s}")
        st.video(link)

    # Save input to CSV
    try:
        df = pd.read_csv("mood_data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Input", "Mood", "Polarity"])

    df.loc[len(df)] = {'Text': text, 'Mood': mood, 'Polarity': polarity}

    df.to_csv("mood_data.csv", index=False)

    # ML Training when enough data
    if len(df) >= 3:
        X = df["Input"].fillna("").astype(str)
        y = df["Mood"].fillna("").astype(str)

        cv = CountVectorizer()
        X_vec = cv.fit_transform(X)

        model = MultinomialNB()
        model.fit(X_vec, y)

        test_vec = cv.transform([text])
        predicted_mood = model.predict(test_vec)[0]

        st.info(f"🤖 *ML Predicted Mood:* {predicted_mood} {emoji_map.get(predicted_mood, '🎧')}")

# Footer
st.markdown("<div class='footer'>🎉 Made with ❤ by CodeCatalysts</div>", unsafe_allow_html=True)