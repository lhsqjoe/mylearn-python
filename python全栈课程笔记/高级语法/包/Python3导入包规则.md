>例如：这里给出了一种可能的包结构（在分层的文件系统中）:

    sound/                          顶层包
          __init__.py               初始化 sound 包
          formats/                  文件格式转换子包
                  __init__.py
                  wavread.py
                  wavwrite.py
                  aiffread.py
                  aiffwrite.py
                  auread.py
                  auwrite.py
                  ...
          effects/                  声音效果子包
                  __init__.py
                  echo.py
                  surround.py
                  reverse.py
                  ...
          filters/                  filters 子包
                  __init__.py
                  equalizer.py
                  vocoder.py
                  karaoke.py
                  ...
                  

>目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
> 最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。<br/>


#### from package import item
当导入使用：from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。

#### import item.subitem.subsubitem

反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。
通常我们并不主张使用*这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。

记住，使用from Package import specific_submodule这种方法永远不会有错。事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。比如，如果模块sound.filters.vocoder 要使用包sound.effects中的模块echo，你就要写成 from sound.effects import echo。

在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。

    import sound.effects.echo

这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

    sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
还有一种导入子模块的方法是:

    from sound.effects import echo　
这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

    echo.echofilter(input, output, delay=0.7, atten=4)

还有一种变化就是直接导入一个函数或者变量:

    from sound.effects.echo import echofilter
同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

    echofilter(input, output, delay=0.7, atten=4)    

#### 从一个包中导入*

设想一下，如果我们使用 from sound.effects import *会发生什么？

Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。

但是很不幸，这个方法在 Windows平台上工作的就不是非常好，因为Windows是一个大小写不区分的系统。

在这类平台上，没有人敢担保一个叫做 ECHO.py 的文件导入为模块 echo 还是 Echo 甚至 ECHO。

（例如，Windows 95就很讨厌的把每一个文件的首字母大写显示）而且 DOS 的 8+3 命名规则对长模块名称的处理会把问题搞得更纠结。

为了解决这个问题，只能烦劳包作者提供一个精确的包的索引了。

导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。

作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊。你说我就不这么做，我就不使用导入*这种用法，好吧，没问题，谁让你是老板呢。这里有一个例子，在:file:sounds/effects/__init__.py中包含如下代码:

    __all__ = ["echo", "surround", "reverse"]
                   