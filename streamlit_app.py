import streamlit as st
import requests
import os
from dotenv import load_dotenv
from utils import display_instructions
import uuid

load_dotenv()

# Backend API endpoint (the FastAPI service)
AGENT_API_PORT = os.getenv("AGENT_API_PORT", "8080")
API_URL = f"http://localhost:{AGENT_API_PORT}/agent"

st.set_page_config(page_title="ICARUS")
st.title("ICARUS: Intentionally Compromisable Agent for Red-teaming and Usage Simulation")
display_instructions()
st.markdown(
    f"""
        Hi! I'm an helpful assistant and I can help fetch information about your recent transactions.

        Try asking me: "What are my recent transactions?"

        - Backend URL: `{API_URL}`
    """
)

# --- Persist session_id in st.session_state so it survives reruns ---
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# --- Initialize session state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat UI ---
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Show my recent transactions")

if prompt:
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call backend
    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                print(str({"input": prompt, "session_id": st.session_state.session_id}))
                resp = requests.post(API_URL, json={"input": prompt, "session_id": st.session_state.session_id})
                if resp.status_code != 200:
                    st.error(f"API error {resp.status_code}: {resp.text}")
                else:
                    data = resp.json()
                    tools_used = []
                    print(data)
                    if data.get("tools_used"):
                        for t in data["tools_used"]:
                            tools_used.append({
                                "tool": t['tool'],
                                "input": t['input'],
                                "tool_output": t['tool_output'].replace("\n", "")
                            })

                    content = f"""
**Tools used**:

{tools_used}

**Response**:

{data['response']}
"""
                    st.markdown(content)
                    st.session_state.chat_history.append({"role": "assistant", "content": content})

    except requests.exceptions.ConnectionError:
        st.error("[ERROR] Could not reach the ICARUS API. Is it running?")
    except Exception as e:
        st.error(f"[ERROR] Unexpected error: {e}")

