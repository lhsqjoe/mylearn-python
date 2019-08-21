# cookie & session
 - 存放位置不同
 - cookie 不安全
 - 单个cookie保存数据不超过4k, 很多浏览器限制一个站点最多保存20个
 
 - 使用cookie 登录
    - 直接把cookie 复制下来，然后手动放入请求头
    - http 模块包含一些关于cookie 的模块，通过他们我们可以自动使用cookie
        - CookieJar  
            - 管理存储cookie, 向传出的http请求 添加cookie
            - cookie 存储在内存中， CookieJar实例回收后cookie 将消失
        - FileCookieJar
        - MozillaCookieJar
        - LwpCookieJar
            - 创建与libwww-perl 标准兼容的Set-Cookie 格式的FileCookieJar实例
        - 他们的关系是CookieJar -->FileCookieJar -->MozillaCookieJar -->LwpCookieJar
    - 利用cookie 访问人人网
        - 自动使用cookie 登录，大致流程是
        - 打开登陆页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie 登录隐私页面  
    - cookie 属性
        - name
        - value
        - domain    可以访问此cookie 的域名
        - path 
        - expires 过期时间
        - size 
        - http 字段   
    - cookie 读取  

# SSL
 - SSL 证书
 - CA 数字证书认证中心，是发放，管理，废除数字证书的授信人的第三方机构   
 - SSL 模块

# js 加密 
    - 在浏览器端对数据进行加密，可以破解，一般是md5  
# ajax
 - 异步  

# Requests
 - 继承了urllib的所有特征
 - 底层用的是urllib3
 - 开源
 - conda install requests
 - get 请求 
    - requests.get(url)
    - requests.request('get', url)
 - get 返回内容
 - post 
    - requests.post(baseurl, data=data, headers=headers)
 - proxy  
 - 用户验证
 - web客户端验证  
 - cookie 
 - session
    - 跟服务器端session不是一个东东
    - 模拟一次会话, 从客户端浏览器链接服务器开始，到客户端浏览器断开
    - 能让我们跨请求时保持某些参数，比如在同一个session实例发出的所有请求之间保持cookie
 - https请求验证 ssl 证书
    - 参数 verify 负责表示是否需要验证SSL证书，默认是True

# xpath    
 - XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航
 - https://www.w3school.com.cn/xpath/index.asp //w3c的教程
 - 常用路径表达式
    - nodename: 选取此节点的所有子节点
    - /: 从根节点开始选
    - //: 选取元素，而不考虑元素的位置
    - .: 当前节点
    - ..: 父节点
    - @： 选取属性
 - 谓语 
    - /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
    - /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。
    - /bookstore/book[last()-1]	选取属于 bookstore 子元素的倒数第二个 book 元素。
    - /bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
    - //title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。
    - //title[@lang='eng']	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
    - /bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
    - /bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。
    
 - 通配符
    - * 匹配任何元素节点
    - @* 匹配任何属性节点。
    - node()      匹配任何类型的节点   

 - 选取若干路径
    - 通过在路径表达式中使用“|”运算符，您可以选取若干个路径。
    - //book/title | //book/price	选取 book 元素的所有 title 和 price 元素。
    - //title | //price	选取文档中的所有 title 和 price 元素。
    - /bookstore/book/title | //price	选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。  
        