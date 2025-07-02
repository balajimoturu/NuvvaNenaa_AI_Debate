def build_agent_prompt1(agent_name, agent_persona, topic):
    return (
        f"You are {agent_name}, {agent_persona}. The topic is '{topic}'. "
        "Talks and debate in supportive to debate point."
        "Debate fairly with 9 total turns, make it fun, metaphors, or idioms."
        "Ideas are generated. Keep it conversational."
    )

def build_agent_prompt2(agent_name, agent_persona, topic):
    return (
        f"You are {agent_name}, {agent_persona}. The topic is '{topic}'. "
        "Talks and debate in opposive to debate point."
        "Debate fairly with 9 total turns, make it strong and give citations and mention author names where required."
        "Love to tell sthort stories at times but not always. Keep it conversational."
    )

def format_statement(agent_name, content):
    return f"### {agent_name} says:\n> {content}\n"