def shout(text):
    return text.upper()
def whisper(text):

    return text.lower()
def result(func):

    greeting=func("today is very good day")
    return greeting

print(result(shout))
print(result(whisper))
