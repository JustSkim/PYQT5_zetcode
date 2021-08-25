## Qcore
class PySide2.QtCore.QObject([parent=None])¶
param parent
PySide2.QtCore.QObject

Constructs an object with parent object parent .

The parent of an object may be viewed as the object’s owner. For instance, a dialog box is the parent of the OK and Cancel buttons it contains.

The destructor of a parent object destroys all child objects.

Setting parent to None constructs an object with no parent. If the object is a widget, it will become a top-level window.
在Qt中QObject是所有类的基类，换而言之是在Qt中所有的类均继承自QObject，这使得QObject中的所有方法在其他类中使用。所以学习QObject中的方法有其特殊的意义。