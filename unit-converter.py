import streamlit as st

# Title of the app
st.title("Unit Converter")

# Dropdown for selecting conversion type
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Function for length conversion
def convert_length(value, from_unit, to_unit):
    if from_unit == "Meters" and to_unit == "Kilometers":
        return value / 1000
    elif from_unit == "Kilometers" and to_unit == "Meters":
        return value * 1000
    elif from_unit == "Miles" and to_unit == "Kilometers":
        return value * 1.60934
    elif from_unit == "Kilometers" and to_unit == "Miles":
        return value / 1.60934
    # Add more conversion logic as needed
    return value

# Function for weight conversion
def convert_weight(value, from_unit, to_unit):
    if from_unit == "Kilograms" and to_unit == "Pounds":
        return value * 2.20462
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return value / 2.20462
    elif from_unit == "Grams" and to_unit == "Ounces":
        return value / 28.3495
    elif from_unit == "Ounces" and to_unit == "Grams":
        return value * 28.3495
    # Add more conversion logic as needed
    return value

# Function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    # Add more conversion logic as needed
    return value

# Logic based on selected conversion type
if conversion_type == "Length":
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Miles"])
    to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Miles"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"Converted Value: {result} {to_unit}")

elif conversion_type == "Weight":
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From Unit", ["Kilograms", "Pounds", "Grams", "Ounces"])
    to_unit = st.selectbox("To Unit", ["Kilograms", "Pounds", "Grams", "Ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"Converted Value: {result} {to_unit}")

elif conversion_type == "Temperature":
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"Converted Value: {result} {to_unit}")
