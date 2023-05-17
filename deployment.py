import streamlit as st
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Deployment of ML Models")

def getPlot(df):
    fig, ax = plt.subplots(figsize=(15, 5))
    plt.title("Origen de planeta por valor de transporte")

    sns.countplot(x="HomePlanet", data=df, hue="Transported")
    plt.xlabel("HomePlanet")
    plt.ylabel("Cantidad")

    return fig


def main():

    df = pd.read_csv("train.csv")

    model = joblib.load("model.joblib")

    tab1, tab2, tab3 = st.tabs(["Datos", "EDA", "Inferencia"])

    with tab1:
        st.header("Datos")
        st.dataframe(df)

    with tab2:
        st.header("EDA")
        st.pyplot(getPlot(df))

    with tab3:
        st.header("Inferencia")
        room = st.number_input('Room Service', 0)
        food = st.number_input('Food Count', 0)
        shopping = st.number_input('Shopping Mall', 0)
        spa = st.number_input('SPA', 0)

        if st.button("Predict"):
            Predict = model.predict([[room, food, shopping, spa]])
            if Predict[0] == 1:
                st.write("Transported")
            else:
                st.write("Not Transported")



if __name__ == "__main__":
    main()


