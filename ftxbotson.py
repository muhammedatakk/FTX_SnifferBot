import requests 
import time
from datetime import datetime
url = 'https://ftx.com/api/futures'

bot_token = "5351650048:AAG7f82h_7KHMWoLkzx1js0WjeipkdwPK2M"  
chat_iD = ["-678365250"]


yuzde_degisim_orani = 3

def send_message(message) :
    for chat_id in chat_iD :
        while True:
            try:
                requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')
                break 
            except Exception as err :
                print('Mesaj Telegrama iletilirken Hata:',err)
                time.sleep(5)


coin_listesi = [
 "ETH-PERP",
 "SOL-PERP",
 "AVAX-PERP",
 "OP-PERP",
 "ADA-PERP",
 "BNB-PERP",
 "LINK-PERP",
 "WAVES-PERP",
 "XRP-PERP",
 "GMT-PERP",
 "NEAR-PERP",
 "DOT-PERP",
 "FTM-PERP",
 "ANC-PERP",
 "ATOM-PERP",
 "MATIC-PERP",
 "RSR-PERP",
 "APE-PERP",
 "LTC-PERP",
 "AXS-PERP",
 "TRX-PERP",
 "AAVE-PERP",
 "EOS-PERP",
 "GALA-PERP",
 "BSV-PERP",
 "MTL-PERP",
 "SAND-PERP",
 "THETA-PERP",
 "BCH-PERP",
 "FTT-PERP",
 "DOGE-PERP",
 "BAND-PERP",
 "DYDX-PERP",
 "XTZ-PERP",
 "GST-PERP",
 "CRV-PERP",
 "PEOPLE-PERP",
 "ALGO-PERP",
 "SUSHI-PERP",
 "C98-PERP",
 "CEL-PERP",
 "HNT-PERP",
 "MANA-PERP",
 "RUNE-PERP",
 "FIL-PERP",
 "LOOKS-PERP",
 "VET-PERP",
 "SRM-PERP",
 "ETC-PERP",
 "EGLD-PERP",
 "KNC-PERP",
 "ENS-PERP",
 "UNI-PERP",
 "GRT-PERP",
 "FLOW-PERP",
 "YFI-PERP",
 "RAY-PERP",
 "XLM-PERP",
 "ICP-PERP",
 "1INCH-PERP",
 "BAL-PERP",
 "XMR-PERP",
 "LINA-PERP",
 "CRO-PERP",
 "ZEC-PERP",
 "KAVA-PERP",
 "FXS-PERP",
 "ENJ-PERP",
 "OMG-PERP",
 "CELO-PERP",
 "ZIL-PERP",
 "COMP-PERP",
 "IMX-PERP",
 "ONE-PERP",
 "MKR-PERP",
 "LRC-PERP",
 "ALICE-PERP",
 "GAL-PERP",
 "ROSE-PERP",
 "CHZ-PERP",
 "KSM-PERP",
 "NEO-PERP",
 "JASMY-PERP",
 "SNX-PERP",
 "ALPHA-PERP",
 "AR-PERP",
 "FLM-PERP",
 "REN-PERP",
 "KSHIB-PERP",
 "CREAM-PERP",
 "GLMR-PERP",
 "CVX-PERP",
 "DENT-PERP",
 "SXP-PERP",
 "PERP-PERP",
 "MINA-PERP",
 "AUDIO-PERP",
 "CAKE-PERP",
 "BAT-PERP",
 "TLM-PERP",
 "DODO-PERP",
 "RNDR-PERP",
 "CHR-PERP",
 "STEP-PERP",
 "LEO-PERP",
 "SKL-PERP",
 "XEM-PERP",
 "SC-PERP",
 "HBAR-PERP",
 "TOMO-PERP",
 "DASH-PERP",
 "BNT-PERP",
 "ZRX-PERP",
 "ONT-PERP",
 "STORJ-PERP",
 "SLP-PERP",
 "ICX-PERP",
 "IOTA-PERP",
 "SCRT-PERP",
 "REEF-PERP",
 "BIT-PERP",
 "SPELL-PERP",
 "STX-PERP",
 "QTUM-PERP",
 "CVC-PERP",
 "SHIB-PERP",
 "IOST-PERP",
 "BADGER-PERP",
 "HT-PERP",
 "CLV-PERP",
 "AMPL-PERP",
 "HOT-PERP",
 "TRU-PERP",
 "DAWN-PERP",
 "PRIV-PERP",
 "FIDA-PERP",
 "RAMP-PERP",
 "YFII-PERP",
 "OKB-PERP",
 "ATLAS-PERP",
 "MID-PERP",
 "ALCX-PERP",
 "PUNDIX-PERP",
 "EDEN-PERP",
 "TONCOIN-PERP",
 "BOBA-PERP",
 "POLIS-PERP",
 "ROOK-PERP",
 "MOB-PERP",
 "HUM-PERP",
 "RON-PERP",
 "ORBS-PERP",
 "BRZ-PERP",
 "UNISWAP-PERP",
 "PROM-PERP",
 "OXY-PERP",
 "SRN-PERP",
 "MTA-PERP",
 "MAPS-PERP",
 "CONV-PERP",
 "KIN-PERP",
 "MCB-PERP",
 "ASD-PERP",
 "BTT-PERP",
 "BAO-PERP"
]

onceki_fiyatlar = [0 for coin in coin_listesi ]
zaman_verisi = [0 for coin in coin_listesi ]
while True :
    for coin in coin_listesi :
        sira = coin_listesi.index(coin)
        while True:
            try:
                data = requests.get(url+'/'+coin).json()
                fiyat = data['result']['last']
                break 
            except Exception as err :
                print('Bilgiler Alınırken Hata Oluştu. Hata:',err,'Coin:',coin)
                time.sleep(5)
        
        if onceki_fiyatlar[sira]  == 0 :
            onceki_fiyatlar[sira] = fiyat 
            zaman_verisi[sira] = datetime.now()
        
        gecen_zaman = str(round((datetime.now() - zaman_verisi[sira]).seconds/60,0)).split('.')[0]
           
        try:
            yuzde_degisim = round((fiyat-onceki_fiyatlar[sira])/onceki_fiyatlar[sira]*100,2)
        except  :
            yuzde_degisim = 0 

        message = f'{coin} {gecen_zaman} dakika içinde %{yuzde_degisim} değişti.'

        if yuzde_degisim>yuzde_degisim_orani or -yuzde_degisim>yuzde_degisim_orani :
            send_message(message)
        
        onceki_fiyatlar[sira]  = fiyat 
        zaman_verisi[sira] = datetime.now()
        
        print(f'{coin} Değişim:{yuzde_degisim}  Fiyat:{fiyat} Geçen Süre:{gecen_zaman}  ')
        time.sleep(0.001)
