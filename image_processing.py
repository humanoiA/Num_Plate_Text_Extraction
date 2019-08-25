import cv2
import os
import pytesseract
import re
try:
    from PIL import Image
except ImportError:
    import Image
file_json=open('Indian_Number_plates.json','r')
co_ord_x1=list()
co_ord_x2=list()
co_ord_y1=list()
co_ord_y2=list()
text=list()
img_width=list()
img_height=list()
img_arr=file_json.read().split('{"con')
for i in img_arr:
    #print(i+'\n\n--\n\n')
    co_ord_x1.append((i[i.find('points":[{"x":')+14:i.find(',{"x"')]).split(',"y"')[0])
    co_ord_y1.append(i[i.find('points":[{"x":')+14:i.find(',{"x"')].split(',"y":')[-1].replace("}",""))
    co_ord_x2.append((i[i.find(',{"x":')+6:i.find('}],"imag')]).split(',"y":')[0])
    co_ord_y2.append((i[i.find(',{"x":')+6:i.find('}],"imag')]).split(',"y":')[-1])
    img_width.append(i[i.find('"imageWidth":')+13:i.find(',"imageHeig')])
    img_height.append(i[i.find(',"imageHeight":')+15:i.find('}],"extras"')])
j=1
err=0
for i in range(1,238):
    img=cv2.imread("img\\"+str(i)+'.jpeg')
    #img = cv2.medianBlur(img,5)
    try:
        crop_img=img[int(float(co_ord_y1[j])*int(img_height[j])):int(float(co_ord_y2[j])*int(img_height[j])),int(float(co_ord_x1[j])*int(img_width[j])):int(float(co_ord_x2[j])*int(img_width[j]))]
        img_gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        #threshold2 = cv2.adaptiveThreshold(crop_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
         #   cv2.THRESH_BINARY,11,2)
        #threshold3 = cv2.adaptiveThreshold(crop_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
         #   cv2.THRESH_BINARY,11,2)
        cv2.imwrite('C:\\Users\\shubh\\Documents\\Python Scripts\\Num_Plate_Detection\\num_plates'+'\\'+str(i)+'.jpeg',img_gray)
        j+=1
        sub_str=pytesseract.image_to_string('num_plates'+'\\'+str(i)+'.jpeg',lang='eng',config ='--psm 6')
        text.append('num_plate number '+str(i)+'-----'+re.sub('[^A-Z0-9\n\t ]', '', sub_str))   
    except Exception as e:
        print(e)
        j+=1
        err+=1
with open('output.txt', 'w') as f:
    for item in text:
        f.write("%s\n" % item)