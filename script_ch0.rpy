label ch0:

    scene room

    "(전화 벨이 울린다)"

    researcher "하하하. 성공했다고!" 

    mainchar "휴일인데 갑자기 왜 그래?"

    researcher "연구실로 와 봐!"

    "당신은 선택을 할 수 있습니다.\n이 선택은 미래에 영향을 미칩니다."

    menu:
        "연구실로 향한다":
            mainchar "알았어. 금방 갈게"
            jump to_researcher

        "휴일을 즐긴다":
            jump vacation

    return

label vacation:
    scene room

    mainchar "미친놈. 나 바빠. 끊어."

    "당신은 휴일을 즐겼다. 앞으로 다가올 일들을 모른채."

    return 

label to_researcher:
    scene researcherRoom

    show researcher

    researcher "왔어?"

    mainchar "무슨 일이야?"

    hide researcher
    show timemachine

    researcher "드디어 타임머신 개발에 성공했어! 하하, 시발 드디어! "

    hide timemachine
    show researcher

    mainchar "근거는?"

    researcher "이런 메모가 적혀왔어."




    return
