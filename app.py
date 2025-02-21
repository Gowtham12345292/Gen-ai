import streamlit as st 
import time
import google.generativeai as genai

# Animated text function with new color
def animated_text(text, speed=0.05):
    placeholder = st.empty()
    displayed_text = ""
    for letter in text:
        displayed_text += letter
        placeholder.markdown(f"""
            <h1 style="text-align:center; color: #007BFF;">✨ {displayed_text}</h1>
        """, unsafe_allow_html=True)
        time.sleep(speed)

# Display new animated text
animated_text("AI Code Doctor - Fix & Optimize!", speed=0.1)

# Configure Google Gemini API Key
genai.configure(api_key="AIzaSyBNuAnoR316s3mlaVY6zsgtmarKR4ZbajE")

# Custom Styling
st.markdown(
    """
    <style>
        body {background-color: #F0F8FF;}
        .title {text-align: center; color: #007BFF; font-size: 42px; font-weight: bold;}
        .subtitle {text-align: center; color: #333; font-size: 22px;}
        .container {
            background: white;
            padding: 20px; 
            border-radius: 12px; 
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .button {
            background-color: #007BFF;
            color: white; 
            font-size: 18px; 
            font-weight: bold; 
            border-radius: 10px; 
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App Title
st.title("🤖 AI-Powered Code Debugging & Optimization")

# Text Area for User Input (Buggy Code)
buggy_code = st.text_area("🐞 Paste Your Code Below:", height=200)

# Function to Debug Code Using Gemini AI
def debug_code_with_gemini(code):
    prompt = f"Debug the following code and provide the corrected version:\n\n{code}"
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ AI Error: Unable to generate response."

# Function to Generate Code Improvement Suggestions
def get_suggestions_with_gemini(code):
    prompt = f"Suggest improvements for the following code, focusing on best practices, efficiency, and readability:\n\n{code}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ No suggestions available."

# Analyze Button with new color scheme
if st.button("🚀 Fix & Improve Code", key="analyze_button"):
    if buggy_code:
        with st.spinner("🛠️ Debugging your code..."):
            fixed_code = debug_code_with_gemini(buggy_code)
        
        with st.spinner("🔍 Generating suggestions..."):
            suggestions = get_suggestions_with_gemini(fixed_code)
        
        # Display Fixed Code
        st.subheader("✅ Debugged Code:")
        st.code(fixed_code, language="python")
        
        # Copy Button for Fixed Code
        st.download_button(
            label="📥 Download Fixed Code",
            data=fixed_code,
            file_name="fixed_code.py",
            mime="text/plain",
            help="Click to save the corrected code."
        )
        
        # Display AI-Generated Suggestions
        st.subheader("💡 Code Improvement Suggestions:")
        st.write(suggestions)
    else:
        st.warning("⚠️ Please enter some code before generating fixes and suggestions!")
