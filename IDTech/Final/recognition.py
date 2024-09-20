import speech_recognition as sr
from openai import OpenAI

client = OpenAI(
    api_key = "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"
)
#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
#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


end_program = False
while not end_program:
    leave = ""
    get_input = ""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        start = input("Type Start to start asking your question: ")
        if start.lower() == "start":
            print("------------------------------------------------------------")
            print("Say something... (5 seconds to start speaking, 10 seconds to ask your questions)")
            audio = recognizer.listen(source, 5, 10)
    try:
        get_input = recognizer.recognize_google(audio)
        print("User: " + get_input)
    except sr.UnknownValueError:
        leave = input("I couldn't udnesrstand that, if you would like to exit please type exit: ")
        if leave.lower() == "exit":
            break

    except sr.RequestError as e:
        print("Error; {0}".format(e))
    if not get_input == "":
        if "bye" in get_input.lower() or "exit" in get_input.lower():
            end_program = True
            print("Have a great day!")
        system_data = [
            {"role": "system", "content": "Code assistant"},
            {"role": "user", "content": get_input}
        ]
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = system_data
        )
        assistant_response = response.choices[0].message.content
        system_data.append({"role": "assistant", "content": assistant_response})
        print("Assistant: " + assistant_response)
    if not leave.lower() == "exit":
        get_input = ""




