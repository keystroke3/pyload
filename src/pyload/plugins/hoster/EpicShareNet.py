# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadhoster import DeadHoster


class EpicShareNet(DeadHoster):
    __name__ = "EpicShareNet"
    __type__ = "hoster"
    __version__ = "0.07"
    __status__ = "stable"

    __pyload_version__ = "0.5"

    __pattern__ = r"https?://(?:www\.)?epicshare\.net/\w{12}"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """EpicShare.net hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("t4skforce", "t4skforce1337[AT]gmail[DOT]com")]