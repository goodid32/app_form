import streamlit as st
import datetime
import sqlite3
import pandas as pd
import os.path

file_path = os.path.dirname(__file__)
db_file_path = os.path.join(file_path, 'users.db')


con = sqlite3.connect(db_file_path)
cur = con.cursor()

st.subheader('회원가입 폼')

with st.form('my_form', clear_on_submit=True):
    st.info('다음 양식을 모두 입력 후 제출합니다.')
    uid = st.text_input('아이디', max_chars=12)
    uname = st.text_input('이름', max_chars=10)
    upw = st.text_input('비밀번호', type='password')
    upw_chk = st.text_input('비밀번호 확인', type='password')
    ubd = st.date_input('생년월일', min_value=datetime.date(1930,1,1))
    ugender = st.radio('성별', options=['남', '여'], horizontal=True)

    submitted = st.form_submit_button('제출')
    if submitted:
        if len(uid) < 6:
            st.warning('아이디는 6글자 이상이어야 합니다!')
            st.stop()

        if upw != upw_chk :
            st.warning('비밀번호가 일치하지 않습니다!!')
            st.stop()

        cur.execute(f"INSERT INTO users ("
                    f"uid,"
                    f"uname,"
                    f"upw,"
                    f"ubd,"
                    f"ugender) VALUES ("
                    f"'{uid}','{uname}','{upw}',"
                    f"'{ubd}','{ugender}')")
        con.commit()

        st.success(f'{uid} {uname} {upw} {upw_chk} {ubd} {ugender}')

st.subheader('회원가입 폼')

df =pd.read_sql('SLECT * FROM user', con)
st.dataframe(df)
