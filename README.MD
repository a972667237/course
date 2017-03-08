# course
###### 也就是单纯用来搞事的，因为懒得继续写了，所以可以看作比较流程化的东西= =、
---
这玩意基于python3, 建议在windows下运行
下载：
```
git clone https://github.com/a972667237/course.git
```
安装依赖：
```
pip install -r requirements.txt
```
依赖安装失败的话，自己查查怎么继续安装咯。。，里面lxml挺容易失败的，可以用html5lib代替，但需要自己去改代码（也就改一点小地方）
```
python session.py your_stu_no your_passwd [course1, course2, ...]
```
example:
```
python session.py 2015150006 123456 1900410002 5000530031
```
运行了之后输入验证码即可
反正也就是个粗制滥造的玩意，顶多也就是用来理解一下session用来干啥的而已