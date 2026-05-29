# 🤝 Contributing to FarmFresh Direct

Thank you for your interest in contributing to **FarmFresh Direct**! We welcome open-source contributions from developers, designers, and domain experts in AgriTech and FinTech. 

By contributing, you help optimize regional supply chains and lower the barrier to digital transformation for smallholder farmers.

---

## 🗺️ Current Technical Roadmap (Active Sprints)
We are actively seeking contributions focused on the following pillars:
1. **Database Persistence Layer:** Migrating the local prototype `sqlite3` storage layer over to a scalable cloud schema (e.g., PostgreSQL).
2. **Predictive Climate Integrations:** Hooking up live weather and transit telemetry APIs to dynamically map route delivery risks.
3. **AI Recipe Personalization Engine:** Upgrading the static inventory loop to leverage local LLM endpoints or rule-based models for tailored health suggestions.

---

## 🚀 Step-by-Step Setup Guide

### 1. Fork and Clone the Repository
* Fork the project repository on GitHub.
* Clone your fork to your local environment:
  ```bash
  git clone https://github.com
  cd farm-fresh-direct
  ```

### 2. Set Up Your Environment
Create an isolated development environment to manage packages safely:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Local Database Initialization
The application runs on an isolated internal SQLite engine (`farmfresh.db`). Running the setup script locally automatically initialises your user and order tracking tables without requiring external server configurations:
```bash
streamlit run app.py
```

---

## 📥 Submission Rules & Pull Requests

To maintain codebase health and code quality, please adhere to this contribution loop:

1. **Create a Feature Branch:** Branch out from `main` using descriptive naming conventions:
   * For features: `feature/your-feature-name`
   * For bugs: `bugfix/your-fix-name`
2. **Keep Code Clean:** Follow standard PEP 8 formatting rules for Python scripts. Use spaces instead of structural tab keys inside terminal text editor sessions.
3. **Verify App Logic Locally:** Double-check that your modifications pass administrative login rules under the default developer testing profile:
   * **Username:** `admin_founder`
   * **Password:** `agritech2026`
4. **Submit a Pull Request (PR):** Open a PR against our primary `main` branch. Provide a concise summary of the problems your additions fix or the optimizations they introduce.

---

## 📜 Code of Conduct
We are dedicated to providing a collaborative, welcoming, and harassment-free environment for everyone. Please treat all maintainers and fellow developers with absolute professional respect.
