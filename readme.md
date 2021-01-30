@[TOC]

> 本文参考于Simple UI官网文档，源地址<https://simpleui.72wo.com/docs/simpleui/doc.html>，仅供学习使用。

# pip源切换

## 源列表
- 豆瓣：http://pypi.douban.com/simple/
- 中科大：https://pypi.mirrors.ustc.edu.cn/simple/
- 清华：https://pypi.tuna.tsinghua.edu.cn/simple

## 一次性使用
```
pip install django-simpleui -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 永久使用

** Linux \& MacOS \|\| Windows **

linux下，修改~/.pip/pip.conf，修改index-url为国内的任意镜像
windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

# 安装及使用

## 安装
```
pip install django-simpleui

或者

git clone https://github.com/newpanjing/simpleui
cd simpleui
python setup.py sdist install
```

## 创建django项目

参考文章：<https://blog.csdn.net/qq_36581961/article/details/111564791>

## 修改django的默认后台模板为simpleui
```python
# settings.py

INSTALLED_APPS = [
      'simpleui',  # 记得加在第一行
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      ...
      
  ]
```

## 克隆静态文件
熟悉django的同学会了解，django有个神奇的模式叫做debug模式，默认是开启的，在settings.py中`debug=True`
关闭后可以有两种方法解决静态资源无法访问的问题

- 在settings.py中加入
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
     
- 克隆静态资源到项目的静态目录，然后交由nginx处理
    python3 manage.py collectstatic

## 启动项目
    python manage.py runserver 8000
    
# 主题

## 默认主题
```python
#指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'
```

## 主题列表
```javascript
var SimpleuiThemes = [
    {
        text: "Default",
        menu: 'rgb(48, 65, 86)',
        logo: 'rgb(48, 65, 86)',
        top: '#FFF'
    },
    {
        text: "Simpleui-x",
        menu: '#2c2e39',
        logo: '#2c2e39',
        top: '#FFF',
        file: "simpleui.css"
    },
    {
        text: "Element-UI",
        file: "element.css",
        top: '#447eff',
        menu: '#FFf',
        logo: '#FFF'
    },
    {
        text: "layui",
        file: "layui.css",
        menu: '#393D49',
        logo: '#23262E',
        top: '#23262E'
    }, {
        text: "Ant Design Pro",
        file: "ant.design.css",
        menu: '#000b16',
        logo: '#002140',
        top: '#FFF'
    }, {
        text: "Admin LTE",
        file: "admin.lte.css",
        top: '#3c8dbc',
        logo: '#3c8dbc',
        menu: '#2b3539'
    }, {
        text: "Highdmin",
        file: "highdmin.css",
        top: '#02c0ce',
        menu: '#e0e0e0',
        logo: '#02c0ce'
    }, {
        text: "Aircraft",
        file: "aircraft.css",
        top: '-webkit-gradient(linear, left bottom, left top, color-stop(0, #4d5b76), color-stop(1, #6f80a1)) !important',
        menu: '#e0e0e0',
        logo: '-webkit-gradient(linear, left bottom, left top, color-stop(0, #4d5b76), color-stop(1, #6f80a1)) !important'
    }, {
        text: "Purple",
        file: "purple.css",
        top: '#FFF',
        logo: '#FFF',
        menu: '#3e4295'
    }, {
        text: "Gray",
        file: "gray.css",
        top: '#213a53',
        logo: '#213a53',
        menu: '#e0e0e0'
    },
    {
        text: "Dark green",
        file: "dark.green.css",
        top: '#f3f3f4',
        menu: '#283846',
        logo: '#283846'
    },
    {
        text: "Orange",
        file: "orange.css",
        top: 'linear-gradient(to right bottom, #da8342, #e45131)',
        logo: 'linear-gradient(to right bottom, #da8342, #e45131)',
        menu: '#FFF'
    },
    {
        text: "Black",
        file: "black.css",
        top: "#333",
        logo: "#333",
        menu: '#FFF'
    },
    {
        text: "Green",
        file: "green.css",
        top: '#19a97b',
        logo: '#FFF',
        menu: '#FFF'
    },
    {
        text: "Light",
        file: "light.css",
        top: "#ebf1f5",
        logo: "#ebf1f5",
        menu: "#ebf1f5"
    }, {
        text: 'Enterprise blue',
        file: 'e-blue.css',
        top: '#3ba1df',
        logo: '#3ba1df',
        menu: '#FFF'
    }, {
        text: 'Enterprise blue pro',
        file: 'e-blue-pro.css',
        top: '#3ba1df',
        logo: '#3ba1df',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise green',
        file: 'e-green.css',
        top: '#27ad60',
        logo: '#27ad60',
        menu: '#FFF'
    }, {
        text: 'Enterprise green pro',
        file: 'e-green-pro.css',
        top: '#27ad60',
        logo: '#27ad60',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise red',
        file: 'e-red.css',
        top: '#c9333e',
        logo: '#c9333e',
        menu: '#FFF'
    }, {
        text: 'Enterprise red pro',
        file: 'e-red-pro.css',
        top: '#c9333e',
        logo: '#c9333e',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise purple',
        file: 'e-purple.css',
        top: '#8263b1',
        logo: '#8263b1',
        menu: '#FFF'
    }, {
        text: 'Enterprise purple pro',
        file: 'e-purple-pro.css',
        top: '#8263b1',
        logo: '#8263b1',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'Enterprise black',
        file: 'e-black.css',
        top: '#1f2c39',
        logo: '#1f2c39',
        menu: '#FFF'
    }, {
        text: 'Enterprise black pro',
        file: 'e-black-pro.css',
        top: '#1f2c39',
        logo: '#1f2c39',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-green',
        file: 'x-green.css',
        top: '#2F9688',
        logo: '#2F9688',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-red',
        file: 'x-red.css',
        top: '#AA3130',
        logo: 'rgb(38, 50, 56)',
        menu: 'rgb(38, 50, 56)'
    }, {
        text: 'x-blue',
        file: 'x-blue.css',
        top: '#FFF',
        logo: '#1E9FFF',
        menu: 'rgb(38, 50, 56)'
    }
]
```

## 自定义主题
在自定义主题之前，请先把simpleui的静态资源克隆到根目录。然后找到theme theme.js 就是用于配置主题列表
按该文件中的格式配置即可
```javascript
var SimpleuiThemes = [
    {
        "text": "Default"
    },
    {
        "text": "Simpleui-x",
        "file": "simpleui.css"
    }
]
```

`admin.lte.less`

```jquery-css
@import "base";

