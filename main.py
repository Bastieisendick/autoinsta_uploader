import telebot
import time
from datetime import date
import random
import os
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

TGBOT_Token = """ENTER YOUR TELEGRAM BOT TOKEN HERE"""
TGBOT_ChatId = "ENTER YOUR TELEGRAM CHAT ID HERE"
InstagramUsername = "ENTER YOUR INSTAGRAM USERNAME HERE"
InstagramPassword = "ENTER YOUR INSTAGRAM PASSWORD HERE"
start_date = date(2020, 12, 1)
dataDir = "data/"
driverExecutablePath = "driver/chromedriver"
browserProfileName = "ENTER YOUR BROWSER PROFILE NAME HERE"
browserProfilePath = "ENTER YOUR BROWSER PROFILE PATH HERE"
browserLanguage = "ENTER YOUR BROWSER LANGUAGE HERE"
browserUserAgent = "ENTER YOUR BROWSER USER AGENT HERE"




time.sleep(round(random.uniform(1, 1800), 3))               #sleep half an hour at max, so it will not be to predictable





bot = None

def log_error(e, error_type):
    if(bot != None):        #if the Telegram Bot was set already, send the error via Telegram
        try:
            bot.send_message(TGBOT_ChatId, str(error_type) + "\n\n" + str(e))
        except Exception as ec:         #if an error happened here, try to send a telegram message and then log it and continue
            try:
                bot.send_message(TGBOT_ChatId, str("Telegram sending error") + "\n\n" + str(ec))
            except Exception as ece:
                with open(dataDir + "debugging/error_log.txt", "a") as error_file:
                    error_file.write("\n\n\n" + str("Telegram sending error: Couldnt send backup") + "\n\n"+ str(time.time()) + "    " + str(ece))
                print("\n\n\n" + str("Telegram sending error: Couldnt send backup") + "\n\n"+ str(time.time()) + "    " + str(ece))
            
            with open(dataDir + "debugging/error_log.txt", "a") as error_file:
                error_file.write("\n\n\n" + str("Telegram sending error") + "\n\n"+ str(time.time()) + "    " + str(ec))
            print("\n\n\n" + str("Telegram sending error") + "\n\n"+ str(time.time()) + "    " + str(ec))

    with open(dataDir + "debugging/error_log.txt", "a") as error_file:
        error_file.write("\n\n\n" + str(error_type) + "\n\n"+ str(time.time()) + "    " + str(e))
    print("\n\n\n" + str(error_type) + "\n\n"+ str(time.time()) + "    " + str(e))



try:            #try to instantiate the Telegram bot object
    bot = telebot.TeleBot(TGBOT_Token)

except Exception as e:          #if an error occured log it in the error log file and continue
    bot = None
    log_error(str(e), "TeleBot instantiation")
    

theme_name = None
video_name = None
video_path = None
quote_text = None
thumbnail_path = None
post_text = None


try:            #select the video, quote, thumbnail and text from the files in a random way

    directories = [f for f in os.listdir(dataDir + "videos/") if os.path.isdir(os.path.join(dataDir + "videos/", f))]
    theme_name = str(random.choice(directories))
    
    videofiles = [file for file in os.listdir(dataDir + "videos/" + theme_name + "/") if file.endswith(".mp4")]
    video_name = str(os.path.splitext(str(random.choice(videofiles)))[0])            #only take the file name, not the extension
    video_path =  os.path.abspath(dataDir + "videos/" + theme_name + "/" + video_name + ".mp4")

    quote_text = str(open(dataDir + "quotes/" + theme_name + "/" + video_name + ".txt").read())

    thumbnailfiles = [file for file in os.listdir(dataDir + "thumbnails/" + theme_name + "/") if file.endswith(".png")]
    thumbnail_path =  os.path.abspath(dataDir + "thumbnails/" + theme_name + "/" + str(random.choice(thumbnailfiles)))

    post_textfiles = [file for file in os.listdir(dataDir + "texts/" + theme_name + "/") if file.endswith(".txt")]
    post_text = str(open(dataDir + "texts/" + theme_name + "/" + str(random.choice(post_textfiles))).read())

