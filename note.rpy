define config.keymap['toggle_note'] = [ 'n' ]

default clues_by_category = {
    "할일": [],
    "단서": [],
    "타임머신": [],
    "인물 정보": [],
    "세계관 설정": []
}

init python:
    def add_note(category, clue_text):
        if category not in clues_by_category:
            clues_by_category[category] = []
        if clue_text not in clues_by_category[category]:
            clues_by_category[category].append(clue_text)
    def delete_note(category, clue_text):
        if category in clues_by_category and clue_text in clues_by_category[category]:
            clues_by_category[category].remove(clue_text)

style menu_frame:
    background "#c0c5ce"  
    padding (20, 20)   

style textbutton:
    background "#a7adba"  
    color "#343d46"  
    size 30  
    xalign 0.5  
    yalign 1.0  
    ypadding 12  
    xpadding 50   

style text:
    color "#000000"  
    size 30  

screen notebook():

    tag menu

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        has vbox

        text "노트" size 40 color "#000000"  
        vbox:
            spacing 20  
            # 카테고리별로 내용 출력
            for category, clues in clues_by_category.items():
                vbox:
                    spacing 10
                    text "[category]" size 32 color "#343d46" 
                    # 해당 카테고리의 내용 출력
                    for clue in clues:
                        text u"  • " + clue size 26
        textbutton "닫기" action Hide("notebook") xalign 0.5
