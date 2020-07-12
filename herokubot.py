import logging
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyperclip
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

########
########
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
########
########





def start(bot, update):
    bot.send_sticker(chat_id=update.message.chat_id,
                     sticker='CAACAgIAAxkBAAIQGl8HwysLDNIkN92gF1U10eWk_LgtAAI0AgACVp29CjGNzk5PQoF3GgQ')
    update.effective_message.reply_text("سلام!")




def echo(bot, update):
    a = update.effective_message.text
    eslahy = a.replace('ی', 'ي')
    sahm = eslahy.replace('ک', 'ك')

    try:
        driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=111C1417")
        time.sleep(2)
        saham = driver.find_element_by_tag_name("body").text
        if sahm in saham:
            update.effective_message_reply_text("پاندا در حال آنالیز " + sahm + "است.")
            bot.send_sticker(chat_id=update.message.chat_id,
                             sticker='CAACAgIAAxkBAAIQIF8LKeAAAYf7kOPwvfkuJhaTBQloegACLwIAAladvQqEjNbr9zqv7hoE')
            driver.quit()
            driver.get("http://www.tsetmc.com/Loader.aspx?ParTree=111C1417")
            element1 = driver.find_element_by_xpath("//a[@class='TopIcon MwIcon MwQuery']")
            time.sleep(2)
            element1.click()
            element2 = driver.find_element_by_xpath("//div[@class='awesome black']")
            time.sleep(2)
            element2.click()
            elememt3 = driver.find_element_by_xpath("//div[@class='awesome tra'][contains(text(),'0')]")
            time.sleep(2)
            elememt3.click()
            elememt4 = driver.find_element_by_xpath("//textarea[@id='InputFilterCode']")
            time.sleep(2)
            elememt4.click()
            pyperclip.copy(
                "(tvol)>(([ih][0].QTotTran5J+[ih][1].QTotTran5J+[ih][2].QTotTran5J+[ih][3].QTotTran5J+[ih][4].QTotTran5J+[ih][5].QTotTran5J+[ih][6].QTotTran5J+[ih][7].QTotTran5J+[ih][8].QTotTran5J+[ih][9].QTotTran5J+[ih][10].QTotTran5J+[ih][11].QTotTran5J+[ih][12].QTotTran5J+[ih][13].QTotTran5J+[ih][14].QTotTran5J+[ih][15].QTotTran5J+[ih][16].QTotTran5J+[ih][17].QTotTran5J+[ih][18].QTotTran5J+[ih][19].QTotTran5J+[ih][20].QTotTran5J+[ih][21].QTotTran5J+[ih][22].QTotTran5J+[ih][23].QTotTran5J+[ih][24].QTotTran5J+[ih][25].QTotTran5J+[ih][26].QTotTran5J+[ih][27].QTotTran5J+[ih][28].QTotTran5J+[ih][29].QTotTran5J)/30)&&((ct).Buy_I_Volume/(ct).Buy_CountI)>=((ct).Sell_I_Volume/(ct).Sell_CountI)&&(pl)>=(pc)&&(plp)>0")
            elememt4.send_keys(Keys.CONTROL, 'v')
            elememt5 = driver.find_element_by_xpath("//div[@class='awesome blue']")
            time.sleep(2)
            elememt5.click()
            mm1 =  saham = driver.find_element_by_tag_name("body").text
            if sahm in mm1 :
                update.effective_message_reply_text("سهم دارای ورود پول هوشمند با الگوریتم اول میباشد.")
            else:
                update.effective_message_reply_text("سهم دارای ورود پول هوشمند با الگوریتم اول نمیباشد.")



        else:
            update.effective_message_reply_text("نماد " + sahm + "یافت نشد.")
            bot.send_sticker(chat_id=update.message.chat_id,
                             sticker='CAACAgIAAxkBAAIQHV8LKaspEnW1gToEbT4H1QjXXSS_AAIrAgACVp29Cp1dR4-5BfNBGgQ')





    except:
        update.effective_message.reply_text("آه! متاسفانه حین انجام پروسه با مشکل مواجه شدیم لطفا دوباره امتحان کنید")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1139770167:AAErOC1_mzcX3mOl671nu2DOTUV9ubh8V28"
    NAME = "pandatbot5"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.start_polling()
    updater.idle()
