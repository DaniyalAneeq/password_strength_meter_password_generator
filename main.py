import streamlit as st
import random
import string
import re
# import pyperclip  # type: ignore

st.set_page_config(page_title="PASSWORD STRENGTH METER", page_icon="🔒")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #597C9A; 
        color: #ffffff
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Target the sidebar */
    [data-testid="stSidebar"] {
        background-color: #393C44;  /* Semi-transparent white */
        backdrop-filter: blur(10px);                 /* Blur effect */
        border-right: 1px solid rgba(255, 255, 255, 0.1);  /* Light border */
    }
    /* Style sidebar headers */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6 {
        color: white;               /* White text for headers */
    }
    /* Style sidebar text */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] a {
        color: white;               /* White text for paragraphs, labels, and links */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.title("🛠️ My Recent Class Projects")
st.sidebar.markdown("""
                    - [Data Sweeper](https://sweep-data.streamlit.app/)
                    - [Unit Converter](https://4unitconverter.streamlit.app/)
                    """)

st.sidebar.markdown("""
                    let's get connected with me on LinkedIn
                    [LinkedIn](https://www.linkedin.com/in/daniyal-aneeq-ahmed-3868452b7/)
                    """)

st.title("🔑 Password Strength Meter & Generator")

st.markdown("""
            This application helps you:
- Check the strength of your password.
- Generate a strong and secure password.
            """)

st.header("🔍 Check Your Password Strength")

password = st.text_input("Enter your password", type="password" )



def evaluate_password_strength(password):
    feedback = []  # List to store feedback messages
    score = 0  # Variable to store the password strength score

    # Check password length
    if len(password) >= 12:
        score += 2  # Stronger score for longer passwords
    elif len(password) >= 8:
        score += 1  # Moderate score for shorter passwords
    else:
        feedback.append("❌ Password should be at least 8 characters long (12+ recommended).")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`-]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (e.g., !@#$%^&*).")

    # Provide feedback based on the score
    if score >= 5:
        feedback.append("✅ Your password is strong!")
    elif score >= 3:
        feedback.append("👍 Your password is medium strength. It could be stronger.")
    else:
        feedback.append("🛑 Your password is weak. Please make it stronger!")

    return score, feedback

# Display password strength feedback
if password:
    score, feedback = evaluate_password_strength(password)
    st.progress(score / 5)  # Show a progress bar based on the score
    st.markdown("### Password Strength Feedback")
    for tip in feedback:
        st.write(tip)  # Display each feedback message
else:
    st.info("Please enter your password to check its strength.")


st.write("")  # Adds one line of space
st.write("")  # Adds another line of space
st.write("")  # Adds another line of space
st.write("")  # Adds another line of space

# Password Generator Section
st.header("🔧 Generate a Strong Password")

# Add a slider to select password length
length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)

# Add checkboxes for including digits and special characters
use_digits = st.checkbox("Include Digits", value=True)
use_special = st.checkbox("Include Special Characters", value=True)

st.markdown(
    """
    <style>
    /* Target the "Generate Password" button */
    div.stButton > button:first-child {
        background-color: #4CAF50;  /* Green background */
        color: white;               /* White text */
        font-weight: bold;          /* Bold text */
        border-radius: 10px;        /* Rounded corners */
        border: none;               /* Remove border */
        padding: 10px 24px;         /* Add padding */
    }
    /* Hover effect */
    div.stButton > button:first-child:hover {
        background-color: #45a049;  /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)




# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include uppercase and lowercase letters
    if use_digits:
        characters += string.digits  # Add digits if the checkbox is selected
    if use_special:
        characters += string.punctuation  # Add special characters if the checkbox is selected
    return ''.join(random.choice(characters) for _ in range(length))  # Generate a random password

# Button to generate a password
if st.button("Generate Password"):
    generated_password = generate_password(length, use_digits, use_special)
    st.success("Password generated successfully!")
    st.code(generated_password)  # Display the generated password in a code block

    # Button to copy the password to the clipboard
    # if st.button("Copy to Clipboard"):
    #     try:
    #         pyperclip.copy(generated_password)  # Copy the password to the clipboard
    #         st.info("Password copied to clipboard!")
    #     except ImportError:
    #         st.error("Please install the 'pyperclip' module to use this feature. Run: `pip install pyperclip`")

# Button to regenerate a new password
if st.button("Regenerate Password"):
    generated_password = generate_password(length, use_digits, use_special)
    st.success("New password generated successfully!")
    st.code(generated_password)
