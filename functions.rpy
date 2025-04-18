init python:
    def add_note(note_text):
        if note_text not in note_list:
            note_list.append(note_text)

screen quick_buttons():
    vbox:
        xpos 0.03  
        ypos 0.05  
        spacing 10

        textbutton "📓 노트":
            action Show("note_screen")
            text_size 35

        textbutton "⚙ 설정":
            action ShowMenu("preferences")
            text_size 35

        textbutton "💾 저장":
            action ShowMenu("save")
            text_size 35