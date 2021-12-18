import qrcode


def qrcodeMaker(text, path):
    img = qrcode.make(text)
    img.save(path)
