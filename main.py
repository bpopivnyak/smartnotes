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
    notes[key] = field_text.toPlainText()
    write_in_file(notes)

list_notes.itemClicked.connect(show_note)
window.show()
app.exec()