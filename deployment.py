import streamlit as st

st.title("Deployment of ML Models")

def main():


    tab_contents = ["US Agriculture Exports", "Hello World", ""]

    # Create a tabs object
    tabs = st.container()

    # Create columns for the tabs
    col1, col2, col3 = st.columns(len(tab_contents))

    with tabs:
        col1.write("Datos")
        col2.write("EDA")
        col3.write("Inferencia")



if __name__ == "__main__":
    main()

