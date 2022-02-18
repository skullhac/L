from grayimageADT import GrayImage

imgFile1='E:\\DataStructures\\Books\\Rance d.Necaise\\PythonDS-master\\Chapter2\\barbara_gray.bmp'
imgFile2='E:\\DataStructures\\Books\\Rance d.Necaise\\PythonDS-master\\Chapter2\\butterfly.jpg'
image2D=GrayImage(imgFile1)
imgdata=image2D.getImageData()
print(imgdata[123,78])
print(imgdata[510,111])
