import qrcode

url = input("Enter the payment URL: ")

# Generate QR code
qr = qrcode.make(url)

qr.save("payment_qr.png")
print("QR code saved as payment_qr.png")