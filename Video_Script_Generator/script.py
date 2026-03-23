import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.prompts import ChatPromptTemplate
from openai import RateLimitError


# 定义一个生成视频脚本的函数(generate_script),参数为视频主题(subject),视频时长(duration),创造性(creativity),用户的密钥(key)
def generate_script(subject, duration, creativity, key):
    try:
        title_template = ChatPromptTemplate.from_messages(
            [
                ("human", "请结合{subject}主题，输出一个吸引用户流量的标题")
            ]
        )
        script_template = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个短视频频道的博主，可以根据标题及相关信息，输出视频脚本"),
                ("human",
                 """视频脚本包括标题和内容。
                 标题{title}需新颖，可包含常见表情符号，且符合主题。
                 内容需考虑以下部分：
                 首先，内容的字数限制需结合用户输入的视频时长{video_time}分钟判断；
                 其次，内容的描述格式按照【开头】\n【中间】\n【结尾】分隔。
                 开头围绕主题展开叙述。中间补充相关的干货内容，表述详尽。结尾呼应前文，给出用户思考。
                 内容风格幽默风趣，面向群体是95后的上班族。
                 最后，内容需结合维基百科的查询结果，仅作参考，对查询的不相关内容进行忽略，查询内容用三个#符号包围。
                 ### {wikipedia_search} ### """)
            ]
        )
        model = ChatOpenAI(openai_api_key=key,
                           temperature=creativity,
                           base_url="https://api.aigc369.com/v1"
                           )
        title_chain = title_template | model
        script_chain = script_template | model
        title = title_chain.invoke({"subject": subject}).content
        search = WikipediaAPIWrapper(lang="zh")
        search_result = search.run(subject)
        script = script_chain.invoke(
            {"title": title, "video_time": duration, "wikipedia_search": search_result}).content
        return search_result, title, script
    except RateLimitError as e:
        print("API调用超出配额限制，请检查账户计划和账单详情。")
        print(e)
        return None


# print(generate_script("布偶猫", 2,1, "sk-proj-SK7HxPRm4BqT7Gt9seZST3BlbkFJK3xiPI5dLgjxhHv5oTi0"))
print(generate_script("布偶猫", 2, 1, os.getenv("OPENAI_API_KEY")))
