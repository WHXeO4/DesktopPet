import sys
from PySide6.QtCore import Qt, QTimer, QPointF
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel

class DeskPet(QWidget):
    def __init__(self):
        super().__init__()
        self.init()
    
    def init(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint|Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        #set picture
        self.pet_images = [QPixmap(f"../DeskTopPet/res/kano_0{i}.png") for i in range(1, 10)]
        self.current_frame = 0
        
        self.label = QLabel(self)
        self.label.setPixmap(self.pet_images[self.current_frame])
        self.label.resize(self.pet_images[self.current_frame].size())
        self.resize(self.pet_images[self.current_frame].size())

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(100)
        
        self.drag_position = QPointF()
        
    def updateAnimation(self):
        self.current_frame = (self.current_frame+1)%len(self.pet_images)
        self.label.setPixmap(self.pet_images[self.current_frame])

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition() - self.frameGeometry().topLeft().toPointF()
            # print("mousePressEvent fired")
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move((event.globalPosition() - self.drag_position).toPoint())
            # print(" mouseMoveEvent fired")

if "__main__" == __name__:
    app = QApplication(sys.argv)
    pet = DeskPet()
    pet.show()
    sys.exit(app.exec())