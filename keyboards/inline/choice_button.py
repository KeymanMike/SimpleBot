from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Купи слона",
                                          callback_data=buy_callback.new(item_name="elephant",
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text="Купи мамонта",
                                          callback_data="buy:mammoth:5"
                                      ),
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Сам купи!",
                                          callback_data="cancel"
                                      )
                                  ]

                              ])

elephant_keyboard = InlineKeyboardMarkup()

ELEPHANT_LINK = "https://pokupki.market.yandex.ru/product/miagkaia-igrushka-salvio-slonik-rozovyi-25sm/101056833785?utm_term=10682610%7C101056833785&lrfake=213&utm_source=google&clid=1603&utm_medium=search&utm_campaign=gp_smart_shgb_search_rus&utm_content=cid:11235895800|gid:111585121593|aid:469070487972|ph:pla-1062560726543|pt:|pn:|src:|st:u&gclid=Cj0KCQiAuJb_BRDJARIsAKkycUnPgY__zkegjaz_bvv1JIAQSGhOyYIKgx-A7jIPb3TeIsI3rGUVch4aAjlnEALw_wcB"

elephant_link = InlineKeyboardButton("КУПИИИИ!!", url=ELEPHANT_LINK)

elephant_keyboard.insert(elephant_link)