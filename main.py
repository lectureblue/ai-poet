from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
import os
import streamlit as st

# load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

st.title("_AI 시인_ :sunglasses:")

title = st.text_input("시의 주제를 입력하세요", "눈사람")
st.write("시의주제 ", title)
if st.button("시 작성"):
    with st.spinner("Wait for it..."):
      llm = init_chat_model(
        "gpt-4o-mini",
        api_key = api_key
      )
      # result = llm.invoke('Hello')
      # 프롬프트 템플릿 생성
      prompt = ChatPromptTemplate.from_messages([
        ("system","You are a helpful assistant"),
        ("user","{input}")
        ])
      # chain = prompt | llm
      # result = chain.invoke({"input":"안녕하세요"})

      # 문자열 출력파서
      output_parser = StrOutputParser()
      chain = prompt | llm | output_parser
      result = chain.invoke({"input": title+"에 대한 시를 생성해줘"})
      st.write(result)