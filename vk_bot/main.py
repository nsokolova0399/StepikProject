import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

vk = vk_api.VkApi(token="vk1.a.1zYvFKvwxgBnTlnp7jj5nj3vt3qsWpLLIrTQMKblJrILHn6IJVZW3seodka9ZVb--m9xLgi_uQaPAlaUE-CzqY7tidwjpJ8q7k52d2iU-J1PJVKFfab3FI1--9_ygcmdF2u0ghWlgyFoDkOVr7F1jHMKmgdCjjhP9ZqyGFlz2vMeBoJeidjuafIvicA_OTIf_tNjnAxlEeBqse8EplRbZg")

import json
from typing import Optional

class Keyboard:

    def __init__(self, button: list, one_time=False, inline=False):
        self.one_time = one_time
        self.inline = inline

        self.keyboard = {
            "one_time": self.one_time,
            "inline": self.inline,
            "buttons": button
        }

    def add_keyboard(self):
        obj = json.dumps(self.keyboard, ensure_ascii=False).encode("utf-8")
        return obj.decode("utf-8")

    def get_empty_keyboard(self):
        self.keyboard["buttons"] = []
        return self.add_keyboard()
class Text:

    def __new__(cls, label: Optional[str], color: Optional[str]="secondary", payload: Optional[str]=None):
        return {
            "action": {
                "type": "text",
                "label": label,
                "payload": payload
            },
            "color": color
        }
class OpenLink:

    def __new__(cls, label: Optional[str], link: Optional[str], payload: Optional[str]=None):
        return {
            "action": {
                "type": "open_link",
                "label": label,
                "link": link,
                "payload": payload
            }
        }
class Location:

    def __new__(cls, payload: Optional[str]=None):
        return {
            "action": {
                "type": "location",
                "payload": payload
            }
        }
class VkPay:

    def __new__(cls, pay_hash: Optional[str], payload: Optional[str]=None):
        return {
            "action": {
                "type": "vkpay",
                "hash": pay_hash,
                "payload": payload
            }
        }
class VkApps:

    def __new__(cls, app_id: Optional[int], owner_id: Optional[int], label: Optional[str], app_hash: Optional[str], payload: Optional[str]=None):
        return {
            "action": {
                "type": "vkapps",
                "app_id": app_id,
                "owner_id": owner_id,
                "label": label,
                "hash": app_hash,
                "payload": payload
            }
        }


def send_message(user_id, message, keyboard=None, photo=None):
    values = {
        "user_id": user_id,
        "message": message,
        "random_id": 0,
        "attachment": photo
    }

    if keyboard is not None:
        values["keyboard"] = keyboard.add_keyboard()
    vk.method("messages.send", values)


main_menu_button = [Text("Основное меню", "primary")]
faq_menu_button = [Text("FAQ", "positive")]


def buttons_menu(text, color):
    if color == "белый":
        return [Text(text, "secondary")]
    if color == "красный":
        return [Text(text, "negative")]
    if color == "зеленый":
        return [Text(text, "positive")]
    return [Text(text,"primary")]



for event in VkLongPoll(vk).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id
        peer_id = event.peer_id

        if text == "начать":
            send_message(user_id, "Я Роман – виртуальный помощник Ренессанс Банка. Я с радостью помогу Вам! Выберите, что Вас интересует:\n • Консультация \n• Лучшие продукты\n • FAQ",
                         Keyboard([buttons_menu("Консультация", "синий"),buttons_menu("Лучшие продукты","синий"),faq_menu_button]),"photo-photo-169511143_457239038")

        if text == "основное меню":
            send_message(user_id,
                         "Я с радостью помогу Вам! Выберите, что Вас интересует:\n • Консультация \n• Лучшие продукты\n • FAQ",
                         Keyboard([buttons_menu("Консультация", "синий"),buttons_menu("Лучшие продукты","синий"),faq_menu_button]))
        if text == "консультация":
            send_message(user_id,
                         "Если Вы хотите консультацию в чате или звонок оператора – выберите соответствующий пункт меню.\n Но я могу помочь Вам с ответами на самые популярные вопросы, просто откройте раздел FAQ.",
                         Keyboard([buttons_menu("Чат с консультантом", "синий"), buttons_menu("Перезвоните мне", "синий"),
                                   faq_menu_button, main_menu_button]))
        if text == "чат с консультантом":
            send_message(user_id,
                         "Я направил Ваш запрос консультанту – ожидайте его сообщения.\n А пока можете задать ему вопрос или описать свою ситуацию.",
                         Keyboard([main_menu_button]))
            # тут отправляем от бота сообщение модератору
            vk.get_api().messages.send(user_id=300297538, message='Клиент ждет Вашего ответа в чате', random_id=0)
        if text == "перезвоните мне":
            send_message(user_id,
                         "Пожалуйста, уточните, как можно к Вам обращаться.",
                         Keyboard([buttons_menu("Продолжить", "синий"),main_menu_button]))
        # подумать как бот будет записывать ответ пользователя
        if text == "продолжить":
            send_message(user_id,
                         "Пожалуйста, укажите свой номер телефона.",
                         Keyboard([buttons_menu("Продолжить", "синий"), main_menu_button]))





