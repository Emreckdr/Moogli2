#ifndef __INC_METIN_II_GAME_SHOP_H__
#define __INC_METIN_II_GAME_SHOP_H__

enum
{
	SHOP_MAX_DISTANCE = 1000
};

class CGrid;

/* ---------------------------------------------------------------------------------- */
class CShop
{
	public:
		typedef struct shop_item
		{
			DWORD	vnum;		// ������ ��ȣ
			#ifdef FULL_YANG
			long	long	price;		// �Ƣ���Y
			#else
			long	price;		// ����
			#endif
#ifdef ENABLE_CHEQUE_SYSTEM
			int		cheque;
#endif
			BYTE	count;		// ������ ����
#ifdef ENABLE_BUY_WITH_ITEM
			DWORD	witemVnum;
#endif
			LPITEM	pkItem;
			int		itemid;		// ������ �������̵�

			shop_item()
			{
				vnum = 0;
				price = 0;
#ifdef ENABLE_CHEQUE_SYSTEM
				cheque = 0;
#endif
				count = 0;
#ifdef ENABLE_BUY_WITH_ITEM
				witemVnum = 0;
#endif
				itemid = 0;
				pkItem = NULL;
			}
		} SHOP_ITEM;

		CShop();
		virtual ~CShop(); // @fixme139 (+virtual)

		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
		void	SetShopItems(TShopItemTable * pItemTable, BYTE bItemCount);

		virtual void	SetPCShop(LPCHARACTER ch);
		virtual bool	IsPCShop()	{ return m_pkPC ? true : false; }

		// �Խ�Ʈ �߰�/����
		virtual bool	AddGuest(LPCHARACTER ch,DWORD owner_vid, bool bOtherEmpire);
		void	RemoveGuest(LPCHARACTER ch);

		// ���� ����
		virtual int	Buy(LPCHARACTER ch, BYTE pos);

		// �Խ�Ʈ���� ��Ŷ�� ����
		void	BroadcastUpdateItem(BYTE pos);

		// �Ǹ����� �������� ������ �˷��ش�.
		int		GetNumberByVnum(DWORD dwVnum);

		// �������� ������ ��ϵǾ� �ִ��� �˷��ش�.
		virtual bool	IsSellingItem(DWORD itemID);

		DWORD	GetVnum() { return m_dwVnum; }
		DWORD	GetNPCVnum() { return m_dwNPCVnum; }

	protected:
		void	Broadcast(const void * data, int bytes);

#ifdef OFFLINE_SHOP
public:
	int		GetItemCount();
	bool	GetItems();
	void	SetLocked(bool val) { m_bLocked = val; }
	bool	IsLocked() { return m_bLocked; }
	void	RemoveGuests(LPCHARACTER except=NULL);
	void	ClearItems();
	void	SetPrivShopItems(std::vector<TShopItemTable *> map_shop);
	LPCHARACTER GetPC() { return m_pkPC; }
protected:
	bool					m_bLocked;
#endif

	protected:
		DWORD				m_dwVnum;
		DWORD				m_dwNPCVnum;

		CGrid *				m_pGrid;

		typedef TR1_NS::unordered_map<LPCHARACTER, bool> GuestMapType;
		GuestMapType m_map_guest;
		std::vector<SHOP_ITEM>		m_itemVector;	// �� �������� ����ϴ� ���ǵ�

		LPCHARACTER			m_pkPC;
};

#endif
