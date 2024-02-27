import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()

    # Decrease the speed (a float value where 1.0 is the default speed)
    engine.setProperty('rate', 150)  # Adjust this value as needed

    print("Welcome to Robo Speaker 1.0.2 created by ArunDada")
    while True:
        x = input("Type here what you want to tell (or 'q' to quit): ")
        if x == "q":
            engine.say('bye my friend')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