except Exception as e:
    log_error(str([str(e), theme_name, video_name, video_path, quote_text, thumbnail_path, post_text]), "Post Selection")
    sys.exit(0)



try:            #validate the paths and insert the missing caption values

    if(os.path.isfile(video_path) != True or os.path.isfile(thumbnail_path) != True):           #if the calculated paths are not files, log an error and exit
        log_error(str([str(e), video_path, thumbnail_path]), "Validate path: Not a file")
        sys.exit(0)

    post_text = post_text.replace("{quote}", quote_text)
    
    
    post_text = post_text.replace("{daycount}", str((date.today() - start_date).days))


except Exception as e:
    log_error(str([str(e), video_path, thumbnail_path]), "Validate data")
    sys.exit(0)


browser = None

try:            #main part, connect to instagram and post the post

    options = uc.ChromeOptions()

    options.add_argument('--user-agent="' + browserUserAgent + '"')
    
    prefs = {
        "intl.accept_languages": browserLanguage,           #Also change the language in the settings of your used Chrome profile
        "intl.selected_languages": browserLanguage
    }

    options.add_experimental_option("prefs", prefs)

    options.add_argument("--user-data-dir=" + browserProfilePath)
    options.add_argument("--profile-directory=" + browserProfileName)


    browser = uc.Chrome(options=options, driver_executable_path=driverExecutablePath)

    time.sleep(round(random.uniform(10.235, 13.63), 3))

    browser.set_window_size(820,1180)

    browser.get("https://www.instagram.com/")

    time.sleep(round(random.uniform(33.534, 45.78), 3))

    actions = ActionChains(browser)

    try:                #check if there is a cookie button present
        cookie_button = browser.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_0']")
        actions = ActionChains(browser)
        actions.move_to_element(cookie_button).perform()

        time.sleep(round(random.uniform(0.34, 1.23), 3))

        cookie_button.click()

        time.sleep(round(random.uniform(11.26, 14.145), 3))

    except NoSuchElementException:
        pass

    browser.save_screenshot(dataDir + "debugging/screenshot_1_login.png")

    try:
        username_input = browser.find_element(By.XPATH, "//input[@name='username']")
        
        actions = ActionChains(browser)
        actions.move_to_element(username_input).perform()

        for char in InstagramUsername:             #simulate some typing
            username_input.send_keys(char)
            time.sleep(round(random.uniform(0.23, 1.31), 3))

        time.sleep(round(random.uniform(2.43, 4.27), 3))


        password_input = browser.find_element(By.XPATH, "//input[@name='password']")
        
        actions = ActionChains(browser)
        actions.move_to_element(password_input).perform()

        for char in InstagramPassword:             #simulate some typing
            password_input.send_keys(char)
            time.sleep(round(random.uniform(0.26, 1.39), 3))

        time.sleep(round(random.uniform(1.21, 3.82), 3))

        submit_button = browser.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")

        actions = ActionChains(browser)
        actions.move_to_element(submit_button).perform()

        time.sleep(round(random.uniform(1.21, 3.82), 3))

        submit_button.click()

        time.sleep(round(random.uniform(56.45, 67.97), 3))

        browser.save_screenshot(dataDir + "debugging/screenshot_2_logged_in.png")

        browser.get("https://www.instagram.com/")

        time.sleep(round(random.uniform(78.12, 83.63), 3))

    except:
        browser.save_screenshot(dataDir + "debugging/screenshot_2_5_alreadyloggedin.png")

    try:                #check if there is a notification button present
        notification_button = browser.find_element(By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']")
        actions = ActionChains(browser)
        actions.move_to_element(notification_button).perform()

        time.sleep(round(random.uniform(0.33, 1.27), 3))

        notification_button.click()

        time.sleep(round(random.uniform(14.89, 15.87), 3))

    except NoSuchElementException:
        pass

    browser.save_screenshot(dataDir + "debugging/screenshot_3_main_page.png")

    create_button = browser.find_element(By.CSS_SELECTOR, "svg[aria-label='Neuer Beitrag']")

    actions = ActionChains(browser)
    actions.move_to_element(create_button).perform()

    time.sleep(round(random.uniform(0.42, 2.23), 3))


    create_button.click()

    time.sleep(round(random.uniform(64.91, 68.64), 3))

    browser.save_screenshot(dataDir + "debugging/screenshot_4_upload_video.png")

    upload_file = browser.find_element(By.CSS_SELECTOR, "input._ac69[accept*='video/mp4']")
    upload_file.send_keys(video_path)

    time.sleep(round(random.uniform(600.46, 900.19), 3))

    try:                #check if there is a reelcreation button present
        reelcreation_button = browser.find_element(By.XPATH, "//button[@class=' _acan _acap _acaq _acas _acav _aj1- _ap30']")
        actions = ActionChains(browser)
        actions.move_to_element(reelcreation_button).perform()

        time.sleep(round(random.uniform(0.45, 1.93), 3))

        reelcreation_button.click()

        time.sleep(round(random.uniform(15.74, 16.35), 3))

    except NoSuchElementException:
        pass
        
        
    continue_button = browser.find_element(By.XPATH, "//div[text()='Weiter']")

    actions = ActionChains(browser)
    actions.move_to_element(continue_button).perform()

    time.sleep(round(random.uniform(0.33, 1.86), 3))

    continue_button.click()

    time.sleep(round(random.uniform(50.45, 52.86), 3))

    browser.save_screenshot(dataDir + "debugging/screenshot_5_upload_thumbnail.png")

    upload_thumbnail = browser.find_element(By.CSS_SELECTOR, "input._ac69[accept='image/jpeg,image/png']")
    upload_thumbnail.send_keys(thumbnail_path)

    time.sleep(round(random.uniform(45.34, 56.41), 3))

    continue_button = browser.find_element(By.XPATH, "//div[text()='Weiter']")

    actions = ActionChains(browser)
    actions.move_to_element(continue_button).perform()

    time.sleep(round(random.uniform(0.38, 1.47), 3))

    continue_button.click()

    time.sleep(round(random.uniform(63.16, 68.63), 3))

    browser.save_screenshot(dataDir + "debugging/screenshot_6_write_caption.png")

    caption_text_field = browser.find_element(By.XPATH, "//div[starts-with(@aria-label, 'Bildunterschrift verfassen')]")
        
    actions = ActionChains(browser)
    actions.move_to_element(caption_text_field).perform()

    time.sleep(round(random.uniform(0.36, 1.79), 3))

    caption_text_field.click()

    time.sleep(round(random.uniform(2.69, 3.39), 3))

    for char in post_text:             #simulate some typing
        caption_text_field.send_keys(char)
        time.sleep(round(random.uniform(0.29, 0.98), 3))

    time.sleep(round(random.uniform(2.63, 3.72), 3))

    share_button = browser.find_element(By.XPATH, "//div[text()='Teilen']")

    actions = ActionChains(browser)
    actions.move_to_element(share_button).perform()

    time.sleep(round(random.uniform(0.31, 1.24), 3))

    share_button.click()

    time.sleep(round(random.uniform(1840.42, 1927.35), 3))

    browser.save_screenshot(dataDir + "debugging/screenshot_7_done.png")

    bot.send_message(TGBOT_ChatId, "Day " + str((date.today() - start_date).days) + "\n\n" + quote_text)

    try:
        browser.quit()
    except:
        pass

except Exception as e:

    try:
        browser.quit()
    except:
        pass
    log_error(str(e), "Instagram connection")
    sys.exit(0)

try:
    browser.quit()
except:
    pass


