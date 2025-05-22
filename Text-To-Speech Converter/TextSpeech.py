from text_to_speech import save

text = input("Enter the text:-\n")
# text = """Hello World and welcome to programming. 
# This is python, an easy syntax programming language ever.
# """

# Specify the language (IETF language tag)
language = "en"

# Specify the output file (only accepts .mp3)
output_file = "text.mp3"

# Saving The File
save(text, language, file=output_file)