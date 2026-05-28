# 🚜 FarmFresh Direct

A modern, easy-to-use farm-to-table web application designed to connect consumers directly with local farmers. The platform aims to promote healthy eating choices while providing a comfortable, safe, and flexible delivery infrastructure.

Built using **Python** and **Streamlit**, and deployed live on **Streamlit Community Cloud**.

---

## 🥗 Key Features

### 1. Promoting Healthy Eating
* **Nutritional Insights:** Every produce item includes explicit health and dietary benefits directly on its card.
* **Smart Recipe Engine:** The app dynamically scans items in the user's active shopping cart and automatically suggests healthy meals they can prepare with those ingredients.

### 2. Effortless User Experience (Easy to Use)
* **Clean Layout:** Organized into distinct, easy-to-navigate tabs for Vegetables and Fruits to avoid clutter.
* **Interactive Cart:** Real-time quantity counters allow users to adjust their market basket with single clicks.
* **Integrated Authentication:** A simple, built-in sidebar login and account registration flow secures customer selections.

### 3. Comfortable & Safe Delivery
* **Flexible Logistics:** Supports standard drop-offs and seamless contactless delivery requests.
* **Calendar Scheduler:** Preventative date-picking system limits deliveries to viable post-harvest timelines.
* **Automatic Tier Pricing:** Transparent subtotaling that automatically applies free delivery incentives on larger orders.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Framework:** Streamlit (UI & State Engine)
* **Data Management:** Pandas

---

## 🚀 How to Run Locally

### Prerequisites
Make sure you have Python installed on your machine. Install the required dependencies using pip:
```bash
pip install streamlit pandas
```

### Launch the Application
Run the Streamlit server directly from your project directory:
```bash
streamlit run app.py
```
The app will automatically spin up in your default desktop browser at `http://localhost:8501`.

---

## 🔒 Default Test Credentials
To evaluate the authenticated shopping view immediately, use the following credentials on the login screen:
* **Username:** `testuser`
* **Password:** `password123`
* *(Alternatively, use the **Sign Up** tab to create a new profile in seconds).*
