import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)
# KPI DATA
total_orders = 1200
total_revenue = 1264761.96
avg_order_value = 1053.97
# CHART DATA 
product_revenue = {
    "Chair": 195620,
    "Printer": 195613,
    "Laptop": 192127,
    "Tablet": 186569,
    "Monitor": 175651,
    "Desk": 167460,
    "Phone": 151722
}
monthly_revenue = {
    "Jan":124313,
    "Feb":112345,
    "Mar":123841,
    "Apr":109186,
    "May":135143,
    "Jun":170616,
    "Jul":85785,
    "Aug":86343,
    "Sep":69322,
    "Oct":89835,
    "Nov":75493,
    "Dec":82541
}
channel_revenue = {
    "Instagram":275285,
    "Email":261809,
    "Google":250441,
    "Facebook":250411,
    "Referral":226816
}
payment_revenue = {
    "Credit Card":263848,
    "Online":262443,
    "Cash":259786,
    "Gift Card":246324,
    "Debit Card":232361
}
order_status = {
    "Cancelled":250,
    "Returned":247,
    "Pending":237,
    "Shipped":235,
    "Delivered":231
}
# TITLE
st.title("📊 E-Commerce Sales Analytics Dashboard")
# KPI CARDS
c1, c2, c3 = st.columns(3)
c1.metric("Total Orders", f"{total_orders}")
c2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
c3.metric("Avg Order Value", f"₹{avg_order_value:.2f}")
st.divider()
# ROW 1 
col1, col2 = st.columns(2)
with col1:
    df = pd.DataFrame(
        product_revenue.items(),
        columns=["Product", "Revenue"]
    )
    fig = px.bar(
        df,
        x="Product",
        y="Revenue",
        title="Revenue by Product"
    )
    st.plotly_chart(fig, use_container_width=True)
with col2:
    df = pd.DataFrame(
        monthly_revenue.items(),
        columns=["Month", "Revenue"]
    )
    fig = px.line(
        df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )
    st.plotly_chart(fig, use_container_width=True)
# ROW 2
col3, col4 = st.columns(2)
with col3:
    df = pd.DataFrame(
        channel_revenue.items(),
        columns=["Channel", "Revenue"]
    )
    fig = px.bar(
        df,
        x="Channel",
        y="Revenue",
        title="Revenue by Marketing Channel"
    )
    st.plotly_chart(fig, use_container_width=True)
with col4:
    df = pd.DataFrame(
        payment_revenue.items(),
        columns=["Payment Method", "Revenue"]
    )
    fig = px.pie(
        df,
        names="Payment Method",
        values="Revenue",
        title="Revenue by Payment Method"
    )
    st.plotly_chart(fig, use_container_width=True)
# ROW 3 
col5, col6 = st.columns(2)
with col5:
    df = pd.DataFrame(
        order_status.items(),
        columns=["Status", "Count"]
    )
    fig = px.pie(
        df,
        names="Status",
        values="Count",
        title="Order Status Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)
with col6:
    top_orders = pd.DataFrame({
        "Order ID":[
            "ORD200789",
            "ORD201122",
            "ORD200632",
            "ORD200469",
            "ORD200328"
        ],
        "Amount":[
            3456.40,
            3390.95,
            3390.80,
            3384.90,
            3370.20
        ]
    })
    fig = px.bar(
        top_orders,
        x="Order ID",
        y="Amount",
        title="Top 5 Highest Value Orders"
    )
    st.plotly_chart(fig, use_container_width=True)
# INSIGHTS 
st.divider()
st.subheader("📌 Business Insights")
st.markdown("""
- Chair generated the highest revenue among all products.
- Instagram was the highest revenue-generating marketing channel.
- Credit Card users contributed the highest revenue.
- June recorded peak monthly revenue performance.
- Order cancellations remain high and require investigation.
""")
st.subheader("🚀 Recommendations")
st.markdown("""
- Increase investment in Instagram marketing campaigns.
- Focus promotions on high-revenue products.
- Investigate causes of order cancellations.
- Encourage digital payment adoption through offers and rewards.
""")