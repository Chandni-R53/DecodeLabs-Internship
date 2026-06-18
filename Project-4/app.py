import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background: #f5f7fb; }
[data-testid="stHeader"] { background: #f5f7fb; }
.block-container { padding: 2rem 2.5rem 1rem; }

.kpi {
    background: white;
    border-radius: 12px;
    padding: 18px 20px;
    border-left: 4px solid #4361ee;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
}
.kpi-label { font-size: 12px; color: #888; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
.kpi-value { font-size: 26px; font-weight: 700; color: #1a1a2e; margin-top: 4px; }
.kpi-note  { font-size: 12px; color: #4361ee; margin-top: 3px; }
</style>
""", unsafe_allow_html=True)

# DATA 
product_rev  = {"Chair":195620,"Printer":195613,"Laptop":192127,"Tablet":186569,"Monitor":175651,"Desk":167460,"Phone":151722}
monthly_rev  = {"Jan":124313,"Feb":112345,"Mar":123841,"Apr":109186,"May":135143,"Jun":170616,"Jul":85785,"Aug":86343,"Sep":69322,"Oct":89835,"Nov":75493,"Dec":82541}
channel_rev  = {"Instagram":275285,"Email":261809,"Google":250441,"Facebook":250411,"Referral":226816}
payment_rev  = {"Credit Card":263848,"Online":262443,"Cash":259786,"Gift Card":246324,"Debit Card":232361}
status_data  = {"Cancelled":250,"Returned":247,"Pending":237,"Shipped":235,"Delivered":231}
avg_rev      = {"Laptop":1110.56,"Chair":1098.99,"Printer":1080.73,"Monitor":1077.62,"Tablet":1042.28,"Desk":985.06,"Phone":972.58}

COLORS = ["#4361ee","#3a86ff","#7b2d8b","#f72585","#4cc9f0","#06d6a0","#ffd166"]
CHART  = dict(paper_bgcolor="white", plot_bgcolor="white", font_color="#444",
              margin=dict(l=10,r=10,t=36,b=40), height=255,
              title_font=dict(size=15, color="#333"))

# TITLE 
st.markdown("## 📊 E-Commerce Sales Dashboard")
st.markdown("<p style='color:#888;margin-top:-10px;margin-bottom:20px'>Annual Performance Overview</p>", unsafe_allow_html=True)

# KPI CARDS 
k1, k2, k3, k4 = st.columns(4)
for col, label, value, note, color in [
    (k1, "Total Orders",     "1,200",     "All Channels", "#4361ee"),
    (k2, "Total Revenue",    "₹12.65L",   "Gross Earnings", "#06d6a0"),
    (k3, "Avg Order Value",  "₹1,054",    "Per Transaction", "#f72585"),
    (k4, "Top Channel",      "Instagram", "₹2.75L Revenue", "#ffd166"),
]:
    col.markdown(f"""
    <div class="kpi" style="border-left-color:{color}">
      <div class="kpi-label">{label}</div>
      <div class="kpi-value">{value}</div>
      <div class="kpi-note" style="color:{color}">{note}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ROW 1 
c1, c2, c3 = st.columns(3)
with c1:
    df = pd.DataFrame(product_rev.items(), columns=["Product","Revenue"]).sort_values("Revenue")
    fig = px.bar(df, x="Revenue", y="Product", orientation="h",
                 title="Revenue by Product", color_discrete_sequence=["#4361ee"])
    fig.update_traces(marker_cornerradius=4)
    fig.update_layout(**CHART, xaxis=dict(showgrid=False, showticklabels=False),
                      yaxis=dict(gridcolor="#f0f0f0"))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

with c2:
    df = pd.DataFrame(monthly_rev.items(), columns=["Month","Revenue"])
    fig = go.Figure(go.Scatter(x=df["Month"], y=df["Revenue"], mode="lines+markers",
        line=dict(color="#4361ee", width=2.5), marker=dict(size=6, color="#4361ee"),
        fill="tozeroy", fillcolor="rgba(67,97,238,0.08)"))
    fig.update_layout(**CHART, title="Monthly Revenue Trend",
                      xaxis=dict(gridcolor="#f0f0f0"), yaxis=dict(gridcolor="#f0f0f0"))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

with c3:
    df = pd.DataFrame(payment_rev.items(), columns=["Method","Revenue"])
    fig = px.pie(df, names="Method", values="Revenue", hole=0.5,
                 title="Payment Method Split", color_discrete_sequence=COLORS)
    fig.update_traces(textposition="outside", textinfo="label+percent",
                      marker=dict(line=dict(color="white", width=2)))
    fig.update_layout(**CHART)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

# ROW 2 
c4, c5, c6 = st.columns(3)
with c4:
    df = pd.DataFrame(channel_rev.items(), columns=["Channel","Revenue"]).sort_values("Revenue",ascending=False)
    clrs = ["#4361ee" if i == 0 else "#c5d0f5" for i in range(len(df))]
    fig = px.bar(df, x="Channel", y="Revenue", title="Marketing Channels",
                 color_discrete_sequence=["#4361ee"])
    fig.update_traces(marker_color=clrs, marker_cornerradius=4)
    fig.update_layout(**CHART, xaxis=dict(gridcolor="#f0f0f0"),
                      yaxis=dict(showgrid=False, showticklabels=False))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

with c5:
    df = pd.DataFrame(status_data.items(), columns=["Status","Count"])
    STATUS_CLR = {"Delivered":"#06d6a0","Shipped":"#4361ee","Pending":"#ffd166",
                  "Returned":"#f7a844","Cancelled":"#f72585"}
    fig = px.pie(df, names="Status", values="Count", hole=0.5,
                 title="Order Status Distribution",
                 color="Status", color_discrete_map=STATUS_CLR)
    fig.update_traces(textposition="outside", textinfo="label+percent",
                      marker=dict(line=dict(color="white", width=2)))
    fig.update_layout(**CHART)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

with c6:
    df = pd.DataFrame(avg_rev.items(), columns=["Product","Avg Revenue"]).sort_values("Avg Revenue")
    fig = px.bar(df, x="Avg Revenue", y="Product", orientation="h",
                 title="Avg Revenue per Product", color_discrete_sequence=["#7b2d8b"])
    fig.update_traces(marker_cornerradius=4)
    fig.update_layout(**CHART, xaxis=dict(showgrid=False, showticklabels=False),
                      yaxis=dict(gridcolor="#f0f0f0"))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar":False})

# INSIGHTS 
st.markdown("### 💡 Key Insights")
i1, i2 = st.columns(2)
insights = [
    "<b>June</b> was the peak month (₹1.7L) — strong mid-year performance.",
    "<b>Instagram</b> leads all marketing channels with ₹2.75L in revenue.",
    "Payment methods are evenly spread — no single dominant preference.",
    "<b>Chair</b> tops total revenue; <b>Laptop</b> wins on average order value.",
    "<b>Cancellations (21%)</b> are highest among all order statuses — needs review.",
    "Delivered + Shipped orders together account for ~39% of all orders.",
]
for idx, ins in enumerate(insights):
    (i1 if idx % 2 == 0 else i2).markdown(
        f"<div style='background:white;padding:12px 16px;border-radius:10px;"
        f"margin-bottom:10px;box-shadow:0 1px 3px rgba(0,0,0,0.06);font-size:15px'>{ins}</div>",
        unsafe_allow_html=True)