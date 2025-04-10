import streamlit  as  st

 
st.title("🌍unit converter App")
st.markdown("### converts length, weight And Time Instantly")
st.write("welcome! select a category,enter a value and get the converted result in real-time")

category = st.selectbox("choose a categoty",["Length","Weight","Time"])

def convert_unites(category,value,unit):
    if category =="Length":
        if unit == "Kilometers to Miles":
            return value * 0.6213371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
        
    elif category =="Time":
        if unit == "seconds to minutes":
            return value / 60 
        elif unit == "minutes to seconds":
            return value * 60 
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value /24 
        elif unit == "days to hours":
            return value * 24
            
if category == "Length":
    unit = st.selectbox("🎞Select conversation",["Kilometers to Miles","Miles to Kilometers"])
elif category == "Weight":
    unit =st.selectbox("⚖️Select conversation",["kilograms to pounds","pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversation",["seconds to minutes", "minutes to seconds","minutes to hours","hours to minutes","hours to days","days to hours"])
value = st.number_input("Enter the value to convert")

if st.button("convert"):
    result = convert_unites(category, value,unit)             
    st.success(f"The result is {result:.2f}")    







