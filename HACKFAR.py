import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load the model and tokenizer
model_name = "facebook/nllb-200-distilled-600M"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a translation pipeline
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="hin_Deva", tgt_lang='eng_Latn', max_length=400)

# Streamlit UI
st.title("Language Translator")

# Input text box
input_text = st.text_area("Enter text to translate")

# Language selection
src_lang = st.selectbox("Select source language", ["Hindi", "English", "French"])  # Add more languages as needed
tgt_lang = st.selectbox("Select target language", ["English", "Hindi", "French"])  # Add more languages as needed

# Translation button
if st.button("Translate"):
    if input_text:
        # Language code mapping
        language_codes = {
            "Hindi": "hin_Deva",
            "English": "eng_Latn",
            "French": "fra_Latn",
        }

        src_lang_code = language_codes[src_lang]
        tgt_lang_code = language_codes[tgt_lang]

        # Perform translation
        translated_text = translator(input_text, src_lang=src_lang_code, tgt_lang=tgt_lang_code)[0]["translation_text"]
        st.write("Translated Text:")
        st.write(translated_text)

# About section
st.sidebar.title("About")
st.sidebar.info(
    "This is a language translation app using the Hugging Face Transformers library. "
    "Select the source and target languages, then enter the text to translate."
)

# import streamlit as st
# import os
# import time
# import glob
# import os


# from gtts import gTTS
# from googletrans import Translator

# try:
#     os.mkdir("temp")
# except:
#     pass
# st.title("Text to speech")
# translator = Translator()

# text = st.text_input("Enter text")
# in_lang = st.selectbox(
#     "Select your input language",
#     ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
# )
# if in_lang == "English":
#     input_language = "en"
# elif in_lang == "Hindi":
#     input_language = "hi"
# elif in_lang == "Bengali":
#     input_language = "bn"
# elif in_lang == "korean":
#     input_language = "ko"
# elif in_lang == "Chinese":
#     input_language = "zh-cn"
# elif in_lang == "Japanese":
#     input_language = "ja"

# out_lang = st.selectbox(
#     "Select your output language",
#     ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
# )
# if out_lang == "English":
#     output_language = "en"
# elif out_lang == "Hindi":
#     output_language = "hi"
# elif out_lang == "Bengali":
#     output_language = "bn"
# elif out_lang == "korean":
#     output_language = "ko"
# elif out_lang == "Chinese":
#     output_language = "zh-cn"
# elif out_lang == "Japanese":
#     output_language = "ja"

# english_accent = st.selectbox(
#     "Select your english accent",
#     (
#         "Default",
#         "India",
#         "United Kingdom",
#         "United States",
#         "Canada",
#         "Australia",
#         "Ireland",
#         "South Africa",
#     ),
# )

# if english_accent == "Default":
#     tld = "com"
# elif english_accent == "India":
#     tld = "co.in"

# elif english_accent == "United Kingdom":
#     tld = "co.uk"
# elif english_accent == "United States":
#     tld = "com"
# elif english_accent == "Canada":
#     tld = "ca"
# elif english_accent == "Australia":
#     tld = "com.au"
# elif english_accent == "Ireland":
#     tld = "ie"
# elif english_accent == "South Africa":
#     tld = "co.za"


# def text_to_speech(input_language, output_language, text, tld):
#     translation = translator.translate(text, src=input_language, dest=output_language)
#     trans_text = translation.text
#     tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
#     try:
#         my_file_name = text[0:20]
#     except:
#         my_file_name = "audio"
#     tts.save(f"temp/{my_file_name}.mp3")
#     return my_file_name, trans_text


# display_output_text = st.checkbox("Display output text")

# if st.button("convert"):
#     result, output_text = text_to_speech(input_language, output_language, text, tld)
#     audio_file = open(f"temp/{result}.mp3", "rb")
#     audio_bytes = audio_file.read()
#     st.markdown(f"## Your audio:")
#     st.audio(audio_bytes, format="audio/mp3", start_time=0)

#     if display_output_text:
#         st.markdown(f"## Output text:")
#         st.write(f" {output_text}")


# def remove_files(n):
#     mp3_files = glob.glob("temp/*mp3")
#     if len(mp3_files) != 0:
#         now = time.time()
#         n_days = n * 86400
#         for f in mp3_files:
#             if os.stat(f).st_mtime < now - n_days:
#                 os.remove(f)
#                 print("Deleted ", f)


# remove_files(7)
