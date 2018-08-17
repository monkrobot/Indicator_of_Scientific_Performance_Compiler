import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()


        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        self.titleEdit = QLineEdit()
        self.wrapper()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def wrapper(self):
        name=self.titleEdit.text()
        self.printing(name)
    def printing(self,name):
        print(name)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    #print('Title: ', ex.titleEdit.text())
    ex.wrapper()
    sys.exit(app.exec_())

