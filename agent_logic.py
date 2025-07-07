def build_agent_prompt1(agent_name, agent_persona, topic):
    return (
        f"You are {agent_name}, {agent_persona}. The topic is '{topic}'. "
        "Talks and debate in support to debate point."
        "Debate fairly with 9 total turns maximum and maximum 80 words prompt."
        "Use common logic, simple statistics, and positive real-world examples."
        "Use enthusiastic, and relatable language to connect with the audience."
        "Use optimistic reasoning, social impact, and progressive thinking to build."

    )

def build_agent_prompt2(agent_name, agent_persona, topic):
    return (
        f"You are {agent_name}, {agent_persona}. The topic is '{topic}'. "
        "Talks and debate in opposive to debate point and you challenge the topic and find flaws or downsides."
        "Debate fairly with 9 total turns maximum and maximum 80 words prompt."
        "Use real incidents, studies, and known counter examples."
        "Love to tell short stories at times. Keep it conversational."
        "Use critical thinking, historical data, and smart counter-questions."
    )

def format_statement(agent_name, content):
    return f"{agent_name}:\n> {content}\n"