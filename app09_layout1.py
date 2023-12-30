#
# 레이아웃 - Part 1.
#

# Streamlit 라이브러리를 불러온다.
import streamlit as st

# Sidebar안에서 레이아웃을 적용해 본다.
st.sidebar.title('타이틀 - 대')
st.sidebar.header('타이틀 - 중')
st.sidebar.subheader('타이틀 - 소')
st.sidebar.write('''
                              
---

''')

x = st.sidebar.selectbox( '다음 중 한가지 선택' , [ '부먹', '찍먹'] )
st.sidebar.write(f'Selectbox 선택 = {x}')
st.sidebar.write('''
                              
---

''')

c = st.sidebar.color_picker( '컬러 선택' )
st.sidebar.write(f'Color_picker 선택 = {c}')
st.sidebar.write('''
                              
---

''')

# Sidebar 레이아웃을 조금 다른 방법으로 적용해 본다 (with).
# with st.sidebar:
#     st.title('타이틀 - 대')
#     st.header('타이틀 - 중')
#     st.subheader('타이틀 - 소')
#     ''                              
#     '---'
#     ''

#     x = st.selectbox( '다음 중 한가지 선택' , [ '부먹', '찍먹'] )
#     st.write(f'Selectbox 선택 = {x}')
#     ''                              
#     '---'
#     ''

#     c = st.color_picker( '컬러 선택' )
#     st.write(f'Color_picker 선택 = {c}')
# ''                              
# '---'
# ''

# Columns 레이아웃을 적용해 본다.

col1, col2, col3 = st.columns(3)    # 3등분.

with col1:
    st.header(':red[컬럼 1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.header(':green[컬럼 2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header(':blue[컬럼 3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''                              
'---'
''
col1, col2, col3 = st.columns([2,6,2])    # 비율로 자름.

with col1:
    st.header(':red[컬럼 1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.header(':green[컬럼 2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header(':blue[컬럼 3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''                              
'---'
''
# Tabs 레이아웃을 적용해 본다.
tab1, tab2, tab3 = st.tabs(['야옹이', '멍멍이', '부엉이'])

with tab1:
   st.header('야옹~')
   st.image('https://static.streamlit.io/examples/cat.jpg', width=300)

with tab2:
   st.header("멍멍~")
   st.image('https://static.streamlit.io/examples/dog.jpg', width=300)

with tab3:
   st.header('부엉~')
   st.image('https://static.streamlit.io/examples/owl.jpg', width=300)

''                              
'---'
''

# Tabs와 Columns를 조합해 본다.
tab1, tab2 = st.tabs(['왼쪽', '오른쪽'])


with tab1:
    col1, col2, col3 = st.columns(3)    # 3등분.

    with col1:
        st.subheader('야옹이')
        st.image('https://static.streamlit.io/examples/cat.jpg')

    with col2:
        st.subheader('멍멍이')
        st.image('https://static.streamlit.io/examples/dog.jpg')

    with col3:
        st.subheader('부엉이')
        st.image('https://static.streamlit.io/examples/owl.jpg')

with tab2:
    col1, col2, col3 = st.columns([1,1,3])    # 비율로 자름.

    with col1:
        st.subheader('야옹이')
        st.image('https://static.streamlit.io/examples/cat.jpg')

    with col2:
        st.subheader('멍멍이')
        st.image('https://static.streamlit.io/examples/dog.jpg')

    with col3:
        st.subheader('부엉이')
        st.image('https://static.streamlit.io/examples/owl.jpg')