import streamlit as st

# 코드 묶음
code_title = '''# 코드스니펫 - 제목 
st.title('[스파르타] Streamlit Style Cheatsheet')'''

code_text = '''# 코드스니펫 - 글쓰기
st.write(':red[색 강조] *글씨 기울임꼴* :blue-background[배경색 넣기] :이모지:')
st.write(':red[sparta] *codingclub* is :blue-background[best] :sunglasses:')
st.write("숫자만 넣으면 알아서 배경색이 생겨요 --> ", 1234)
'''

code_input = '''# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")
'''

code_button = '''# 코드스니펫 - 버튼
st.button('그냥 버튼')
if st.button('노크하기'):
    st.write('여기 사람 있어요')'''

code_slider = '''# 코드스니펫 - 슬라이더
age = st.slider("당신은 몇 살인가요?", 0, 130, 25) # 문자/최솟값/최댓값/첫 표시 값
st.write("저는 ", age, "살 입니다!")
'''

code_option = '''#코드스니펫 - 옵션
option = st.selectbox("연락을 어떻게 받고 싶으신가요??", ("이메일", "유선 통화", "문자"))
st.write("선택한 방식:", option)
'''

code_image = '''# 코드스니펫 - 이미지
st.image(
    "https://images.unsplash.com/photo-1709148910322-5a58adaf0e9d?q=80&w=1981&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
)
'''

code_spinner = '''# 코드스니펫 - 스피너
import time
import streamlit as st

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
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
keyword = st.text_input("키워드를 입력하세요.")
st.code(code_input)
st.caption('예제 2 - st.text_input()를 쓰면 입력창을 만들 수 있어요')
st.caption('괄호 안에 입력 값을 넣으면 입력창 위에 표시할 수 있어요')
st.write('\n')
st.divider()

# 예제 3
st.write('\n')
st.button('그냥 버튼')
if st.button('노크하기'):
    st.write('여기 사람 있어요')
st.code(code_button)
st.caption('예제 3 - st.button()으로 버튼을 만들 수 있습니다.')
st.caption('클릭했을 때 나오는 행동도 만들 수 있습니다.')
st.write('\n')
st.divider()

# 예제 4
st.write('\n')
age = st.slider("당신은 몇 살인가요?", 0, 130, 25)
st.write("저는 ", age, "살 입니다!")
st.code(code_slider)
st.caption('예제 4 - st.slider()로 숫자 값을 선택할 수 있어요.')
st.caption('슬라이더에서 찍은 값을 저장하고 데이터로 활용할 수 있습니다.')
st.write('\n')
st.divider()

# 예제 5
st.write('\n')
option = st.selectbox("연락을 어떻게 받고 싶으신가요??", ("이메일", "유선 통화", "문자"))
st.write("선택한 방식:", option)
st.code(code_option)
st.caption('예제 5 - st.selectbox()로 선택지를 만들 수 있어요.')
st.write('\n')
st.divider()

# 예제 6
st.write('\n')
st.image(
    "https://images.unsplash.com/photo-1709148910322-5a58adaf0e9d?q=80&w=1981&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
)
st.code(code_image)
st.caption('예제 6 - st.image()로 이미지를 화면에 그릴 수 있어요.')
st.caption('괄호 안에는 이미지 파일이나 이미지 주소가 들어가야 해요.')
st.write('\n')
st.divider()

# 예제 7
import time
import streamlit as st

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.code(code_spinner)
st.caption('예제 7 - st.spinner()로 빙글빙글 돌아가는 대기 애니메이션을 구현할 수 있어요')
st.caption('버튼을 눌러 스피너가 돌아가게 만들 수도 있어요!')

if st.button('다시보기'):
    st.spinner('다시 돌아가는 중...')
