BOARD_WIDTH = 32
BOARD_HEIGHT = 32*7+10
ROOT="d:/ymir work/ui/game/belt_inventory/"

window = {
	"name" : "AkiraMenuWindow", "x" : SCREEN_WIDTH - 176 - 148, "y" : SCREEN_HEIGHT - 37 - 565 + 209 + 32 - 37, "width" : BOARD_WIDTH+40, "height" : BOARD_HEIGHT, "type" : "window",
	"children" :
	(
		{
			"name" : "ExpandBtn", "type" : "button", "x" : 2, "y" : 15, "default_image" : ROOT+"btn_expand_normal.tga", "over_image" : ROOT+"btn_expand_over.tga", "down_image" : ROOT+"btn_expand_down.tga", "disable_image" : ROOT+"btn_expand_disabled.tga", "tooltip_text" : "Hýzlý Menü Aç",
		},
		{
			"name" : "AkiraMenuLayer", "x" : 5, "y" : 0, "width" : BOARD_WIDTH+40, "height" : BOARD_HEIGHT,
			"children" :
			(
				{
					"name" : "MinimizeBtn", "type" : "button", "x" : 2, "y" : 15+20, "width" : 10, "default_image" : ROOT+"btn_minimize_normal.tga", "over_image" : ROOT+"btn_minimize_over.tga", "down_image" : ROOT+"btn_minimize_down.tga", "disable_image" : ROOT+"btn_minimize_disabled.tga", "tooltip_text" : "Hýzlý Menü Kapat",
				},
				{
					"name" : "AkiraMenuWindowBoard", "type" : "board", "style" : ("attach", "float"), "x" : 10, "y" : 0, "width" : BOARD_WIDTH, "height" : BOARD_HEIGHT,
					"children" :
					(
						{"name" : "SystemsWindowSlot", "type" : "grid_table", "x" : 5, "y" : 5, "start_index" : 0, "x_count" : 1, "y_count" : 7, "x_step" : 32, "y_step" : 32, "image" : "d:/ymir work/ui/public/slot_cover_button_04.sub",},
					),
				},
			)
		},
	),
}
