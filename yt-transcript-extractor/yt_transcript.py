# PIP Commands (Ensure these are installed)
# pip install youtube-transcript-api
# pip install googletrans==4.0.0-rc1
# pip install deep-translator


# Importing Libraries
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator
import time


# ========== Function: Extract Video ID ==========
def id_extractor(video_url):
    if 'feature' in video_url and 'shorts' in video_url:
        video_id = video_url.split('/')[-1].split('?')[0]
    
    elif 'shorts' in video_url:
        video_id = video_url.split('/')[-1]
    
    elif 'feature' in video_url:
        video_id = video_url.split('/')[-1].split('?')[0]
    
    else:
        video_id = video_url.split('=')[-1]
    
    return video_id


# ========== Function: Format Timestamp ==========
def format_timestamp(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))


# ========== Function: Fetch Transcript ==========
def fetch_transcript():
    transcript_obj = {}
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id, languages=['en', 'hi'])

        for entry in transcript:
            print(f"{format_timestamp(entry['start'])}  :   {entry['text']}")
            transcript_obj.update({format_timestamp(entry['start']): entry['text']})

        return transcript_obj

    except Exception as e:
        return f"An error occurred:-\n\n{e}"


# ========== Function: Translate a Single Text ==========
def translate(text):
    try:
        translated = GoogleTranslator(source='auto', target=language).translate(text=text)
        time.sleep(2.0)     # Delay so that the translation process runs smoothly 
        return translated
    
    except:
        return "An error occurred!!!"


# ========== Input Video URL ==========
video_url = "https://www.youtube.com/shorts/tA59GVOU4gU"
id = id_extractor(video_url)


# ========== Fetch & Print Transcript ==========
fetched = fetch_transcript()


# ========== Choose Language AFTER printing transcript ==========
translated_text = {}

language = input("""\n\nEnter the language you want to convert the transcript to:

1 for English
2 for Urdu
3 for Turkish  

Enter Your choice:  """)

if language == '1':
    language = 'en'
elif language == '2':
    language = 'ur'
elif language == '3':
    language = 'tr'
else:
    print("Invalid language input! Defaulting to English.")
    language = 'en'


# ========== Translate Transcript ==========
for key, text in fetched.items():
    translated_text[key] = translate(text)


# ========== Display Translated Output ==========
print(f"\n******** {language.upper()} Translation ********\n")
for key, value in translated_text.items():
    print(f"{key} → {value}")


# ========== SEARCH FEATURE (Commented) ==========
'''
searched_obj = {}

search_for = input("Enter what you want to search: ")

for key, value in fetch_transcript().items():
    if search_for.lower() in value.lower():
        searched_obj.update({key: value})

for key, value in searched_obj.items():
    print(f"{key} → {value}")
'''


# ========== TRANSLATION COMPARISON TEST (Commented) ==========
'''
text = 'why was Saudi Arabia never colonized'

# translated = GoogleTranslator(source="auto", target='en').translate(text=text)
translated = GoogleTranslator(source="auto", target='ur').translate(text)

google = 'سعودی عرب کبھی استعمار کیوں نہیں ہوا؟'
print(f"""From deep_translator: {translated}
From Google On Browser: {google}
""")
'''


# ========== MANUAL TEST CASES FOR ID (Commented) ==========
'''
# Hindi Transcript (Video) URL → search bar
print(id_extractor("https://www.youtube.com/watch?v=vzgG7gfveCM"))

# English Transcript (Video) URL → search bar
print(id_extractor("https://www.youtube.com/watch?v=I9KJRXjqKAI"))

# English Transcript (Shorts) URL → search bar
print(id_extractor("https://www.youtube.com/shorts/tA59GVOU4gU"))

# Hindi Transcript (Shorts) URL → search bar
print(id_extractor("https://www.youtube.com/shorts/7CJh8Z5dewY"))

# (Video) URL → copied from shared button
print(id_extractor("https://youtu.be/I9KJRXjqKAI?feature=shared"))

# (Shorts) URL → copied from shared button
print(id_extractor("https://youtube.com/shorts/tA59GVOU4gU?feature=shared"))
'''
