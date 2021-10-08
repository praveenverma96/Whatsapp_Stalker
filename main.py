import Constants as C
from telegram.ext import Updater, CommandHandler, MessageHandler ,Filters
import random
from selenium import webdriver
import time
import datetime

# this function will return message to user when called ( when input format is wrong)
def rand_m():
    a = C.random_messages
    r = random.choice(a)
    return r

# below function will return the start message
def start_command(update, context):
    update.message.reply_text(C.start_msg)

def handle_message(update , context):
    text = str(update.message.text).lower()
    user_message = text.split()
    if len(user_message) == 2:
        try:
            int(user_message[0]) # to check if the first word in the string is a number
            try:
                int(user_message[1]) # validating that the second word is not a number
                print('galat format 1')
                update.message.reply_text(rand_m())
            except Exception:
                print(user_message[1]+' ki stalking chalu')
                update.message.reply_text(user_message[1]+' ki stalking chalu')
                CHROME_PROFILE_PATH = C.CHROME_PROFILE_PATH

                options_ = webdriver.ChromeOptions()
                options_.add_argument(CHROME_PROFILE_PATH)
                #Below option is used so that chrome profile path could be used so that we may not have to Scan Whatsapp QR code everytime
                driver = webdriver.Chrome(executable_path= C.executable_path , options=options_)


                driver.get("https://web.whatsapp.com/send/?phone=91" + user_message[0] + "&text&app_absent=0&lang=en")
                driver.implicitly_wait(2)
                c = "akon"
                time.sleep(3)
                # below code will fetch the current status of our whatsapp contact and send this to user only when status is changed
                while True:
                    time.sleep(2)
                    try:
                        a = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span').text
                        if c != a and a != "click here for contact info":
                            now = datetime.datetime.now()
                            print(user_message[1] + " is " + a + ' @ ' + now.strftime("%H:%M:%S"))
                            z_ = user_message[1] + " is " + a + ' @ ' + now.strftime("%H:%M:%S")
                            c = 'online'
                            update.message.reply_text(z_)


                    except Exception:
                        if c != 'offline':
                            now = datetime.datetime.now()
                            print(user_message[1] +" " +user_message[0]+ " is offline" + ' @ ' + now.strftime("%H:%M:%S"))
                            c = 'offline'
                            z__ = user_message[1] + " is offline" + ' @ ' + now.strftime("%H:%M:%S")
                            update.message.reply_text(z__)
        except:
            print('galat format 2')
            update.message.reply_text(rand_m())
    else:
        print('galat format 3')
        update.message.reply_text(rand_m())

    # update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")

# below function will start out telegram bot, to understand this please go through the telegram's documentation
def main():
    updater = Updater(C.KEY_, use_context= True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()

main() # Calling our main function created above