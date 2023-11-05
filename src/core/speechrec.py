import speech_recognition as sr
import enum
class Recognizer(enum.Enum):
    bing            =       1,
    google          =       2,
    google_cloud    =       3,
    houndify        =       4,
    ibm             =       5,
    sphinx          =       6,
    wit             =       7

def recognize(recognizer, recognizer_type, audio, language):

    query = None
    if recognizer_type==Recognizer.bing:
        query = recognizer.recognize_bing(audio, language)

    elif recognizer_type==Recognizer.google:
        query = recognizer.recognize_google(audio, language)

    elif recognizer_type==Recognizer.google_cloud:
        query = recognizer.recognize_google_cloud(audio, language)

    elif recognizer_type==Recognizer.houndify:
        query = recognizer.recognize_houndify(audio, language)

    elif recognizer_type==Recognizer.ibm:
        query = recognizer.recognize_ibm(audio, language)

    elif recognizer_type==Recognizer.sphinx:
        query = recognizer.recognize_sphinx(audio, language)

    elif recognizer_type==Recognizer.wit:
        query = recognizer.recognize_wit(audio, language)

    return query

def generateTextFromSpeech(recognizer_type=Recognizer.google):
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-uk')#recognize(r, recognizer_type, audio, language='en-uk')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

