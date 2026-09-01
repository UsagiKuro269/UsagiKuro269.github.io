import cv2 as cv

img = cv.imread("smashing-mantis-shrimp.jpg")
img1 = cv.imread("smashing-mantis-shrimp.jpg")
print(img.shape)

y_start = 100
y_end = 600

x_start = 0
x_end =900

cropimg = img[x_start:x_end, y_start:y_end]

text = "Jennifer A XIIA"
font = cv.FONT_HERSHEY_COMPLEX
tickness = 2
textcolor = (0,0,0)

cv.putText(img1, text, (100, 100), font, tickness, textcolor)

imggauss = cv.GaussianBlur(img, (5,5), 0)

cropgaussimg = imggauss[x_start:x_end, y_start:y_end]

cv.putText(cropgaussimg, text, (50, 100), font, tickness, textcolor)

newFileName = "Gambarawal.jpg"
cv.imwrite(newFileName, img)
print(f"Image saved as {newFileName}")

newFileName1 = "CroppedImg.jpg"
cv.imwrite(newFileName, cropimg)
print(f"Image saved as {newFileName1}")

newFileName2 = "Teks.jpg"
cv.imwrite(newFileName, img1)
print(f"Image saved as {newFileName2}")

newFileName3 = "Gausseffect.jpg"
cv.imwrite(newFileName, imggauss)
print(f"Image saved as {newFileName3}")

newFileName4 = "Hasilterakhir.jpg"
cv.imwrite(newFileName, cropgaussimg)
print(f"Image saved as {newFileName4}")

cv.imshow('ko shrimp', img)
cv.imshow('crop', cropimg)
cv.imshow('tambah teks', img1)
cv.imshow('gauss effect', imggauss)
cv.imshow('hasil', cropgaussimg)

cv.waitKey(0)
cv.destroyAllWindows()