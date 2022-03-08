import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer


def display(svg_str):
    # file = open('kosaraju_1.svg','rb')
    

    svg_bytes = bytearray(svg_str, encoding='utf-8')

    app = QApplication(sys.argv)
    svgWidget = QSvgWidget()
    svgWidget.renderer().load(svg_bytes)
    svgWidget.setGeometry(100,100,300,300)
    svgWidget.show()
    sys.exit(app.exec_())