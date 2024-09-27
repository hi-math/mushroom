import streamlit as st
import pandas as pd
import time
import pandas as pd
import datetime

st.title("데이터 전처리 1 : 속성 삭제하기")

st.write("결과에 영향을 주지 않는 속성은 오히려 모델을 학습하는데 방해가 됩니다. ")

st.write("모델 학습에 사용될 속성만 남겨봅시다.")


def reload():
    progress_text = "데이터가 변환됩니다. 잠시만 기다리세요."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.rerun()

st.session_state['dataset_ele']=data.copy()


if 'dataset' in st.session_state:
    
    st.session_state['dataset']
    
    data = st.session_state['dataset'].copy()
    data_test = st.session_state['data_test'].copy()
    del_column = st.selectbox("삭제할 속성을 선택하세요", list(data.columns.tolist()), index=None)    
    
    if st.button("삭제하기") and del_column:
        if del_column == "class":
            st.warning("결과 속성은 지울수 없습니다.")
            
        else:
            data.drop(del_column, axis=1, inplace=True)
            data_test.drop(del_column, axis=1, inplace=True)
            
            st.session_state['dataset']=data.copy()
            st.session_state['data_test']=data_test.copy()
            st.session_state['dataset_ele']=data.copy()
            
            st.success('완료되었습니다!', icon="✅")
            reload()
        
if st.button("페이지 이동하기"):
    st.switch_page("pages/3데이터전처리2.py")
