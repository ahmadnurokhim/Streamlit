import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(layout="wide")
df = pd.read_csv("superstore - orders.csv")

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])
df['order_year'] = df['order_date'].dt.year



# periksa tahun terakhir dari data
# itung sales, jml order, jml konsumen, profit % di tahun tsb

CURR_YEAR = max(df['order_date'].dt.year)
PREV_YEAR = CURR_YEAR - 1

"# IM"
st.metric("Sales", 1000, "10%")
data = pd.pivot_table(
    #data=df[df['order_date'].dt.year==CURR_YEAR],
    data=df,
    index='order_year',
    aggfunc={
        'sales': 'sum',
        'profit': 'sum',
        'order_id': pd.Series.nunique,
        'customer_id': pd.Series.nunique
    }
).reset_index()

data['gpm'] = data['profit'] / data['sales'] * 100.0

mx_sales, mx_order, mx_customer, mx_gpm = st.columns(4)

with mx_sales:
    curr_sales = data.loc[data['order_year']==CURR_YEAR, 'sales'].values[0]
    prev_sales = data.loc[data['order_year']==PREV_YEAR, 'sales'].values[0]
    sales_diff_pct = 100.0 * (curr_sales - prev_sales) / prev_sales
    st.metric('Sales', curr_sales, f"{sales_diff_pct:.2f}%")

with mx_order:
    st.metric("\# of Orders", 100, "20%")

st.dataframe(data, use_container_width=True)

# altair membuat chart dari data dalam parameter
st.header("Sales trend")
freq = st.selectbox('Freq', ['Harian', 'Bulanan'])
time_unit = {
    'Harian': 'yearmonthdate',
    'Bulanan': 'yearmonth'
}
sales_line = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_line().encode(
    alt.X('order_date', title='Order Date', timeUnit=time_unit[freq]),
    alt.Y('sales', title='Revenue', aggregate='sum')
)

st.altair_chart(sales_line, use_container_width=True)

sales_bar = alt.Chart(df[df['order_year']==CURR_YEAR]).mark_bar().encode(
    alt.X('order_date', title='Order Date', timeUnit=time_unit[freq]),
    alt.Y('sales', title='Revenue', aggregate='sum')
)

st.altair_chart(sales_bar, use_container_width=True)

south, west, central, east = st.columns(4)
with south:
    "South"
    sales_cat = alt.Chart(df[(df['order_year']==CURR_YEAR) & (df['region']=='South')]).mark_bar().encode(
        alt.X('category', title='Category', axis=alt.Axis(labelAngle=0)),
        alt.Y('sales', title='Revenue', aggregate='sum')
    )
    st.altair_chart(sales_cat, use_container_width=True)
with west:
    "West"
    sales_cat = alt.Chart(df[(df['order_year']==CURR_YEAR) & (df['region']=='West')]).mark_bar().encode(
        alt.X('category', title='Category', axis=alt.Axis(labelAngle=0)),
        alt.Y('sales', title='Revenue', aggregate='sum')
    )
    st.altair_chart(sales_cat, use_container_width=True)
with central:
    "Central"
    sales_cat = alt.Chart(df[(df['order_year']==CURR_YEAR) & (df['region']=='Central')]).mark_bar().encode(
        alt.X('category', title='Category', axis=alt.Axis(labelAngle=0)),
        alt.Y('sales', title='Revenue', aggregate='sum')
    )
    st.altair_chart(sales_cat, use_container_width=True)
with east:
    "East"
    sales_cat = alt.Chart(df[(df['order_year']==CURR_YEAR) & (df['region']=='South')]).mark_bar().encode(
        alt.X('category', title='Category', axis=alt.Axis(labelAngle=0)),
        alt.Y('sales', title='Revenue', aggregate='sum')
    )
    st.altair_chart(sales_cat, use_container_width=True)
