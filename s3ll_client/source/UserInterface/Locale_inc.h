#pragma once

//////////////////////////////////////////////////////////////////////////
// ### Yeni Source Eklentileri ###
#define LOCALE_SERVICE_EUROPE				// Official Locale Avrupa Desteği
#define ENABLE_COSTUME_SYSTEM				// Official Kostüm Sistemi
#define ENABLE_ENERGY_SYSTEM				// Official Enerji Sistemi
#define ENABLE_DRAGON_SOUL_SYSTEM			// Official Simya Sistemi
#define ENABLE_NEW_EQUIPMENT_SYSTEM			// Official Yeni Ekipman Sistemi
#define ENABLE_PACK_GET_CHECK				// Official Pack Kontrol Sistemi
#define ENABLE_CANSEEHIDDENTHING_FOR_GM		// Official Gm'ler Görünmez Karakterleri Görme Sistemi
#define ENABLE_PROTOSTRUCT_AUTODETECT		// Official Protoları Kontrol Etme Sistemi
#define ENABLE_PLAYER_PER_ACCOUNT5			// Official Lycan Eklentisi
#define ENABLE_LEVEL_IN_TRADE				// Official Ticaret'de Level Gösterme Sistemi
#define ENABLE_DICE_SYSTEM					// Official Zar Sistemi
#define ENABLE_EXTEND_INVEN_SYSTEM			// Official 4 Envanter Sistemi
#define ENABLE_LVL115_ARMOR_EFFECT			// Official 115 Level Zırh Parlamaları
#define ENABLE_TEXT_LEVEL_REFRESH			// Official Level Yenileme
#define ENABLE_USE_COSTUME_ATTR				// Official Kostüm Efsun Arttırma
#define ENABLE_HIGHLIGHT_SYSTEM				// Official Yeni İtem Efekti
#define ENABLE_WOLFMAN_CHARACTER			// Official Lycan Karakter
#define ENABLE_MOUNT_COSTUME_SYSTEM			// Official Binek Sistemi
#define ENABLE_WEAPON_COSTUME_SYSTEM		// Official Sİlah Kostümü Sistemi
#define ENABLE_SASH_SYSTEM					// Official Scaleli Kuşak Sistemi
#define ENABLE_ITEM_ATTR_COSTUME			// Official Kostüm Efsun Değiştirme
#define ENABLE_COSTUME_ATTR_SYSTEM			// Official Kostüm Efsun Değiştirme
#define AZURA_PROTO_UPDATE					// Official İtem Proto
#define ENABLE_DS_GRADE_MYTH				// Official Mitsi Simya Sistemi
#define ENABLE_SHOP_DECORATION_SYSTEM		// Official Kaşmir Sistemi
#define ENABLE_CHEQUE_SYSTEM				// Official Won Sistemi
#define __GAYA__							// Official Gaya Sistemi
#define ENABLE_7AND8TH_SKILLS				// Official 7/8 Skiller Eklenti
#define ELEMENT_TARGET						// Official Element Sistemi
#define OFFICIAL_TILSIM_SYSTEM				// Official Tılsım Sistemi
#define ENABLE_CUBE_RENEWAL_WORLDARD		// Official Cube Sistemi
#define ENABLE_ITEM_SOUL_SYSTEM				// Official Rüya Ruhu Sistemi
#define ENABLE_QUEST_RENEWAL				// Official Quest Sistemi

#if defined(ENABLE_OFFLINE_SHOP) && defined(ENABLE_CHEQUE_SYSTEM)
#	define ENABLE_OFFLINE_SHOP_USE_CHEQUE
#endif
//#define ENABLE_FULL_YANG					// Full Yang Sistemi
// ### WJ Mob Bilgi Eklentisi ###
#define WJ_SHOW_MOB_INFO					// Official Mob Bilgisi Sistemi
#ifdef WJ_SHOW_MOB_INFO						// Official Mob Bilgisi Sistemi
#define ENABLE_SHOW_MOBAIFLAG				// Agresif Bilgisi Sistemi
#define ENABLE_SHOW_MOBLEVEL				// Level Bilgisi Sistemi
#endif
// ### WJ Mob Bilgi Eklentisi ###
#define ENABLE_ATTR_TRANSFER_SYSTEM
#define ENABLE_CHAT_LOG_VIEWER				// Chat Log Sistemi
#define ENABLE_OBJ_SCALLING					// Scale Fonksiyonları.
#define ENABLE_OFFLINE_SHOP					// Great Offline Shop Sistemi
#define ENABLE_SHINING_SYSTEM				// Silah - Kostüm - Zırh Efekt Sistemi
#define ENABLE_ENB_MODE						// ENB Mode System(HD)
#define ENABLE_DISCORD_RPC					// Discord Eklentisi
#define ENABLE_EMOJI_IN_TEXT				// Rubinum Emoji Eklentisi
#define ENABLE_BOSS_EFFECT_SYSTEM			// Boss Effect
#define ENABLE_BUY_WITH_ITEM				// Nesne ile Shop item Satma
#define ENABLE_RENEWAL_SHOPEX				// Yıldönümü Parası Sistemi
#define __BL_WEATHER_INFO__					// Dinamik Hava Durumu
#define ENABLE_CHAT_INFO					// Chat İnfoSystem
#define DUNGEON_LIST_TIME					// Zindan Takip Sistemi
#define ENABLE_GLOBAL_CHAT					// Bayraklı Globol Chat


///////////###Kullanım Dışı Sistemler###///////////////
// #define ENABLE_MAGIC_REDUCTION_SYSTEM
//#define ENABLE_SLOT_WINDOW_EX
//#define ENABLE_ACCE_COSTUME_SYSTEM

