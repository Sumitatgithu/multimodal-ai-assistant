from llm.chat_engine import get_response
from voice.speech_to_text import transcribe_audio
from voice.text_to_speech import speak

def main():
    print("Multimodal AI Assistant Started")

    while True:
        mode = input("Choose mode (text/voice/exit): ")

        if mode == "text":
            user_input = input("You: ")
            response = get_response(user_input)
            print("AI:", response)
            speak(response)

        elif mode == "voice":
            file = input("Enter audio file path: ")
            text = transcribe_audio(file)
            response = get_response(text)
            print("AI:", response)
            speak(response)

        elif mode == "exit":
            break

if __name__ == "__main__":
    main()
