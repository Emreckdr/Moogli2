#ifndef __INC_METIN2_COMMON_DEFINES_H__
#define __INC_METIN2_COMMON_DEFINES_H__

//////////////////////////////////////////////////////////////////////////
// ### Genel Sistemler ###
//#define ENABLE_QUEST_CATEGORY
#define ENABLE_D_NJGUILD						// Lonca Düzenlemesi
#define ENABLE_FULL_NOTICE						// Yeni Notice
#define ENABLE_NEWSTUFF							// Yeni Stuff
#define ENABLE_PORT_SECURITY					// Port Güvenlik
#define ENABLE_BELT_INVENTORY_EX				// Kemer Envanteri
#define ENABLE_USE_COSTUME_ATTR					// Kostüm Efsunlama
#define ENABLE_CHECK_GHOSTMODE_HACK				// Hayalet Mod Düzenlemesi
#define ENABLE_BOOKS_STACKFIX					// Beceri Kitabı Düzenlemesi
#define ENABLE_PLAYER_PER_ACCOUNT5				// Lycan Güncellemesi
#define ENABLE_PERMA_BLEND_SYSTEM				// Perma Sebnem Sistemi
#define ENABLE_CMD_WARP_IN_DUNGEON				// Dungeon Warp Fixi
#define __PET_SYSTEM__							// Pet Sistemi
#define ENABLE_EXTEND_INVEN_SYSTEM				// 4 Envanter Sistemi
#define ENABLE_ITEM_ATTR_COSTUME				// Kostüm Efsun Değiştirme
#define ENABLE_SASH_SYSTEM						// Scaleli Kuşak Sistemi
#define ENABLE_BUY_WITH_ITEM					// Nesne İle Pazar Kurma
#define ENABLE_RENEWAL_SHOPEX					// Yıldönümü Parası Sistemi
#define __BL_WEATHER_INFO__						// Dinamik Hava Güncellemesi
#define ENABLE_GLOBAL_CHAT						// Global Chat Bayrak,Level ve Ch Gösterme Düzenlemesi
#define DUNGEON_LIST_TIMER						// Zindan Takip Sistemi
#define ENABLE_TALISMAN_ATTR					// Tilsim Efsun Nesnesi
#define ENABLE_FIX_READ_ETC_DROP_ITEM_FILE_BY_VNUM 		// ETC Drop İtem Fix
#define ENABLE_DICE_SYSTEM						// Official Zar Sistemi
#define ENABLE_MOUNT_COSTUME_SYSTEM				// Official Binek Sistemi
#define ENABLE_WEAPON_COSTUME_SYSTEM			// Official Silah Kostümü
#define AZURA_PROTO_UPDATE						// Official Proto Güncellemesi
#define ENABLE_DS_GRADE_MYTH					// Official Mitsi Simya Sistemi
#define __ENABLE_SHOP_DECORATION_SYSTEM__		// Official Kaşmir Paketi Sistemi
#define ENABLE_CHEQUE_SYSTEM					// Official Won Eklentisi
#define ENABLE_OFFLINE_SHOP_USE_CHEQUE			// Official Won Offlineshop Eklenti
#define ENABLE_SHOP_USE_CHEQUE					// Official Won Parası Sistemi
#define __GAYA__								// Official Gaya Sistemi
#define __7AND8TH_SKILLS__						// Official 7/8 skiller
#define ELEMENT_TARGET							// Official Element Sistemi
#define OFFICIAL_TILSIM_SYSTEM					// Official Tılsım Sistemi
#define ELEMENT_NEW_BONUSES						// Official Yeni Bonuslar
#define __COSTUME_ATTR_SYSTEM__					// Official Kostüm Transfer
#define __ATTR_TRANSFER_SYSTEM__				// Official Kostüm Efsunlama
#define ENABLE_CUBE_RENEWAL_WORLDARD			// Official Cube Sistemi
#define ENABLE_CUBE_ATTR_SOCKET					// Official Cube Sistemi Fixi
#define ENABLE_ITEM_SOUL_SYSTEM					// Official Rüya Ruhu Sistemi
#define __DEFENSE_WAVE__						// Official Hidra Gemi Savunması
#define __QUEST_RENEWAL__						// Official Quest Category
#ifdef __QUEST_RENEWAL__
	// #define _QR_MS_ // Marty Sama
#endif
// ### Lycan Karakteri Başlangıç ###			// Official Lycan Karakteri
#define ENABLE_WOLFMAN_CHARACTER
#ifdef ENABLE_WOLFMAN_CHARACTER
#define USE_MOB_BLEEDING_AS_POISON
#define USE_MOB_CLAW_AS_DAGGER
// #define USE_ITEM_BLEEDING_AS_POISON
// #define USE_ITEM_CLAW_AS_DAGGER
#define USE_WOLFMAN_STONES
#define USE_WOLFMAN_BOOKS
#endif
// ### Lycan Karakteri Bitiş ###				// Official Lycan Karakteri

// ### OfflineShop Sistemi Başlangıç ###		// OfflineShop Sistemi Great
#define OFFLINE_SHOP							// OfflineShop Sistemi
#define GIFT_SYSTEM								// OfflineShop Banka
#define SHOP_TIME_REFRESH 1*60					// OfflineShop Yenile
#define SHOP_BLOCK_GAME99						// OfflineShop CH99
#define SHOP_AUTO_CLOSE							// OfflineShop Oto Kapanma
#define SHOP_GM_PRIVILEGES GM_IMPLEMENTOR		// OfflineShop Gm Eklenti
//#define FULL_YANG								// OfflineShop Full Yang
//#define SHOP_DISTANCE // Show shops in pos distance like WoM2
//#define SHOP_ONLY_ALLOWED_INDEX //Enable limiting for other map index which is not defined in player.shop_limit
//#define SHOP_HIDE_NAME // Enable hidding shop npc names like "Player's shop"
// ### OfflineShop Sistemi Bitiş ###			// OfflineShop Sistemi Great

// #define ENABLE_MAGIC_REDUCTION_SYSTEM
#ifdef ENABLE_MAGIC_REDUCTION_SYSTEM
// #define USE_MAGIC_REDUCTION_STONES
#endif
// ### CommonDefines Systems ###
//////////////////////////////////////////////////////////////////////////
// ### General Features ###
//////////////////////////////////////////////////////////////////////////
enum eCommonDefines {
	EVENT_MOB_RATE_LIMIT = 1000, // 1000 default
	MAP_ALLOW_LIMIT = 32, // 32 default
	PRIV_EMPIRE_RATE_LIMIT = 200, // 200 default
	PRIV_EMPIRE_TIME_LIMIT = 60*60*24*7, // 1 week default
	PRIV_GUILD_RATE_LIMIT = 50, // 50 default
	PRIV_GUILD_TIME_LIMIT = 60*60*24*7, // 1 week default
	PRIV_PLAYER_RATE_LIMIT = 100, // 100 default
};
//////////////////////////////////////////////////////////////////////////
#endif

