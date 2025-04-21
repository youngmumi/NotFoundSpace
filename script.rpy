# 이 파일에 게임 스크립트를 입력합니다.
define config.overlay_screens = [ ]

define config.has_autosave = True
define autosave_on_choice = True

# 여기에서부터 게임이 시작합니다.
label start:

    scene war_background with fade

    "우리는 행복해진 순간마다 잊는다. 누군가가 우리들을 위해 피를 흘렸다는 것을\n -프랭클린 D 루즈벨트"

    "전쟁이 일어나고, 종전 후에 단 두 나라만이 살아 남았습니다."

    "공산주의 A나라와 민주주의 B나라."

    python:
        add_note("세계관 설정", "세계 3차 대전이 일어나고 종전 후 두 나라만이 살아 남았다.")
        add_note("세계관 설정", "세상에는 공산주의 A나라와 민주주의 B나라만 존재한다.")

    scene black with fade

    "당신은 B나라의 연구원입니다."

    $ player = renpy.input("당신의 이름은 무엇인가요?")

    if player == "":
        $ player = "주인공"

    "[player]님. 당신의 선택에 따라 미래는 물론 과거가 결정됩니다."

    "기억하세요. 누군가가 피를 흘렸기에 당신이 행복하다는 걸."

    "그리고 당신이 희생해야 누군가가 행복하다는 걸."

    $ chapter = 0

    call ch0

    $ chapter = 1

    call ch1

    return
