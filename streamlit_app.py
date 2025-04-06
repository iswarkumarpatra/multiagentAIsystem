import streamlit as st
import requests

# FastAPI Backend URLs
API_URL = "http://127.0.0.1:8000/recommend"
AI_CHAT_URL = "http://127.0.0.1:8000/ask_ai"
PRODUCT_CHAT_URL = "http://127.0.0.1:8000/ask_product"

# Page Configuration
st.set_page_config(
    page_title="AI E-Commerce Recommender",
    page_icon="🛒",
    layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
        .stTextInput, .stButton {
            text-align: center;
        }
        .recommend-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #f4f4f4;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🛒 AI-Powered E-Commerce Recommendation System")
st.markdown("💡 Get personalized product suggestions instantly!")

# User Input Section
user_id = st.text_input("🔹 Enter your User ID:", "", help="Your unique user ID for personalized recommendations.")

if st.button("✨ Get Recommendations"):
    if user_id:
        with st.spinner("🔍 Fetching recommendations..."):
            try:
                response = requests.get(f"{API_URL}/{user_id}")

                if response.status_code == 200:
                    data = response.json()
                    recommendations = data.get("recommendations", "")

                    # Ensure recommendations are in list format
                    if isinstance(recommendations, str):
                        recommendations = recommendations.split("\n")  

                    if recommendations:
                        st.subheader("🛍️ Recommended Products for You:")
                        st.markdown("Here are some handpicked recommendations based on your interests:")

                        for item in recommendations:
                            if item.strip():
                                st.markdown(f"✅ **{item.strip()}**")

                    else:
                        st.warning("😕 No recommendations found. Try again later!")

                else:
                    st.error(f"❌ Failed to fetch recommendations: {response.status_code}")

            except Exception as e:
                st.error(f"🚨 Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid User ID!")

# Live Chat with AI
st.subheader("💬 Chat with AI for Personalized Suggestions")
user_query = st.text_input("💡 Ask AI for specific product suggestions:", help="Example: 'What are the best smartphones under $500?'")

if st.button("🤖 Ask AI"):
    if user_id and user_query:
        with st.spinner("🤖 Thinking..."):
            try:
                response = requests.post(AI_CHAT_URL, json={"user_id": user_id, "query": user_query})

                if response.status_code == 200:
                    ai_response = response.json().get("response", "No response from AI.")
                    st.success(f"🧠 AI Suggestion: **{ai_response}**")
                else:
                    st.error(f"❌ AI request failed! Status Code: {response.status_code}")

            except Exception as e:
                st.error(f"🚨 Error: {e}")
    else:
        st.warning("⚠️ Please enter your User ID and a query!")

# AI Chat for Specific Product Information
st.subheader("🔍 Ask AI About a Specific Product")
product_query = st.text_input("💡 Ask about a product:", help="Example: 'Is this laptop good for gaming?'")
product_choice = st.radio("🔎 Search by:", ["Product ID", "Product Name"])

if product_choice == "Product ID":
    product_id = st.text_input("Enter Product ID:")
    product_name = None
else:
    product_id = None
    product_name = st.text_input("Enter Product Name:")

if st.button("🔍 Get Product Info"):
    if (product_id or product_name) and product_query:
        with st.spinner("🤖 AI is thinking..."):
            try:
                response = requests.post(PRODUCT_CHAT_URL, json={"product_id": product_id, "product_name": product_name, "query": product_query})

                if response.status_code == 200:
                    ai_response = response.json().get("response", "No response from AI.")
                    st.success(f"🧠 AI: **{ai_response}**")
                else:
                    st.error(f"❌ Failed! Status Code: {response.status_code}")

            except Exception as e:
                st.error(f"🚨 Error: {e}")
    else:
        st.warning("⚠️ Please enter product details and a question!")
