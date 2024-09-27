import streamlit as st
import pandas as pd

st.image("img/main.png")

if 'name' not in st.session_state:
    st.session_state['name'] = ""
if 'name' not in st.session_state:
    st.session_state['name'] = ""
if 'name' not in st.session_state:
    st.session_state['name'] = ""
if 'name' not in st.session_state:
    st.session_state['name'] = ""

st.write("이 프로젝트에서 사용할 이름을 입력해주세요.")

name = st.text_input("name")

if name:
    st.session_state["name"] = name
    st.caption(f"{st.session_state["name"]}님 환영합니다.")


if st.button("페이지 이동하기") and st.session_state["name"] != "":
    st.switch_page("pages/1파일업로드.py")
