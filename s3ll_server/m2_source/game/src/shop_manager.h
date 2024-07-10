#ifndef __INC_METIN_II_GAME_SHOP_MANAGER_H__
#define __INC_METIN_II_GAME_SHOP_MANAGER_H__

class CShop;
typedef class CShop * LPSHOP;

class CShopManager : public singleton<CShopManager>
{
public:
	typedef std::map<DWORD, CShop *> TShopMap;

#ifdef OFFLINE_SHOP
public:
	bool	StartOfflineShop(DWORD id, bool onboot = false);
	bool	CreateOfflineShop(LPCHARACTER owner, const char *szSign,const std::vector<TShopItemTable*> pTable, DWORD days, DWORD kasmirBaslik, DWORD kasmirNPC);
	LPSHOP	CreateNPCShop(LPCHARACTER ch, std::vector<TShopItemTable *> map_shop);
	DWORD	GetShopCount() { return m_map_pkShop.size(); }
#endif

public:
	CShopManager();
	virtual ~CShopManager();

	bool	Initialize(TShopTable * table, int size);
#if defined(ENABLE_RENEWAL_SHOPEX)
	bool	InitializeShopEX(TShopTable* table, int size);
#endif
	void	Destroy();

	LPSHOP	Get(DWORD dwVnum);
	LPSHOP	GetByNPCVnum(DWORD dwVnum);

	bool	StartShopping(LPCHARACTER pkChr, LPCHARACTER pkShopKeeper, int iShopVnum = 0);
	void	StopShopping(LPCHARACTER ch);

	void	Buy(LPCHARACTER ch, BYTE pos);
	void	Sell(LPCHARACTER ch, BYTE bCell, BYTE bCount=0);

	LPSHOP	CreatePCShop(LPCHARACTER ch, TShopItemTable * pTable, BYTE bItemCount);
	LPSHOP	FindPCShop(DWORD dwVID);
	void	DestroyPCShop(LPCHARACTER ch);

private:
	TShopMap	m_map_pkShop;
	TShopMap	m_map_pkShopByNPCVnum;
	TShopMap	m_map_pkShopByPC;

	bool	ReadShopTableEx(const char* stFileName);
};

#endif