from PySide6.QtCore import QObject, QTranslator, Slot, QCoreApplication, Signal

# Main Window Class
class MainWindow(QObject):
    language_changed = Signal()

    def __init__(self):
        QObject.__init__(self)
        self.trans = QTranslator(self)

    @Slot(str)
    def switchLanguage(self, lang):
        if lang:
            self.trans.load('./locale/' + lang)
            QCoreApplication.installTranslator(self.trans)
            self.language_changed.emit()
        else:
            QCoreApplication.removeTranslator(self.trans)