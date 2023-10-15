# import streamlit as st
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# # Load the model and tokenizer
# model_name = "facebook/nllb-200-distilled-600M"
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# # Create a translation pipeline
# translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="hin_Deva", tgt_lang='eng_Latn', max_length=400)

# # Streamlit UI
# st.title("Language Translator")

# # Input text box
# input_text = st.text_area("Enter text to translate")

# # Language selection
# src_lang = st.selectbox("Select source language", ["Hindi", "English", "French"])  # Add more languages as needed
# tgt_lang = st.selectbox("Select target language", ["English", "Hindi", "French"])  # Add more languages as needed

# # Translation button
# if st.button("Translate"):
#     if input_text:
#         # Language code mapping
#         language_codes = {
#             "Hindi": "hin_Deva",
#             "English": "eng_Latn",
#             "French": "fra_Latn",
#         }

#         src_lang_code = language_codes[src_lang]
#         tgt_lang_code = language_codes[tgt_lang]

#         # Perform translation
#         translated_text = translator(input_text, src_lang=src_lang_code, tgt_lang=tgt_lang_code)[0]["translation_text"]
#         st.write("Translated Text:")
#         st.write(translated_text)

# # About section
# st.sidebar.title("About")
# st.sidebar.info(
#     "This is a language translation app using the Hugging Face Transformers library. "
#     "Select the source and target languages, then enter the text to translate."
# )

import streamlit as st
import os
import time
import glob
import os


from gtts import gTTS
from googletrans import Translator

st.set_page_config(page_title="EC_HACKATHON-2023")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: rgb(121, 37, 199);">
  <div class="container-fluid">
    <a class="navbar-brand" href="#"><img 
      src= 
"https://media.istockphoto.com/id/1202558173/vector/translate-science-gradient-color-paper-cut-style-icon-design.jpg?s=612x612&w=0&k=20&c=55DCFw9pCp5HW0--tqo_wjaxKoh1FKLo9hY4OJzcv-A=" 
      alt="" width="50" 
      height="45"></a></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#">Contact Us</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">GitHub</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About Project</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)
st.title("Translation Bot")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
            .st-emotion-cache-cio0dv {
            padding-left: 20%;
            padding-right: 1rem;
            }
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

LANGUAGES = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese (simplified)': 'zh-cn',
    'chinese (traditional)': 'zh-tw',
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'iw',
    'hebrew': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar (burmese)': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu',
}


try:
    os.mkdir("temp")
except:
    pass
translator = Translator()

text = st.text_input("Enter text")

# Create a list of language names from the LANGUAGES dictionary
language_names = list(LANGUAGES.keys())

in_lang = st.selectbox(
    "Select your input language",
    language_names
)

# Use the selected language name to get the language code from the LANGUAGES dictionary
input_language = LANGUAGES.get(in_lang, "en")  # Default to English if not found

out_lang = st.selectbox(
    "Select your output language",
    language_names
)

# Use the selected language name to get the language code from the LANGUAGES dictionary
output_language = LANGUAGES.get(out_lang, "en")  # Default to English if not found


english_accent = st.selectbox(
    "Select your english accent",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

if english_accent == "Default":
    tld = "co.in"
elif english_accent == "India":
    tld = "co.in"

elif english_accent == "United Kingdom":
    tld = "co.uk"
elif english_accent == "United States":
    tld = "com"
elif english_accent == "Canada":
    tld = "ca"
elif english_accent == "Australia":
    tld = "com.au"
elif english_accent == "Ireland":
    tld = "ie"
elif english_accent == "South Africa":
    tld = "co.za"


def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


display_output_text = st.checkbox("Display output text")

if st.button("convert"):
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown(f"## Output text:")
        st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
