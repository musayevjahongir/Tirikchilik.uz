import sends
import requests
from settings import TOKEN
from time import sleep
from pprint import pprint


def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result']
    else:
        return False


def get_last_update(updates: list[dict]) -> dict:
    return updates[-1]

last_update_id = -1
text1= """
Yetkazib berish uchun manzilni kiriting (ko'cha, uy raqami, mo'ljal) 

Buyurtmalar 10:00 dan 18:00 gacha yektazib beriladi.
Iltimos, 10:00 dan 18:00 gacha bo'ladigan manzilni ko'rsating. ⬇️
"""
while True:
    try:
        updates = get_updates()
        # pprint(updates)
        last_update = get_last_update(updates)
        # pprint(last_update)
        if last_update['update_id'] != last_update_id:
            user = last_update['message']['from']

            if last_update['message']["text"]=="/start" or last_update['message']["text"]=="🏠Bosh menyu":
                    
                text = """Assalomu Alaykum,

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)

O'zbekiston bo'ylab yetkazib berish 2-5 ish kunini tashkil qiladi.

Toshkent bo'ylab yetkazib berish - 20 000 so'm.

O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin."""
                sends.send_start(user["id"], text, sends.start)
            

            elif last_update['message']["text"]=="🔥Mahsulotlar":

                sends.send_start(user["id"], "Bo'limni tanlang👇🏻", sends.mahsulotlar)

            elif last_update['message']["text"]=="🚖Buyurtma berish":

                sends.send_start(user["id"], "Yetkazib berish turini tanlang 👇🏻", sends.Buyurtma_berish)


            elif last_update['message']["text"]=="🚖O'zbekiston bo'ylab":

                t="""Yetkazib berish shartlari:
    O'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi. 
    Toshkent bo'ylab yetkazib berish - 20 000 so'm.
    O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

    450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!
    Yetkazib berish uchun viloyatni tanlang ⬇️
    """

                sends.send_start(user["id"], t, sends.uzb_buylab)

            elif last_update['message']["text"]=="🚖Toshkent shaxri bo'ylab":

                t1="""Yetkazib berish shartlari:
    O'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi. 
    Toshkent bo'ylab yetkazib berish - 20 000 so'm.
    O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

    450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!
    Qaerga yetkazib berish kerak? Quyidagi tugmani bosish orqali joylashuvingizni yuboring 👇🏻
    """

                sends.send_start(user["id"], t1, sends.toshkent_ichida)


            elif last_update['message']["text"]=="🏃O'zim olib ketaman":

                t2="""Buyurtmangiz 1-3 ish kuni davomida (shanba va yakshanbadan tashqari) tayyor bo'ladi.  Buyurtmangiz tayyor bo'lgandan so'ng, menejerimiz siz bilan bog'lanadi va manzili haqida xabar beradi.

    Olib ketish vaqti: 14:00 dan 18:00 gacha.
    Manzil: Mirzo-Ulug'bek tumani, Chust 10A.
    Shanba va yakshanbadan tashqari.
    Telefon raqamini kiriting yoki quyidagi tugmani bosib yuboring ⬇️
    """
                
                sends.send_start(user["id"], t2, sends.uzim_olaman)

            elif last_update['message']["text"]=="Oqqo'rg'on tumani" or last_update['message']["text"]=="Olmaliq shahri" or last_update['message']["text"]=="Angren shaxri" or last_update['message']["text"]=="Oxangaron tumani" or last_update['message']["text"]=="Bekabad tumani" or last_update['message']["text"]=="Bostonliq tumani" or last_update['message']["text"]=="Buka tumani" or last_update['message']["text"]=="Zangiota tumani" or last_update['message']["text"]=="Qibray shahri" or last_update['message']["text"]=="Quyichirchiq tumani" or last_update['message']["text"]=="Parkent tumani" or last_update['message']["text"]=="Piskent tumani" or last_update['message']["text"]=="Toshkent tumani" or last_update['message']["text"]=="Urtachichiq tumani" or last_update['message']["text"]=="Chinaz tumani" or last_update['message']["text"]=="Chirchiq shahri" or last_update['message']["text"]=="Yuqori chirchi tumani" or last_update["message"]["text"]=="Yangiyol tumani":

                sends.send_start(user["id"], text1, sends.t_tuman)

            elif last_update['message']["text"]=="Toshkent viloyati":

                sends.send_start(user["id"], "Yetkazib berish uchun shahar yoki tumanni tanlang ⬇️", sends.toshkent_tumanlari)

            elif last_update['message']["text"]=="Andijon viloyati":

                sends.send_start(user["id"], "Yetkazib berish uchun shahar yoki tumanni tanlang ⬇️", sends.andijon)
            


            elif last_update["message"]["text"]=="Andijon shahri" or last_update["message"]["text"]=="Oltinko'l tumani" or last_update["message"]["text"]=="Andijon tumani" or last_update["message"]["text"]=="Asaka tumani" or last_update["message"]["text"]=="Baliqchi tumani" or last_update["message"]["text"]=="Bo'z tumani" or last_update["message"]["text"]=="Buloqboshi tumani" or last_update["message"]["text"]=="Jalaquduq tumani" or last_update["message"]["text"]=="Izboskan shahri" or last_update["message"]["text"]=="Qurg'ontepa tumani" or last_update["message"]["text"]=="Marhamat tumani" or last_update["message"]["text"]=="Paxtaobot tumani" or last_update["message"]["text"]=="Ulug'nor tumani" or last_update["message"]["text"]=="Xonabot shahri" or last_update["message"]["text"]=="Xo'jaobod tumani" or last_update["message"]["text"]=="Shahrihan tumani":

                sends.send_start(user["id"], text1, sends.andijon_tumanlari)

            elif last_update["message"]["text"]=="Buxoro viloyati":

                sends.send_start(user["id"], "Yetkazib berish uchun shahar yoki tumanni tanlang ⬇️", sends.Buxoro_tumanlari)



            elif last_update["message"]["text"]=="Buxoro tumani" or last_update["message"]["text"]=="Buxoro shahri" or last_update["message"]["text"]=="Oltoy tumani" or last_update["message"]["text"]=="Vobkent tumani" or last_update["message"]["text"]=="G'ijduvon tumani" or last_update["message"]["text"]=="Jondor tumani" or last_update["message"]["text"]=="Kogon shahri" or last_update["message"]["text"]=="Kogon tumani" or last_update["message"]["text"]=="Qorako'l shahri" or last_update["message"]["text"]=="Qorovulbozor tumani" or last_update["message"]["text"]=="Peshku tumani" or last_update["message"]["text"]=="Romitan tumani" or last_update["message"]["text"]=="Shofirkon tumani" :

                sends.send_start(user["id"], text1, sends.Buxoro) 

            elif last_update["message"]["text"]=="💼Hamkorlik": 
                t="""Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.

Menejer bilan bog'lanish uchun: @tirik_chilik"""
                sends.send_start(user["id"], t, sends.start)

            elif last_update["message"]["text"] == "ℹ️Ma'lumot":

                sends.send_start(user["id"], "Kerakli bo'limni tanlang ⬇️", sends.malumot)

            elif last_update["message"]["text"]=="✍️ Izoh qoldirish":
                t3="""✅ Tirikchilik loyihasini tanlaganingiz uchun rahmat.
Bizning xizmatlarimiz sifatini yaxshilashga yordam bersangiz juda xursand bo’lar edik :)
Buning uchun 5 ballik tizim asosida bizni baholang yoki o'z tilaklaringizni yozib jo'nating."""
                sends.send_start(user['id'], t3, sends.izoh)

            elif last_update["message"]["text"]=="😊Menga hamma narsa yoqdi, 5❤️":
                
                t4="""Mamnun qolganingizdan xursandmiz 😊. Siz va yaqinlaringizni har doim xursand qilishga harakat qilamiz 🤗"""

                sends.send_start(user["id"], t4, sends.start)

            elif last_update["message"]["text"]=="😊 Yaxshi, 4⭐️⭐️⭐️⭐️":

                t5="Sizga yoqqanidan xursandmiz 😊. Bot ishlashini yaxshilash uchun qanday maslahatlaringiz bor?👇🏻"

                sends.send_start(user["id"], t5, sends.Buxoro)


            elif last_update["message"]["text"] == "😐 Qoniqarli, 3 ⭐️⭐️⭐️" :

                t7="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. 
