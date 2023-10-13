import streamlit as st
import requests

# Define Hugging Face API endpoint and your API key
API_ENDPOINT = "https://api-inference.huggingface.co/models/facebook/m2m100_1.2B"
API_KEY = "x"  # Replace with your Hugging Face API key

# Define supported languages
LANGUAGES = {
    "Afrikaans": "af",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    # Add more languages as needed
}

st.title("AI Translator with Hugging Face API")
st.write("Translate text between different languages using the Hugging Face API.\n")

user_input = st.text_area("Input text", height=200, max_chars=5120)
source_lang = st.selectbox("Source language", options=list(LANGUAGES.keys()))
target_lang = st.selectbox("Target language", options=list(LANGUAGES.keys()))

if st.button("Run Translation"):
    st.spinner("Translating...")

    src_lang = LANGUAGES[source_lang]
    trg_lang = LANGUAGES[target_lang]

    payload = {
        "inputs": user_input,
        "source_language": src_lang,
        "target_language": trg_lang,
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        translated_text = response.json()["translation_text"]
        st.success("Translation Successful")
        st.write("Translated Text:")
        st.write(translated_text)
    except requests.exceptions.RequestException as e:
        st.error(f"Translation failed: {str(e)}")

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
