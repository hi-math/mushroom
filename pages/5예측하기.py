import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import seaborn  as sns
import matplotlib.pyplot as plt


st.title("예측하기")

st.write("만든 모델로 예측을 해봅시다.")

data = st.session_state['dataset'].copy()
data_test = st.session_state['data_test'].copy()
train = data.drop(['class'],axis=1)

input_data = {}
dt = st.session_state['model']

data_ele = st.session_state['dataset_ele']

data_col = list(data_ele.columns.tolist())

for n, col in enumerate(data_col[1:]):
    locals()[col] = st.selectbox(col, data_ele[col].unique(), key = n)
    input_data[col] = locals()[col]

input_data_df = pd.DataFrame([input_data])

input_data_df 

if st.button("예측하기") :
    input_data_df_dum = pd.get_dummies(input_data_df)
    input_data_df_label = input_data_df_dum.reindex(columns=train.columns, fill_value=0)
    result = dt.predict(input_data_df_label)
    if result[0]==0:
        st.success("식용버섯입니다.")
    else :
        st.warning("독버섯입니다.")
    