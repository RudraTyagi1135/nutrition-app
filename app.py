import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Gemini API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])





# Function to get Gemini response
def get_gemini_response(input_prompt, image, user_input):

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    response = model.generate_content(
        [input_prompt, image[0], user_input]
    )

    return response.text


# Function to process uploaded image
def input_image_setup(uploaded_file):

    if uploaded_file is not None:

        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]

        return image_parts

    else:
        return None


# Nutrition prompt
input_prompt = """
You are an expert nutritionist.

Analyze the food items from the image and provide:

1. Food item names
2. Estimated calories for each item
3. Protein, carbohydrates, and fats (approximate)
4. Total calories of the meal
5. Brief health suggestion

Format:

1. Item Name
   - Calories:
   - Protein:
   - Carbohydrates:
   - Fats:

2. Item Name
   - Calories:
   - Protein:
   - Carbohydrates:
   - Fats:

------------------------
Total Calories:
Health Suggestion:
"""


# Streamlit page config
st.set_page_config(
    page_title="AI Nutritionist App",
    page_icon="🍎",
    layout="centered"
)

# App title
st.title("🍎 AI Nutritionist App")

st.write("Upload a food image and get nutrition analysis using Gemini AI.")


# User input
user_input = st.text_input(
    "Additional Prompt (Optional)",
    placeholder="Example: Is this meal good for weight loss?"
)

# File uploader
uploaded_file = st.file_uploader(
    "Choose a food image...",
    type=["jpg", "jpeg", "png"]
)

# Display uploaded image
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_column_width=True
    )


# Submit button
submit = st.button("Analyze Nutrition")


# Main logic
if submit:

    if uploaded_file is None:

        st.error("Please upload an image first.")

    else:

        with st.spinner("Analyzing image..."):

            try:

                image_data = input_image_setup(uploaded_file)

                response = get_gemini_response(
                    input_prompt,
                    image_data,
                    user_input
                )

                st.subheader("Nutrition Analysis")

                st.write(response)

            except Exception as e:

                st.error(f"Error: {str(e)}")
