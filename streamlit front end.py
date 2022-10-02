import streamlit as st
import pickle

pickle_in=open("flight_price_pred.pkl","rb")
model=pickle.load(pickle_in)


def main():
    st.title("✈️️Flight Price Prediction✈️")
    st.text(".....................................................................................")
    st.image("/Users/kamalpreet/Downloads/plane.jpeg")
    journey=st.date_input("Departure Date")
    journey_time=st.time_input("Departure Time")
    arrival=st.date_input("Arrival Date")
    arrival_time=st.time_input("Arrival Time")
    a = journey.strftime("%Y/%m/%d")
    for i in a:
        Journey_day = int(a[8:10])
        Journey_month = int(a[5:7])
    b = journey_time.strftime("%H/%M")
    for i in b:
        Departure_hour = int(b[0:2])
        Departure_min = int(b[3:5])
    c = arrival_time.strftime("%H/%M")
    for i in c:
        arrival_hour = int(c[0:2])
        arrival_min = int(c[3:5])
    Total_Stops = st.selectbox("Stopage", [0, 1, 2, 3, 4])

    airline = st.selectbox("Airline", ["Jet Airways", "IndiGo", "Air India", "SpiceJet", "Vistara", "Air Asia", "GoAir","Multiple carriers Premium economy", "Jet Airways Bussiness","Vistara Premium economy", "Truejet"])

    if airline== "Jet Airways":
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "IndiGo":
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "Air India":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "SpiceJet":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 1
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "Vistara":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 1
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "Air Asia":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 1
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "GoAir":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 1
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "Multiple carriers Premium economy":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy= 1
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "Jet Airways Bussiness":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 1
        Vistara_Premium_economy = 0
        Truejet = 0
    elif airline == "Vistara Premium economy":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy=0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 1
        Truejet = 0
    elif airline == "Truejet":
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        SpiceJet = 0
        Vistara = 0
        Air_Asia = 0
        GoAir = 0
        Multiple_carriers_Premium_economy= 0
        Jet_Airways_Bussiness = 0
        Vistara_Premium_economy = 0
        Truejet = 1


    source=st.selectbox("Source",["Chennai","Delhi","Kolkata","Mumbai","Cochin","Delhi","Hyderabad","Kolkata","New Delhi"])
    if source=="Chennai":
        Chennai=1
        Delhi=0
        Kolkata=0
        Mumbai=0
        Cochin=0
        Hyderabad=0
        New_Delhi=0
    elif source=="Delhi":
        Chennai=0
        Delhi=1
        Kolkata=0
        Mumbai=0
        Cochin=0
        Hyderabad=0
        New_Delhi=0
    elif source == "Kolkata":
        Chennai = 0
        Delhi = 0
        Kolkata = 1
        Mumbai = 0
        Cochin = 0
        Hyderabad = 0
        New_Delhi = 0
    elif source == "Mumbai":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 1
        Cochin = 0
        Hyderabad = 0
        New_Delhi = 0
    elif source == "Cochin":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Cochin = 1
        Hyderabad = 0
        New_Delhi = 0
    elif source == "Hyderabad":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Cochin = 0
        Hyderabad = 1
        New_Delhi = 0
    elif source == "New Delhi":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Cochin = 0
        Hyderabad = 0
        New_Delhi = 1



    destination = st.selectbox("Destination", ["Chennai","Delhi","Kolkata","Mumbai","Cochin","Delhi","Hyderabad","Kolkata","New Delhi"])
    if destination=="Chennai":
        Chennai=1
        Delhi=0
        Kolkata=0
        Mumbai=0
        Cochin=0
        Hyderabad=0
        New_Delhi=0
    elif destination=="Delhi":
        Chennai=0
        Delhi=1
        Kolkata=0
        Mumbai=0
        Cochin=0
        Hyderabad=0
        New_Delhi=0
    elif destination == "Kolkata":
        Chennai = 0
        Delhi = 0
        Kolkata = 1
        Mumbai = 0
        Cochin = 0
        Hyderabad = 0
        New_Delhi = 0
    elif destination == "Mumbai":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 1
        Cochin = 0
        Hyderabad = 0
        New_Delhi = 0
    elif destination == "Cochin":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Cochin = 1
        Hyderabad = 0
        New_Delhi = 0
    elif destination == "Hyderabad":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Cochin = 0
        Hyderabad = 1
        New_Delhi = 0
    elif destination == "New Delhi":
        Chennai = 0
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Cochin = 0
        Hyderabad = 0
        New_Delhi = 1

    duration_hour=abs(arrival_hour-Departure_hour)
    duration_min=abs(arrival_min-Departure_min)




    if st.button("PREDICT 😎"):
        result=model.predict([[Journey_day,Journey_month,Departure_hour,Departure_min,arrival_hour,arrival_min,Total_Stops,Jet_Airways,IndiGo,Air_India,SpiceJet,Vistara,Air_Asia,GoAir,Multiple_carriers_Premium_economy,Jet_Airways_Bussiness,Vistara_Premium_economy,Truejet,Chennai,Delhi,Kolkata,Mumbai,Cochin,Delhi,Hyderabad,Kolkata,New_Delhi,duration_hour,duration_min]])
        st.header("your flight fare is Rs. {} 🥳".format(int(result)))




if __name__=='__main__':
    main()
