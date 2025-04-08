from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

operado = 0
operador = None
operando = 0
app = QApplication([])
window = QWidget()
layout = QGridLayout()
display = QLineEdit()
layout.addWidget(display, 0, 0, 1, 4)

def operação(operado, operador, operando):
    if operador == "+":
        return operado + operando
    elif operador == "-":
        return operado - operando
    elif operador == "÷":
            return operado / operando
    elif operador == "×":
            return operado * operando
    else:
        print("erro: operador invalido")

def click(valor):
    global operado, operador, operando
    if valor in ["+", "-", "×", "÷"]:
        operador = valor
        operado = float(display.text())
        display.clear()
    elif valor == "=":
        operando = float(display.text())
        resultado = operação(operado, operador, operando)
        display.setText(str(resultado))
    elif valor == "CE":
        display.clear()
        operado = 0
        operador = None
        operando = 0
    elif valor == "C":
        display.clear()
    else:
        display.setText(display.text() + valor)

botões = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("÷", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
     ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("CE", 5, 0,)
]

for text, lin, col in botões:
    botão = QPushButton(text)
    botão.clicked.connect(lambda checked, t=text: click(t))
    layout.addWidget(botão, lin, col)

window.setLayout(layout)
window.show()
app.exec()
