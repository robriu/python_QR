import qrcode

print('[INFO] This program generates QR code from texts.')
try:
    qr = qrcode.make(input('[INPUT] Enter text: '))
    print ('[UPDATE] QR Code generated...')

    print ('[UPDATE] Creating output file...')
    qr.save(input('[INPUT] Enter output filename: '))

    print('[SUCCESS] Execution Done.')
    
except Exception as e:
    print("[FAILURE]: " + str(e))

print('[INFO] Program Finished.')