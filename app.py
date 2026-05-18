import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION & STYLING ---
st.set_page_config(page_title="FarmFresh Direct", page_icon="🥗", layout="wide")

# Custom CSS for clean UI and accessibility
st.markdown("""
    <style>
    .main { background-color: #f9fbf9; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 8px; }
    .stButton>button:hover { background-color: #1b5e20; color: white; }
    .health-tip { padding: 15px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; border-radius: 4px; margin-bottom: 20px; }
    .delivery-box { padding: 15px; background-color: #efebe9; border-left: 5px solid #5d4037; border-radius: 4px; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALISATION ---
# Keeps track of the shopping cart across page reruns
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- MOCK DATA: FARM PRODUCE ---
# Inventory optimized for healthy eating metrics
PRODUCE_DATA = {
    "Vegetables": [
        {"name": "Organic Spinach", "price": 25.00, "unit": "per 250g bunch", "health_benefit": "Rich in Iron & Vitamins A/C. Boosts energy levels.", "category": "Greens"},
        {"name": "Vine-Ripened Tomatoes", "price": 30.00, "unit": "per kg", "health_benefit": "High in Lycopene, an antioxidant that protects heart health.", "category": "Cruciferous"},
        {"name": "Fresh Broccoli florets", "price": 35.00, "unit": "per 500g", "health_benefit": "Packed with fiber and Vitamin C to support strong immunity.", "category": "Cruciferous"},
        {"name": "Sweet Potatoes", "price": 20.00, "unit": "per kg", "health_benefit": "Great source of beta-carotene and slow-release healthy carbs.", "category": "Roots"}
    ],
    "Fruits": [
        {"name": "Crisp Gala Apples", "price": 40.00, "unit": "per kg", "health_benefit": "High dietary fiber supports gut health and digestion.", "category": "Orchard"},
        {"name": "Organic Strawberries", "price": 45.00, "unit": "per 400g punnet", "health_benefit": "Loaded with antioxidants that fight inflammation.", "category": "Berries"},
        {"name": "Local Avocados", "price": 15.00, "unit": "each", "health_benefit": "Contains healthy monounsaturated fats for brain health.", "category": "Tropical"}
    ]
}

# Healthy recipe matching engine based on selected items
RECIPES = [
    {"name": "Superfood Green Smoothie", "requires": ["Organic Spinach", "Crisp Gala Apples"], "instructions": "Blend spinach, apple slices, water, and ice for a fast morning detox."},
    {"name": "Roasted Heart-Healthy Medley", "requires": ["Sweet Potatoes", "Fresh Broccoli florets", "Vine-Ripened Tomatoes"], "instructions": "Toss chopped veggies in olive oil, salt, pepper. Roast at 200°C for 25 mins."},
    {"name": "Avocado & Tomato Summer Salad", "requires": ["Local Avocados", "Vine-Ripened Tomatoes", "Organic Spinach"], "instructions": "Dice avocado and tomatoes. Serve over a bed of spinach with lemon dressing."}
]

# --- APP LAYOUT ---
st.title("🚜 FarmFresh Direct")
st.subheader("Order fresh, support local farmers, and elevate your health journey.")

# Sidebar for Easy Navigation
app_mode = st.sidebar.radio(
    "Navigate App", 
    ["1. Browse & Shop Produce", "2. View Cart & Comfortable Delivery"]
)

# --- MODE 1: BROWSE & SHOP ---
if "Browse & Shop Produce" in app_mode:
    st.markdown("### 🛒 Freshly Harvested Today")
    
    # Healthy Eating Educational Anchor
    st.markdown(
        "<div class='health-tip'>💡 <b>Healthy Eating Tip:</b> Aim to make half your plate fruits and vegetables "
        "to reduce inflammation and protect your cellular longevity.</div>", 
        unsafe_allow_html=True
    )
    
    # Create tabs for structured grouping
    tab_veg, tab_fruit = st.tabs(["🥦 Fresh Vegetables", "🍓 Fresh Fruits"])
    
    def render_produce_grid(produce_list):
        # Render item cards in clean columns
        cols = st.columns(2)
        for idx, item in enumerate(produce_list):
            with cols[idx % 2]:
                st.markdown(f"#### {item['name']}")
                st.write(f"**Price:** R {item['price']:.2f} {item['unit']}")
                st.caption(f"🌿 *Health Benefit:* {item['health_benefit']}")
                
                # Interactive easy-to-use quantity selector
                current_qty = st.session_state.cart.get(item['name'], 0)
                qty = st.number_input(
                    f"Quantity for {item['name']}", 
                    min_value=0, max_value=20, value=current_qty, key=f"input_{item['name']}"
                )
                
                if qty > 0:
                    st.session_state.cart[item['name']] = qty
                elif item['name'] in st.session_state.cart and qty == 0:
                    del st.session_state.cart[item['name']]
                st.divider()

    with tab_veg:
        render_produce_grid(PRODUCE_DATA["Vegetables"])
        
    with tab_fruit:
        render_produce_grid(PRODUCE_DATA["Fruits"])

# --- MODE 2: CART & COMFORTABLE DELIVERY ---
elif "View Cart & Comfortable Delivery" in app_mode:
    st.markdown("### 📦 Your Order & Delivery Settings")
    
    if not st.session_state.cart:
        st.warning("Your cart is currently empty! Head back to the shop tab to pick your harvest.")
    else:
        col_summary, col_delivery = st.columns()
        
        # Left Side: Cart Calculations
        with col_summary:
            st.markdown("#### Order Summary")
            all_items = PRODUCE_DATA["Vegetables"] + PRODUCE_DATA["Fruits"]
            item_lookup = {i["name"]: i for i in all_items}
            
            subtotal = 0.0
            cart_rows = []
            
            for name, qty in list(st.session_state.cart.items()):
                item_details = item_lookup[name]
                cost = item_details["price"] * qty
                subtotal += cost
                cart_rows.append({
                    "Produce": name,
                    "Quantity": qty,
                    "Cost": f"R {cost:.2f}"
                })
            
            st.table(pd.DataFrame(cart_rows))
            
            # --- FEATURE 1: PROMOTING HEALTHY EATING VIA SMART RECIPES ---
            st.markdown("#### 🥗 Dynamic Healthy Meal Suggestions")
            active_cart_names = list(st.session_state.cart.keys())
            matched_any = False
            
            for recipe in RECIPES:
                # Check if user has bought items matching a healthy recipe
                matches = [req for req in recipe["requires"] if req in active_cart_names]
                if matches:
                    matched_any = True
                    match_percentage = len(matches) / len(recipe["requires"])
                    
                    if match_percentage == 1.0:
                        st.success(f"🎉 **Ready to Make: {recipe['name']}**")
                        st.write(recipe["instructions"])
                    else:
                        missing = [r for r in recipe["requires"] if r not in active_cart_names]
                        st.info(f"💡 *You're close to a healthy meal!* Add **{', '.join(missing)}** to make **{recipe['name']}**.")
            
            if not matched_any:
                st.caption("Mix greens and colorful veggies to unlock personalized recipe recommendations.")

        # Right Side: Comfortability of Delivery
        with col_delivery:
            st.markdown("#### 🚚 Doorstep Delivery Details")
            st.write("Our produce is safely dispatched in eco-friendly climate-controlled storage vehicles.")
            
            # Form elements for effortless input
            name = st.text_input("Recipient Full Name")
            address = st.text_area("Delivery Address Details")
            
            # Date picking optimized to guarantee fresh harvest timelines
            min_delivery_date = datetime.now() + timedelta(days=1)
            delivery_date = st.date_input("Preferred Delivery Date", min_value=min_delivery_date)
            
            # Safe contactless drop option for user convenience
            delivery_type = st.radio(
                "Delivery Preference (Comfort Option)",
                ["Standard Hand-Over", "Contactless Drop-off (Leave at door/reception)"]
            )
            
            # Transparent delivery tier pricing
            delivery_fee = 35.00 if subtotal < 250 else 0.00
            total_cost = subtotal + delivery_fee
            
            st.markdown("<div class='delivery-box'>", unsafe_allow_html=True)
            st.write(f"**Items Subtotal:** R {subtotal:.2f}")
            st.write(f"**Safe Delivery Fee:** R {delivery_fee:.2f} " + ("(FREE over R250!)" if subtotal >= 250 else ""))
            st.markdown(f"### **Estimated Total: R {total_cost:.2f}**")
            st.markdown("</div>", unsafe_allow_html=True)
            st.write("")
            
            if st.button("Confirm Order & Secure Delivery"):
                if name and address:
                    st.balloons()
                    st.success(f"✨ Thank you, {name}! Your farm order has been securely scheduled for {delivery_date.strftime('%d %B %Y')}.")
                    st.info(f"Status: {delivery_type} requested. Tracking details sent via SMS.")
                    # Reset the cart upon success
                    st.session_state.cart = {}
                else:
                    st.error("Please fill in your Name and Delivery Address to continue safely.")
