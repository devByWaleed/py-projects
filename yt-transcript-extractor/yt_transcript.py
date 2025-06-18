# PIP cmds

# pip install youtube-transcript-api
# pip install googletrans==4.0.0-rc1
# pip install deep-translator




# Importing Library

# from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def id_extractor(video_url):

    # For yt shorts url (if copied from shared button) 
    if 'feature' in video_url and 'shorts' in video_url:
        url_detail = video_url.split('/')
        
        url_detail = url_detail[-1].split('?')
        
        video_id = url_detail[0]
        

    # For yt shorts url (if copied browser search bar) 
    elif 'shorts' in video_url:
        url_detail = video_url.split('/')

        video_id = url_detail[-1]


    # For yt video url (if copied from shared button) 
    elif 'feature' in video_url:
        url_detail = video_url.split('/')
        
        url_detail = url_detail[-1].split('?')
        
        video_id = url_detail[0]
        

    # For yt video url (if copied browser search bar) 
    else:
        url_detail = video_url.split('=')

        video_id = url_detail[-1]
    
    # Returning final id
    return video_id


id = id_extractor("https://www.youtube.com/shorts/tA59GVOU4gU")


# Hindi Transcript (Video) URL → search bar
# print(id_extractor("https://www.youtube.com/watch?v=vzgG7gfveCM"))

# # English Transcript (Video) URL → search bar
# print(id_extractor("https://www.youtube.com/watch?v=I9KJRXjqKAI"))

# # English Transcript (Shorts) URL → search bar
# print(id_extractor("https://www.youtube.com/shorts/tA59GVOU4gU"))

# # Hindi Transcript (Shorts) URL → search bar
# print(id_extractor("https://www.youtube.com/shorts/7CJh8Z5dewY"))

# # (Video) URL → copied from shared button
# print(id_extractor("https://youtu.be/I9KJRXjqKAI?feature=shared"))

# # (Shorts) URL → copied from shared button
# print(id_extractor("https://youtube.com/shorts/tA59GVOU4gU?feature=shared"))



# function for formatting the time of video
def format_timestamp(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))


# function for fetching the transcript
# def fetch_transcript():

#     transcript_obj = {}
#     try:
#         # transcript is an array of object
#         transcript = YouTubeTranscriptApi.get_transcript(id, languages=['en', 'hi'])
        
#         # print(transcript)
#         for entry in transcript:
#             transcript_obj.update({format_timestamp(entry['start']): entry['text']})
#             print(f"{format_timestamp(entry['start'])} → {entry['text']}")

#         return transcript_obj
    
#     # Handling Error
#     except Exception as e:
#         return f"An error occurred:-\n\n{e}"


# fetch_transcript()

# from googletrans import Translator
from deep_translator import GoogleTranslator
import time


# transcript_obj = {
#     "00:00:00" : "why was Saudi Arabia never colonized",
#     "00:00:02" : "Saudi Arabia is one of the few",
#     "00:00:04" : "territories that was never colonized for",
#     "00:00:09" : "the Ottoman Empire controlled the",
#     "00:00:11" : "coastal regions of Arabia and no other",
#     "00:00:13" : "Colonial Powers wanted to battle for it",
#     "00:00:16" : "the second reason is that the Suz Canal",
#     "00:00:18" : "did not yet exist which made the Red Sea",
#     "00:00:21" : "much less important another reason is",
#     "00:00:23" : "that oil was not yet discovered or",
#     "00:00:26" : "useful which made Saudi Arabia seem",
#     "00:00:28" : "absolutely useless to control as it is",
#     "00:00:31" : "mostly desert",
# }

# #  Logic For Translating the transcript

# translated_text = {}

# language = input("""Enter the language you want to convert the transcript:-

# 1 for English
# 2 for Urdu
# 3 for Turkish  
    
# Enter Your choice:  """)

# if language == '1':
#     language = 'en'

# elif language == '2':
#     language = 'ur'

# elif language == '3':
#     language = 'tr'

# # for key, text in fetch_transcript().items:
# for key, text in transcript_obj.items():


#     try:
#         time.sleep(1.5)  # Small delay to avoid getting blocked
#         translated = GoogleTranslator(source='auto', target=language).translate(text)
#         translated_text.update({key: translated})
#         time.sleep(1.5)  # Small delay to avoid getting blocked
    
#     except Exception as e:
#         print(f"An error occurred:-\n\n{e}")



# print(f"******** {language} Translation:-\n\n")

# for key, value in translated_text.items():
#     print(f"{key} → {value}")



text = 'why was Saudi Arabia never colonized'

# translated = GoogleTranslator(source="auto", target='en').translate(text=text)
translated = GoogleTranslator(source="auto", target='ur').translate(text)

google = 'سعودی عرب کبھی استعمار کیوں نہیں ہوا؟'
print(f"""From deep_translator: {translated}
From Google On Browser: {google}
""")




'''
searched_obj = {}

search_for = input("Enter what you want to search: ")

for key, value in fetch_transcript().items():

    if search_for in value:
        searched_obj.update({key: value})
    
for key, value in searched_obj.items():
        print(f"{key} → {value}")

'''










    