import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("EDA")

    # File uploader
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)

        # Display the DataFrame
        st.write("### DataFrame:")
        st.write(df)

        # Choose columns for visualization
        selected_columns = st.multiselect("Select columns for visualization", df.columns)

        if selected_columns:
            # Perform explanatory data analysis
            st.write("### Explanatory Data Analysis:")
            visualize_data(df, selected_columns)

def visualize_data(df, selected_columns):
    # Create a pair plot for selected columns
    fig = px.scatter_matrix(df[selected_columns])
    
    # Display the plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
