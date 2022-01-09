# Instale os pacotes abaixo para funcionar corretamente
#pip install qrcode
#pip install pillow
#pip install PyQt5

import qrcode
from PyQt5 import uic,QtWidgets
from PIL import Image


def criarQrCode():
    url = telaInicial.lineEdit.text()
    try:
        qr = qrcode.QRCode(version=1, box_size=8, border=7)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('C:/Users/Usu/Downloads/QrCode.png')
        telaInicial.labelAlerta.setText('Qrcode Salvo na pasta -> C:/Users/Usu/Downloads/QrCode.png ')
        exibirImagem()
    except:
        telaInicial.labelAlerta.setText('Erro ao gerar QrCode')


def exibirImagem():
    imagem = Image.open('C:/Users/Usu/Downloads/QrCode.png')
    imagem.show()


# Interface Grafica
tela = QtWidgets.QApplication([])
telaInicial = uic.loadUi('tela_inicial.ui')
telaInicial.show()
telaInicial.pushButton.clicked.connect(criarQrCode)
tela.exec()


