import streamlit as st
from textblob import TextBlob as tb
st.title("🙂 Sentiment Analysis")
text=st.text_input("Enter text here :")
text=text.strip()
if st.button("🔍Analyse"):
    blob=tb(text)
    pol=blob.sentiment.polarity
    st.subheader("Result of analysis")
    if pol>0.2:
        st.success(f"😄The sentence has positive polarity: {pol}")
    elif pol<-0.2:
        st.error(f"😡The sentence has negative polarity: {pol}")
    else:
        st.warning(f"😐The sentence has neutral polarity: {pol}")
