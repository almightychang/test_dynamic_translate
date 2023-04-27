import os
import sys

# IMPORT MODULES
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from model import MainWindow



# INSTACE CLASS
if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    main.language_changed.connect(engine.retranslate)
    engine.rootContext().setContextProperty("backend", main)
    
    # Load QML File
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    # Check Exit App
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
