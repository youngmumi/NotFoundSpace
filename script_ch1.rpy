label ch1:

    scene black with fade

    show text "CHAPTER 1\n어제의 식물에 오늘의 물을" at truecenter with dissolve
    with Pause(2.5)
    hide text with dissolve

    scene researcherRoom

    mainchar "달라진 건 없는 것 같은데. 정말 과거로 돌아온 게 맞나?"

    "연구실 구석에 다른 사람이 보입니다."

    menu:
        "핸드폰을 꺼내 날짜를 확인한다":
            "당신은 핸드폰을 꺼내 날짜를 확인했습니다."
            "표시된 날짜는 2월 24일입니다."
        "다른 사람에게 날짜를 물어본다":
            $ sociality += 1
            mainchar "저기요, 오늘이 며칠이죠?"
            ramdom_person1 "..."
            mainchar "저 사람에게 나는 보이지 않는 건가?"
            python:
                add_note("타임머신", "과거의 사람에게는 나의 모습이 보이지 않는다.")
            "당신은 핸드폰을 꺼내 날짜를 확인했습니다."
            "표시된 날짜는 2월 24일입니다."

    mainchar "과거의 그 자리로 이동하는 모양이군."
    
    python:
        add_note("타임머신", "타임 머신은 그 자리의 과거로 이동시켜준다.")

    mainchar "책상 위에 있는 메모는 뭐지? 매즈의 메모인 것 같은데."

    menu:
        "메모를 본다":
            $ ch1_seeTheMemo += 1
            $ sociality -= 1
            "메모의 내용: 저거 타면 뭐가 어떻게 될지는 확인 무.\n테스트 대상으로는 [player]가 적합해보임 -> 가족 없음?\n연구원 모두가 동의의"
            python:
                delete_note("인물 정보", "매즈: 나와 함께 근무하는 연구원이다. 타임머신의 정체를 밝혀냈다.")
                add_note("인물 정보", "매즈: 망할 놈.")
            "노트 내용이 변경되었습니다."
        "메모를 보지 않는다.":
            mainchar "프라이버시는 존중하는 게 낫지."

    mainchar "식물에 물을 줘야겠지."

    menu: 
        "식물에 물을 준다.":
            "식물에 물을 주었다."
        "식물에 물을 주지 않는다.":
            $ morality -= 1
            "말라가는 식물이 당신을 원망하는 듯 하다."
        "식물에 'Fuck you'라는 메모를 남긴다." if ch1_seeTheMemo == 1:
                $ morality -= 1
                $ sociality -= 1
                mainchar "엿이나 먹으라지."

    "미션을 완료한 당신은 현재로 돌아가기 위해 타임머신의 버튼을 눌렀다."
    python:
        delete_note("할일", "어제(2월 24일)로 돌아가서 식물에 물을 줘야한다.")
    
    scene black with fade
    scene researcherRoom

    "현재로 돌아왔다."

    return 