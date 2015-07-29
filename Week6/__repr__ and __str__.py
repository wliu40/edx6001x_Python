'''
Add an __eq__ method that returns True if coordinates refer to same point in the plane 
(i.e., have the same x and y coordinate).
Define __repr__, a special method that returns a string that looks like a valid Python expression that could be 
used to recreate an object with the same value. In other words, eval(repr(c)) == c given the definition of __eq__ 
from part 1.
-------------------------------
4.6.3  str()和 repr() (及 `` 操作符)

内建函数str()和repr()或反引号操作符（``）可以方便地以字符串的方式获取对象的内容、类型、数值属性等信息。
str()函数得到的字符串可读性好，而repr()函数得到的字符串通常可以用来重新获得该对象，通常情况下obj == eval(repr(obj)) 
这个等式是成立的。这两个函数接受一个对象作为其参数，返回适当的字符串。

尽管str(),repr()和``运算在特性和功能方面都非常相似，事实上repr()和``做的是完全一样的事情，它们返回的是一个对象的“官方”
字符串表示，也就是说绝大多数情况下可以通过求值运算（使用内建函数eval()）重新得到该对象，但str()则有所不同。
str()致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于eval()求值，但很适合用于print语句输出。
需要再次提醒的是，并不是所有repr()返回的字符串都能够用 eval()内建函数得到原来的对象.

也就是说 repr() 输出对 Python比较友好，而str()的输出对用户比较友好。
虽然如此，很多情况下这三者的输出仍然都是完全一样的。
-----------------------------------------
# an example of the repr
>>> from datetime import date
>>>
>>> repr(date.today())        # calls date.today().__repr__()
'datetime.date(2009, 1, 16)'
>>> eval(_)                   # _ is the output of the last command
datetime.date(2009, 1, 16)

'''


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self, thatPoint):
        return self.x == thatPoint.x and self.y == thatPoint.y
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ', ' + str(self.y) + ')'
