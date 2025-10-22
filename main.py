from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

#ChatOpenAI 초기화
llm = ChatOpenAI(api_key=api_key,model='gpt-4o-mini')


#프롬프트 템플릿 생성
prompt = ChatPromptTemplate.from_messages([
   ("system", "You are a helpful assistant."),
   ("user", "{input}")
])


#문자열 출력 파서
output_parser = StrOutputParser()


#LLM 체인 구성
chain = prompt | llm | output_parser

# content = '가을'
# result = chain.invoke({"input": content + '에 대한 시를 써줘'})
# print(result)

# 제목
st.title("AI 시인")

# 사용자 입력필드 
content = st.text_input("시의 주제를 입력하세요", "가을") # 사용자 입력값
st.write("시의 주제", content) # 결과값 출력

# 시 작성 요청
if st.button('시 작성'):
   with st.spinner("wait for it...."):
      result = chain.invoke({"input": content + '에 대한 시를 써줘'})
      st.write(result)
