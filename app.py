import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="The Fresh Connection Dashboard", layout="wide")

# Load all datasets from GitHub raw URLs (replace with your actual GitHub repo path)
base_url = "https://raw.githubusercontent.com/yourusername/yourrepo/main/data/"

@st.cache_data
def load_data():
    return {
        "finance": pd.read_csv(base_url + "finance_report.csv"),
        "supplier": pd.read_csv(base_url + "supplier.csv"),
        "product": pd.read_csv(base_url + "product.csv"),
        "customer": pd.read_csv(base_url + "customer.csv"),
        "component": pd.read_csv(base_url + "component.csv"),
        "supplier_component": pd.read_csv(base_url + "supplier_component.csv"),
        "warehouse": pd.read_csv(base_url + "warehouse.csv"),
        "bottling_line": pd.read_csv(base_url + "bottling_line.csv"),
        "mixers": pd.read_csv(base_url + "mixers.csv")
    }

data = load_data()

st.title("📊 The Fresh Connection KPI Dashboard")

# Sidebar filters
with st.sidebar:
    st.header("🔍 Filters")
    available_rounds = sorted(data["product"]["Round"].unique())
    selected_round = st.selectbox("Select Round", available_rounds)
    st.markdown("---")
    st.write("Note: Filter applies selectively on visualized tabs")

tab1, tab2, tab3, tab4 = st.tabs(["🛒 Purchase", "🧾 Sales", "📦 Supply Chain", "🏭 Operations"])

# ----------------------------------- PURCHASE TAB -----------------------------------
with tab1:
    st.subheader("Purchase KPIs and Financial Impact")

    df = data["supplier"]
    df_filtered = df[df["Round"] == selected_round]

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df_filtered, x="Supplier", y="Delivery reliability (%)", color="Supplier", title="Delivery Reliability (%)")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(df_filtered, x="Supplier", y="Rejection  (%)", color="Supplier", title="Rejection Percentage (%)")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Raw Material Purchase Value by Supplier")
    fig = px.bar(df_filtered, x="Supplier", y="Purchase  value previous round", color="Supplier", title="Raw Material Cost Contribution")
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------- SALES TAB -----------------------------------
with tab2:
    st.subheader("Sales KPIs and Financial Impact")

    product_df = data["product"]
    customer_df = data["customer"]

    product_filtered = product_df[product_df["Round"] == selected_round]
    customer_filtered = customer_df[customer_df["Round"] == selected_round]

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(product_filtered, x="Product", y="Forecast error (MAPE)", color="Product", title="Forecasting Error by Product")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(customer_filtered, x="Customer", y="Service level (pieces)", color="Customer", title="Service Level by Customer")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Shelf Life Attained by Customer")
    fig = px.bar(customer_filtered, x="Customer", y="Attained shelf life (%)", color="Customer", title="Shelf Life Performance")
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------- SUPPLY CHAIN TAB -----------------------------------
with tab3:
    st.subheader("Supply Chain KPIs and Financial Impact")

    component_df = data["component"]
    component_filtered = component_df[component_df["Round"] == selected_round]

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(component_filtered, x="Component", y="Component availability (%)", color="Component", title="Component Availability")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(product_filtered, x="Product", y="OSA", color="Product", title="Product Availability (OSA)")
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------- OPERATIONS TAB -----------------------------------
with tab4:
    st.subheader("Operations KPIs and Financial Impact")

    warehouse_df = data["warehouse"]
    bottling_df = data["bottling_line"]

    inbound_df = warehouse_df[(warehouse_df["Warehouse"] == "Raw materials warehouse") & (warehouse_df["Round"] == selected_round)]
    bottling_filtered = bottling_df[bottling_df["Round"] == selected_round]

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(inbound_df, x="Round", y="Cube utilization (%)", title="Inbound Warehouse Utilization")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(bottling_filtered, x="Bottling line", y="Production plan adherence (%)", color="Bottling line", title="Production Plan Adherence")
        st.plotly_chart(fig, use_container_width=True)
