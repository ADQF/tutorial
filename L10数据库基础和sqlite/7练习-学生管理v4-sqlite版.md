作业二：学生管理系统 (v4 sqlite)
====
## 题目要求
（第4版 sqlite数据库版。）
做一个学员名字管理系统（控制台输入和输出）。 
（编码风格：可以函数封装也可以类封装，sqlite返回元组或字典都行）
### 准备
设计和创建students表
- id  主键 自增 整数
- name 学生姓名 字符串  必填
- sex   性别  字符串
- age   年龄  整数
- phone 电话号码    字符串    
创建好表后可以先插入几条测试数据。

### 具体需求
终端开始打印主菜单信息如下。提问用户选择哪种操作？
```
1-查询学员姓名
2-添加学员姓名
3-修改学员姓名
4-删除学员姓名
0-退出程序

请选择操作？
>?  1
```
1. 管理员输入1时，输出如下
    ``` 
    行号        姓名       年龄        性别      电话
    -------------------------------------------------
    1           小明        10         male         137000000
    2           小红        12         female         137000000
    3           张三        9          male           137000000
    ```
2. 管理员输入2时，提示继续输入名字，用户输入后将结果保存到数据库表中，提示保存成功。
添加成功之后，回到主菜单。用户再次查询学员列表，发现学员已增加。
    ```
        请输入要添加学生的新姓名：
        >?  xxx
        请输入要添加学生的年龄:
        >?  10
        请输入要添加学生的性别:
        >?  10
        添加完毕。
    ```
3. 管理员输入3时，提示修改"第几个"名字，选择编号后提示继续输入修改后的名字，修改后的结果保存到student_list中。保存成功后回到主菜单。
    ```
        要修改第几个学生？：
        >?  1
        修改后的姓名是？：
        >?  大明
        修改后的年龄是？：
        >?  10
        修改成功。
    ```
4. 管理员输入4时，打印子菜单
    ```
    删除>请输入子选项：
       1> 按序号删除
       2> 全部删除  (clear)
    ```
    子选项选择1时，提问要删除第几个学生，管理员输入编号后删除对应学生。
    ```要删除第几个学生？：
        >?  1
        删除成功
    ```
    子选项选择2时，提示是否删除全部，选择'Y'时删除全部。
    ```
        确认全部删除？（Y/N）:
        >?  Y
        删除全部成功
    ```
5. 管理员输入0时，退出程序。

## 提示
参考L4数据结构容器/excercise3-字典版.py 和 L10数据库基础和sqlite/3sqlite示例2.py 完成本次作业。

- 函数封装
- print()
- input()
- if elif
- 列表 append
- 列表 遍历输出 for
- 列表 修改  列表[0] = '新值'
- 列表 pop()
- while for
- break
- 字典 增删改查
- 列表嵌套字典的结构
- sqlite数据库增删改查


