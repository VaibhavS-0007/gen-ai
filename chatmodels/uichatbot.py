from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# ---------- Page setup ----------
st.set_page_config(page_title="Mood Chat Bot", page_icon="🎭", layout="centered")

st.markdown(
    """
    <style>
    .block-container {max-width: 760px; padding-top: 2rem;}
    .hero-title {
        text-align: center; font-size: 2.4rem; font-weight: 800;
        background: linear-gradient(90deg, #ff4b4b, #8e44ff, #ffb400);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero-sub {text-align: center; opacity: 0.7; margin-bottom: 1.5rem;}
    .mode-pill {
        display: inline-block; padding: 0.25rem 0.8rem; border-radius: 999px;
        background: rgba(128,128,128,0.18); font-weight: 600; font-size: 0.85rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Modes (same prompts as the original script) ----------
MODES = {
    1: {
        "emoji": "😡",
        "name": "Angry",
        "desc": "Replies with rage and fury",
        "prompt": "you have to ans in angry way coz are angery mode",
    },
    2: {
        "emoji": "😢",
        "name": "Sad",
        "desc": "Replies with a heavy heart",
        "prompt": "you are a sad chat bot give ans in sad way",
    },
    3: {
        "emoji": "😂",
        "name": "Funny",
        "desc": "Replies with jokes and humor",
        "prompt": "you are funny chat bot make conversation in funny way",
    },
}


# ---------- Same model setup as the original script ----------
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b")
    return ChatHuggingFace(llm=llm)


model = load_model()

# ---------- Sidebar: mode selector (can be changed any time) ----------
with st.sidebar:
    st.markdown("### 🎭 Bot mood")
    choice = st.radio(
        "Choose the way you want answers",
        options=list(MODES.keys()),
        index=2,
        format_func=lambda k: f"{MODES[k]['emoji']}  {MODES[k]['name']}",
        key="choice",
    )
    st.caption(MODES[choice]["desc"])
    st.divider()
    st.caption("Switch the mood any time, even mid-chat.")
    st.caption("Type **0** in the chat box to exit.")

mode = MODES[choice]

# ---------- Session state ----------
if "msghistory" not in st.session_state:
    st.session_state.msghistory = [SystemMessage(content=mode["prompt"])]
if "bot_moods" not in st.session_state:
    st.session_state.bot_moods = []  # UI only: which mood each bot reply was in
if "exited" not in st.session_state:
    st.session_state.exited = False

msghistory = st.session_state.msghistory

# Apply the currently selected mood: swap the SystemMessage at the start of the history.
# Everything else in the history (the conversation so far) stays as it is.
msghistory[0] = SystemMessage(content=mode["prompt"])

# ---------- Header ----------
st.markdown(
    f'<div class="hero-title">{mode["emoji"]} {mode["name"]} Bot</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="hero-sub">Type 0 to exit</div>', unsafe_allow_html=True)

# ---------- Render history ----------
# index 0 is the SystemMessage, then user / bot strings alternate
for i, text in enumerate(msghistory[1:]):
    is_user = i % 2 == 0
    if is_user:
        if text == "0":
            continue
        with st.chat_message("user"):
            st.markdown(text)
    else:
        past_mood = st.session_state.bot_moods[i // 2]
        with st.chat_message("assistant", avatar=past_mood["emoji"]):
            st.markdown(text)

# ---------- Input ----------
if st.session_state.exited:
    st.info("Chat ended.")
else:
    prompt = st.chat_input("You : ")

    if prompt:
        msghistory.append(prompt)
        if prompt == "0":
            st.session_state.exited = True
            st.rerun()
        else:
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant", avatar=mode["emoji"]):
                with st.spinner(f"{mode['name']} bot is thinking..."):
                    responce = model.invoke(msghistory)
                st.markdown(responce.content)

            msghistory.append(responce.content)
            st.session_state.bot_moods.append(mode)