import sqlite3
import ollama
from fastapi import FastAPI, HTTPException

# Initialize FastAPI app
app = FastAPI()

# Function to fetch customer data from SQLite
def get_customer_data(customer_id):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT Browsing_History, Purchase_History FROM customers WHERE Customer_ID = ?", (customer_id,))
        user_data = cursor.fetchone()
    finally:
        conn.close()

    if user_data is None:
        return None
    
    browsing_history, purchase_history = user_data
    return {"browsing_history": browsing_history, "purchase_history": purchase_history}

# Function to fetch product details from SQLite (Fixed version)
def get_product_data(product_id=None, product_name=None):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    try:
        if product_id:
            cursor.execute("SELECT * FROM products WHERE Product_ID = ?", (product_id,))
        elif product_name:
            cursor.execute("SELECT * FROM products WHERE Subcategory = ?", (product_name,))
        else:
            return None

        product_data = cursor.fetchone()
        if product_data is None:
            return None

        # Fetch column names dynamically to match the database schema
        column_names = [desc[0] for desc in cursor.description]

        # Convert fetched data into a dictionary
        product_dict = dict(zip(column_names, product_data))

    finally:
        conn.close()

    return product_dict

# Function to fetch product recommendations using LLM
def get_recommendations(user_id):
    user_data = get_customer_data(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    
    browsing_history = user_data["browsing_history"]
    purchase_history = user_data["purchase_history"]
    
    prompt = f"""
    Based on this customer's browsing history: {browsing_history}
    and purchase history: {purchase_history},
    suggest 3 personalized products from this category.
    """

    try:
        response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
        recommendations = response.get("message", {}).get("content", "No recommendations available.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

    return {"recommendations": recommendations}

# FastAPI endpoint to get recommendations
@app.get("/recommend/{user_id}")
def recommend(user_id: str):
    return get_recommendations(user_id)

# AI Chat API for personalized product queries
@app.post("/ask_ai")
def ask_ai(data: dict):
    user_id = data.get("user_id")
    query = data.get("query")

    if not user_id or not query:
        raise HTTPException(status_code=400, detail="User ID and query are required!")

    user_data = get_customer_data(user_id)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    browsing_history = user_data["browsing_history"]
    purchase_history = user_data["purchase_history"]

    ai_prompt = f"""
    User Query: {query}
    User Browsing History: {browsing_history}
    User Purchase History: {purchase_history}

    Provide a detailed AI response tailored to the user's interests.
    """

    try:
        ai_response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": ai_prompt}])
        response_text = ai_response.get("message", {}).get("content", "No response from AI.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

    return {"response": response_text}

# API: Ask AI about a specific product
@app.post("/ask_product")
def ask_product(data: dict):
    product_id = data.get("product_id")
    product_name = data.get("product_name")
    query = data.get("query")

    if not query or (not product_id and not product_name):
        raise HTTPException(status_code=400, detail="Product ID or Name and a query are required!")

    product_data = get_product_data(product_id, product_name)
    if not product_data:
        raise HTTPException(status_code=404, detail="Product not found")

    ai_prompt = f"""
    User Query: {query}
    
    Product Details:
    - Name: {product_data.get('Subcategory', 'Unknown')}
    - Category: {product_data.get('Category', 'Unknown')}
    - Price: ${product_data.get('Price', 'N/A')}
    - Brand: {product_data.get('Brand', 'Unknown')}
    - Rating: {product_data.get('Product_Rating', 'N/A')}⭐
    - Availability: {product_data.get('Holiday', 'Unknown')}
    - Season: {product_data.get('Season', 'Unknown')}
    - Location: {product_data.get('Location', 'Unknown')}
    - Similar Products: {product_data.get('Similar_Products', 'None')}
    
    Provide an AI-generated detailed response about this product.
    """

    try:
        ai_response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": ai_prompt}])
        response_text = ai_response.get("message", {}).get("content", "No response from AI.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")

    return {"response": response_text}
