import uiScriptLocale
import item

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",
	"x" : SCREEN_WIDTH - 175 - 140 + 4,
	"y" : SCREEN_HEIGHT - 37 - 575 + 9,
	"style" : ("movable", "float",),
	"width" : 140,
	"height" : 180 + 47 + 36,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 140,
			"height" : 180 + 47 + 36,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 6,
					"y" : 6,
					"width" : 130,
					"color" : "yellow",
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"center" },
					),
				},
				
				{
					"name" : "Costume_Base",
					"type" : "image",
					"x" : 13,
					"y" : 38,
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/new_costume_bg.jpg",
					"children" :
					(
						{
							"name" : "CostumeSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 127,
							"height" : 188,
							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},#Body
										{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},#Hair
										{"index":COSTUME_START_INDEX+2, "x":12, "y":127, "width":32, "height":32},#Mount
										{"index":COSTUME_START_INDEX+3, "x":62, "y":127, "width":32, "height":32},#Sash
										{"index":COSTUME_START_INDEX+4, "x":12, "y":13, "width":32, "height":96},#Weapon
										{"index":item.EQUIPMENT_RING1, 	"x":12,	"y":167, "width":32, "height":32},
										{"index":item.EQUIPMENT_RING2, 	"x":63,	"y":167, "width":32, "height":32},


							),
						},
					),
				},
			),
		},
	),
}
