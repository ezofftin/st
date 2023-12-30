#
# 상태표시 예시.
#

# Streamlit 라이브러리를 불러온다.
import streamlit as st

# Time 라이브러리를 불러온다.
import time

# Progress 바로 상태 표시.
st.progress(value=20)
''                              
'---'
''

# 풍선, 눈송이 등과 같은 특수 효과.
# st.balloons( ) # 풍선
# st.snow( )

# 다양한 상태표시 출력. 
# 주의: icon은 한개의 문자로 입력해야 한다!
st.error('오류 메시지' , icon='😰' )
st.warning( '경고 메시지', icon='⚠️' )
st.info( '공지' , icon='ℹ')
st.success( '성공 메시지', icon='😊')
''                              
'---'
''

# Spinner로 실행중 상태 표시.
with st.spinner(text = '실행중...' ):
    time.sleep(3.0)
    st.success( '종료!', icon='😊' )
