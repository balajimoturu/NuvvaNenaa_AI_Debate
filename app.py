import streamlit as st
from openai_wrapper import get_completion
from agent_logic import build_agent_prompt1, build_agent_prompt2, format_statement

st.set_page_config(page_title="Nuvva Nenaa - AI Debate Arena", layout="wide")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

# Session initialization
if "history" not in st.session_state:
    st.session_state.history = []
if "turn" not in st.session_state:
    st.session_state.turn = 0
if "debate_started" not in st.session_state:
    st.session_state.debate_started = False
if "agent1_prompt" not in st.session_state:
    st.session_state.agent1_prompt = ""
if "agent2_prompt" not in st.session_state:
    st.session_state.agent2_prompt = ""
if "agent1_name" not in st.session_state:
    st.session_state.agent1_name = ""
if "agent2_name" not in st.session_state:
    st.session_state.agent2_name = ""
if "agent1_turns" not in st.session_state:
    st.session_state.agent1_turns = []
if "agent2_turns" not in st.session_state:
    st.session_state.agent2_turns = []

# UI - Setup Form
st.title("🎭 Nuvva Nenaa - AI Debate Arena")

with st.form("setup"):
    topic = st.text_input("📝 Enter Debate Topic")
    agent1 = st.text_input("🧊 Agent 1 Name - Persona", "Bright Byte - Cool and Calm")
    agent2 = st.text_input("🔥 Agent 2 Name - Persona", "Critique Core - Logical and Sharp")
    submitted = st.form_submit_button("Start Debate 🎤")

if submitted and topic:
    st.session_state.agent1_name = agent1.split("-")[0].strip()
    st.session_state.agent2_name = agent2.split("-")[0].strip()
    st.session_state.agent1_prompt = build_agent_prompt1(st.session_state.agent1_name, agent1, topic)
    st.session_state.agent2_prompt = build_agent_prompt2(st.session_state.agent2_name, agent2, topic)
    st.session_state.history = [{"role": "system", "content": st.session_state.agent1_prompt}]
    st.session_state.turn = 0
    st.session_state.agent1_turns = []
    st.session_state.agent2_turns = []
    st.session_state.debate_started = True

    #st.session_state.turn += 1


# UI - Agent Cards
if st.session_state.debate_started:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"<div class='agent-card agent1-card'><b>{st.session_state.agent1_name}</b><br>Supportive View</div>",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"<div class='agent-card agent2-card'><b>{st.session_state.agent2_name}</b><br>Opposing View</div>",
            unsafe_allow_html=True,
        )

# Next Turn Button
if st.session_state.debate_started and st.session_state.turn < 9:
    col_left, col_mid, col_right = st.columns([10, 2, 10])
    with col_mid:   
        label = "🔥 Start Debate" if st.session_state.turn == 0 else "Next Turn ➡️"
        if st.button(label):
            # Agent 1 speaks
            history = [{"role": "system", "content": st.session_state.agent1_prompt}] + [
                {"role": "assistant", "content": msg} for msg in st.session_state.agent1_turns + st.session_state.agent2_turns
            ]
            reply1 = get_completion(history)
            st.session_state.agent1_turns.append(reply1)
            
            # Agent 2 speaks
            history[0]["content"] = st.session_state.agent2_prompt
            history.append({"role": "assistant", "content": reply1})
            reply2 = get_completion(history)
            st.session_state.agent2_turns.append(reply2)

            st.session_state.turn += 1
            st.rerun() #To render the updated button

# Voting Section at Top if Finished
if st.session_state.turn >= 4:
    st.markdown("---")
    # Header - Centered
    st.markdown("<h3 style='text-align: center;'>🗳️ Who convinced you more?</h3>", unsafe_allow_html=True)

    # Create 3 columns and use only the middle one
    col1, col2, col3 = st.columns([1, 5, 1])  # Adjust width ratios as needed
    with col2:
        choice = st.radio("Pick the winning agent:", (st.session_state.agent1_name, st.session_state.agent2_name), index=0)
        if st.button("Show Summary 🏁"):
            summary_prompt = (
                f"Summarize why {choice} gave a stronger debate regarding {topic}. "
                f"List 2 good points from the debated points of other agent ({st.session_state.agent1_name if choice != st.session_state.agent1_name else st.session_state.agent2_name})."
            )
            summary = get_completion([{"role": "user", "content": summary_prompt}])
            st.success("🏆 Debate Summary")
            st.markdown(f"<div style='text-align: justify;'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("---")



# Display all messages in reverse order (newest on top)
display_blocks = []
for i in range(min(len(st.session_state.agent1_turns), len(st.session_state.agent2_turns))):
    a1 = f"<div class='chat-bubble chat1'>{format_statement(st.session_state.agent1_name, st.session_state.agent1_turns[i])}</div><br><br>"
    a2 = f"<div class='chat-bubble chat2'>{format_statement(st.session_state.agent2_name, st.session_state.agent2_turns[i])}</div>"
    display_blocks.insert(0, a1)
    display_blocks.insert(0, a2)

for block in display_blocks:
    st.markdown(block, unsafe_allow_html=True)

# First time prompt (only before turn 1)
if st.session_state.debate_started and st.session_state.turn == 0:
    st.markdown("<h3 style='text-align: center;'>👋 Ready to begin? Click 'Start Debate' to get the first move!</h3>", unsafe_allow_html=True)
