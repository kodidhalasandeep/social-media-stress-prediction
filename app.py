import streamlit as st
import sqlite3
import hashlib
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# =================================================
# PAGE CONFIG (MUST BE FIRST)
# =================================================
st.set_page_config(
    page_title="Stress Level Predictor",
    layout="centered"
)

# =================================================
# DATABASE & AUTH FUNCTIONS
# =================================================
def get_db():
    return sqlite3.connect("users.db")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    # Create default admin
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if cur.fetchone() is None:
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", hash_password("admin123"), "admin")
        )

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hash_password(password), "user")
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT username, role FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )
    user = cur.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, username, role FROM users")
    users = cur.fetchall()
    conn.close()
    return users

# =================================================
# INIT DATABASE
# =================================================
init_db()

# =================================================
# SESSION STATE
# =================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =================================================
# 🔐 AUTH SECTION
# =================================================
if not st.session_state.logged_in:

    st.title("🔐 Login / Registration")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # -------- LOGIN --------
    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.username = user[0]
                st.session_state.role = user[1]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # -------- REGISTER --------
    with tab2:
        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registration successful! Please login.")
            else:
                st.error("Username already exists")

# =================================================
# 😌 MAIN APP (AFTER LOGIN)
# =================================================
else:

    # ---------------- SIDEBAR ----------------
    st.sidebar.success(f"👤 {st.session_state.username}")
    st.sidebar.write(f"Role: **{st.session_state.role}**")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # ---------------- ADMIN PANEL ----------------
    if st.session_state.role == "admin":
        st.sidebar.markdown("### 👑 Admin Panel")

        if st.sidebar.button("View Registered Users"):
            users = get_all_users()
            df = pd.DataFrame(users, columns=["ID", "Username", "Role"])
            st.subheader("📋 Registered Users")
            st.dataframe(df)

    # =================================================
    # 😌 STRESS LEVEL PREDICTOR
    # =================================================
    model = load_model('stress_model.h5', compile=False)
    scaler = joblib.load('stress.pkl')

    gender_map = {'Male': 0, 'Female': 1, 'Other': 2}
    job_map = {
        'Finance': 0, 'Education': 1, 'Student': 2,
        'IT': 3, 'Unemployed': 4, 'Health': 5
    }

    st.title("😌 Stress Level Predictor")
    st.markdown("### Enter the following details:")

    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    gender = st.selectbox("Gender", list(gender_map.keys()))
    job_type = st.selectbox("Job Type", list(job_map.keys()))
    social_time = st.number_input("Daily Social Media Time (hours)", min_value=0.0, step=0.1)
    notifications = st.number_input("Number of Notifications", min_value=0, step=1)
    work_hours = st.number_input("Work Hours Per Day", min_value=0.0, max_value=24.0, step=0.1)
    sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.1)
    screen_before_sleep = st.number_input("Screen Time Before Sleep (hours)", min_value=0.0, step=0.1)
    breaks = st.number_input("Breaks During Work", min_value=0, step=1)

    if st.button("Predict Stress Level"):
        try:
            gender_val = gender_map[gender]
            job_val = job_map[job_type]

            features = np.array([[age, gender_val, job_val,
                                  social_time, notifications,
                                  work_hours, sleep_hours,
                                  screen_before_sleep, breaks]])

            scaled = scaler.transform(features)
            prediction = model.predict(scaled)
            stress_level = round(prediction[0][0], 2)

            st.success(f"😌 Predicted Stress Level: **{stress_level}**")

        except Exception as e:
            st.error(f"Prediction Error: {e}")