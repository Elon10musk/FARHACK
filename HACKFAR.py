import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load the model and tokenizer
model_name = "facebook/nllb-200-distilled-600M"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a translation pipeline
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="hin_Deva", tgt_lang='eng_Latn', max_length=400)

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
