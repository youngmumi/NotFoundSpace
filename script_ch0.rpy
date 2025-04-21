label ch0:

    scene room at fullscreen_bg

    centered "2월 25일"

    show cat

    cat "미야옹."

    mainchar "츄르는 더 이상 없어. 요놈아."

    "(전화 벨이 울린다)"

    researcher "드디어 알아냈어." 

    mainchar "휴일인데 갑자기 왜 그래?"

    researcher "연구실로 와 줘."

    python:
        add_note("인물 정보", "[player]: 연구원. 고양이를 키운다. 가족이 없는 무연고자")

    "당신은 선택을 할 수 있습니다.\n이 선택은 미래에 영향을 미칩니다."

    menu:
        "연구실로 향한다":
            mainchar "알았어. 금방 갈게"

            cat "야옹"

            "당신의 고양이가 잘 다녀오라는 듯이 운다."
            jump to_researcher

        "휴일을 즐긴다":
            jump vacation_ending

    return

label vacation_ending:
    scene room at fullscreen_bg

    mainchar "미친놈. 나 바빠. 끊어."

    cat "(당신의 다리를 핥는다)"

    "당신은 휴일을 즐겼다. 앞으로 다가올 일들을 모른채."

    "당신은 앞으로 일어날 일들에 대해 영원히 배제되었습니다."

    "휴가 엔딩 - 엔딩 1"

    return 

label to_researcher:
    scene researcherRoom at fullscreen_bg

    show researcher

    researcher "왔어?"

    mainchar "무슨 일이야?"

    hide researcher
    show timemachine

    researcher "그 기계가 무슨 기계인지 알아냈어. 타임머신인 게 분명해."

    python:
        add_note("인물 정보", "매즈: 나와 함께 근무하는 연구원이다. 타임머신의 정체를 밝혀냈다.")

    hide timemachine
    show researcher

    mainchar "근거는?"

    researcher "(복잡한 수식이 적힌 종이를 보여준다)"

    mainchar "이게 현실적으로 말도 안되는 소리인 건 알지?"

    researcher "우리 일이 언제는 말이 되었나? 그래서 테스트를 하려고 하는데..."

    show researcher at left
    show boss at right

    boss "테스트는 다 마쳤나?"

    researcher "...당연하죠. 테스트 없이 임무를 진행하는 사람이 어딨습니까?"

    boss "정확히 30분 뒤에 임무를 진행하도록 하지."

    hide boss
    show researcher at center

    mainchar "...솔직히 말해. 테스트는 아직이잖아. "

    researcher "아무도 테스트에 지원하지 않아서 말이야. 그래서 그런데 네가 해주는 건 어때?"

    menu:
        "미쳤어?":
            researcher "너무하네."
            jump r_u_crazy

        "미친게 틀림 없군.":
            researcher "너무한 거 아니야?"
            jump r_u_crazy

        "그러지 뭐.":
            $ sociality += 1
            jump test

    return

label r_u_crazy:
    scene researcherRoom at fullscreen_bg

    show researcher   

    mainchar "어느날 갑자기 나타난 이상한 기계에, 제대로 테스트도 안된 상황에,\n비현실적인 '타임머신'이라는 걸 타면서"

    mainchar "뭐, 나 보고 테스트를 해 달라?"

    researcher "무리한 부탁인 건 알아. 하지만 네가 적격자야."

    mainchar "어떤 의미에서?"

    researcher "현장 요원이었다가 갑자기 연구직으로 바꾼 너의 화려한 경력 때문에?"

    mainchar "그건 부정할 순 없고."

    mainchar "아니면, 가족도 없는 무연고자이기 때문은 아니고?"

    researcher "그것도 부정할 순 없지."

    jump test

label test:
    scene researcherRoom at fullscreen_bg
    show researcher   

    mainchar "이제 내가 뭘 해주면 되는 데?"

    researcher "밝혀진 건 아무것도 없어. 이 장치를 들고 버튼을 눌러. 돌아오고 싶을 때도 마찬가지고"
    
    python:
        add_note("타임머신", "어느 날 갑자기 나타난 기계, 밝혀진 건 아무것도 없다. 작동할 때는 버튼을 누른다. 돌아올 때도 마찬가지.")

    mainchar "어떤 테스트를 하고 오면 되는데?"

    researcher "어제 내가 저 식물에 물을 주는 걸 까먹었거든. 물을 줬다면 저 식물이 살아 있겠지."

    researcher "어제, 2월 24일로 돌아가서 저 식물에 물을 주고 와. 그렇다면 저 식물은 살아 있을 거고.\n네가 타임머신을 타고 과거를 건드린다해서 미래가 바뀌는지 말지를 알게되겠지."

    mainchar "좋아."
    
    python:
        add_note("할일", "어제(2월 24일)로 돌아가서 식물에 물을 줘야한다.")

    "노트에 할일이 추가되었습니다. 왼쪽 '노트' 버튼을 눌러 노트를 확인할 수 있습니다."

    mainchar "다녀올게."

    researcher "만약 네가 못 오게 되면 너네 집 고양이는 내가 책임질테니 걱정말고 다녀와."

    hide researcher

    "당신은 타임머신의 버튼을 눌렀다."

    jump ch1

    return