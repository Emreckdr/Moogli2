import uiScriptLocale

BOARD_WIDTH = 575+47
BOARD_HEIGHT = 40+10*24+16
PAGE_BUTTON = BOARD_WIDTH/2
ROOT_PATH = "d:/ymir work/ui/game/event/"
LOCALE_PATH = "d:/ymir work/ui/akira_page/"

window = {
	"name" : "AkiraAutoEventWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : BOARD_WIDTH-13,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":BOARD_WIDTH/2, "y":3, "text":"Etkinlik Takvimi", "text_horizontal_align":"center" },
						{ "name":"TitleRefresh", "type":"button", "x":BOARD_WIDTH-57, "y":1, "tooltip_text":"Yenile", "default_image" : "d:/ymir work/ui/game/guild/refresh_button_01.sub", "over_image" : "d:/ymir work/ui/game/guild/refresh_button_02.sub", "down_image" : "d:/ymir work/ui/game/guild/refresh_button_03.sub",},
					),
				},
				{
					"name" : "BlackBoard",
					"type" : "thinboard_circle",
					"x" : 13, "y" : 32, "width" : BOARD_WIDTH-28, "height" : BOARD_HEIGHT-42,
				},
			),
		},
	),
}

