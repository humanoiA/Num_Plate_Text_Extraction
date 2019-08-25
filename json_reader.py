import json
import requests
import os
file_json=open('Indian_Number_plates.json','r')
url=list()
co_ord_x1=list()
co_ord_x2=list()
co_ord_y1=list()
co_ord_y2=list()
img_arr=file_json.read().split('{"con')
for i in img_arr:
    #print(i+'\n\n--\n\n')
    url.append(i[i.find('tent":')+7:i.find(',"ann')].replace('"',''))
    co_ord_x1.append((i[i.find('points":[{"x":')+14:i.find(',{"x"')]).split(',"y"')[0])
    co_ord_y1.append(i[i.find('points":[{"x":')+14:i.find(',{"x"')].split(',"y":')[-1].replace("}",""))
    co_ord_x2.append((i[i.find(',{"x":')+6:i.find('}],"imag')]).split(',"y":')[0])
    co_ord_y2.append((i[i.find(',{"x":')+6:i.find('}],"imag')]).split(',"y":')[-1])
for i in range(1,238):
    img_data = requests.get(url[i],allow_redirects=True)
    open('C:\\Users\\shubh\\Documents\\Python Scripts\\Num_Plate_Detection\\img\\'+str(i)+'.jpeg', 'wb').write(img_data.content)