@primary: #2096c8 !important;
@color: white;

@menu-color: #8aa4af !important;
@menu-background: #2b3539 !important;

@menu-color-hover: #FFF;
@menu-background-hover: #1f272b;

@menu-title-color: #FFF;
@menu-title-background-color: #212c32;

@menu-title-color-hover: #FFF;
@menu-title-background-color-hover: #1f272b;


@navbar-color: #fff;
@navbar-background: #3c8dbc;
```

`编译`
```
npm install less -g

lessc admin.lte.less>admin.lte.css
```

# 图标
参考fontawesome的图标：<https://fontawesome.com/icons?d=gallery>
## 默认图标
```
SIMPLEUI_DEFAULT_ICON = False
# True开启默认图标 默认是开启
# False 关闭默认图标
```

## 自定义图标
> 注：simpleui 原则上不涉及代码，所以采用setting方式。后续可考虑扩展Model的 Meta class 进行配置图标


```
SIMPLEUI_ICON = {
    '系统管理': 'fab fa-apple',
    '员工管理': 'fas fa-user-tie'
}
```

# 菜单

## 自定义菜单
- system_keep 保留系统菜单
    该字段用于告诉simpleui，是否需要保留系统默认的菜单，默认为False，不保留。 
    如果改为True，自定义和系统菜单将会并存

- menu_display 过滤显示菜单和排序功能
    该字段用于告诉simpleui，是否需要开启过滤显示菜单和排序功能。
    默认可以不用填写，缺省配置为默认排序，不对菜单进行过滤和排序。
    开启认为传一个列表，如果列表为空，则什么也不显示。列表中的每个元素要对应到menus里面的name字段

- dynamic 开启动态菜单功能
    该字段用于告诉simpleui，是否需要开启动态菜单功能。
    默认可以不用填写，缺省配置为False，不开启动态菜单功能。
    开启为True，开启后，每次用户登陆都会刷新左侧菜单配置。
    需要注意的是：开启后每次访问admin都会重读配置文件，所以会带来额外的消耗。

> 字段说明
> - name 菜单名
> - icon 图标，参考element-ui和fontawesome图标
> - url 链接地址，绝对或者相对,如果存在models字段，将忽略url
> - models 子菜单，自2021.02.01+版本 支持最多3级菜单

`如果SIMPLEUI_CONFIG中存在menus字段，将会覆盖系统默认菜单。并且menus中输出的菜单不会受权限控制。

# 模板

## 修改模板
在simpleui的基础上修改模板需要对django有一定了解
- 先把simpleui克隆到静态目录下，参考克隆静态文件到根目录
- 找到静态目录下的admin目录，里面就是simpleui的模板，直接修改相关html页面即可生效。

