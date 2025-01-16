# Open Data Analysis Platform

## Introduction
The **Open Data Analysis Platform** is a powerful and user-friendly solution for analyzing datasets with features like sentiment analysis, word clouds, trend analysis, and AI-powered insights. This platform is tailored for SMEs, researchers, and data enthusiasts who want to derive actionable insights from their data without complex setups.

---

## Features
- **Sentiment Analysis**: Visualize the sentiment distribution in your dataset.
- **Word Clouds**: Generate word clouds to explore frequently used words.
- **Trend Analysis**: Visualize data trends over time.
- **AI-Powered Insights**: Ask custom questions about your data for deeper understanding.

---

## Requirements
To use this project, you need the following dependencies:

```plaintext
streamlit==1.16.0
pandas==1.5.3
matplotlib==3.6.2
wordcloud==1.8.2.2
nltk==3.7
scikit-learn==1.2.0
plotly==5.11.0
altair==4.2.2
```

Install the dependencies using:
```bash
pip install -r requirements.txt
```

---

## Installation
1. Clone the GitHub repository to your local machine:
   ```bash
   git clone https://github.com/rmtariq/OpenDataAnalysisPlatform.git
   cd OpenDataAnalysisPlatform
   ```

2. Remove any previous `.git` folders or conflicts (if applicable):
   ```bash
   rm -rf .git
   git init
   git remote add origin https://github.com/rmtariq/OpenDataAnalysisPlatform.git
   ```

3. Ensure `.gitignore` is properly set up:

```plaintext
# Ignore system files
.DS_Store
Thumbs.db


Commit and push this file:
```bash
git add .gitignore
git commit -m "Added .gitignore"
git push origin main
```

---

## Setting Up the Environment

1. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application
1. Start the Streamlit application:
   ```bash
   streamlit run app2.py
   ```

2. Open the link provided by Streamlit in your browser (e.g., `http://localhost:8501`).

3. Use the interface to upload a dataset in CSV format. Ensure the dataset has the following columns:
   - `Text`: Textual data for analysis.
   - `Sentiment`: Pre-labeled sentiments (optional for advanced analysis).
   - `Date`: Dates for timeline visualizations.

---

## Dataset Example
| Text                        | Sentiment | Date       |
|-----------------------------|-----------|------------|
| "The service was great"     | Positive  | 2025-01-01 |
| "The product quality is bad"| Negative  | 2025-01-02 |

---

## Resolving Potential Errors
- **Missing Dependencies**: If you encounter missing packages, install them manually:
  ```bash
  pip install <package-name>
  ```
  Replace `<package-name>` with the missing package name (e.g., `wordcloud`).

- **Streamlit Errors**: Ensure the `app2.py` script is properly configured and run it from the repository root.

---

## Updating and Pushing Changes
If you make changes to the project, follow these steps:

1. Add and commit your changes:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```

2. Push changes to the repository:
   ```bash
   git push origin main
   ```

---

## Contact Information
If you encounter issues or have questions, feel free to reach out:

- **Name**: Dr. RM Tariqi
- **Email**: [rmtariq@gmail.com](mailto:rmtariq@gmail.com)
- **GitHub**: [GitHub Profile](https://github.com/rmtariq)

---

## Final Checklist
- Verify all dependencies are installed.
- Ensure `.gitignore` excludes unnecessary files.
- Test the application locally to confirm it runs without errors.
- Push all updates to the GitHub repository.

---
