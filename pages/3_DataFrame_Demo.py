import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='dark')

# Menyiapkan dataframe yang akan digunakan
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Menyiapkan daily_sharing_df
def create_daily_sharing_df(df):
  daily_sharing_df = df.groupby(by='dteday').agg({
    'cnt' : 'sum'
  })
  daily_sharing_df.rename(columns={
    "cnt": "Total Customer"
  }, inplace=True)
  return daily_sharing_df

def create_daily_sharing_casual_df(df):
  daily_sharing_casual_df = df.groupby(by='dteday').agg({
    'casual': 'sum',
  })
  daily_sharing_casual_df.rename(columns={
    'casual': "Casual Customer"
  }, inplace=True)
  return daily_sharing_casual_df

def create_daily_sharing_registered_df(df):
  daily_sharing_registered_df = df.groupby(by='dteday').agg({
    'registered': 'sum',
  })
  daily_sharing_registered_df.rename(columns={
    'registered': "Registered Customer"
  }, inplace=True)
  return daily_sharing_registered_df


# Menyiapkan monthly_sharing_df
def create_monthly_sharing_df(df):
  monthly_sharing_df = day_df.groupby(by='mnth').agg({
    'cnt': 'sum'
  })
  monthly_sharing_df.rename(index={
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
  }, inplace=True)
  monthly_sharing_df.rename(columns={
    "cnt": "Total Customer"
  }, inplace=True)
  return monthly_sharing_df

# Menyiapkan seasonly_sharing_df
def create_seasonly_sharing_df(df):
  seasonly_sharing_df = day_df.groupby(by='season').agg({
    'cnt': ['sum', 'mean']
  })
  seasonly_sharing_df.rename(index={
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
  }, inplace=True)
  seasonly_sharing_df.rename(columns={
    "cnt": "Total Customer"
  }, inplace=True)
  return seasonly_sharing_df

# Menyiapkan weathersit_sharing_df
def create_weathersit_sharing_df(df):
  weathersit_rent_df = day_df.groupby(by='weathersit').agg({
    'cnt': ['sum', 'mean']
  })
  weathersit_sharing_df.rename(index={
    1: "Clear",
    2: "Mist",
    3: "Light Snow",
    4: "Heavy Rain"
  }, inplace=True)
  weathersit_sharing_df.rename(columns={
    "cnt": "Total Customer"
  }, inplace=True)
  return weathersit_sharing_df

def create_hourly_sharing_df(df):
  hourly_sharing_df = hour_df.groupby(by='hr').agg({
    'cnt': 'mean'
  })
  hourly_sharing_df.rename(columns={
    "cnt": "Total Customer"
  }, inplace=True)
  return hourly_sharing_df


# Membuat komponen filter
min_date = pd.to_datetime(day_df['dteday']).dt.date.min()
max_date = pd.to_datetime(day_df['dteday']).dt.date.max()
 
with st.sidebar:
    st.image('data:image/jpeg;base64,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')
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dteday'] >= str(start_date)) & 
                (day_df['dteday'] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_sharing_df = create_daily_sharing_df(main_df)
daily_sharing_casual_df = create_daily_sharing_casual_df(main_df)
daily_sharing_registered_df = create_daily_sharing_registered_df(main_df)
monthly_sharing_df = create_monthly_sharing_df(main_df)
seasonly_sharing_df = create_seasonly_sharing_df(main_df)
weathersit_sharing_df = create_weathersit_sharing_df(main_df)
hourly_sharing_df = create_hourly_sharing_df(main_df)

# Membuat Dashboard secara lengkap

# Membuat judul
st.header('Bike Sharing Dashboard')

# Membuat jumlah penyewaan harian
st.subheader('Total Customer')
col1, col2, col3 = st.columns(3)

with col1:
    daily_sharing_registered = daily_sharing_registered_df['Registered Customer'].sum()
    st.metric('Registered', value= daily_sharing_registered)

with col2:
    daily_sharing_casual = daily_sharing_casual_df['Casual Customer'].sum()
    st.metric('Casual', value= daily_sharing_casual)
 
with col3:
    daily_sharing = daily_sharing_df['Total Customer'].sum()
    st.metric('Total', value= daily_sharing)

# Membuat jumlah penyewaan bulanan
st.subheader('Monthly Bike Sharing')
fig, ax = plt.subplots(figsize=(24, 12))
ax.plot(
    monthly_sharing_df.index,
    monthly_sharing_df['Total Customer'],
    marker='o', 
    linewidth=4,
    color='tab:green'
)

for index, row in enumerate(monthly_sharing_df['Total Customer']):
    ax.text(index, row + 1, str(row), ha='center', va='center', fontsize=20, rotation=-45)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)


# Membuat jumlah penyewaan berdasarkan season
st.subheader('Seasonly Bike Sharing')

fig, ax = plt.subplots(figsize=(16, 8))

seasonal_data = day_df.groupby('season')['cnt'].sum()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
color = ['blue', 'blue', 'red', 'blue']
plt.bar(season_names, seasonal_data, color=color,)
plt.xticks(fontsize=25)
plt.yticks(fontsize=20)
plt.xlabel('Season', fontsize=30)
plt.ylabel('Total Customer', fontsize=30)
plt.title('Total Customer in each Season', fontsize=35)
for bar in ax.patches:
    value = bar.get_height()
    text = f'{value}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + value
    ax.text(text_x, text_y, text, ha='center',size=25)

st.pyplot(fig)

# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Weatherly Bike Sharing')

fig, ax = plt.subplots(figsize=(16, 8))

seasonal_data = day_df.groupby('weathersit')['cnt'].sum()
season_names = ['Clear', 'Mist', 'Light Snow']
color = ['red', 'blue', 'blue']
plt.bar(season_names, seasonal_data, color=color)
plt.xticks(fontsize=25)
plt.yticks(fontsize=20)
plt.xlabel('Weathersit', fontsize=30)
plt.ylabel('Total Customer', fontsize=30)
plt.title('Total Customer in each Wheater', fontsize=35)
for bar in ax.patches:
    value = bar.get_height()
    text = f'{value}'
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_y() + value
    ax.text(text_x, text_y, text, ha='center',size=25)

st.pyplot(fig)

# Membuat jumlah penyewaan berdasarkan jam
st.subheader('Hourly Bike Sharing')

fig, ax = plt.subplots(figsize=(24, 12))
ax.plot(
    hourly_sharing_df.index,
    hourly_sharing_df['Total Customer'],
    marker='o', 
    linewidth=4,
    color='tab:blue'
)

plt.xticks(fontsize=25)
plt.yticks(fontsize=20)
plt.xlabel('Hour', fontsize=30)
plt.ylabel('Average Customer', fontsize=30)
plt.title('Average Customer for each Hour', fontsize=35)
plt.annotate('(17.00) Maximum', xy=(17, 461.45), fontsize=25)
plt.annotate('(04.00) Minimum', xy=(4, 6.36), fontsize=25)

st.pyplot(fig)


st.caption('Copyright (c) Jakfar Abdussalam 2023')
