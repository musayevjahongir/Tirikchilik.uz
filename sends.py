from settings import TOKEN, URL
import requests



def send_start(chat_id, text, reply_markup):
    url = URL +"sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        'reply_markup': reply_markup
    }

    requests.post(url, json=payload)

def send_photo(chat_id, photo, caption, reply_markup):

    url=URL + "sendPhoto"

    payload = {
        "chat_id": chat_id,
        "text": photo,
        "caption" : caption,
        "parse_mode":"HTML",
        'reply_markup': reply_markup
    }

    requests.post(url, json=payload)




def send_til(chat_id, text, reply_markup):
    url = URL+ "sendMessage" 
    payload ={
        "chat_id": chat_id,
        "text": text,
        'reply_markup': reply_markup
    }
    requests.post(url, text, json=payload)

til = {
    "inline_keyboard" : [
            [{"text" : "🇷🇺 Русский"}],
            [{"text" : "🇺🇿 O'zbekcha"}]
    ]
}

def send_message(chat_id, text, reply_markup):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": text,
        'reply_markup': reply_markup
    }
    requests.post(url, json=payload)

btn1 = {
    'text': '🇷🇺 Русский',
    'url': 'https://t.me/naxalov'

}
btn2 = {
    'text': "🇺🇿 O'zbekcha",
    'url': 'http://google.com'
}

reply_markup = {
    "inline_keyboard": [
        [btn1, btn2]
    ],
}

