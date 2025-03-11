import streamlit as st

def main():
    st.title("Commute Emission Calculator")
    
    # User input for distance travelled
    Distance = st.number_input("Enter Distance travelled (in kilometers):", min_value=0.0, step=1.0)
    
    # Mode of transport selection
    mode = st.selectbox("Select your mode of transport:", ["Personal Car", "Two Wheeler", "Bus", "Train"])
    
    # Emission factors (in kg CO₂ per km)
    emission_factors = {
        "Personal Car": 0.2,
        "Two Wheeler": 0.1,
        "Bus": 0.05,
        "Train": 0.02
    }
    
    # Calculate emissions
    if Distance > 0:
        Emission = Distance * emission_factors[mode]
        
        # Display result
        st.write(f"### Emission: {Emission:.2f} kg of CO₂")
    else:
        st.write("Please enter a valid distance greater than 0.")

if __name__ == "__main__":
    main()