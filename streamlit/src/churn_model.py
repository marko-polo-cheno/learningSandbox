import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

import pickle


def create_pickle():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    df_churn = pd.read_csv(r'C:\Users\markz\PycharmProjects\streamlit_learning\src\telco_churn.csv')

    df_churn = df_churn[['gender', 'PaymentMethod', 'MonthlyCharges', 'tenure', 'Churn']].copy()

    df = df_churn.copy()

    df.fillna(0, inplace=True)

    print(df.head())

    encode = ['gender', 'PaymentMethod']

    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df, dummy], axis=1)
        del df[col]

    df['Churn'] = np.where(df['Churn'] == 'Yes', 1, 0)

    x = df.drop('Churn', axis=1)

    y = df['Churn']

    clf = RandomForestClassifier()
    clf.fit(x, y)

    pickle.dump(clf, open('churn_clf.pkl', 'wb'))
