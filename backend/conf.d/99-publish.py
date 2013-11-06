from dash.output import Memcache

conf.publish_list([
    "bps to belwue",
    "bps from belwue",
    "bps to belwue ipv6 only",
    "bps from belwue ipv6 only",
    "percentage ipv6 to belwue",
    "percentage ipv6 from belwue",
    "total octets belwue to selfnet",
    "total octets selfnet to belwue",
    "usv1 current",
    "usv2 current",
    "usv3 current",
    "usv4 current",
    "usv1 rack temperature",
    "usv2 rack temperature",
    "usv3 rack temperature",
    "usv4 rack temperature",
    "routes ipv4 stuwost1",
    "routes ipv4 stuwost2",
    "routes ipv6 stuwost1",
    "routes ipv6 stuwost2",
    "open selfnet rt tickets",
    "open wh-netz rt tickets",
    "noc wlan clients",
    "user vpn clients",
    "selfstreaming clients multicast",
    "selfstreaming clients unicast",
    "cgn flows patty",
    "cgn flows marge",
    "accesses per second www",
    "ping 8.8.8.8",
    "ping6 2001:4860:4860::8888",
    "ping www.belwue.de",
    "ping6 www.belwue.de",
    "ping www.heise.de",
    "ping6 www.heise.de",
    "ping www.selfnet-status.de",
    "ping6 www.selfnet-status.de",
    "ping vpn heuss",
    "ping6 vpn heuss",
    "ping vpn kade",
    "ping6 vpn kade",
    "ping vpn axa",
    "ping6 vpn axa",
    "ping vpn moehringen",
    "ping6 vpn moehringen",
    "ping switch schwabengarage",
    "ping6 switch schwabengarage",

])

memcache = Memcache(["localhost:11211"])
conf.output(memcache)

# restore data from memcache
memcache.restore()

