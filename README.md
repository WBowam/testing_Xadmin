testing_Xadmin
==============
Date:2014-06-13  
Title:Xadmin入门（2）  
Tags:Xadmin
Category:It

## Xadmin 的插件介绍
(本来想自己总结一遍的，可太喜欢Xadmin的文档了，言简意赅，排版精美，就直接搬了，望大侠们勿喷）
### 1. Action

#### 功能

Action 插件在数据列表页面提供了数据选择功能, 选择后的数据可以经过 Action 做特殊的处理. 默认提供的 Action 为批量删除功能.

#### 截图
![Action](http://xadmin.readthedocs.org/en/docs-chinese/_images/action.png)

#### 使用

开发者可以设置 Model OptionClass 的 actions 属性, 该属性是一个列表, 包含您想启用的 Action 的类. 系统已经默认内置了删除数据的 Action, 当然您可以自己制作 Action 来实现特定的功能, 制作 Action 的实例如下.

首先要创建一个 Action 类, 该类需要继承 BaseActionView. BaseActionView 是 ModelAdminView 的子类:
```
from xadmin.plugins.actions import BaseActionView

class MyAction(BaseActionView):

    # 这里需要填写三个属性
    action_name = "my_action"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = _(u'Test selected %(verbose_name_plural)s') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.

    model_perm = 'change'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            # obj 的操作
            ...
        # 返回 HttpResponse
        return HttpResponse(...)
```
然后在 Model 的 OptionClass 中使用这个 Action:
```
class MyModelAdmin(object):

    actions = [MyAction, ]
```
这样就完成了自己的 Action

#### API
```
class xadmin.plugins.actions.ActionPlugin(admin_view)
```
#### 我的效果如下:       [我的源码在此](https://github.com/tulpar008/testing_Xadmin)
![Action](http://tulparblog.qiniudn.com/action.png)

### 2. 数据过滤器
#### 功能

在数据列表页面提供数据过滤功能, 包括: 模糊搜索, 数字范围搜索, 日期搜索等等

#### 截图
![数据过滤器](http://xadmin.readthedocs.org/en/docs-chinese/_images/filter.png)

#### 使用

在 Model OptionClass 中设置以下属性:  

`list_filter` 属性:  

该属性指定可以过滤的列的名字, 系统会自动生成搜索器  

`search_fields` 属性:  

属性指定可以通过搜索框搜索的数据列的名字, 搜索框搜索使用的是模糊查找的方式, 一般用来搜素名字等字符串字段   

`free_query_filter` 属性:  

默认为 True , 指定是否可以自由搜索. 如果开启自有搜索, 用户可以通过 url 参数来进行特定的搜索, 例如:  

`http://xxx.com/xadmin/auth/user/?name__contains=tony`
使用过滤器的例子:  
```
class UserAdmin(object):
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
```

#### 制作过滤器

您也可以制作自己的过滤器, 用来进行一些特定的过滤. 过滤器需要继承 `xadmin.filters.BaseFilter` 类, 并使用 `xadmin.filters.manager` 注册过滤器.


### 3. 图表插件
#### 功能

在数据列表页面, 跟列表数据生成图表. 可以指定多个数据列, 生成多个图表.

#### 截图
![图表](http://xadmin.readthedocs.org/en/docs-chinese/_images/chart.png)

#### 使用

在 Model OptionClass 中设定 data_charts 属性, 该属性为 dict 类型, key 是图表的标示名称, value 是图表的具体设置属性. 使用示例:  
```
class RecordAdmin(object):
    data_charts = {
        "user_count": {'title': u"User Report", "x-field": "date", "y-field": ("user_count", "view_count"), "order": ('date',)},
        "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }
```
图表的主要属性为:   

`title` : 图表的显示名称  

`x-field` : 图表的 X 轴数据列, 一般是日期, 时间等  

`y-field` : 图表的 Y 轴数据列, 该项是一个 list, 可以同时设定多个列, 这样多个列的数据会在同一个图表中显示  

`order` : 排序信息, 如果不写则使用数据列表的排序  



#### API
```
class xadmin.plugins.chart.ChartsPlugin(admin_view)[source]
class xadmin.plugins.chart.ChartsView(request, *args, **kwargs)[source]¶
```


### 4.数据导出
#### 功能

该插件在数据列表页面提供了数据导出功能, 可以导出 `Excel`, `CSV`, `XML`, `json` 格式.  

#### 截图
![数据导出](http://xadmin.readthedocs.org/en/docs-chinese/_images/export.png)

#### 使用

###### Note：如果想要导出 Excel 数据, 需要安装 xlwt.

默认情况下, xadmin 会提供 Excel, CSV, XML, json 四种格式的数据导出. 您可以通过设置 OptionClass 的 list_export 属性来指定使用 哪些导出格式 (四种各使用分别用 xls, csv, xml, json 表示), 或是将 list_export 设置为 None 来禁用数据导出功能. 示例如下:
```
class MyModelAdmin(object):

    list_export = ('xls', xml', 'json')
```

### 5. 列表定时刷新
#### 功能

该插件在数据列表页面提供了定时刷新功能, 对于需要实时刷新列表页面查看即时数据的情况非常有用.

#### 截图
![列表刷新](http://xadmin.readthedocs.org/en/docs-chinese/_images/refresh.png)

#### 使用

使用数据刷新插件非常简单, 设置 OptionClass 的 refresh_times 属性即可. refresh_times 属性是存有刷新时间的数组. xadmin 默认不开启该插件. 示例如下:
```
class MyModelAdmin(object):
    
    # 这会显示一个下拉列表, 用户可以选择3秒或5秒刷新一次页面.
    refresh_times = (3, 5)
```

### 6. 显示数据详情
#### 功能

该插件可以在列表页中显示相关字段的详细信息, 使用 Ajax 在列表页中显示.

#### 截图
![数据详情](http://xadmin.readthedocs.org/en/docs-chinese/_images/details.png)

#### 使用

使用该插件主要设置 `OptionClass` 的 `show_detail_fields`, `show_all_rel_details` 两个属性. `show_detail_fields` 属性设置哪些字段要显示详细信息, `show_all_rel_details` 属性设置时候自动显示所有关联字段的详细信息, 该属性默认为 `True`. 示例如下:
```
class MyModelAdmin(object):
    
    show_detail_fields = ['group', 'father', ...]
```

### 7. 数据即时编辑

#### 功能

该插件可以在列表页中即时编辑某字段的值, 使用 Ajax 技术, 无需提交或刷新页面即可完成数据的修改, 对于需要频繁修改的字段(如: 状态)相当有用.

#### 截图
![即时编辑](http://xadmin.readthedocs.org/en/docs-chinese/_images/editable.png)

####使用

使用该插件主要设置 OptionClass 的 list_editable 属性. list_editable 属性设置哪些字段需要即时修改功能. 示例如下:
```
class MyModelAdmin(object):
    
    list_editable = ['price', 'status', ...]
```

### 8.改主题的插件
`adminx.py`中加入下面代码即可
```
from xadmin import views
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)
```
