# -*- coding:utf-8 -*-
""" 主机状态汇报接收 """

from datetime import datetime
from json import loads

# from service.whiteportservice import whiteports, insertports, deleteports
from service.hostservice import getHoststatus, hoststatus
from util.auth import jwtauth

from handlers.base import BaseHandler


# @jwtauth
class HostHandler(BaseHandler):
    """接收post过来的主机信息"""

    def write_error(self, status_code, **kwargs):
        self.write("Unable to parse JSON.")

    def post(self):

        if self.request.headers["Content-Type"].startswith("application/json"):
            json_args = loads(self.request.body.decode("utf-8"))
            # 原方式是从蜜罐客户端提交过来的时间作为最后在线时间
            # lasttime = json_args["lasttime"]
            # 现方式是蜜罐客户端提交过来请求，但以服务器端时间为准（从服务器端生成时间）
            lasttime = datetime.now()
            hostname = json_args["hostname"]
            ip = json_args["ip"]
            status = json_args["status"]

            # 主机信息入库
            if hoststatus(lasttime, hostname, ip, status):
                self.write("insert status data ok")


@jwtauth
class GetHostHandler(BaseHandler):
    """获取主机状态列表前端展示"""

    def get(self):
        self.write(getHoststatus())
