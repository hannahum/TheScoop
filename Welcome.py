import streamlit as st


st.set_page_config(
    page_title = "Welcome",
    page_icon = "👋",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("The Scoop 🍦")

st.markdown(
    """
    **Welcome to the Scoop!** \n
    Tell us your latest cravings, dietary restrictions, or select our random feature to find a scoop of ice cream just right for you!
    """
)

welcome = st.image('welcome.jpg')
st.markdown('</div>', unsafe_allow_html=True)


