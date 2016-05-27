# shadowsocks-log-analyser
To list all ips and its connected times from the shadowsocks log file.

# Shadowsocks列出log里所有ip和对应连接次数的Python脚本

# 使用方法：
- 首先下载`/var/log/shadowsocks.log`
- 查看ip格式是ipv4的还是ipv6的（搬瓦工就是ipv6的）,方法：from后面是`::ffff:`的就是ipv6的ip
- 更改python脚本前两行

`ipv6=True`:ip格式是ipv6的开启这个
`sort=False`：默认按照ip出现时间排序，true为按照连接次数排序

- 运行Python脚本`python ss_log.py`
- 查看输出

# 进一步分析
使用这家网站可以批量查询ip，可以得到省份、运行商信息
http://ip.cha127.com/piliang.htm

最后，你可以把数据导入到Excel里分析嘛！！

比如这样

![](http://i.imgur.com/z4sDFtF.png?1)

# 猥琐地使用去吧~~
