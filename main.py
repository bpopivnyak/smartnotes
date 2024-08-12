from PyQt6.QtWidgets import*


app = QApplication([])
window = QWidget()

window = QWidget()
text_edit = QTextEdit()
notes_list = QListWidget()
create_note_btn = QPushButton()
save_note_btn = QPushButton()
delete_note_btn = QPushButton()
add_tag_btn = QPushButton()
list_notes_lbl = QLineEdit()
tag_list = QListWidget()
tag_input = QLineEdit()
delete_teg_btn = QPushButton()
search_note_btn = QPushButton()

main_line = QHBoxLayout()
main_line.addWidget(text_edit)


v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
v1.addWidget(add_tag_btn)
v1.addWidget(delete_teg_btn)
v1.addWidget(tag_list)
v1.addWidget(tag_input)
v1.addWidget(search_note_btn)
v1.addWidget(delete_note_btn)
v1.addWidget(text_edit)
v1.addWidget(save_note_btn)
v1.addWidget(create_note_btn)
main_line.addLayout(v1)


window.setLayout(main_line)
window.show()
app.exec()






window.show
app.exec()