import streamlit as st
from script import generate_script

st.title("🎦短视频文案生成器")
with st.sidebar:
    openai_api = st.text_input("请输入OpenAI API密钥", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api_keys)")
subject = st.text_input("💭请输入短视频主题")
time = st.slider("⌛️请确定短视频的时长（分钟）", value=1.0, min_value=0.5, max_value=5.0, step=0.5)
number = st.number_input("🪐请输入视频文案的创造力（数字越大⬆️文案多样,数字越小⬇️文案严谨）", value=1.0, min_value=0.0, max_value=2.1, step=0.1)
submitted = st.button("生成文案")
if submitted and not openai_api:
    st.info("请输入OpenAI API密钥")
    st.stop()
if submitted and not subject:
    st.info("请输入短视频主题")
    st.stop()
if submitted:
    with st.spinner("🤔AI正在思考中......"):
        search_result, title, script = generate_script(subject, time, number, openai_api)
    st.success("短视频文案已生成")
    st.subheader("🔥短视频标题:")
    st.write(title)
    st.subheader("📖短视频文案:")
    st.info(script)
    with st.expander("🔎维基百科查询结果"):
        st.info(search_result)
