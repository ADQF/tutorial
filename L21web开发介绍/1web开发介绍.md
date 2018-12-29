web开发介绍
===
## 什么是web开发？bs/cs架构
web，也就是我们平时浏览访问的网站，基于http协议，html。信息、图片、视频、用户交互。除了浏览器，实际上一些手机应用和客户端应用也是web开发技术的。

C/S   client server 客户端-服务器模型，例如游戏客户端、LOL客户端、暴雪战网，优点直接在操作系统上运行，效率高；缺点，客户端先从服务器下载更新包，更新比较麻烦。
B/S   browser server 浏览器-服务器模型，例如平时的各种网站。优点是服务器代码更新，客户端浏览器直接访问到的就是最新内容，html/css/js开发从业者多开发效率高，缺点只是比CS架构效率略低。
目前市场上占大多数的应用是BS架构。

## 学习web开发的意义
1. 涉及知识全面 http 网络 Python后台 html前端 Linux部署等。对爬虫、客户端开发、手机端开发、运维打下基础。
2. 由Python基础知识 转向 应用。
3. 就业。  xx管理系统, ERP OA（金蝶 钉钉），互联网公司（微博、抖音）。

## 常见web框架
每种编程语言都有web开发框架，Java ssh structs hibernate spring 由于十几年的发展和学习成本高 所有Java开发的公司都是这套技术栈。Python的web框架由于学习成本低和各有特色，百花争鸣，常用的以下：
- flask    小而微，半自动化，封装了web核心功能，其他功能orm依赖插件扩展。
- Django   大而全，开箱即用。包含orm admin后台 命令行工具CLI。
- tornado  异步10。缺点异步10 modejs更专业。学习成本高。并发性能可由其他框架多进程部署取代。
- sanic    基于py3.5的原生异步语法实现性能提升，但代码质量和生态还不稳定。语法类似flask。
- webpy    极微型框架，单位件千行。适合个人小项目，建议课下阅读源代码。
- bottle   类似flask

flask，django的github火热读，程序员圈流行度，插件、生态，代码质量最优秀的两个框架。 
django适合中大型项目，国内django占大多数。

## 计划
1. flask 基础
2. 简单web项目
3. django
4. 复杂web项目
5. 复杂项目二。


## MVC架构
model  模型层   .py文件  定义类、方法，业务逻辑。
view   视图层   .html  .css  .js  ，负责接收后台传来的数据，将数据和网页外观一起呈现给客户端。
controller  控制层   路由调度

静态网页： 纯html组成。   动态网页：可以跟后端数据交互，比如注册登录。但是早期的动态网页耦合度高，不易修改。


优点： 分层明确，耦合度低














##Client-server model, such as game client, LOL client, Blizzard Battle Network, the advantages directly run on the operating system, high efficiency; shortcomings, the client first downloads the update package from the server, the update is more troublesome.

