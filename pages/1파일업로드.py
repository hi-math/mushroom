import streamlit as st
import pandas as pd

if 'dataset' not in st.session_state:
    st.session_state['dataset'] = pd.DataFrame()
if 'dataset_raw' not in st.session_state:
    st.session_state['dataset_raw'] = pd.DataFrame()


dataset = pd.read_csv("mushrooms.csv")    
st.session_state['dataset'] = dataset
st.session_state['dataset_raw'] = dataset
st.session_state['data_test'] = pd.read_csv("mushrooms_test.csv")


st.title("데이터 관찰 확인하기")

st.write("독버섯과 관련된 데이터를 확인해봅시다.")

st.dataframe(dataset[0:50])

st.write("codap을 이용하여 데이터를 확인하고 다음 물음에 답해봅시다.")
st.link_button("codap열기", "https://codap.concord.org/app/static/dg/ko/cert/index.html")

import streamlit as st

tab1, tab2, tab3, tab4, tab5 = st.tabs(["1번", "2번", "3번", "4번", "5번"])
answer = {1:"",
          2:"",
          3:"",
          4:"",
          5:""}

with tab1:
    
    st.header("문제 1")
    st.write("버섯은 식용버섯과 독버섯 두 가지로 구분된다.")
    q1 = st.radio("1",
                  ["Y", "N"],
                  label_visibility="hidden", 
                  key=1)
    answer[1]=q1
    
with tab2:
    
    st.header("문제 2")
    st.write("버섯 서식지 중에는 숲에 서식하는 버섯이 가장 많다.")
    q2 = st.radio("2",
                  ["Y", "N"],
                  label_visibility="hidden",
                  key=2)
    answer[2]=q2
    
with tab3:
    
    st.header("문제 3")
    st.write("독버섯은 대체로 상처가 있다.")
    q3 = st.radio("3",
                  ["Y", "N"],
                  label_visibility="hidden",
                  key=3)
    answer[3]=q3
    
with tab4:
    
    st.header("문제 4")
    st.write("냄새는 식용버섯과 독버섯을 구분하는데 유용한 정보이다.")
    q4 = st.radio("4",
                  ["Y", "N"],
                  label_visibility="hidden",
                  key=4)
    answer[4]=q4
    
with tab5:
    
    st.header("문제 5")
    st.write("쓰레기장에서 자란 버섯은 독버섯이다.")
    q5 = st.radio("5",
                  ["Y", "N"],
                  label_visibility="hidden",
                  key=5)
    answer[5]=q5

if st.button("정답 확인!"):
    right = 0
    if answer[1]=="Y":
        right += 1
    if answer[2]=="Y":
        right += 1
    if answer[3]=="N":
        right += 1
    if answer[4]=="Y":
        right += 1
    if answer[5]=="N":
        right += 1
    
    if right!=5:
        st.write(f"정답은 {right}개 입니다. 다시 도전해보세요.")
    
    else:
        st.write("모두 정답입니다. 다음페이지로 이동해보세요!")
        if st.button("다음 페이지로", key=10):
            st.switch_page("pages/2데이터전처리1.py")
            
