import streamlit as st
import home, data_info, prediction, graphs, scope, info, personal

st.title("WELCOME")

pages = {
    "Home" : home,
    "Data Info" : data_info,
    "Prediction" : prediction,
    "Visualize data" : graphs,
    "Future Scope"  : scope,
    "Model Info"  : info,
   "About me" : personal
}

st.sidebar.title("The PAGES")
page = st.sidebar.radio("Pages", list(pages.keys()))

pages[page].app()