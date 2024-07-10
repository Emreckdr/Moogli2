import app
import localeInfo
app.ServerName = None

SRV1 = {
	"name":"Alesta",
	"host":"192.168.1.161",
	"auth1":11002,
	"ch1":13000,
	"ch2":16000,
	"ch3":19000,
	"ch4":21000,
}

SRV2 = {
	"name":"Truva",
	"host":"192.168.1.161",
	"auth1":11002,
	"ch1":13000,
	"ch2":16000,
	"ch3":19000,
	"ch4":21000,
}

SRV3 = {
	"name":"Yakamoz",
	"host":"192.168.1.161",
	"auth1":11002,
	"ch1":13000,
	"ch2":16000,
	"ch3":19000,
	"ch4":21000,
}

SRV4 = {
	"name":"Türkiye",
	"host":"192.168.1.161",
	"auth1":11002,
	"ch1":13000,
	"ch2":16000,
	"ch3":19000,
	"ch4":21000,
}

SRV5 = {
	"name":"Dandanakan",
	"host":"192.168.1.161",
	"auth1":11002,
	"ch1":13000,
	"ch2":16000,
	"ch3":19000,
	"ch4":21000,
}

STATE_NONE = "|cFFFF0000|hDevre Dýþý"

STATE_DICT = {
	0 : "|cFFFF0000|hDevre Dýþý",
	1 : "|cff00ff00|hTavsiye Edilen",
	2 : "|cff00ff00|hBilinmiyor",
	3 : "|cFFFF0000|hDolu"
}

we = {
	1:{"key":11,"name":"CH 1","ip":SRV1["host"],"tcp_port":SRV1["ch1"],"udp_port":SRV1["ch1"],"state":STATE_NONE,},
	2:{"key":12,"name":"CH 2","ip":SRV1["host"],"tcp_port":SRV1["ch2"],"udp_port":SRV1["ch2"],"state":STATE_NONE,},
	3:{"key":13,"name":"CH 3","ip":SRV1["host"],"tcp_port":SRV1["ch3"],"udp_port":SRV1["ch3"],"state":STATE_NONE,},
	4:{"key":14,"name":"CH 4","ip":SRV1["host"],"tcp_port":SRV1["ch4"],"udp_port":SRV1["ch4"],"state":STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : SRV1["name"],
	1 : SRV2["name"],
	2 : SRV1["name"],
	3 : SRV2["name"],
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
		2 : { "ip":SRV1["host"], "port":SRV1["auth1"], },
		3 : { "ip":SRV2["host"], "port":SRV2["auth1"], },
		4 : { "ip":SRV2["host"], "port":SRV2["auth1"], },
		5 : { "ip":SRV3["host"], "port":SRV3["auth1"], },
		6 : { "ip":SRV3["host"], "port":SRV3["auth1"], },
		7 : { "ip":SRV4["host"], "port":SRV4["auth1"], },
		8 : { "ip":SRV4["host"], "port":SRV4["auth1"], },
		9 : { "ip":SRV5["host"], "port":SRV5["auth1"], },
		10 : { "ip":SRV5["host"], "port":SRV5["auth1"], },
	}
}

REGION_DICT = {
	0 : {
		1 : { "name" :SRV1["name"], "channel" : we, },
		2 : { "name" :SRV2["name"], "channel" : we, },
		3 : { "name" :SRV3["name"], "channel" : we, },
		4 : { "name" :SRV4["name"], "channel" : we, },
		5 : { "name" :SRV5["name"], "channel" : we, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "mark" : "10.tga", "symbol_path" : "10", },
	20 : { "ip" : SRV2["host"], "tcp_port" : SRV2["ch1"], "mark" : "10.tga", "symbol_path" : "20", },
	30 : { "ip" : SRV3["host"], "tcp_port" : SRV3["ch1"], "mark" : "10.tga", "symbol_path" : "30", },
	40 : { "ip" : SRV4["host"], "tcp_port" : SRV4["ch1"], "mark" : "10.tga", "symbol_path" : "40", },
	50 : { "ip" : SRV5["host"], "tcp_port" : SRV5["ch1"], "mark" : "10.tga", "symbol_path" : "50", },
}

TESTADDR = { "ip" : SRV1["host"], "tcp_port" : SRV1["ch1"], "udp_port" : SRV1["ch1"], }
TESTADDR = { "ip" : SRV2["host"], "tcp_port" : SRV2["ch1"], "udp_port" : SRV2["ch1"], }
TESTADDR = { "ip" : SRV3["host"], "tcp_port" : SRV3["ch1"], "udp_port" : SRV3["ch1"], }
TESTADDR = { "ip" : SRV4["host"], "tcp_port" : SRV4["ch1"], "udp_port" : SRV4["ch1"], }
TESTADDR = { "ip" : SRV5["host"], "tcp_port" : SRV5["ch1"], "udp_port" : SRV5["ch1"], }

#DONE


