import speech_recognition as sr
from openai import OpenAI
import pyttsx3
engine = pyttsx3.init()
import colorama
from colorama import Fore, Style


colorama.init(autoreset=True)
# Initialize OpenAI client
client = OpenAI(api_key="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")
#Function for getting the speech, returns user's input
def get_speech_input(recognizer, source):
    line()
    print(f"{Fore.YELLOW}Say something... (5 seconds to start speaking, 10 seconds to ask your questions)")
    #LIstens to mic
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    #If the previous line doesn't do anything(user doesnt talk), the error will be handled
    try:
        #Recognizes Audio
        input_text = recognizer.recognize_google(audio)
        line()
        #Prints the user's text
        print(f"{Fore.CYAN}User: {input_text}")
        #returns the text
        return input_text
    except sr.UnknownValueError:
        line()
        #If no audio is heard, prints that it couldn't hear anything
        print(f"{Fore.RED}I couldn't understand that.")
        return None
    #incase there was an error with the user's mic
    except sr.RequestError as e:
        line()
        print(f"{Fore.RED}Could not request results; {e}")
        return None

def main():
    bot_type = input("What type of bot would you like to speak to?\n")
    end_program = False
    recognizer = sr.Recognizer()
    #infinite loop until the user decides to exit
    while not end_program:
        #Imports the microphone as the audio source for 
        with sr.Microphone() as source:
            line()

            start = input(f"{Fore.GREEN}Type 'exit' to quit. Press enter to continue:\n").strip().lower()
            #If the user chooses to exit, break
            if start == "exit":
                end_program = True
                line()
                print(f"{Fore.BLUE}Goodbye!")
                break
            #Otherwise, it will:
            else:
                #Call the method from before that will recognize the audio and transcribe it
                user_input = get_speech_input(recognizer, source)
                if user_input:
                    #if the user says "bye" or "exit" anywhere in their speech, the program will end
                    if "bye" in user_input.lower() or "exit" in user_input.lower():
                        end_program = True
                        line()
                        print(f"{Fore.BLUE}Have a great day!")
                        #Otherwise, it will assign the model:
                    else:
                        #
                        system_data = [
                            #Tells the AI that it will be a code assistant
                            {"role": "system", "content": bot_type},
                            #Makes the AI respond to the user input variable from before
                            {"role": "user", "content": user_input}
                        ]
                        #Generates the AI's response
                        response = client.chat.completions.create(
                            #the AI's model
                            model="gpt-3.5-turbo",
                            messages=system_data
                        )
                        #Puts the response into a variable
                        assistant_response = response.choices[0].message.content
                        #Puts the previous chat into a dictionarry so that it can keep track of what was said previously in the conversation
                        system_data.append({"role": "assistant", "content": assistant_response})
                        line()
                        #Prints the AI's response
                        engine.say(assistant_response)
                        print(f"{Fore.MAGENTA}Assistant: {assistant_response}")
                else:
                    #If the user doesn't input anything, it will prompt them to leave or continue
                    leave = input(f"{Fore.YELLOW}If you would like to exit, please type 'exit'. Press Enter to continue:\n").strip().lower()
                    if leave == "exit":
                        end_program = True
                        line()
                        print(f"{Fore.GREEN}Goodbye!")
#Fucntion that draws a line for organization
def line():
    print(f"{Fore.WHITE}--------------------------------------------------------------------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()
