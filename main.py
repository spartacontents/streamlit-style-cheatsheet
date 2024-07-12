import streamlit as st

# 코드 묶음
code_title = '''# 코드스니펫 - 제목 
st.title('[스파르타] Streamlit Style Cheatsheet')'''

code_text = '''# 코드스니펫 - 글쓰기
st.write(':red[색 강조] *글씨 기울임꼴* :blue-background[배경색 넣기] :이모지:')
st.write(':red[sparta] *codingclub* is :blue-background[best] :sunglasses:')
st.write("숫자만 넣으면 알아서 배경색이 생겨요 --> ", 1234)
'''

code_button = '''# 코드스니펫 - 버튼
st.button('그냥 버튼')
if st.button('노크하기'):
    st.write('여기 사람 있어요')'''

code_slider = '''# 코드스니펫 - 슬라이더
age = st.slider("당신은 몇 살인가요?", 0, 130, 25) # 문자/최솟값/최댓값/첫 표시 값
st.write("저는 ", age, "살 입니다!")
'''

code_form = ''' #코드스니펫 - 폼
col1, col2 = st.columns(
    2)  # 두 개의 컬럼 생성. 표현하고 싶은 내용을 열 데이터로 나눠 보여주고 싶을 떄 사용합니다.

with col1:
    text1 = st.text_input("form을 이용하지 않는 경우")
    text2 = st.text_area("form을 이용하지 않는 경우")
    st.write("1번 입력값: " + text1)
    st.write("2번 입력값: " + text2)

with col2:
    with st.form("form을 사용합니다"):
        text3 = st.text_input("form을 이용하는 경우")
        text4 = st.text_area("form을 이용하는 경우")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.write("1번 입력값: " + text3)
            st.write("2번 입력값: " + text4)
        else:
            st.write("1번 입력값: ")
            st.write("2번 입력값: ")
'''

code_option = '''#코드스니펫 - 옵션
option = st.selectbox("연락을 어떻게 받고 싶으신가요??", ("이메일", "유선 통화", "문자"))
st.write("선택한 방식:", option)
'''

# 예제 0
st.title('[스파르타] Streamlit Style Cheatsheet')
st.code(
    '이 페이지는 명령어와 예제로 구성되어 있습니다.\n각 코드스니펫의 내용을 확인하고 코드 블럭 오른쪽의 복사 버튼을 누르고 붙여 넣어 보세요!'
)
st.markdown(
    '''만약 더 궁금한 것이 있다면 [👉링크👈](https://docs.streamlit.io/develop/api-reference)로 들어가보세요!'''
)
st.divider()
st.write('\n')
st.code(code_title)
st.caption('예제 0 - st.title()로 제목을 작성하세요 :sunglasses:')
st.write('\n')
st.divider()

# 예제 1
st.write('\n')
st.write(' :red[색 강조] *글씨 기울임꼴* :blue-background[배경색 넣기] :이모지:')
st.write(' :red[sparta] *codingclub* is :blue-background[best] :sunglasses:')
st.write("숫자만 넣으면 알아서 배경색이 생겨요 --> ", 1234)
st.write('\n')

st.code(code_text)
st.caption('예제 1 - st.write()를 쓰면 글씨를 쓸 수 있어요')
st.write('\n')
st.divider()

# 예제 2
st.write('\n')
st.button('그냥 버튼')
if st.button('노크하기'):
    st.write('여기 사람 있어요')
st.code(code_button)
st.caption('예제 2 - st.button()으로 버튼을 만들 수 있습니다.')
st.caption('클릭했을 때 나오는 행동도 만들 수 있습니다.')
st.write('\n')
st.divider()

# 예제 3
st.write('\n')
age = st.slider("당신은 몇 살인가요?", 0, 130, 25)
st.write("저는 ", age, "살 입니다!")
st.code(code_slider)
st.caption('st.slider()로 숫자 값을 선택할 수 있어요.')
st.caption('슬라이더에서 찍은 값을 저장하고 데이터로 활용할 수 있습니다.')
st.write('\n')
st.divider()

# 예제 4
st.write('\n')
st.write('\n')
col1, col2 = st.columns(
    2)  # 두 개의 컬럼 생성. 표현하고 싶은 내용을 열 데이터로 나눠 보여주고 싶을 떄 사용합니다.

with col1:
    text1 = st.text_input("form을 이용하지 않는 경우")
    text2 = st.text_area("form을 이용하지 않는 경우")
    st.write("1번 입력값: " + text1)
    st.write("2번 입력값: " + text2)

with col2:
    with st.form("form을 사용합니다"):
        text3 = st.text_input("form을 이용하는 경우")
        text4 = st.text_area("form을 이용하는 경우")
        submitted = st.form_submit_button("제출")

        if submitted:
            st.write("1번 입력값: " + text3)
            st.write("2번 입력값: " + text4)
        else:
            st.write("1번 입력값: ")
            st.write("2번 입력값: ")

st.code(code_form)
st.caption('st.form()을 사용하여 여러 요소를 묶어 보여줄 수 있어요.')
st.caption('폼을 사용하면 여러 값을 입력하고 버튼을 눌러 한 번에 값을 담아 받을 수 있어요')
st.write('\n')
st.divider()

# 예제 5
st.write('\n')
option = st.selectbox("연락을 어떻게 받고 싶으신가요??", ("이메일", "유선 통화", "문자"))
st.write("선택한 방식:", option)
st.code(code_option)
st.caption('예제 5 - st.selectbox()로 선택지를 만들 수 있어요.')
