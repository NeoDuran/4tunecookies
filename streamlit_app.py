import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="포춘쿠키 앱",
    page_icon="🥠",
    layout="centered"
)

# 응원 문구 리스트
fortune_messages = [
    "지금까지 고생 많았어! 너의 노력이 빛을 발할 거야. 행운을 빌어!",
    "수능 대박! 찍는 것마다 정답이길!",
    "긴장 풀고, 아는 문제 다 맞히고 와! 넌 할 수 있어!",
    "오늘 너의 운빨, 최고 레벨! 화이팅!",
    "컨디션 조절 잘하고, 마지막까지 힘내! 행운이 함께하길!",
    "정답의 기운이 너에게로! 콕콕 잘 찍어!",
    "네가 쏟은 모든 노력, 행운으로 돌아올 거야! 아자아자!",
    "모르는 문제는 운 좋게 스킵, 아는 문제는 확실하게! 굿럭!",
    "수능 끝나는 벨 울릴 때까지 행운이 가득하길!",
    "최고의 컨디션으로 최고의 결과 만들자! 행운을 빈다!"
]

# 타이틀
st.title("🥠 포춘쿠키 하나 먹어보세요!")
st.subheader("수능 준비로 지친 수험생에게 행운의 포춘 쿠키를 준비했어요.")

st.write("")
st.write("")

# 버튼
if st.button("🥠 포춘쿠키 열어보기", use_container_width=True):
    # GIF 표시를 위한 placeholder 생성
    gif_placeholder = st.empty()
    
    # GIF 표시
    gif_placeholder.markdown(
        """
        <div style="text-align: center;">
            <img src="https://media0.giphy.com/media/v1.Y2lkPTZjMDliOTUycTN5NmdjaTQydnc1MDN1MW9haWZ1aXMxcTU0MGt2NWtoOXl3NXZ6dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4GW0C8HbjJPMOlzpnw/200w.gif" alt="fortune cookie" width="300">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 2-3초 대기
    time.sleep(2.5)
    
    # GIF 제거
    gif_placeholder.empty()
    
    # 랜덤 메시지 선택
    selected_message = random.choice(fortune_messages)
    
    # 결과 표시
    st.write("---")
    st.subheader("🎉 포춘쿠키 확인하기")
    st.success(f"💌 {selected_message}")
    st.balloons()

# 푸터
st.write("")
st.write("")
st.write("")
st.markdown(
    """
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        수험생 여러분, 화이팅! 🍀
    </div>
    """,
    unsafe_allow_html=True
)

