import os
import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate word cloud
def generate_wordcloud(data, column, sentiment_filter=None):
    try:
        if sentiment_filter:
            data = data[data['sentiment'] == sentiment_filter]
        text = " ".join(data[column].astype(str).dropna())
        wordcloud = WordCloud(width=800, height=400, max_words=100, background_color="white").generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error generating word cloud: {e}")

# Function to load dataset
@st.cache_data
def load_data(uploaded_file):
    try:
        return pd.read_csv(uploaded_file, on_bad_lines='skip')
    except pd.errors.ParserError:
        st.error("Error loading dataset: The file contains invalid or inconsistent rows.")
        return None
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

# Function to generate insights using OpenAI GPT
def generate_insights(question, data):
    try:
        preview = data.head().to_string()
        prompt = f"Dataset preview:\n{preview}\n\nQuestion: {question}\n\nProvide detailed insights based on the dataset."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data analysis assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        st.error(f"Failed to generate insights: {e}")
        return "No insights available."

# Streamlit app
def main():
    st.title("Open Data Analysis Platform")
    st.write("Upload any dataset to explore insights and visualizations!")

    # Dataset upload
    uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])

    if uploaded_file:
        # Load the dataset
        data = load_data(uploaded_file)

        if data is not None:
            st.write("### Dataset Preview")
            st.dataframe(data.head())

            # Sentiment Distribution
            if 'sentiment' in data.columns:
                st.write("### Sentiment Distribution")
                st.bar_chart(data['sentiment'].value_counts())
            else:
                st.warning("The dataset does not contain a 'sentiment' column.")

            # Generate Word Cloud
            st.write("### Word Cloud")
            sentiment_filter = st.selectbox(
                "Filter by sentiment (optional):", 
                options=["All"] + (list(data['sentiment'].unique()) if 'sentiment' in data.columns else [])
            )
            if sentiment_filter == "All":
                generate_wordcloud(data, 'title_clean' if 'title_clean' in data.columns else 'title')
            else:
                generate_wordcloud(data, 'title_clean' if 'title_clean' in data.columns else 'title', sentiment_filter=sentiment_filter)

            # Timeline Insight
            if 'date' in data.columns and 'sentiment' in data.columns:
                try:
                    data['date'] = pd.to_datetime(data['date'], errors='coerce')
                    sentiment_trend = data.groupby(data['date'].dt.date)['sentiment'].value_counts().unstack()
                    st.write("### Sentiment Trend Over Time")
                    st.line_chart(sentiment_trend)
                except Exception as e:
                    st.warning("Could not generate timeline insight: Ensure 'date' column is properly formatted.")

            # Dataset Summary
            st.write("### Dataset Summary")
            st.write(data.describe(include='all'))

            # AI-Powered Insights
            st.write("### AI-Powered Insights")
            question = st.text_input("Ask a question about the dataset:")
            if st.button("Generate Insights"):
                with st.spinner("Generating insights..."):
                    insights = generate_insights(question, data)
                st.write(insights)
    else:
        st.info("Please upload a dataset to proceed.")

if __name__ == "__main__":
    main()
