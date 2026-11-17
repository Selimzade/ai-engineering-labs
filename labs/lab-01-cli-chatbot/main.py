from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = "Sən qısa və aydın cavab verən Azərbaycanca AI mentorsan."

history = []

while True:
    user_input = input("\nSən: ").strip()
    if user_input.lower() in ("exit", "quit", "çıx"):
        break
    if user_input == "/reset":
        history = []
        print("Tarixcə tamizləndi.")
        continue

    history.append({"role": "user", "content": user_input})
    history = history[-11:]

    print("Claude: ", end="", flush=True)

    reply = ""

    with client.messages.stream(model="claude-haiku-4-5", max_tokens=1000, system=SYSTEM, messages=history) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            reply += text

    print()
    usage = stream.get_final_message().usage
    print(f"input tokens: {usage.input_tokens} | output tokens: {usage.output_tokens}")

    history.append({"role": "assistant", "content": reply})