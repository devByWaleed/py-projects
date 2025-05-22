from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

text = "Merhaba"

language = detect(text)

print(language)