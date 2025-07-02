import streamlit as st
from openai_wrapper import get_completion
from agent_logic import build_agent_prompt1, build_agent_prompt2, format_statement

st.set_page_config(page_title="Nuvva Nenaa", layout="centered")
st.title("NUVVA NENAA - AI DEBATE ARENA 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "debate_started" not in st.session_state:
    st.session_state.debate_started = False
if "summary_shown" not in st.session_state:
    st.session_state.summary_shown = False

with st.form("setup"):
    topic = st.text_input("📝 Enter Debate Topic")
    agent1 = st.text_input("🎭 Enter 1st Agent name & role (seperated with '-')", "Chill Chandler - Cool and Calm")
    agent2 = st.text_input("🎯 Enter 2nd Agent name & role (seperated with '-')", "Visionary Rage - Logical and sharp")
    submitted = st.form_submit_button("Start Debate 🔥")

if submitted and topic:
    st.session_state.debate_started = True
    st.session_state.summary_shown = False
    st.session_state.messages = []
    st.session_state.agent1_name = agent1.split("-")[0].strip()
    st.session_state.agent2_name = agent2.split("-")[0].strip()

    prompt1 = build_agent_prompt1(st.session_state.agent1_name, agent1, topic)
    prompt2 = build_agent_prompt2(st.session_state.agent2_name, agent2, topic)

    history = [
        {"role": "system", "content": prompt1},
    ]
    for i in range(5):
        reply1 = get_completion(history)
        st.session_state.messages.append(format_statement(st.session_state.agent1_name, reply1))
        history.append({"role": "assistant", "content": reply1})

        history[0]["content"] = prompt2
        reply2 = get_completion(history)
        st.session_state.messages.append(format_statement(st.session_state.agent2_name, reply2))
        history.append({"role": "assistant", "content": reply2})

if st.session_state.debate_started:
    for m in st.session_state.messages:
        st.markdown(m)

    choice = st.radio("Who won the debate?", (st.session_state.agent1_name, st.session_state.agent2_name))
    if st.button("Show Summary"):
        st.session_state.summary_shown = True

    if st.session_state.summary_shown:
        summary_prompt = f"Summarize why {choice} gave a stronger debate and list 2 good points from the other agent."
        summary = get_completion([{"role": "user", "content": summary_prompt}])
        st.markdown(f"## 🏁 Debate Conclusion:\n{summary}")
