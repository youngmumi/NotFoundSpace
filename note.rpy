define config.keymap['toggle_note'] = [ 'n' ]

screen quick_note_button():
 frame:
        background "#0008"  # 반투명 검정 배경
        xalign 0.95
        yalign 0.05
        padding (10, 5)

        textbutton "노트":
            action Show("note_screen")
            text_size 20

screen note_screen():
    tag note

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        xmaximum 800
        ymaximum 600

        vbox:
            spacing 15
            text "노트" size 40
            null height 20

            if note_list:
                for note in note_list:
                    text u"• [note]" size 28
            else:
                text "아직 기록된 단서가 없습니다." size 28

            null height 30
            textbutton "닫기" action Hide("note_screen")

