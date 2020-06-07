# Image-Security
It provides a way to secure your image and building your privacy by providing QR Code of the Image taken which can provide mere string data. To retrieve the same image, one will be needing password with which QR Code has been created. 
Important Libraries whch are used are: OpenCV, NumPy, QRCode and  Pillow.

Steps Involved:
1. Firstly, the image will be captured from the Webcam.
2. The image of the captured picture will be stored in the same folder. The directory of the image can be changed.
3. Next, the image will be loaded to get the numpy values from the converted pixel values of the frame.
4. Image will be converted into a QR Code with a secured password given by the user.
5. Another program will check the password and if found coorect will load the numpy file and re-create the image from the QR Code.
