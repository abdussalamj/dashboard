# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
from streamlit.logger import get_logger

byseason_df = pd.read_csv("byseason.csv")
byseason_df.rename(index={
    0: "Musim",
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}, inplace=True)
byseason_df.rename(columns={
    "Jumlah Customer.1": "Rata-rata Customer"
}, inplace=True)
byseason_df

byweathersit_df = pd.read_csv("byweathersit.csv")
byweathersit_df.rename(index={
    0: "Cuaca",
    1: "Clear",
    2: "Mist",
    3: "Light Snow",
}, inplace=True)
byweathersit_df.rename(columns={
    "cnt": "Jumlah Customer",
    "cnt.1": "Rata-rata Customer"
}, inplace=True)
byweathersit_df

byhour_df = pd.read_csv("byhour.csv")
byhour_df.rename(columns={
    "casual" : "Casual",
    "casual.1": "Rata-rata casual",
    "registered": "Registered",
    "registered.1": "Rata-rata Registered",
    "cnt": "Jumlah Customer",
    "cnt.1": "Rata-rata Customer"
}, inplace=True)
byhour_df

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )
st.header('Bike Rental Dashboard 🚲')

if __name__ == "__main__":
    run()
