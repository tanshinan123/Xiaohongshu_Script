import streamlit as st
from utils import generate_xiaohongshu

st.header("可乐"
          "的AI写作助手🤖️️")
with st.sidebar:
    key = st.text_input("请输入OpenAI API密钥", type="password")
    st.markdown("[获取OpenAI API密钥>>](https://platform.openai.com/account/api_keys)")

theme = st.text_input("主题💭")
submit = st.button("AI写作")

if submit and not key:
    st.info("请输入OpenAI API密钥")
    st.stop()

if submit and not theme:
    st.info("请输入内容主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力写作中💻..."):
        result = generate_xiaohongshu(theme, key)
    st.divider()
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown("###### 标题1💡")
        st.write(result.titles[0])
        st.markdown("###### 标题2💡")
        st.write(result.titles[1])
        st.markdown("###### 标题3💡")
        st.write(result.titles[2])
        st.markdown("###### 标题4💡")
        st.write(result.titles[3])
        st.markdown("###### 标题5💡")
        st.write(result.titles[4])
    with right_column:
        st.markdown("###### 正文🔥")
        st.write(result.content)
