from PyQt6.QtWidgets import*


app = QApplication([])
window = QWidget()



text_edit = QTextEdit()
list_notes_lbl = QLineEdit()
notes_list = QListWidget()
create_note_btn = QPushButton()
delete_note_btn = QPushButton()
save_note_btn = QPushButton()
list_teg_lbl = QLineEdit()
tegs_list = QListWidget()
teg_input = QLineEdit()
add_teg_btn = QPushButton()
delete_teg_btn = QPushButton()
search_note_btn = QPushButton()



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






window.show
app.exec()