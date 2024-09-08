from PyQt6.QtWidgets import*

from filehelper import *

notes = read_from_file()
print(notes)
app = QApplication([])
window = QWidget()



text_edit = QTextEdit()
list_notes = QListWidget()
list_notes.addItems(notes)
list_notes_lbl = QLineEdit("список заміток")
notes_list = QListWidget()
create_note_btn = QPushButton("створити замітку")
delete_note_btn = QPushButton("видалити замітку")
save_note_btn = QPushButton("зберегти замітку")
list_teg_lbl = QLineEdit("список тегів")
tegs_list = QListWidget()
teg_input = QLineEdit()
add_teg_btn = QPushButton("додати ло замітки")
delete_teg_btn = QPushButton("відкріпити від замітки")
search_note_btn = QPushButton("шукати замітки по теги")



main_line = QHBoxLayout()
main_line.addWidget(text_edit)

v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
h1 = QHBoxLayout()
h1.addWidget(create_note_btn)
h1.addWidget(delete_teg_btn)
v1.addWidget(save_note_btn)
v1.addWidget(list_teg_lbl)
v1.addWidget(tegs_list)
h2 = QHBoxLayout()
h2.addWidget(add_teg_btn)
h2.addWidget(delete_teg_btn)
v1.addWidget(delete_teg_btn)
v1.addWidget(search_note_btn)

main_line.addLayout(v1)



window.setLayout(main_line)
window.show()
app.exec()




def show_note():
    key = list_notes.selectedItems()[0].text()
    text_edit.setText(notes[key])
    text_edit.clear()
    tegs_list.addItems(notes)
    print(key)

def save_note():
    key = notes_list.selectedItems()[0].text()
    notes[key]["текст"] = text_edit.toPlainText()
    write_in_file(notes)

def new_note():
    note_name, ok  = QInputDialog.getText(window,"Створення замітки","Текст замітки")
    if ok == True:
        notes[note_name] = {
            "текст":"",
            "теги":[]
        }

        list_notes.clear()
        list_notes.addItems(notes)
        write_in_file(notes)

def delete_note():
    key = list_notes.selectedItems()[0].text()
    notes.pop(key)
    list_notes.clear()
    list_notes.addItems(notes)
    write_in_file(notes)
delete_note_btn.cklicked.connected(delete_note)

def add_tag():
    note_key = list_notes.selectedItems()[0].texr()
    tag_name, ok  = QInputDialog.getText(window,"Створення тегу","Назва тегу")
    if ok == True:
        notes[note_key]["теги"].append(tag_name)
        tegs_list.clear()
        tegs_list.addItems(notes[note_key]["теги"])
        write_in_file(notes)
add_teg_btn.clicked.connect(add_tag)

def delete_tag():
    note_key = list_notes.selectedItems()[0].text()
    tag_key = tegs_list.selectedItems()[0].text()
    notes[note_key]["теги"].remove(tag_key)
    tegs_list.clear()
    tegs_list.addItems(notes[note_key]["теги"])
    write_in_file(notes)

def search():
    tag_name = list_notes_lbl.text()
    filtered_notes = {}
    if tag_name == "":
        list_notes.clear()
        list_notes.addItems(notes)
    else:
        for element in notes:
            if tag_name in notes[element]["теги"]:
                filtered_notes[element] = notes[element]

        list_notes.clear()
        list_notes.addItems(filtered_notes)
search_note_btn.clicked.connect(search)
button_note_del.clicked.connect(delete_note)
button_note_create.clicked.connect(new_note)
save_note_btn.clicked.connect(save_note)
list_notes.itemClicked.connect(show_note)
window.show()
app.exec()