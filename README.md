# 📊 Advertising Sales Prediction

### Predict product sales using advertising budgets and Machine Learning

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Live-brightgreen)](https://advertising-sales-prediction-01.streamlit.app/)

🚀 **Live Demo:** [Try Advertising Sales Prediction](https://advertising-sales-prediction-01.streamlit.app/)

---

## 📌 About the Project

**Advertising Sales Prediction** is a Machine Learning web application that estimates product sales based on advertising budgets allocated to three channels:

- 📺 TV Advertising
- 📻 Radio Advertising
- 📰 Newspaper Advertising

The application uses a trained Linear Regression model to analyze the advertising budget inputs and predict the expected sales. It provides a simple, interactive interface built with Streamlit.

This project demonstrates how Machine Learning can be applied to a regression problem and deployed as a web application.

## ✨ Features

- 📊 Predict sales from TV, Radio, and Newspaper advertising budgets.
- 🤖 Use a trained Linear Regression model.
- ⚡ Get predictions through an interactive web interface.
- ✍️ Enter budgets using clear input placeholders.
- ✅ Validate inputs before making predictions.
- 🌐 Access the application online through Streamlit Community Cloud.
- 💻 Run the project locally on your computer.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical operations |
| Pandas | Dataset handling and analysis during model development |
| Scikit-learn | Feature scaling and machine learning utilities |
| Joblib | Saving and loading the trained model |
| Streamlit | Interactive web application |
| Git & GitHub | Version control and project hosting |

## 🧠 Machine Learning Workflow

1. **Dataset:** Use advertising data containing TV, Radio, and Newspaper budgets along with Sales.
2. **Preprocessing:** Standardize the input features using `StandardScaler`.
3. **Model training:** Train a Linear Regression model using Gradient Descent.
4. **Evaluation:** Evaluate performance using MAE, MSE, RMSE, and R².
5. **Model persistence:** Save the trained model components in `sales_model.pkl`.
6. **Deployment:** Load the saved model in Streamlit and make predictions from user inputs.

## 📈 Model Performance

The following results were obtained during model evaluation:

| Metric | Result |
|---|---:|
| Training MSE | 2.6761 |
| Test MAE | 1.2748 |
| Test MSE | 2.9078 |
| Test RMSE | 1.7052 |
| Test R² Score | 0.9059 |

The test R² score of approximately **0.906** indicates that the model explains about 90.6% of the variation in sales on the test dataset.

*These metrics describe the model evaluation results from the development workflow. Results may vary if the dataset, split, preprocessing, or model is changed.*

## 🖥️ How to Use the Application

1. Open the [live application](https://advertising-sales-prediction-01.streamlit.app/).
2. Enter your TV advertising budget.
3. Enter your Radio advertising budget.
4. Enter your Newspaper advertising budget.
5. Click **Predict Sales**.
6. View the estimated sales prediction.

### Example Input

| Advertising Channel | Budget |
|---|---:|
| TV | 150 |
| Radio | 30 |
| Newspaper | 20 |

**Example predicted sales:** approximately `16.01` using the current saved model.

*The prediction is an estimate based on the trained model, not a guarantee of actual sales.*

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/manishxcode01/Advertising-Sales-Prediction.git
```

### 2. Navigate to the project directory

If the files are in the `Desktop/Sales_model` folder within the repository, run:

```bash
cd Advertising-Sales-Prediction/Desktop/Sales_model
```

If your files are located directly in the repository root, run:

```bash
cd Advertising-Sales-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

### 5. Open the local app

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

**Note:** Keep `sales_model.pkl` in the same directory as `app.py`. The model file must be present for the application to run.

## 📁 Project Structure

```text
Advertising-Sales-Prediction/
├── app.py
├── sales_model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

*The structure above represents the intended project layout. If your GitHub repository currently places these files inside `Desktop/Sales_model/`, use that subdirectory when running the app.*

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building a regression-based Machine Learning solution.
- Understanding feature scaling and model prediction.
- Evaluating a model using regression metrics.
- Saving and loading trained model components.
- Building an interactive application using Streamlit.
- Deploying a Machine Learning project to the cloud.
- Managing code and project files using Git and GitHub.

## 🔮 Future Improvements

- 📈 Add interactive visualizations of advertising budgets and predicted sales.
- 📊 Compare multiple regression algorithms.
- 🧪 Add more detailed model evaluation and validation.
- 📂 Allow users to upload a CSV file for batch predictions.
- 🎨 Improve the UI with charts, prediction summaries, and a more polished layout.

## 👨‍💻 Author

**Manish Kumar**

B.Tech Computer Science Engineering Student | Aspiring Software Engineer | DSA & C++ | AWS & AI/ML Enthusiast

- **GitHub:** [@manishxcode01](https://github.com/manishxcode01)
- **Project Repository:** [Advertising-Sales-Prediction](https://github.com/manishxcode01/Advertising-Sales-Prediction)
- **Live Application:** [Try it here](https://advertising-sales-prediction-01.streamlit.app/)

---

⭐ If you find this project useful, consider giving the repository a star!

*Built as a hands-on project to explore Machine Learning, Python, and web application deployment.*
