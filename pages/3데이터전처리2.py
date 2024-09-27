import streamlit as st
import pandas as pd
import pandas as pd
import datetime
import time

st.title("데이터 전처리 2 : 문자 데이터 변환하기")

st.write("수치데이터가 아닌 것은 처리할 수 없습니다. 그림과 같은 방법으로 처리합니다.")

st.image("img/Get_Dummies.png")

   
data = st.session_state['dataset'].copy()
data_test = st.session_state['data_test'].copy()

def reload():
    progress_text = "잠시후에 데이터가 변환됩니다. 잠시만 기다리세요."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.rerun()
    
# if st.button("이전 단계로"):
#     reload()


st.divider()
st.write("먼저 class를 변환해봅시다. 독버섯이면 1, 아니면 0으로 변환하겠습니다.")
if st.button("변환하기"):
    data['class'] = data['class'].map({'e': 0, 'p': 1})
    data_test['class'] = data_test['class'].map({'e': 0, 'p': 1})
    st.session_state['dataset']=data.copy()
    st.session_state['data_test']=data_test.copy()
    st.success('완료되었습니다!', icon="✅")

if 'dataset' in st.session_state:
    st.session_state['dataset']
    st.write("수치데이터가 아닌 데이터를 변환해봅시다.")
    data = st.session_state['dataset'].copy()
    data_test = st.session_state['data_test'].copy()
    non_numeric_columns = data.select_dtypes(exclude=['number', 'boolean']).columns
    
if st.button("변환하기",  key = 5):
    
    for col in non_numeric_columns:
        data = pd.get_dummies(data, columns=[col], drop_first=True)
        data_test = pd.get_dummies(data_test, columns=[col], drop_first=True)
    
    st.success('완료되었습니다!', icon="✅")
    st.session_state['dataset']=data.astype(int).copy()
    st.session_state['data_test']=data_test.astype(int).copy()
    reload()

if len(non_numeric_columns)==0:
    if st.button("페이지 이동하기"):
        st.switch_page("pages/4모델생성.py")

