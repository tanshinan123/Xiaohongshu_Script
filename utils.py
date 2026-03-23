import os
from prompt_template import system_template_txt, user_template_txt
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
# from xiaohongshu_model import Xiaohongshu
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

def generate_xiaohongshu(theme, key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_txt),
        ("user", user_template_txt)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       api_key=key
                       )
# xiaohongshu_model
    class Xiaohongshu(BaseModel):
        titles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
        content: str = Field(description="小红书的正文内容")

    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result


#print(generate_xiaohongshu("布偶猫", os.getenv("OPENAI_API_KEY")))
