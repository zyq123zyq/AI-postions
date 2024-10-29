import streamlit as st

st.title("AI大模型应用产品网")

col,col1 = st.columns(2)
with col:
    st.image("https://d00.paixin.com/thumbs/1742172/20214169/staff_1024.jpg",use_column_width=True)
    flag = st.button("说道",use_container_width=True)
    if flag:
        st.switch_page("pages/demo03.py")

with col1:
    st.image("https://d00.paixin.com/thumbs/1742172/20214169/staff_1024.jpg",use_column_width=True)
    flag1 = st.button("绘图",use_container_width=True)
    if flag1:
        st.switch_page("pages/textToImage.py")