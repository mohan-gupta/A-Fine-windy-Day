import streamlit as st
import pickle
import numpy as np
import base64

def load_model():
    model_path = "Model/model.pkl"
    loaded_model = pickle.load(open(model_path, 'rb'))
    return loaded_model

def predict(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12):
    X = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12])
    pred = model.predict(X)
    pred = round(pred,2)
    st.markdown("<b>Windmill Generated Power(kW/h)</b> = "+str(pred), unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

contnt = "<p>Switching to renewable energy sources is a great way to reduce dependency on imported fuels and " \
          "increase cost efficiency. It is time we move towards a low-carbon future by embracing solar, hydro," \
         "geothermal energy and so on , to protect mother nature.</p> \
          <p>An efficient energy source that has been gaining popularity around the world is wind turbines. Wind turbines " \
         "generate power by capturing the kinetic energy of the wind. Factors such as temperature, wind direction, " \
         "turbine status, weather, blade length, and so on influence the amount of power generated.</p>"

if __name__ == '__main__':
    st.markdown(
        """
    <style>
    span[data-baseweb="tag"] {
      background-color: white !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    model = load_model()
    add_bg_from_local("bg_img/windmills.jpg")
    st.markdown(f'<h1 style="font-family:sans-serif; color:White;">A Fine Windy Day</h1>',
                unsafe_allow_html=True)

    st.markdown(contnt, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        resistance = st.number_input(label="resistance(ohm)", value=324.104273, format="%.6f")
        motor_torque = st.number_input("motor_torque(N-m)", value=775.757046, format="%.6f")
        blades_angle = st.number_input("blades_angle(°)", value=-99.000000, format="%.6f")
        rotor_torque = st.number_input("rotor_torque(N-m)", value=76.148322, format="%.6f")

    with col2:
        wind_speed = st.number_input("wind_speed(m/s)",value=10.793214, format="%.6f")
        atmospheric_pressure = st.number_input("atmospheric_pressure(Pascal)",value=111185.503086, format="%.6f")
        gearbox_temperature = st.number_input("gearbox_temperature(°C)",value=41.145516, format="%.6f")
        engine_temperature = st.number_input("engine_temperature(°C)", value=41.982697, format="%.6f")

    with col3:
        wind_direction = st.number_input("wind_direction(°)",value=354.104164, format="%.6f")
        shaft_temperature = st.number_input("shaft_temperature(°C)",value=77.944745, format="%.6f")
        area_temperature = st.number_input("area_temperature(°C)",value=26.081614, format="%.6f")
        blade_breadth = st.number_input("blade_breadth(m)", value=0.427621, format="%.6f")

    predict(resistance, motor_torque, blades_angle, rotor_torque,
            wind_speed, atmospheric_pressure, gearbox_temperature, engine_temperature,
            wind_direction, shaft_temperature, area_temperature, blade_breadth)
