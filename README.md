# shadowsocks-log-analyser
To list all ips from the shadowsocks log file.

# Shadowsocks列出log里所有ip的Python脚本

# 使用方法：
- 首先下载/var/log/shadowsocks.log
- 查看ip格式是ipv4的还是ipv6的,方法：from后面是::ffff:的就是ipv6的ip
- 更改python脚本中log文件的位置`f=open('shadowsocks.log')`
- 运行Python脚本`python ss_log_v4.py`,ipv6运行`python ss_log_v6.py`
- 查看输出

# 进一步分析
使用这家网站可以批量查询ip，可以得到省份、运行商信息
http://ip.cha127.com/piliang.htm

# 猥琐的使用去吧~~
