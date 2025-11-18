import streamlit as st

#python -m streamlit run main.py
st.title("Hello Super App")
st.subheader("Brewed with Streamlit")
st.text("Welcome to our first interactive app")
st.write("Choose your fav. variety of super food from the dropdown below")

Chai = st.selectbox("Your fav Chai: ",["Masala Chai", "Adrak Chai", "Green Tea", "Lemon Tea", "Ginger Tea", "Black Tea"])
st.write("Your choosen {Chai} is a great choice!".format(Chai=Chai))
st.success("Your Chai has been Brewed Successfully!")







