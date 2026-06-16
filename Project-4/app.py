import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIG 
st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)
# DATA 
total_orders = 1200
total_revenue = 1264761.96
avg_order_value = 1053.97
product_revenue = {
    "Chair":195620,
    "Printer":195613,
    "Laptop":192127,
    "Tablet":186569,
    "Monitor":175651,
    "Desk":167460,
    "Phone":151722
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
avg_revenue_product = {
    "Laptop":1110.56,
    "Chair":1098.99,
    "Printer":1080.73,
    "Monitor":1077.62,
    "Tablet":1042.28,
    "Desk":985.06,
    "Phone":972.58
}
# TITLE 
st.title("📊 E-Commerce Sales Dashboard")
# KPI CARDS 
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Orders", "1200")
c2.metric("Total Revenue", "₹12.65L")
c3.metric("Average Order Value", "₹1054")
c4.metric("Top Channel", "Instagram")
# CHART STYLE 
def compact_chart(fig):
    fig.update_layout(
        height=230,
        margin=dict(l=5, r=5, t=35, b=5),
        showlegend=False
    )
    return fig
# ROW 1 
col1, col2, col3 = st.columns(3)
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
    st.plotly_chart(
        compact_chart(fig),
        use_container_width=True,
        config={"displayModeBar": False}
    )
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
        title="Monthly Revenue"
    )
    st.plotly_chart(
        compact_chart(fig),
        use_container_width=True,
        config={"displayModeBar": False}
    )
with col3:
    df = pd.DataFrame(
        payment_revenue.items(),
        columns=["Payment", "Revenue"]
    )
    fig = px.pie(
        df,
        names="Payment",
        values="Revenue",
        title="Revenue by Payment Method"
    )
    fig.update_traces(
    textposition="inside",
    textinfo='label+percent'
    )
    st.plotly_chart(
        compact_chart(fig),
        use_container_width=True,
        config={"displayModeBar": False}
    )
# ROW 2 
col4, col5, col6 = st.columns(3)
with col4:
    df = pd.DataFrame(
        channel_revenue.items(),
        columns=["Channel", "Revenue"]
    )
    fig = px.bar(
        df,
        x="Channel",
        y="Revenue",
        title="Marketing Channels"
    )
    st.plotly_chart(
        compact_chart(fig),
        use_container_width=True,
        config={"displayModeBar": False}
    )
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
    fig.update_traces(
    textposition="inside",
    textinfo='label+percent'
    )
    st.plotly_chart(
        compact_chart(fig),
        use_container_width=True,
        config={"displayModeBar": False}
    )
with col6:
    df = pd.DataFrame(
        avg_revenue_product.items(),
        columns=["Product", "Avg Revenue"]
    )
    fig = px.bar(
        df,
        x="Product",
        y="Avg Revenue",
        title="Average Revenue per Product"
    )
    st.plotly_chart(
        compact_chart(fig),
        use_container_width=True,
        config={"displayModeBar": False}
    )
# INSIGHTS 
st.markdown("### Key Insights")
st.markdown("""
- Instagram generated the highest revenue among marketing channels.
- Credit Card customers contributed the most revenue.
- June recorded the strongest monthly sales performance.
- Chair was the highest revenue-generating product.
- High cancellation volume requires further investigation.
""")