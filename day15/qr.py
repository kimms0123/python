import qrcode

won = 'https://www.instagram.com/everyone_woo/'
qr = qrcode.make(won)
qr.save('won.png')