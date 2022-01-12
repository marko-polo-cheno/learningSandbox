from src.churn_app import run_app
from src.churn_model import create_pickle

# streamlit run C:/Users/markz/PycharmProjects/streamlit_learning/main.py
if __name__ == '__main__':
    create_pickle()
    run_app()