Bizni yaxshilashga yordam bering, 
sharh va takliflaringizni qoldiring👇🏻. 
Yaxshilashga harakat qilamiz🙏🏻."""

                sends.send_start(user["id"], t7, sends.Buxoro)

            elif last_update["message"]["text"] == "😤Men shikoyat qilmoqchiman👎🏻" or last_update["message"]["text"] == "☹️ Yoqmadi, 2 ⭐️⭐️":

                t8="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. Yaxshilashga harakat qilamiz🙏🏻"""

                sends.send_start(user["id"], t8, sends.Buxoro)

            elif last_update["message"]["text"]=="☎️ Kontaktlar":

                t9="""Teskari aloqa uchun:
@tirik_chilik"""
                sends.send_start(user["id"], t9, sends.malumot)
            elif last_update["message"]["text"]=="🌐 Tilni tanlash":

                t10="""Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️"""

                sends.send_message(user["id"], t10, sends.reply_markup)
            

            elif last_update["message"]["text"]=="📥Savat":

                sends.send_start(user["id"], "Sizning savatingiz bo'sh", sends.start)


            elif last_update["message"]["text"]=="Troll.uz":
                sends.send_start(user['id'], "Bo'limni tanlang👇🏻", sends.troll)


            elif last_update["message"]["text"]=="Futbolkalar":

                 sends.send_start(user['id'], "Mahsulotni tanlang 👇🏻", sends.futbolka)


            elif last_update["message"]["text"]=="Don't be sheep":

                dont_shep="/c/Users/musay/Desktop/new/Dasturlash/PYTHON/Tirikchilik.uz/dont_be_sheep.jpg"

                ception="""<b>Don't be Sheep</b>

So’kinishni xush ko’rmaydiganlar, ammo ichidagi gapni yumshoqroq aytmoqchi bo’lganlar uchun futbolka😌

Matosi: 100% o’zbek paxtasi

Qo'shimcha sovg'a sifatida  Stiсker Pack №1 beriladi :)

<b>Narxi: 140 000 UZS</b>"""

                sends.send_photo(user["id"], dont_shep, ception, sends.dont_sheep)
            
            elif last_update["message"]["text"] == "🚀 Yetkazib berish shartlari":

                t6="""Yetkazib berish shartlari:
O'zbekiston bo'ylab yetkazib berish 2-5 ish kuni ichida amalga oshiriladi. 
Toshkent bo'ylab yetkazib berish - 20 000 so'm.
O‘zbekiston bo'ylab yetkazib berish - 30 000 so‘m.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!"""
                
                sends.send_start(user["id"], t6, sends.malumot)




            last_update_id=last_update['update_id']
    except: 
        pass
    sleep(0.5) 