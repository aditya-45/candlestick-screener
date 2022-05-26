import os
import pandas as pd
import streamlit as st


from datetime import date
import plotly.graph_objects as go

from stock_specific import *



st.set_page_config(
    page_title="Stock Explorer",
    page_icon="🧊",
    initial_sidebar_state="auto",
    #menu_items={
    #    'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "This is an *extremely* cool app!"
    #}
)

page = st.sidebar.selectbox(
    "Choose a page", ['Stock Search'])


def consolidated():
    Consol, Break = consolbreak()
    
    Consolidated = pd.DataFrame(Consol, columns=['Consolidate'])
    st.table(Consolidated)


def breakout():
    Consol, Break = consolbreak()
    Breakout = pd.DataFrame(Break, columns=['Breakout'])
    st.table(Breakout)


def vol_breakout():
    colab = vol_break()
    Vol_Breakout = pd.DataFrame(colab, columns=['Volume Breakout'])
    st.table(Vol_Breakout)


def hundredma():
    ma, tma = moving_avg()
    hundredma = pd.DataFrame(ma, columns=['Hundred_MA'])
    st.table(hundredma)


def twohundredma():
    ma, tma = moving_avg()
    twohundredma = pd.DataFrame(tma, columns=['two_Hundred_MA'])
    st.table(twohundredma)

## Watchlist ##


def consolidated_w():
    consolbreak_w()
    Consolidated_w = pd.DataFrame(Consol_w, columns=['Consolidate'])
    st.table(Consolidated_w)


def breakout_w():
    consolbreak_w()
    Breakout_w = pd.DataFrame(Break_w, columns=['Breakout'])
    st.table(Breakout_w)


def vol_breakout_w():
    vol_break_w()
    Vol_Breakout_w = pd.DataFrame(colab_w, columns=['Volume Breakout'])
    st.dataframe(Vol_Breakout_w)


def hundredma_w():
    moving_avg_w()
    hundredma_w = pd.DataFrame(ma_w, columns=['Hundred_MA'])
    st.table(hundredma_w)


def twohundredma_w():
    moving_avg_w()
    twohundredma_w = pd.DataFrame(tma_w, columns=['two_Hundred_MA'])
    st.table(twohundredma_w)


def none():
    st.dataframe(nulldf)


analysis_dict = {
    "None": none,
    "Consolidating": consolidated,
    "Breaking Out": breakout,
    "Volume Breakout": vol_breakout,
    "Hundred MA": hundredma,
    "Two Hundred MA": twohundredma,

}

analysis_dict_w = {
    "None": none,
    "Consolidating": consolidated_w,
    "Breaking Out": breakout_w,
    "Volume Breakout": vol_breakout_w,
    "Hundred MA": hundredma_w,
    "Two Hundred MA": twohundredma_w,

}


if page == 'Stock Search':
    st.title('Stock Search')
    
    valid_intervals = ['1d','5d','1wk','1mo','3mo']
    Valid_periods = ['9mo', '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    
    
    col1, col2 = st.columns(2)
    
    inter = col1.selectbox("Select Interval:", valid_intervals)
    per = col2.selectbox("Select Period:", Valid_periods)
    
    df = pd.read_csv('symb.csv')
    list1 = df['Symbol'].tolist()
    symbol = st.selectbox('Symbols', list1)

    with st.expander("Show Chart"):
        fig, hunma, twoma, twentyma, cmp, state = stock_specific(symbol, per, inter)
        st.plotly_chart(fig, use_container_width=True)
    
    col4, col1, col2, col3 = st.columns(4)
    
    col4.metric("CMP", cmp, state)
    col1.metric("Two Hundred MA", twoma)
    col2.metric("Hundred MA", hunma)
    col3.metric("Twenty One MA", twentyma)
    
    #st.dataframe(data)
    
