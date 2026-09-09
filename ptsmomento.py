import cv2 as cv

img = cv.imread("bgblack.png")
tinggi, lebar, _ = img.shape
print(f"Info : Lebar {lebar}px, Tinggi {tinggi}px ")

y_start = 0
y_end = 500

x_start = 0
x_end = 700

cropimg = img[x_start:x_end, y_start:y_end]

cv.rectangle(cropimg, (0,100), (lebar-700, tinggi-2000), (81,39,18), 500)
text ="''Janganlah kamu berbuat seolah-"
text1 ="olah kamu mau memerintah atas"
text2 ="mereka yang dipercayakan"
text3 ="kepadamu, tetapi hendaklah"
text4 = "kamu"
text5 = "menjadi TELADAN"
text6 = "bagi"
text7 = "kawanan domba itu.''"
text8 = "1 Petrus 5:3"
font = cv.FONT_HERSHEY_COMPLEX
tickness = 2
textColor = (255,255,255)
textColor1 = (0,179,255)
textFontSize = 0.8

cv.line(cropimg, (200, 500), (300, 500), textColor1, tickness)

cv.putText(cropimg, text, (65, 200), font, textFontSize, textColor)
cv.putText(cropimg, text1, (70, 250), font, textFontSize, textColor)
cv.putText(cropimg, text2, (100, 300), font, textFontSize, textColor)
cv.putText(cropimg, text3, (60, 350), font, textFontSize, textColor)
cv.putText(cropimg, text4, (365, 350), font, textFontSize, textColor1)
cv.putText(cropimg, text5, (120, 400), font, textFontSize, textColor1)
cv.putText(cropimg, text6, (320, 400), font, textFontSize, textColor)
cv.putText(cropimg, text7, (140, 450), font, textFontSize, textColor)
cv.putText(cropimg, text8, (180, 550), font, textFontSize, textColor)
cv.imshow("ayat", cropimg)
cv.waitKey(0)
cv.destroyAllWindows()