# 웹사트의 robots.txt를 확인하는 프로그램

import urllib.robotparser

user_agent="PyRobot"
domain_url="https://shop.hakhub.net"
robot_url=f"{domain_url}/robots.txt"
page_url=f"{domain_url}/page/1/"
admin_url=f"{domain_url}/wp-admin/"

rp=urllib.robotparser.RobotFileParser()
rp.set_url(robot_url)
rp.read()
rrate=rp.request_rate(user_agent) # robots.txt의 Request-rate를 확인

print(rp.crawl_delay(user_agent))
print(rp.can_fetch(user_agent, page_url))
print(rp.can_fetch(user_agent, domain_url))
print(rp.can_fetch(user_agent, admin_url))