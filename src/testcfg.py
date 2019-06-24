from configparser import ConfigParser

#初始化类
cp = ConfigParser()
cp.read("../config/onion.cfg")

#得到所有的section，以列表的形式返回
section = cp.sections()[0]
print(section)

#得到该section中的option的值，返回为string类型
print(cp.get(section, "login_url"))
print(cp.get(section, "user_name"))
print(cp.get(section, "password"))

