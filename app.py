import streamlit as st

st.subheader('회원가입 폼')

with st.form('my_form', clear_on_submit=True):
    st.info('다음 양식을 모두 입력 후 제출합니다.')
    uid = st.text_input('아이디', max_chars=12)
    uname = st.text_input('이름', max_chars=10)
