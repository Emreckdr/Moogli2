import uiCommon, ui, time, playersettingmodule, localeInfo, mouseModule, constInfo, uiScriptLocale, interfaceModule, dbg, wndMgr, snd, item, player, net, app
import eventtime

class eventsystemwindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()


	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/takvim_gui.py")
		except:
			import exception
			exception.Abort("FelixEventTakvimiPenceresi.LoadWindow.LoadObject")
		try:
			self.titleBar = self.GetChild("titlebar")
			self.board = self.GetChild("board")
			self.FelixScrollBar = self.GetChild("ScrollBar")
			self.title_name_olds = self.GetChild("title_name_old")
##---------------------------------------------------------------------------			
			self.pazartesi_baslangic = self.GetChild("pazartesi_baslangicc")
			self.pazartesi_bitis = self.GetChild("pazartesi_bitiss")
##---------------------------------------------------------------------------			
			self.sali_baslangic = self.GetChild("sali_baslangicc")
			self.sali_bitis = self.GetChild("sali_bitiss")
##---------------------------------------------------------------------------			
			self.carsamba_baslangic = self.GetChild("carsamba_baslangicc")
			self.carsamba_bitis = self.GetChild("carsamba_bitiss")
##---------------------------------------------------------------------------			
			self.persembe_baslangic = self.GetChild("persembe_baslangicc")
			self.persembe_bitis = self.GetChild("persembe_bitiss")
##---------------------------------------------------------------------------			
			self.cuma_baslangic = self.GetChild("cuma_baslangicc")
			self.cuma_bitis = self.GetChild("cuma_bitiss")
##---------------------------------------------------------------------------			
			self.ctesi_baslangic = self.GetChild("ctesi_baslangicc")
			self.ctesi_bitis = self.GetChild("ctesi_bitiss")
##---------------------------------------------------------------------------			
			self.pazar_baslangic = self.GetChild("pazar_baslangicc")
			self.pazar_bitis = self.GetChild("pazar_bitiss")
