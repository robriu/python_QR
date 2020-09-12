import qrcode

print ("---------------------------")
print ("Hey. I'm ready! \r\n")

img = qrcode.make(input('Input data: \r\n'))
img.save(input('Output file name: \r\n'))

print ('Done. \r\n')
print ("---------------------------")