# 스탯
default morality = 0
default sociality = 0
default empathy = 0
default anti_morality = 0

# ch1 선택
default ch1_seeTheMemo = 0



# 퀵 버튼 
screen quick_buttons():
    frame:
        background None  # 배경 제거
        xalign 0.0
        yalign 0.0
        padding (10, 10, 10, 10)
        has vbox

        spacing 15  # 버튼 간의 간격

        textbutton "노트":
            action Show("notebook")
            text_size 35
            style "quick_button_style"  # 개별 버튼 스타일 적용

        textbutton "저장":
            action ShowMenu("save")
            text_size 35
            style "quick_button_style"  # 개별 버튼 스타일 적용

        textbutton "불러오기":
            action ShowMenu("load")
            text_size 35
            style "quick_button_style"  # 개별 버튼 스타일 적용

        textbutton "환경설정":
            action ShowMenu("preferences")
            text_size 35
            style "quick_button_style"  # 개별 버튼 스타일 적용

style quick_button_style:
    background "#c0c5ce"  # 버튼 배경 색상
    color "#000000"  # 버튼 텍스트 색상
    size 30  # 텍스트 크기
    padding (20, 15)  # 버튼 안쪽 여백 (패딩)
    xalign 0.5  # 가로 중앙 정렬
    yalign 0.5  # 세로 중앙 정렬
    hover_background "#4f5b66"  # 호버 시 배경 색상 변경
    