##---------------------------------------------------------------------------			
			
			self.GetChild("btnayisik").SAFE_SetEvent(self.__MenuFunction, 1)
			self.GetChild("btnfutbol").SAFE_SetEvent(self.__MenuFunction, 2)
			self.GetChild("btnbulmaca").SAFE_SetEvent(self.__MenuFunction, 3)
			self.GetChild("btnokeykart").SAFE_SetEvent(self.__MenuFunction, 4)
			self.GetChild("btnexp").SAFE_SetEvent(self.__MenuFunction, 5)
			self.GetChild("btnaltigen").SAFE_SetEvent(self.__MenuFunction, 6)
		except:
			import exception
			exception.Abort("FelixEventTakvimiPenceresi.LoadWindow.BindObject")
			
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		

		
		self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.pazartesi_bitis.SetText("Pazartesi Biti� : " + "Event se�imi yap�lmad� !")
		self.sali_baslangic.SetText("Sal� Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.sali_bitis.SetText("Sal� Biti� : " + "Event se�imi yap�lmad� !")
		self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.carsamba_bitis.SetText("�ar�amba Biti� : " + "Event se�imi yap�lmad� !")
		self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.persembe_bitis.SetText("Per�embe Biti� : " + "Event se�imi yap�lmad� !")
		self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.cuma_bitis.SetText("Cuma Biti� : " + "Event se�imi yap�lmad� !")
		self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.ctesi_bitis.SetText("Cumartesi Biti� : " + "Event se�imi yap�lmad� !")
		self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + "Event se�imi yap�lmad� !")
		self.pazar_bitis.SetText("Pazar Biti� : " + "Event se�imi yap�lmad� !")

	def __MenuFunction(self, value):
		if value == 1:
			self.title_name_olds.SetText("Ay I���� Define Sand��� Etkinli�i Takvimi G�steriliyor")
			self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + eventtime.AY_ISIK["pazartesi_basla"])
			self.pazartesi_bitis.SetText("Pazartesi Biti� : " + eventtime.AY_ISIK["pazartesi_bitir"])
			self.sali_baslangic.SetText("Sal� Ba�lang�� : " + eventtime.AY_ISIK["sali_basla"])
			self.sali_bitis.SetText("Sal� Biti� : " + eventtime.AY_ISIK["sali_bitir"])
			self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + eventtime.AY_ISIK["carsamba_basla"])
			self.carsamba_bitis.SetText("�ar�amba Biti� : " + eventtime.AY_ISIK["carsamba_bitir"])
			self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + eventtime.AY_ISIK["persembe_basla"])
			self.persembe_bitis.SetText("Per�embe Biti� : " + eventtime.AY_ISIK["persembe_bitir"])
			self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + eventtime.AY_ISIK["cuma_basla"])
			self.cuma_bitis.SetText("Cuma Biti� : " + eventtime.AY_ISIK["cuma_bitir"])
			self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + eventtime.AY_ISIK["ctesi_basla"])
			self.ctesi_bitis.SetText("Cumartesi Biti� : " + eventtime.AY_ISIK["ctesi_bitir"])
			self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + eventtime.AY_ISIK["pazar_basla"])
			self.pazar_bitis.SetText("Pazar Biti� : " + eventtime.AY_ISIK["pazar_bitir"])
			
		elif value == 2:
			self.title_name_olds.SetText("Futbol Topu Etkinli�i Takvimi G�steriliyor")
			self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + eventtime.FUTBOL["pazartesi_basla"])
			self.pazartesi_bitis.SetText("Pazartesi Biti� : " + eventtime.FUTBOL["pazartesi_bitir"])
			self.sali_baslangic.SetText("Sal� Ba�lang�� : " + eventtime.FUTBOL["sali_basla"])
			self.sali_bitis.SetText("Sal� Biti� : " + eventtime.FUTBOL["sali_bitir"])
			self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + eventtime.FUTBOL["carsamba_basla"])
			self.carsamba_bitis.SetText("�ar�amba Biti� : " + eventtime.FUTBOL["carsamba_bitir"])
			self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + eventtime.FUTBOL["persembe_basla"])
			self.persembe_bitis.SetText("Per�embe Biti� : " + eventtime.FUTBOL["persembe_bitir"])
			self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + eventtime.FUTBOL["cuma_basla"])
			self.cuma_bitis.SetText("Cuma Biti� : " + eventtime.FUTBOL["cuma_bitir"])
			self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + eventtime.FUTBOL["ctesi_basla"])
			self.ctesi_bitis.SetText("Cumartesi Biti� : " + eventtime.FUTBOL["ctesi_bitir"])
			self.pazar_bitis.SetText("Pazar Biti� : " + eventtime.FUTBOL["pazar_bitir"])
			self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + eventtime.FUTBOL["pazar_basla"])

		elif value == 3:
			self.title_name_olds.SetText("Bulmaca Kutusu Etkinli�i Takvimi G�steriliyor")
			self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + eventtime.BULMACA["pazartesi_basla"])
			self.pazartesi_bitis.SetText("Pazartesi Biti� : " + eventtime.BULMACA["pazartesi_bitir"])
			self.sali_baslangic.SetText("Sal� Ba�lang�� : " + eventtime.BULMACA["sali_basla"])
			self.sali_bitis.SetText("Sal� Biti� : " + eventtime.BULMACA["sali_bitir"])
			self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + eventtime.BULMACA["carsamba_basla"])
			self.carsamba_bitis.SetText("�ar�amba Biti� : " + eventtime.BULMACA["carsamba_bitir"])
			self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + eventtime.BULMACA["persembe_basla"])
			self.persembe_bitis.SetText("Per�embe Biti� : " + eventtime.BULMACA["persembe_bitir"])
			self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + eventtime.BULMACA["cuma_basla"])
			self.cuma_bitis.SetText("Cuma Biti� : " + eventtime.BULMACA["cuma_bitir"])
			self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + eventtime.BULMACA["ctesi_basla"])
			self.ctesi_bitis.SetText("Cumartesi Biti� : " + eventtime.BULMACA["ctesi_bitir"])
			self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + eventtime.BULMACA["pazar_basla"])
			self.pazar_bitis.SetText("Pazar Biti� : " + eventtime.BULMACA["pazar_bitir"])

		elif value == 4:
			self.title_name_olds.SetText("Okey Kart� Etkinli�i Takvimi G�steriliyor")
			self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + eventtime.OKEY_KART["pazartesi_basla"])
			self.pazartesi_bitis.SetText("Pazartesi Biti� : " + eventtime.OKEY_KART["pazartesi_bitir"])
			self.sali_baslangic.SetText("Sal� Ba�lang�� : " + eventtime.OKEY_KART["sali_basla"])
			self.sali_bitis.SetText("Sal� Biti� : " + eventtime.OKEY_KART["sali_bitir"])
			self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + eventtime.OKEY_KART["carsamba_basla"])
			self.carsamba_bitis.SetText("�ar�amba Biti� : " + eventtime.OKEY_KART["carsamba_bitir"])
			self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + eventtime.OKEY_KART["persembe_basla"])
			self.persembe_bitis.SetText("Per�embe Biti� : " + eventtime.OKEY_KART["persembe_bitir"])
			self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + eventtime.OKEY_KART["cuma_basla"])
			self.cuma_bitis.SetText("Cuma Biti� : " + eventtime.OKEY_KART["cuma_bitir"])
			self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + eventtime.OKEY_KART["ctesi_basla"])
			self.ctesi_bitis.SetText("Cumartesi Biti� : " + eventtime.OKEY_KART["ctesi_bitir"])
			self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + eventtime.OKEY_KART["pazar_basla"])
			self.pazar_bitis.SetText("Pazar Biti� : " + eventtime.OKEY_KART["pazar_bitir"])

		elif value == 5:
			self.title_name_olds.SetText("Tecr�be Puan� Etkinli�i Takvimi G�steriliyor")
			self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + eventtime.EXP["pazartesi_basla"])
			self.pazartesi_bitis.SetText("Pazartesi Biti� : " + eventtime.EXP["pazartesi_bitir"])
			self.sali_baslangic.SetText("Sal� Ba�lang�� : " + eventtime.EXP["sali_basla"])
			self.sali_bitis.SetText("Sal� Biti� : " + eventtime.EXP["sali_bitir"])
			self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + eventtime.EXP["carsamba_basla"])
			self.carsamba_bitis.SetText("�ar�amba Biti� : " + eventtime.EXP["carsamba_bitir"])
			self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + eventtime.EXP["persembe_basla"])
			self.persembe_bitis.SetText("Per�embe Biti� : " + eventtime.EXP["persembe_bitir"])
			self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + eventtime.EXP["cuma_basla"])
			self.cuma_bitis.SetText("Cuma Biti� : " + eventtime.EXP["cuma_bitir"])
			self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + eventtime.EXP["ctesi_basla"])
			self.ctesi_bitis.SetText("Cumartesi Biti� : " + eventtime.EXP["ctesi_bitir"])
			self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + eventtime.EXP["pazar_basla"])
			self.pazar_bitis.SetText("Pazar Biti� : " + eventtime.EXP["pazar_bitir"])

		elif value == 6:
			self.title_name_olds.SetText("Alt�gen Hediye Kutusu Etkinli�i Takvimi G�steriliyor")
			self.pazartesi_baslangic.SetText("Pazartesi Ba�lang�� : " + eventtime.ALTIGEN["pazartesi_basla"])
			self.pazartesi_bitis.SetText("Pazartesi Biti� : " + eventtime.ALTIGEN["pazartesi_bitir"])
			self.sali_baslangic.SetText("Sal� Ba�lang�� : " + eventtime.ALTIGEN["sali_basla"])
			self.sali_bitis.SetText("Sal� Biti� : " + eventtime.ALTIGEN["sali_bitir"])
			self.carsamba_baslangic.SetText("�ar�amba Ba�lang�� : " + eventtime.ALTIGEN["carsamba_basla"])
			self.carsamba_bitis.SetText("�ar�amba Biti� : " + eventtime.ALTIGEN["carsamba_bitir"])
			self.persembe_baslangic.SetText("Per�embe Ba�lang�� : " + eventtime.ALTIGEN["persembe_basla"])
			self.persembe_bitis.SetText("Per�embe Biti� : " + eventtime.ALTIGEN["persembe_bitir"])
			self.cuma_baslangic.SetText("Cuma Ba�lang�� : " + eventtime.ALTIGEN["cuma_basla"])
			self.cuma_bitis.SetText("Cuma Biti� : " + eventtime.ALTIGEN["cuma_bitir"])
			self.ctesi_baslangic.SetText("Cumartesi Ba�lang�� : " + eventtime.ALTIGEN["ctesi_basla"])
			self.ctesi_bitis.SetText("Cumartesi Biti� : " + eventtime.ALTIGEN["ctesi_bitir"])
			self.pazar_baslangic.SetText("Pazar Ba�lang�� : " + eventtime.ALTIGEN["pazar_basla"])
			self.pazar_bitis.SetText("Pazar Biti� : " + eventtime.ALTIGEN["pazar_bitir"])

	def Destroy(self):
		self.ClearDictionary()
		self.board = None

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

