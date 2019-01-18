import cv2
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Image(QStandardItem):
    def __init__(self, path=None, cv_img=None):
        super().__init__()

        self.path = path
        if path is not None:
            self._openFile(path)
        if cv_img is not None:
            self._img_cv = cv_img

        self.setText(path)

    def _openFile(self, path):
        if type(path) is str:
            self._img_cv = cv2.imread(path)
            self._img_cv = cv2.cvtColor(self._img_cv, cv2.COLOR_BGR2RGB)

    @property
    def CV(self):
        return self._img_cv.copy()

    @property
    def QT(self):
        return self._convertCV2QT(self.CV)

    def _convertCV2QT(self, img_cv):
        height, width, channel = img_cv.shape
        bytesPerLine = 3 * width
        img_qt = QImage(img_cv.data, width, height,
                        bytesPerLine, QImage.Format_RGB888)
        return img_qt
