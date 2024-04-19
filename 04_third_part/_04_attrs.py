from attr import attrs, attrib
from cattr import structure,unstructure

# 首先是 attrs，它主要是用来修饰 class 类的，而 attrib主要是用来做属性定义的
@attrs #相当于帮Color实现了init方法和repr方法：主要是 attrs 这个修饰符起了作用，然后根据定义的 attrib 属性自动帮我们实现了__init__、__repr__、__eq__、__ne__、__lt__、__le__、__gt__、__ge__、__hash__这几个方法
class Color(object):
    r = attrib(type=int, default=0)
    g = attrib(type=int, default=0)
    b = attrib(type=int, default=0)
    # attrib方法有如下参数
    # name：属性的名字，是一个字符串类型。
    # default：属性的默认值，如果没有传入初始化数据，那么就会使用默认值。如果没有默认值定义，那么就是 NOTHING，即没有默认值。
    # validator：验证器，检查传入的参数是否合法。
    # init：是否参与初始化，如果为 False，那么这个参数不能当做类的初始化参数，默认是 True。
    # `metadata：元数据，只读性的附加数据。
    # type：类型，比如 int、str 等各种类型，默认为 None。
    # converter：转换器，进行一些值的处理和转换器，增加容错性。
    # kw_only：是否为强制关键字参数，默认为 False。
    
   
    

print(Color(1,2,3))
print(unstructure(Color(5,6,7))) # 对象转json
print(structure(unstructure(Color(8,9,10)), Color)) # json转对象