## 重写页面
例如重写首页，在templates目录中新建admin文件夹，然后添加index.html 如果选择继承方式，就只能采用block 代码如下：

```html
{% extends 'admin/index.html' %}
{% load static %}

{% block head %}
    {{ block.super }}
    ..此处写你的代码
{% endblock %}

{% block script %}
    {{ block.super }}
    ..此处写你的代码
{% endblock %}

```

```html
<html>
    <head>
        <title>完全自定义</title>
    </head>
    <body>
        这里你是自定义的html代码
    </body>
</html>
```

```html

{% extends 'admin/index.html' %}
{% load static %}

{% block head %}
    {{ block.super }}
    ..此处写你的代码
{% endblock %}
```

# 自定义按钮&action
`需要在2.1.2以上版本生效`
django admin 默认提供了自定义按钮的支持，但是样式、图标均不可自定义，
simpleui在django admin 自定义action的基础上增加了样式、图标、按钮类型自定义。

```python
@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'idCard', 'phone', 'birthday', 'department', 'enable', 'create_time')
   
    # 增加自定义按钮
    actions = ['make_copy', 'custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass
    make_copy.short_description = '复制员工'
```

## 字段参数
> icon 按钮图标，参考https://element.eleme.cn/#/zh-CN/component/icon与https://fontawesome.com，把class 复制进来即可
> type 按钮类型，参考：https://element.eleme.cn/#/zh-CN/component/button
> style 自定义css样式
> confirm 弹出确认框，在3.4或以上版本中生效
  
```python
from django.contrib import messages
def message_test(self, request, queryset):
    messages.add_message(request, messages.SUCCESS, '操作成功123123123123')
    
# 给按钮增加确认
message_test.confirm = '你是否执意要点击这个按钮？'
```

## 链接按钮
```python
actions = ['custom_button']

def custom_button(self, request, queryset):
    pass

# 链接按钮，设置之后直接访问该链接
# 3中打开方式
# action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
# 设置了action_type，不设置url，页面内将报错
# 设置成链接类型的按钮后，custom_button方法将不会执行。

custom_button.action_type = 0
custom_button.action_url = 'http://www.baidu.com'
```

## layer对话框按钮
> 对话框按钮是在`admin`中进行配置`action`，可以自定义输入的字段，然后通过`ajax`请求到`action`中进行业务的处理。
> 需要继承`AjaxAdmin` 在`from simpleui.admin import AjaxAdmin`包中
> `simplepro`也会同步支持对话框按钮功能。


# 配置
simpleui在django 原生`admin`的基础上增加了若干自定义的配置，这些配置均是在`settings.py`文件中完成。

## 关闭登录页粒子动画
```
SIMPLEUI_LOGIN_PARTICLES = False
```

## 修改默认图标
```python
# 首页 修改默认
SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'  # 配置
SIMPLEUI_HOME_TITLE = '百度一下你就知道' # 标题
SIMPLEUI_HOME_ICON = 'fa fa-user'   # 图标

# 首页 跳转地址
SIMPLEUI_INDEX = 'https://www.88cto.com'
# 可以设置相对与绝对路径。该地址并无特殊之处，将会调用window.open直接打开该地址

# 首页 模块  服务器信息、快速操作、最近动作，使用分析 离线模式 关闭Loading遮罩层
SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4' # logo修改
SIMPLEUI_HOME_INFO = False # 服务器信息 隐藏
SIMPLEUI_HOME_QUICK = False # 快速操作 隐藏
SIMPLEUI_HOME_ACTION = False # 最近动作 隐藏
SIMPLEUI_ANALYSIS = False # 使用分析 隐藏
SIMPLEUI_STATIC_OFFLINE = True # 离线模式 不填该项或者为False的时候，默认从第三方的cdn获取
SIMPLEUI_LOADING = False # 关闭Loading遮罩层
```

# 插件支持 

## django-import-export
simpleui对数据导入导出插件也做了支持，您可以直接安装使用。

## admindoc
admindoc需要simpleui 3.3+ 版本

## simplepro
<https://simpleui.72wo.com/simplepro>

# 国际化
simpleui 国际化采用js前端国际化，因为没有涉及到后端，所以没有django标准的国际化文件。
将simpleui 克隆到静态目录，然后添加需要的语言
语言命名与django LANGUAGE_CODE 一致
例如： 中文简体：zh-hans 英文：en-us
将文件命名为: [code].js
- zh-hans.js
- en-us.js

# 常见问题
<https://simpleui.72wo.com/docs/simpleui/QUICK.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98>
