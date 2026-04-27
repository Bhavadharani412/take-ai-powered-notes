import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# --------------------------------
# Load ENV
# --------------------------------
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="AI Notes Generator",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------
# Title
# --------------------------------
st.title("🧠 AI Course Notes Generator")
st.caption("Paste transcript / long text and get clear notes")

# --------------------------------
# Text Input
# --------------------------------
text_input = st.text_area(
    "Paste Transcript / Text Here",
    height=350,
    placeholder="Paste any transcript..."
)

# --------------------------------
# Chunking Function
# --------------------------------
def split_text(text, chunk_size=5000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# --------------------------------
# AI Notes Generation
# --------------------------------
def generate_notes(chunk):

    prompt = f"""
Turn transcript into elite study notes.

Output Format:

# Title

## Main Concepts
## Explained Clearly
## Key Terms
## Examples
## Revision Summary
## Possible Interview Questions

Use clean markdown.
Simple language.
No fluff.

Transcript:
{chunk}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

# --------------------------------
# Main Button
# --------------------------------
if st.button("Generate Notes"):

    if not text_input.strip():
        st.warning("Paste some text first.")
        st.stop()

    with st.spinner("Generating notes..."):

        chunks = split_text(text_input)

        final_notes = ""

        for i, chunk in enumerate(chunks):
            st.write(f"Processing Part {i+1}/{len(chunks)}...")
            notes = generate_notes(chunk)
            final_notes += notes + "\n\n"

    st.success("Done!")

    st.subheader("📘 Notes Output")
    st.markdown(final_notes)

    st.download_button(
        "Download Notes",
        final_notes,
        file_name="course_notes.txt"
    )