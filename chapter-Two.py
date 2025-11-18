import streamlit as st

st.title("Shobhit Chai Wala")

col1,col2 = st.columns(2)

with col1:
    st.image("https://images.pexels.com/photos/734983/pexels-photo-734983.jpeg",width=300)
    Vote1 = st.button("Vote for Masala Chai")

with col2:
    st.image("https://images.pexels.com/photos/905485/pexels-photo-905485.jpeg",width=200)
    Vote2 = st.button("Vote for Lemon Tea")

if Vote1:
    st.success("You voted for Masala Chai")
elif Vote2:
    st.success("You voted for Lemon Tea")

name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox("Chosse your Chai",["Masala chai","Adrak chai","Lemon Tea","Tulsi Tea"])

st.write(f"Welcome {name} and your {tea} with Shobhit Chai Wala")



add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala Added!")

tea_type = st.radio("Pick your chai base:",["Milk","Water","Alomamd Milk"])
st.write(f"You selected {tea_type} as your base.")    
flavour = st.selectbox("Choose flavour:",["Adrak","Kesar","Tulsi"])
st.write(f"Selected flavour: {flavour}")

sugar = st.slider("Select suger level{Spoons}")
st.write(F"Selected sugar level:{sugar} spoons")

cups = st.number_input("How many cups",min_value=1,max_value=10)
st.write(f"Sleceted sugar level:{cups}")

name = st.text_input("Enter your name:")
st.write(f"Welcome {name} to Shobhit Chai Wala!")

if st.button("Make Chai"):
    st.success("Your Chai has been Brewed Successfully!")

DOB = st.date_input("Enter your DOB:")
st.write(f"Your  is DOB:{DOB}")

with st.expander("Show Chai Making Inatructions"):
    st.write("""
    1. Boil water/milk
    2. Add tea leaves   
    3. Add masala and Flavor 
    4. Add sugar
    5. Let it simmer for 5 mins
    6. Serve hot and enjoy!
""")

st.markdown("### Welcome to Shobhit Chai App")
st.markdown("> Blockquote: The Best Chai in Town!")



















