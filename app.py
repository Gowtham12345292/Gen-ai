import streamlit as st
import time
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyBNuAnoR316s3mlaVY6zsgtmarKR4ZbajE")

# Custom Styling
st.markdown(
    """
    <style>
        body {background-color: #f4f4f4;}
        .title {text-align: center; color: #FF4500; font-size: 40px; font-weight: bold;}
        .subtitle {text-align: center; color: #333; font-size: 20px;}
        .container {background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);}
        .button {background-color: #FF4500; color: white; font-size: 18px; font-weight: bold; border-radius: 8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Animated Header Function
def animated_text(text, speed=0.05):
    placeholder = st.empty()
    displayed_text = ""
    for letter in text:
        displayed_text += letter
        placeholder.markdown(f"""
            <h1 class='title'>{displayed_text} 🚀</h1>
        """, unsafe_allow_html=True)
        time.sleep(speed)

# Display Animated Header
animated_text("Welcome to GenAI App - AI Code Reviewer!", speed=0.1)

# App Layout
st.markdown("<h2 class='subtitle'>🤖 AI-Powered Code Debugging</h2>", unsafe_allow_html=True)
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Text Area for User Input (Buggy Code)
buggy_code = st.text_area("🐞 Enter your buggy code:", height=200)

# Function to Debug Code Using Gemini AI
def debug_code_with_gemini(code):
    prompt = f"Debug the following code and provide the corrected version:\n\n{code}"
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ Error in AI response."

# Function to Generate Code Improvement Suggestions
def get_suggestions_with_gemini(code):
    prompt = f"Suggest improvements for the following code, focusing on best practices, performance optimization, and readability:\n\n{code}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ No suggestions available."

# Process Code When Input is Given
if buggy_code:
    with st.spinner("🛠️ Debugging your code..."):
        fixed_code = debug_code_with_gemini(buggy_code)
    
    with st.spinner("🔍 Generating suggestions..."):
        suggestions = get_suggestions_with_gemini(fixed_code)
    
    # Display Fixed Code
    st.subheader("✅ Fixed Code:")
    st.code(fixed_code, language="python")
    
    # Copy Button for Fixed Code
    st.download_button(
        label="📋 Copy Fixed Code",
        data=fixed_code,
        file_name="fixed_code.py",
        mime="text/plain",
        help="Download the corrected code"
    )
    
    # Display AI-Generated Suggestions
    st.subheader("💡 Suggestions for Improvement:")
    st.write(suggestions)

# Close the Container Div
st.markdown("</div>", unsafe_allow_html=True)

