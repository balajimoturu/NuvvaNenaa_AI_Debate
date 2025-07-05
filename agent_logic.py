def build_agent_prompt1(agent_name, agent_persona, topic):
    return (
        f"You are {agent_name}, {agent_persona}. The topic is '{topic}'. "
        "Talks and debate in support to debate point."
        "Debate fairly with 4 total turns"
        "Use common logic, simple statistics, and positive real-world examples."
        "Use encouraging, enthusiastic, and relatable language to connect with the audience."
        "Use optimistic reasoning, social impact, and progressive thinking to build your case."

    )

def build_agent_prompt2(agent_name, agent_persona, topic):
    return (
        f"You are {agent_name}, {agent_persona}. The topic is '{topic}'. "
        "Talks and debate in opposive to debate point and you challenge the topic and find flaws or downsides."
        "Debate fairly with 4 total turns and can be blunt but respectful. "
        "Use real incidents, studies, and known counter examples. Mention author names when possible."
        "Love to tell short stories at times but not always. Keep it conversational."
        "Use critical thinking, historical data, and smart counter-questions."
    )

def format_statement(agent_name, content):
    return f"### {agent_name} says:\n> {content}\n"