start = {
    "keyboard": [
        [{'text': '🔥Mahsulotlar'}, {'text': '📥Savat'}],
        [{'text':'💼Hamkorlik'}, {'text':"ℹ️Ma'lumot"}],
        [{"text":"🌐 Tilni tanlash"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

mahsulotlar = {
    "keyboard": [
        [{'text': '🚖Buyurtma berish'}, {'text': '📥Savat'}],
        [{'text':'Troll.uz'}, {'text':"Temur Alixonov"}],
        [{"text":"#ЧЗX"}, {'text': "Konsta"}],
        [{"text":"Go Uz"}, {'text': "Subyektiv"}],
        [{"text":"🏠Bosh menyu"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

Buyurtma_berish = {
    "keyboard": [
        [{'text': "🚖O'zbekiston bo'ylab"}],
        [{'text':"🚖Toshkent shaxri bo'ylab"}],
        [{"text":"🏃O'zim olib ketaman"}],
        [{"text":"🏠Bosh menyu"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

uzb_buylab = {
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}],
        [{'text':"Toshkent viloyati"}],
        [{"text":"Andijon viloyati"}],
        [{"text":"Buxoro viloyati"}],
        [{"text":"Jizzax viloyati"}],
        [{"text":"Qashqadaryo viloyati"}],
        [{"text":"Navoiy viloyati"}],
        [{"text":"Namangan viloyati"}],
        [{"text":"Qoraqalpog'iston Respublikasi"}],
        [{"text":"Samarqand viloyati"}],
        [{"text":"Surxondaryo viloyati"}],
        [{"text":"Sirdaryo viloyati"}],
        [{"text":"Farg'ona viloyati"}],
        [{"text":"Xorazm viloyati"}],
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

toshkent_ichida  = {
    "keyboard": [
        [{'text': "📍Manzilni yuborish", 'request_location': True}],
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

uzim_olaman = {
    "keyboard": [
        [{'text': "📱Raqamni yuborish", 'request_contact': True}],
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

toshkent_tumanlari={
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}],
        [{"text":"Oqqo'rg'on tumani"}],
        [{"text":"Olmaliq shahri"}],
        [{"text":"Angren shaxri"}],
        [{"text":"Oxangaron tumani"}],
        [{"text":"Bekabad tumani"}],
        [{"text":"Bostonliq tumani"}],
        [{"text":"Buka tumani"}],
        [{"text":"Zangiota tumani"}],
        [{"text":"Qibray shahri"}],
        [{"text":"Quyichirchiq tumani"}],
        [{"text":"Parkent tumani"}],
        [{"text":"Piskent tumani"}],
        [{"text":"Toshkent tumani"}],
        [{"text":"Urtachichiq tumani"}],
        [{"text":"Chinaz tumani"}],
        [{"text":"Chirchiq shahri"}],
        [{"text":"Yuqori chirchi tumani"}],
        [{"text":"Yangiyol tumani"}],
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

t_tuman = {
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

andijon = {
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}],
        [{"text":"Andijon shahri"}],
        [{"text":"Oltinko'l tumani"}],
        [{"text":"Andijon tumani"}],
        [{"text":"Asaka tumani"}],
        [{"text":"Baliqchi tumani"}],
        [{"text":"Bo'z tumani"}],
        [{"text":"Buloqboshi tumani"}],
        [{"text":"Jalaquduq tumani"}],
        [{"text":"Izboskan shahri"}],
        [{"text":"Qurg'ontepa tumani"}],
        [{"text":"Marhamat tumani"}],
        [{"text":"Paxtaobot tumani"}],
        [{"text":"Ulug'nor tumani"}],
        [{"text":"Xonabot shahri"}],
        [{"text":"Xo'jaobod tumani"}],
        [{"text":"Shahrihan tumani"}],
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

andijon_tumanlari = {
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

Buxoro_tumanlari = {
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}],
        [{"text":"Buxoro shahri"}],
        [{"text":"Oltoy tumani"}],
        [{"text":"Buxoro tumani"}],
        [{"text":"Vobkent tumani"}],
        [{"text":"G'ijduvon tumani"}],
        [{"text":"Jondor tumani"}],
        [{"text":"Kogon shahri"}],
        [{"text":"Kogon tumani"}],
        [{"text":"Qorako'l shahri"}],
        [{"text":"Qorovulbozor tumani"}],
        [{"text":"Peshku tumani"}],
        [{"text":"Romitan tumani"}],
        [{"text":"Shofirkon tumani"}],
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
    
}

Buxoro = {
    "keyboard": [
        [{"text":"🏠Bosh menyu"}, {"text":"⬅️Ortga"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

malumot = {
    "keyboard": [
        [{"text":"✍️ Izoh qoldirish"}],
        [{"text":"🚀 Yetkazib berish shartlari"}, {"text": "☎️ Kontaktlar"}],
        [{"text":"🏠Bosh menyu"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}
izoh = {
    "keyboard": [
        [{"text":"😊Menga hamma narsa yoqdi, 5❤️"}],
        [{"text":"😊 Yaxshi, 4⭐️⭐️⭐️⭐️"}],
        [{"text":"😐 Qoniqarli, 3 ⭐️⭐️⭐️"}],
        [{"text":"☹️ Yoqmadi, 2 ⭐️⭐️"}],
        [{"text":"😤Men shikoyat qilmoqchiman👎🏻"}],
        [{"text":"🏠Bosh menyu"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

troll = {
    "keyboard": [
        [{"text":"⬅️ Orqaga"}],
        [{'text': '🚖Buyurtma berish'}, {'text': '📥Savat'}],
        [{"text":"Futbolkalar"}, {"text":"Xudi"}],
        [{"text":"Svitshotlar"}, {"text":"Kepkalar"}],
        [{"text":"Stikerlar"}, {"text":"To'plamlar"}],
        [{"text":"🏠Bosh menyu"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

futbolka = {
    "keyboard": [
        [{'text': "Don't be sheep"}, {'text': 'Make Plove Not Var'}],
        [{"text":"Turn on insoff"}, {"text":"Musaffo Sky"}],
        [{"text":"Surish Kerak"}, {"text":"Tanish Bilish"}],
        [{"text":"Tirikchilik"}, {"text":"Use Farosat"}],
        [{"text":"Adolat"}, {"text":"100% paxta"}],
        [{"text":"Plover"}, {"text":"Haqiqat🚫"}],
        [{"text":"Somsa"}, {"text":"QIS 🤌"}],
        [{"text":"Hot Like Non"}, {"text":"Has been selected"}],
        [{"text":"Shashlik"}, {"text":"Say Xo'p"}],
        [{"text":"⬅️ Orqaga"}, {'text': '📥Savat'}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}

dont_sheep= {
    "keyboard": [
        [{'text': 'Oq'}, {'text': 'Qora'}],
        [{"text":"⬅️ Orqaga"}]
    ],
    "one_time_keyboard": True,
    "resize_keyboard": True
}



 # send_start(chat_id=927181585, text="ok", reply_markup=start)