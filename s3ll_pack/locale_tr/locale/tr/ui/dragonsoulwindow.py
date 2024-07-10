import uiScriptLocale
import app

DISPLAY_WINDOW_X = 0

window = {
	"name" : "InventoryWindow",

	## 600 - (width + ���������� ���� ���� 24 px)
	#"x" : SCREEN_WIDTH - 176 - 287 - 10,
	#"y" : SCREEN_HEIGHT - 37 - 505,
		
	"x" : SCREEN_WIDTH - 175 - 287 - DISPLAY_WINDOW_X,
	"y" : SCREEN_HEIGHT - 37 - 40 - 525,

	"style" : ("movable", "float",),

	"width" : 287,
	"height" : 525,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 287,
			"height" : 525,

			"children" :
			(
				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 0,

					"image" : "d:/ymir work/ui/dragonsoul/dragon_soul_bg.tga",

				},
				{
					"name" : "Inventory_Tab_01", "type" : "radio_button",
					"x" : 16, "y" : 331,
					"default_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_01_1.tga",
					"over_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_01_2.tga",
					"down_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_01_3.tga",
				},
				{
					"name" : "Inventory_Tab_02", "type" : "radio_button",
					"x" : 59, "y" : 331,
					"default_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_02_1.tga",
					"over_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_02_2.tga",
					"down_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_02_3.tga",
				},
				{
					"name" : "Inventory_Tab_03", "type" : "radio_button",
					"x" : 102, "y" : 331,
					"default_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_03_1.tga",
					"over_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_03_2.tga",
					"down_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_03_3.tga",
				},
				{
					"name" : "Inventory_Tab_04", "type" : "radio_button",
					"x" : 145, "y" : 331,
					"default_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_04_1.tga",
					"over_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_04_2.tga",
					"down_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_04_3.tga",
				},
				{
					"name" : "Inventory_Tab_05", "type" : "radio_button",
					"x" : 188, "y" : 331,
					"default_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_05_1.tga",
					"over_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_05_2.tga",
					"down_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_05_3.tga",
				},
				{
					"name" : "Inventory_Tab_06", "type" : "radio_button",
					"x" : 231, "y" : 331,
					"default_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_06_1.tga",
					"over_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_06_2.tga",
					"down_image"	: "d:/ymir work/ui/dragonsoul/btn_soul_06_3.tga",
				},
				
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 15,
					"y" : 355,

					"start_index" : 0,
					"x_count" : 8,
					"y_count" : 4,
					"x_step" : 32,
					"y_step" : 32,

					#"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},
				{
					"name" : "EquipmentSlot",
					"type" : "slot",

					"x" : 0,
					"y" : 0,

					"width" : 287,
					"height" : 280,

					"slot" : (
								{"index":DRAGON_SOUL_EQUIPMENT_SLOT_START+0, "x":128, "y":53, "width":32, "height":32},
								{"index":DRAGON_SOUL_EQUIPMENT_SLOT_START+1, "x":59, "y":93, "width":32, "height":32},
								{"index":DRAGON_SOUL_EQUIPMENT_SLOT_START+2, "x":59, "y":179, "width":32, "height":32},
								{"index":DRAGON_SOUL_EQUIPMENT_SLOT_START+3, "x":128, "y":219, "width":32, "height":32},
								{"index":DRAGON_SOUL_EQUIPMENT_SLOT_START+4, "x":194, "y":179, "width":32, "height":32},
								{"index":DRAGON_SOUL_EQUIPMENT_SLOT_START+5, "x":194, "y":93, "width":32, "height":32},
							),
				},
				{
					"name" : "deck1",
					"type" : "toggle_button",

					"x" : 21,
					"y" : 230,

					"default_image" : "d:/ymir work/ui/dragonsoul/deck1_1.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/deck1_2.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/deck1_3.tga",
				},
				{
					"name" : "deck2",
					"type" : "toggle_button",

					"x" : 234,
					"y" : 230,

					"default_image" : "d:/ymir work/ui/dragonsoul/deck2_1.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/deck2_2.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/deck2_3.tga",
				},
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 271,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":130, "y":3, "text":uiScriptLocale.DRAGONSOUL_TITLE, "text_horizontal_align":"center" },
					),
				},
				## Tab Area
				{
					"name" : "TabControl",
					"type" : "window",

					"x" : 10,
					"y" : 279,

					"width" : 267,
					"height" : 30,

					"children" :
					(
						## Tab
						{
							"name" : "Tab_01",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"width" : 267,
							"height" : 30,

							"image" : "d:/ymir work/ui/dragonsoul/tap01.tga",
						},
						{
							"name" : "Tab_02",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"width" : 267,
							"height" : 30,

							"image" : "d:/ymir work/ui/dragonsoul/tap02.tga",
						},
						{
							"name" : "Tab_03",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"width" : 267,
							"height" : 30,

							"image" : "d:/ymir work/ui/dragonsoul/tap03.tga",
						},
						{
							"name" : "Tab_04",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"width" : 267,
							"height" : 30,

							"image" : "d:/ymir work/ui/dragonsoul/tap04.tga",
						},
						{
							"name" : "Tab_05",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"width" : 267,
							"height" : 30,

							"image" : "d:/ymir work/ui/dragonsoul/tap05.tga",
						},
						{
							"name" : "Tab_06",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,

							"width" : 267,
							"height" : 30,

							"image" : "d:/ymir work/ui/dragonsoul/tap06.tga",
						},
						## RadioButton
						{
							"name" : "Tab_Button_01",
							"type" : "radio_button",

							"x" : 2,
							"y" : 2,

							"width" : 36,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_02",
							"type" : "radio_button",

							"x" : 42,
							"y" : 2,

							"width" : 36,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_03",
							"type" : "radio_button",

							"x" : 82,
							"y" : 2,

							"width" : 36,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_04",
							"type" : "radio_button",

							"x" : 122,
							"y" : 2,

							"width" : 36,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_05",
							"type" : "radio_button",

							"x" : 162,
							"y" : 2,

							"width" : 36,
							"height" : 27,
						},
						{
							"name" : "Tab_Button_06",
							"type" : "radio_button",

							"x" : 202,
							"y" : 2,

							"width" : 36,
							"height" : 27,
						},
					),
				},
				{
					"name" : "tab_text_area",
					"type" : "text",

					"x" : 18,
					"y" : 315,

					"text" : uiScriptLocale.DRAGONSOUL_TAP_TITLE_1,
					"color" : 0xFFC0C0C0,
				},
				{					
					"name" : "activate",
					"type" : "toggle_button",

					"x" : 217,
					"y" : 492,

					"text" : uiScriptLocale.DRAGONSOUL_ACTIVATE,

					"default_image" : "d:/ymir work/ui/dragonsoul/m_button01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/m_button02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/m_button03.tga",
				},

				## ENABLE_REFINE_DS_WINDOW_BEGIN
				{
					"name" : "second_option",
					"type" : "toggle_button",

					"x" : 150,
					"y" : 492,

					"text" : uiScriptLocale.DO_REFINE,

					"default_image" : "d:/ymir work/ui/dragonsoul/m_button01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/m_button02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/m_button03.tga",
				},
				## ENABLE_REFINE_DS_WINDOW_END
			),
		},
	),
}