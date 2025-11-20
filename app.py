import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# --------------------------------------------------
# Simple modern Streamlit app template
# Drop this file into your old project and adapt the
# data-loading sections and assets (logo, images) as needed.
# --------------------------------------------------

# --- Page config ---
st.set_page_config(page_title="Cafe Management — Dashboard", page_icon="☕", layout="wide")

# --- Custom CSS for nicer visuals ---
st.markdown(
    """
    <style>
    /* Container */
    .reportview-container .main .block-container{padding-top:1.5rem;}

    /* Card style for metric boxes */
    .metric-card{
        background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        border: 1px solid rgba(255,255,255,0.03);
    }

    /* Smaller text for footers */
    .muted{color: #9aa0a6; font-size:12px}

    /* Make Streamlit sidebar header larger */
    .css-1d391kg .css-10trblm {font-size:18px}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Top bar ---
col1, col2 = st.columns([0.15, 0.85])
with col1:
    st.image("https://raw.githubusercontent.com/streamlit/streamlit/develop/examples/image/cafe.jpg", width=80)
with col2:
    st.markdown("## Cafe Management — Dashboard")
    st.write("A compact, modern template you can adapt for your project.")

st.markdown("---")

# --- Sidebar controls ---
st.sidebar.title("Controls")
filter_date = st.sidebar.date_input("Choose date", value=None)
show_demo_data = st.sidebar.checkbox("Use demo data", value=True)
st.sidebar.markdown("---")
with st.sidebar.expander("Settings"):
    theme = st.selectbox("Theme", ["Light", "Dark"], index=0)
    st.write("Change these to adapt visual style.")

# --- Demo data loader ---
def load_demo_data(n=30):
    rng = pd.date_range(end=pd.Timestamp.today(), periods=n)
    data = pd.DataFrame({
        "date": rng,
        "orders": np.random.poisson(20, size=n),
        "revenue": np.round(np.random.normal(2500, 600, size=n), 2),
        "top_item": np.random.choice(["Latte","Espresso","Cappuccino","Tea","Sandwich"], size=n),
    })
    data['revenue'] = data['revenue'].clip(lower=0)
    return data

# Load data
if show_demo_data:
    df = load_demo_data(60)
else:
    # Replace this with your project's data loading logic
    df = pd.DataFrame(columns=["date","orders","revenue","top_item"])  # placeholder

# If user selected a date, filter
if filter_date:
    df_filtered = df[df['date'].dt.date == filter_date]
else:
    df_filtered = df.copy()

# --- KPIs ---
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total Orders", int(df['orders'].sum()))
    st.markdown('</div>', unsafe_allow_html=True)
with k2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Total Revenue", f"₹{df['revenue'].sum():,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)
with k3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Avg Orders / Day", round(df['orders'].mean(), 1))
    st.markdown('</div>', unsafe_allow_html=True)
with k4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Top Item", df['top_item'].mode().iloc[0] if not df['top_item'].empty else "—")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- Charts and table ---
st.subheader("Orders & Revenue")
colA, colB = st.columns([2,1])
with colA:
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['orders'], marker='o')
    ax.set_title('Orders over time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Orders')
    plt.xticks(rotation=30)
    st.pyplot(fig)

with colB:
    st.subheader("Summary")
    st.write(df_filtered.describe())

st.subheader("Recent transactions")
st.dataframe(df.sort_values('date', ascending=False).head(10).reset_index(drop=True))

# --- Quick add form ---
st.markdown("---")
st.subheader("Add a quick sale")
with st.form("add_sale"):
    c1, c2, c3 = st.columns(3)
    with c1:
        item = st.selectbox("Item", ["Latte","Espresso","Cappuccino","Tea","Sandwich"])
    with c2:
        qty = st.number_input("Qty", min_value=1, value=1)
    with c3:
        price = st.number_input("Price per item (₹)", min_value=1.0, value=120.0)
    submitted = st.form_submit_button("Add")
    if submitted:
        st.success(f"Added {qty} x {item} @ ₹{price:.2f}")
        # In real app: append to DB or CSV

# --- Footer ---
st.markdown("<div class='muted'>Built with Streamlit — adapt this template for your old projects. Replace the demo data loader with your real data source (CSV, DB, or API).</div>", unsafe_allow_html=True)

# Helper: Save export sample
st.download_button("Export current data (CSV)", data=df.to_csv(index=False).encode('utf-8'), file_name='cafe_data_export.csv')
