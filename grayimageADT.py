from PIL import Image
from my2darray import Array2D
from statistics import mean

class GrayImage:
    def __init__(self, imgFile):
        self._img = Image.open(imgFile, "r")
        self._width, self._height = self._img.size
        self._imgData = self._img.getdata()
        self._pixel_values = Array2D(self._width, self._height)
    def __str__(self):
        return 'Image Size ('+ str(self._width)+ 'x' + self._height + ')\n'+ 'Image Data size ('+str(len(self._imgData))+')'

        # if self._img.mode == "RGB":
        #     channels = 3
        #     imgAvg = int(mean(self._imgData[0] + self._imgData[1] + self._imgData[2]))
        # elif self._img.mode == "L":
        #     channels = 1
        #     imgAvg = self._imgData[0]
        # else:
        #     print("Unknown mode: %s" % self._img.mode)
        #     return None

    def getImageData(self):
        counter = 0
        for i in range(self._width):
            j = 0
            while j <= self._height-1:
                # print('({}x{})={}'.format(i,j,counter))
                self._pixel_values[i, j] = self._imgData[counter]
                j += 1
                counter += 1
        return self._pixel_values


    def imgWidth(self):
        return self._width

    def imgHeight(self):
        return self._height

    def clear(self, value):
        assert value>0 and value<256, "Value shoud be in range 0-255"
        for i in range(self._width):
            for j in range(self._height):
                self._pixel_values = value

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self._width \
            and col >= 0 and col < self._height,\
            "image width or Height out of range."
        return self._pixel_values[row,col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple)==2, "Invalid no of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self._width \
            and col >= 0 and col < self._height, \
            "image width or Height out of range."
        self._pixel_values[row,col] = value
