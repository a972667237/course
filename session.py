import requests
import random
from io import BytesIO
from PIL import Image
import time
from bs4 import BeautifulSoup
import sys
import re
from tkinter import Tk, Label

file_name, stu_no, passwd, *courses = sys.argv


session = requests.session()

post_url = 'http://192.168.240.168/xuanke/entrance1.asp'
login_url = "http://192.168.240.168/xuanke/edu_login.asp"
image_url = "http://192.168.240.168/xuanke/captcha.asp?x=%s" + str(random.random())
result_url = "http://192.168.240.168/xuanke/showresult.asp"
info_domain_url = 'http://192.168.240.168/xuanke/sele_count1.asp?course_no='

image_res = session.get(image_url)
file = BytesIO(image_res.content)
img = Image.open(file)
img.show()

code = input("code:")
#then input your code
time.sleep(3)

dict = {
    'stu_no': stu_no,
    'passwd': passwd,
    'GetCode': code
}

post_res = session.post(post_url, data=dict)

def gui_out(message):
    root = Tk()
    label = Label(root,text=message)
    label.pack()
    root.mainloop()

class Course:
    def __init__(self, course_id):
        self.course_id = course_id
        self.course_url = info_domain_url + course_id
        course_res = session.get(self.course_url)
        course_soup = BeautifulSoup(course_res.content, 'lxml')
        self.course_name = course_soup.find_all('font')[0].text
        result = re.findall(r'\xba([0-9]+)', course_res.text)
        self.max_count = result[0][0:]
        self.now_count = result[1][0:]

    def start(self):
        self.update_now()
        if not self.now_count:
            gui_out("cookies过期，请重新运行")
        if self.now_count < self.max_count:
            gui_out(self.course_name + '：有空位，id为' + self.course_id)
        else:
        	print (self.course_name + "，限定" + self.max_count + "目前" + self.now_count)

    def update_now(self):
        course_res = session.get(self.course_url)
        result = re.findall(r'\xba([0-9]+)', course_res.text)
        self.max_count = result[0][0:]
        self.now_count = result[1][0:]


course_list = []
for course in courses:
    newCourse = Course(course)
    course_list.append(newCourse)


while course_list:
    for course in course_list:
        course.start()
    time.sleep(2)
