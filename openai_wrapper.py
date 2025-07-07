import os

USE_GEMINI = False  # toggle to switch API

if USE_GEMINI:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")

    def get_completion(messages, max_tokens=90):
        try:
            user_prompt = "\n".join([m["content"] for m in messages])
            response = model.generate_content(user_prompt)
            return response.text.strip()
        except Exception as e:
            return f"⚠️ API error: {str(e)}"
else:
    from openai import OpenAI
    from dotenv import load_dotenv
    import tiktoken

    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def count_tokens(text, model="gpt-3.5-turbo"):
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))

    def get_completion(messages, max_tokens=150):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"⚠️ API error: {str(e)}"