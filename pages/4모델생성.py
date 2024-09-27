import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime
from sklearn import tree
from sklearn import svm
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import seaborn  as sns
import matplotlib.pyplot as plt


st.title("모델 생성하기")

st.write("학습데이터로 모델을 만들어봅시다.")


data = st.session_state['dataset'].copy()
data_test = st.session_state['data_test'].copy()

train = data.drop(['class'],axis=1)
target = data['class']
data_test_test = data_test.drop(['class'],axis=1)
data_test_target = data_test['class']
data_test_test = data_test_test.reindex(columns=train.columns, fill_value=0)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

    
# if st.button("이전 단계로"):
#     reload()

if 'dataset' in st.session_state:
    st.write("의사결정 트리 모델생성")
    st.caption("의사결정트리는 가지치기를 이용하여 분류하는 알고리즘입니다. 이제 가지의 특징을 세팅하여 모델을 만들어봅시다.")

    with st.form("model gen"):
        criterion = st.selectbox("모델 선택",["gini", "entropy"],)
        depth = st.number_input("나무 깊이", step=1, min_value=2, max_value=10)
        min_samples_split = st.number_input("최소 샘플 개수", step=1, min_value=2, max_value=100)
        button = st.form_submit_button("모델 생성")
        if button:
            dt = tree.DecisionTreeClassifier(criterion=criterion , max_depth=depth, min_samples_split =min_samples_split)
            dt.fit(train, target)
            st.session_state["model"] = dt
            
            pred = dt.predict(train)
            accuracy = accuracy_score(target, pred)
            st.write(f"의사결정 트리 학습데이터 정확도는 {round(accuracy,5)}입니다.")
            
            pred_test = dt.predict(data_test_test)
            accuracy_test = accuracy_score(data_test_target, pred_test)
            st.write(f"의사결정 트리 테스트 데이터 정확도는 {round(accuracy_test,5)}입니다.")
            
            cm = confusion_matrix(target, pred)
            fig,ax = plt.subplots(figsize=(5, 5))
            sns.heatmap(cm, annot=True, linewidths=0.5,linecolor="red", fmt= '.0f',ax=ax)
            st.pyplot(fig)
            
            st.write(f"독버섯을 피한 경우는 {cm[1,1]}")
            st.write(f"식용버섯을 골라 먹은 경우는 {cm[0,0]}")
            st.write(f"독버섯인데 먹을 경우는 {cm[1,0]}")
            st.write(f"식용버섯인데 안먹을 경우는 {cm[0,1]}")
            score = round((cm[1,1] + cm[0,0] - 5* cm[1,0])/4785,3)
            st.write(f"총점은 {score*100}점 입니다.")
            
            