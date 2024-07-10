import uiScriptLocale
import app

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +13
TEXT_TEMPORARY_X = -10
BUTTON_TEMPORARY_X = 5
PVP_X = -10

if app.ENABLE_ENVIRONMENT_EFFECT_OPTION:
	window = {
		"name" : "SystemOptionDialog",
		"style" : ("movable", "float",),

		"x" : 0,
		"y" : 0,

		"width" : 305,
		"height" : 300,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",

				"x" : 0,
				"y" : 0,

				"width" : 305,
				"height" : 300,

				"children" :
				(
					## Title
					{
						"name" : "titlebar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 8,

						"width" : 284,
						"color" : "gray",

						"children" :
						(
							{ 
							"name":"titlename", "type":"text", "x":0, "y":3, 
							"horizontal_align":"center", "text_horizontal_align":"center",
							"text": uiScriptLocale.SYSTEMOPTION_TITLE, 
							 },
						),
					},

					
					## Music
					{
						"name" : "music_name",
						"type" : "text",

						"x" : 30,
						"y" : 75,

						"text" : uiScriptLocale.OPTION_MUSIC,
					},
					
					{
						"name" : "music_volume_controller",
						"type" : "sliderbar",

						"x" : 110,
						"y" : 75,
					},
					
					{
						"name" : "bgm_button",
						"type" : "button",

						"x" : 20,
						"y" : 100,

						"text" : uiScriptLocale.OPTION_MUSIC_CHANGE,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					
					{
						"name" : "bgm_file",
						"type" : "text",

						"x" : 100,
						"y" : 102,

						"text" : uiScriptLocale.OPTION_MUSIC_DEFAULT_THEMA,
					},
					
					## Sound
					{
						"name" : "sound_name",
						"type" : "text",

						"x" : 30,
						"y" : 50,

						"text" : uiScriptLocale.OPTION_SOUND,
					},
					
					{
						"name" : "sound_volume_controller",
						"type" : "sliderbar",

						"x" : 110,
						"y" : 50,
					},	

					## ī�޶�
					{
						"name" : "camera_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 135+2,

						"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE,
					},
					
					{
						"name" : "camera_short",
						"type" : "radio_button",

						"x" : 110,
						"y" : 135,

						"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_SHORT,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					
					{
						"name" : "camera_long",
						"type" : "radio_button",

						"x" : 110+70,
						"y" : 135,

						"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_LONG,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},

					## �Ȱ�
					{
						"name" : "fog_mode",
						"type" : "text",

						"x" : 30,
						"y" : 160+2,

						"text" : uiScriptLocale.OPTION_FOG,
					},
					
					{
						"name" : "fog_level0",
						"type" : "radio_button",

						"x" : 110,
						"y" : 160,

						"text" : uiScriptLocale.OPTION_FOG_DENSE,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "fog_level1",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 160,

						"text" : uiScriptLocale.OPTION_FOG_MIDDLE,
						
						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "fog_level2",
						"type" : "radio_button",

						"x" : 110 + 100,
						"y" : 160,

						"text" : uiScriptLocale.OPTION_FOG_LIGHT,
						
						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},

					## Ÿ�� ����
					{
						"name" : "tiling_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 185+2,

						"text" : uiScriptLocale.OPTION_TILING,
					},
					
					{
						"name" : "tiling_cpu",
						"type" : "radio_button",

						"x" : 110,
						"y" : 185,

						"text" : uiScriptLocale.OPTION_TILING_CPU,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "tiling_gpu",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 185,

						"text" : uiScriptLocale.OPTION_TILING_GPU,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "tiling_apply",
						"type" : "button",

						"x" : 110+100,
						"y" : 185,

						"text" : uiScriptLocale.OPTION_TILING_APPLY,

						"default_image" : ROOT_PATH + "middle_Button_01.sub",
						"over_image" : ROOT_PATH + "middle_Button_02.sub",
						"down_image" : ROOT_PATH + "middle_Button_03.sub",
					},

				## ENABLE_ENB_MODE
				{
					"name" : "enbMode_status",
					"type" : "text",

					"x" : 40 + TEXT_TEMPORARY_X,
					"y" : 175+2,

					"text" : uiScriptLocale.ENB_MODE,
				},

				{
					"name" : "enbMode_on",
					"type" : "radio_button",

					"x" : 110,
					"y" : 175,

					"text" : uiScriptLocale.ENB_MODE_ON,
					"tooltip_text" : uiScriptLocale.ENB_MODE_ON_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				{
					"name" : "enbMode_off",
					"type" : "radio_button",

					"x" : 110 + 70,
					"y" : 175,

					"text" : uiScriptLocale.ENB_MODE_OFF,
					"tooltip_text" : uiScriptLocale.ENB_MODE_OFF_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

					## ȯ�� ȿ��
					## �� on/off
					{
						"name" : "night_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 210,

						"text" : uiScriptLocale.OPTION_NIGHT_MODE,
					},
					
					{
						"name" : "night_mode_on",
						"type" : "radio_button",

						"x" : 110,
						"y" : 210,

						"text" : uiScriptLocale.OPTION_NIGHT_MODE_ON,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "night_mode_off",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 210,

						"text" : uiScriptLocale.OPTION_NIGHT_MODE_OFF,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					## �� ������ on/off
					{
						"name" : "snow_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 235,

						"text" : uiScriptLocale.OPTION_SNOW_MODE,
					},
					
					{
						"name" : "snow_mode_on",
						"type" : "radio_button",

						"x" : 110,
						"y" : 235,

						"text" : uiScriptLocale.OPTION_SNOW_MODE_ON,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "snow_mode_off",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 235,

						"text" : uiScriptLocale.OPTION_SNOW_MODE_OFF,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					## �� �ٴ� �ؽ��� on/off
					{
						"name" : "snow_texture_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 260,

						"text" : uiScriptLocale.OPTION_SNOW_TEXTURE_MODE,
					},
					
					{
						"name" : "snow_texture_mode_on",
						"type" : "radio_button",

						"x" : 110,
						"y" : 260,

						"text" : uiScriptLocale.OPTION_SNOW_TEXTURE_MODE_ON,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "snow_texture_mode_off",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 260,

						"text" : uiScriptLocale.OPTION_SNOW_TEXTURE_MODE_OFF,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},

					## �׸���
	#				{
	#					"name" : "shadow_mode",
	#					"type" : "text",

	#					"x" : 30,
	#					"y" : 210,

	#					"text" : uiScriptLocale.OPTION_SHADOW,
	#				},
					
	#				{
	#					"name" : "shadow_bar",
	#					"type" : "sliderbar",

	#					"x" : 110,
	#					"y" : 210,
	#				},
				),
			},
		),
	}
else:
	window = {
		"name" : "SystemOptionDialog",
		"style" : ("movable", "float",),

		"x" : 0,
		"y" : 0,

		"width" : 305,
		"height" : 255,

		"children" :
		(
			{
				"name" : "board",
				"type" : "board",

				"x" : 0,
				"y" : 0,

				"width" : 305,
				"height" : 255,

				"children" :
				(
					## Title
					{
						"name" : "titlebar",
						"type" : "titlebar",
						"style" : ("attach",),

						"x" : 8,
						"y" : 8,

						"width" : 284,
						"color" : "gray",

						"children" :
						(
							{ 
							"name":"titlename", "type":"text", "x":0, "y":3, 
							"horizontal_align":"center", "text_horizontal_align":"center",
							"text": uiScriptLocale.SYSTEMOPTION_TITLE, 
							 },
						),
					},

					
					## Music
					{
						"name" : "music_name",
						"type" : "text",

						"x" : 30,
						"y" : 75,

						"text" : uiScriptLocale.OPTION_MUSIC,
					},
					
					{
						"name" : "music_volume_controller",
						"type" : "sliderbar",

						"x" : 110,
						"y" : 75,
					},
					
					{
						"name" : "bgm_button",
						"type" : "button",

						"x" : 20,
						"y" : 100,

						"text" : uiScriptLocale.OPTION_MUSIC_CHANGE,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					
					{
						"name" : "bgm_file",
						"type" : "text",

						"x" : 100,
						"y" : 102,

						"text" : uiScriptLocale.OPTION_MUSIC_DEFAULT_THEMA,
					},
					
					## Sound
					{
						"name" : "sound_name",
						"type" : "text",

						"x" : 30,
						"y" : 50,

						"text" : uiScriptLocale.OPTION_SOUND,
					},
					
					{
						"name" : "sound_volume_controller",
						"type" : "sliderbar",

						"x" : 110,
						"y" : 50,
					},	

					## ī�޶�
					{
						"name" : "camera_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 135+2,

						"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE,
					},
					
					{
						"name" : "camera_short",
						"type" : "radio_button",

						"x" : 110,
						"y" : 135,

						"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_SHORT,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},
					
					{
						"name" : "camera_long",
						"type" : "radio_button",

						"x" : 110+70,
						"y" : 135,

						"text" : uiScriptLocale.OPTION_CAMERA_DISTANCE_LONG,

						"default_image" : ROOT_PATH + "Middle_Button_01.sub",
						"over_image" : ROOT_PATH + "Middle_Button_02.sub",
						"down_image" : ROOT_PATH + "Middle_Button_03.sub",
					},

					## �Ȱ�
					{
						"name" : "fog_mode",
						"type" : "text",

						"x" : 30,
						"y" : 160+2,

						"text" : uiScriptLocale.OPTION_FOG,
					},
					
					{
						"name" : "fog_level0",
						"type" : "radio_button",

						"x" : 110,
						"y" : 160,

						"text" : uiScriptLocale.OPTION_FOG_DENSE,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "fog_level1",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 160,

						"text" : uiScriptLocale.OPTION_FOG_MIDDLE,
						
						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "fog_level2",
						"type" : "radio_button",

						"x" : 110 + 100,
						"y" : 160,

						"text" : uiScriptLocale.OPTION_FOG_LIGHT,
						
						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},

					## Ÿ�� ����
					{
						"name" : "tiling_mode",
						"type" : "text",

						"x" : 40 + TEXT_TEMPORARY_X,
						"y" : 185+2,

						"text" : uiScriptLocale.OPTION_TILING,
					},
					
					{
						"name" : "tiling_cpu",
						"type" : "radio_button",

						"x" : 110,
						"y" : 185,

						"text" : uiScriptLocale.OPTION_TILING_CPU,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "tiling_gpu",
						"type" : "radio_button",

						"x" : 110+50,
						"y" : 185,

						"text" : uiScriptLocale.OPTION_TILING_GPU,

						"default_image" : ROOT_PATH + "small_Button_01.sub",
						"over_image" : ROOT_PATH + "small_Button_02.sub",
						"down_image" : ROOT_PATH + "small_Button_03.sub",
					},
					
					{
						"name" : "tiling_apply",
						"type" : "button",

						"x" : 110+100,
						"y" : 185,

						"text" : uiScriptLocale.OPTION_TILING_APPLY,

						"default_image" : ROOT_PATH + "middle_Button_01.sub",
						"over_image" : ROOT_PATH + "middle_Button_02.sub",
						"down_image" : ROOT_PATH + "middle_Button_03.sub",
					},
				## ENABLE_ENB_MODE
				{
					"name" : "enbMode_status",
					"type" : "text",

					"x" : 40 + TEXT_TEMPORARY_X,
					"y" : 210+2,

					"text" : uiScriptLocale.ENB_MODE,
				},

				{
					"name" : "enbMode_on",
					"type" : "radio_button",

					"x" : 110,
					"y" : 210,

					"text" : uiScriptLocale.ENB_MODE_ON,
					"tooltip_text" : uiScriptLocale.ENB_MODE_ON_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				{
					"name" : "enbMode_off",
					"type" : "radio_button",

					"x" : 110 + 70,
					"y" : 210,

					"text" : uiScriptLocale.ENB_MODE_OFF,
					"tooltip_text" : uiScriptLocale.ENB_MODE_OFF_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

					## �׸���
	#				{
	#					"name" : "shadow_mode",
	#					"type" : "text",

	#					"x" : 30,
	#					"y" : 210,

	#					"text" : uiScriptLocale.OPTION_SHADOW,
	#				},
					
	#				{
	#					"name" : "shadow_bar",
	#					"type" : "sliderbar",

	#					"x" : 110,
	#					"y" : 210,
	#				},
				),
			},
		),
	}