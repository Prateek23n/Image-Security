from __future__ import with_statement
import qrcode
from PIL import Image
import sqlite3
import numpy as np
import io
import os
image=Image.open('Picture.png')
data=np.asarray(image)
#print("Datatype:",type(data))
#print("Shape:",data.shape)
width,height=image.size
print("Width:",width)
print("Height:",height)
print("Mode:",image.mode)
#print("Data:",data)
#print(pixel)
qr=qrcode.QRCode()
string_data=input("Enter password to secure QR code:")
print("Password Entered:",string_data)
qr.add_data(string_data,optimize=0)
qr.make()
img=qr.make_image()
img.save('QR.png')
np.save('data.npy',data)
#get_val=Image.fromarray(data)
#get_val.save("New.png")
#conn=sqlite3.connect('image_to_qr.db')
#c=conn.cursor()
#c.execute("DROP TABLE i2q")
#c.execute('CREATE TABLE IF NOT EXISTS i2q(arr ARRAY,text TEXT)')
#print("TABLE CREATED...")
#c.execute("INSERT INTO i2q(arr,text) VALUES(?,?)",(iar,string_data))
#conn.commit()
#print("Insertion Successful...")
#c.execute("SELECT arr FROM i2q")
#for i in c.fetchall():
#    print(i)
#print(type(i))
