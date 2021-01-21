import os
import telebot
from time import sleep
from telebot import types
from PIL import ImageGrab
import psutil

#work in linux 

Magenta = '\033[95m'
os.system("clear")


print("\n")
print(Magenta+"""

 █████╗ ██╗     ██╗     ██████╗ ███████╗    ██████╗ ███████╗███╗   ███╗ ██████╗ ████████╗███████╗██████╗     
██╔══██╗██║     ██║    ██╔═══██╗██╔════╝    ██╔══██╗██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗    
███████║██║     ██║    ██║   ██║███████╗    ██████╔╝█████╗  ██╔████╔██║██║   ██║   ██║   █████╗  ██████╔╝    
██╔══██║██║     ██║    ██║   ██║╚════██║    ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══╝  ██╔══██╗    
██║  ██║███████╗██║    ╚██████╔╝███████║    ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗██║  ██║    
╚═╝  ╚═╝╚══════╝╚═╝     ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝    
                                                                            
""")

print("\n")
print("Bot is ready !")
print("\n")

#---------------#
TOKEN = "your token"
bot = telebot.TeleBot(TOKEN)
#---------------#

def poweroptions(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.last_name
    #---------
    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton("Shutdown⬇️")
    dokme2 = types.KeyboardButton("Restart🔄")
    dokme5 = types.KeyboardButton("Hibernate❄️")
    dokme3 = types.KeyboardButton("Sleep💤")
    dokme4 = types.KeyboardButton("Home🏘")
    dokmeha.add(dokme1,dokme2,dokme5,dokme3,dokme4)
    bot.send_message(userchatid, "Welcome to power options", reply_markup=dokmeha)

def system_monitor(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.last_name

    bot.send_message(userchatid,"cpu: "+str(psutil.cpu_percent())+"% \nram: "+str(psutil.virtual_memory().percent)+"% \nbattery: "+str(int(psutil.sensors_battery().percent))+"% \n\nroot disk used: "+str(psutil.disk_usage('/').percent)+"% \nhome disk used: "+str(psutil.disk_usage('/home').percent)+"% \n\nbattery power plugged: "+str(psutil.sensors_battery().power_plugged)+"\n\nfans: "+str(psutil.sensors_fans())) 

def takescreenshot(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.last_name

    bot.send_message(userchatid,"🙂Taking a screen shot...")
    ThisIsPhoto = ImageGrab.grab()
    ThisIsPhoto.save("screenshot.png")
    bot.send_message(userchatid,"Screenshot was taked 😊\n◼️ Sending...")
    photo = open("screenshot.png","rb")
    bot.send_photo(userchatid,photo,caption="Here you are")
    photo.close()
    os.remove("screenshot.png")
    startcmd(user, 1)

def download_this_file(user):
    userchatid = user.chat.id
    usertext = user.text
    filename_or_fileadress = usertext.replace("/download ","")
    if(os.path.isdir(str(filename_or_fileadress))):
        bot.send_message(userchatid,"This is folder :)")
    else:
        if(os.path.isfile(str(filename_or_fileadress))):
            bot.send_message(userchatid,"Downloading "+str(filename_or_fileadress)+"...")
            thefile = open(filename_or_fileadress,"rb")
            bot.send_document(userchatid,thefile,caption="This is your file")
        else:
            bot.send_message(userchatid,"Not Found")
            pass

def filemanager(user):
    userchatid = user.chat.id
    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton("Home🏘")
    dokme2 = types.KeyboardButton("📥 Download")
    dokme3 = types.KeyboardButton("🗂 File List")
    dokmeha.add(dokme2, dokme3, dokme1)
    bot.send_message(userchatid,"Welcome to filemanager",reply_markup=dokmeha)

def downloadfile(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,"Usage :\n/download [file name/file adress]")

def justfilelist(user):
    userchatid = user.chat.id
    bot.send_message(userchatid,"Usage:\n/filemanager [dir]")

def filemanagerlist(user):
    userchatid = user.chat.id
    usertext = user.text

    directory = usertext.replace("/filemanager ","")

    if(os.path.isdir(directory)):
        bot.send_message(userchatid,"🔎 Scanning....")

        sleep(1)

        foldercount = 0
        folderlist = ""

        filecount = 0
        filelist = ""

        for r, d, f in os.walk(directory):
            for folder in d:
                if(foldercount > 30 or foldercount == 30):
                    break
                else:
                    if("\\" in r):
                        pass
                    else:
                        foldercount += 1
                        folderlist = folderlist+"\n"+"📁 "+r+"/"+folder
            for file in f:
                if(filecount > 30 or filecount == 30):
                    break
                else:
                    filecount += 1
                    filelist = filelist+"\n"+"🧾 "+r+"/"+file
        bot.send_message(userchatid,"🗂 30 First Folders In "+directory+" : \n\n"+str(folderlist))
        bot.send_message(userchatid,"🗃 30 First File In "+directory+" : \n\n"+str(filelist))
    else:
        bot.send_message(userchatid,"I can't find this directory  :(")

def startcmd(user , check):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.last_name

    dokmeha = types.ReplyKeyboardMarkup(row_width=2)
    dokme1 = types.KeyboardButton("📸 Take a screen shot")
    dokme2 = types.KeyboardButton("🔋 Power options")
    dokme3 = types.KeyboardButton("📊 System monitor")
    dokme4 = types.KeyboardButton("🗃 File Manager")

    dokmeha.add(dokme1, dokme2, dokme3, dokme4)

    bot.send_message(
        userchatid, "Hi Ai how can i help you?", reply_markup=dokmeha)
    if check == 1:
        print("User "+str(userchatid)+" Back to Home")
    else:
        print("User "+str(userchatid)+" Started The Bot")
#--------------#


@bot.message_handler(content_types=['text'])
def botmain(user):
    admin = "fateme_malakooti"
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.last_name
    #------------------------------------#
    if(userusername == admin):
        #-------------#
        if(usertext == "/start" or usertext == "Home🏘"):
            if (usertext == "Home🏘"):
                check = 1
            else:
                check = 2

            startcmd(user , check)

        if(usertext == "🔋 Power options"):
            poweroptions(user)

        if(usertext == "📸 Take a screen shot"):
            takescreenshot(user)
        
        if (usertext == "📊 System monitor"):
            system_monitor(user)

        if (usertext == "Shutdown⬇️"):
            bot.send_message(userchatid, "Shutting down the system...")
            bot.send_message(userchatid, "3️⃣")
            sleep(1)
            bot.send_message(userchatid, "2️⃣")
            sleep(1)
            bot.send_message(userchatid, "1️⃣")
            sleep(1)
            bot.send_message(userchatid, "system shut down successfully✅")
            os.system("shutdown now")
        
        if (usertext == "Restart🔄"):
            bot.send_message(userchatid, "Restarting the system...")
            bot.send_message(userchatid, "3️⃣")
            sleep(1)
            bot.send_message(userchatid, "2️⃣")
            sleep(1)
            bot.send_message(userchatid, "1️⃣")
            sleep(1)
            bot.send_message(userchatid, "system restart successfully✅")
            os.system("reboot")

        if (usertext == "Sleep💤"):
            bot.send_message(userchatid, "Sleeping the system...")
            bot.send_message(userchatid, "3️⃣")
            sleep(1)
            bot.send_message(userchatid, "2️⃣")
            sleep(1)
            bot.send_message(userchatid, "1️⃣")
            sleep(1)
            bot.send_message(userchatid, "system sleep successfully✅")
            os.system("systemctl suspend")

        if (usertext == "Hibernate❄️"):
            bot.send_message(userchatid, "Hibernateing the system...")
            bot.send_message(userchatid, "3️⃣")
            sleep(1)
            bot.send_message(userchatid, "2️⃣")
            sleep(1)
            bot.send_message(userchatid, "1️⃣")
            sleep(1)
            bot.send_message(userchatid, "system Hibernate successfully✅")
            os.system("systemctl hibernate")

        if(usertext == "🗃 File Manager"):
            filemanager(user)
        
        if(usertext == "📥 Download"):
            downloadfile(user)
        
        if(usertext.startswith("/download ")):
            download_this_file(user)
        
        if(usertext == "/download"):
            downloadfile(user)

        if(usertext == "🗂 File List" or usertext == "/filemanager"):
            justfilelist(user)

        if(usertext.startswith("/filemanager ")):
            filemanagerlist(user)



    #-------------#
    else:
        print("Shoma Ali nistid")


#---------------#
bot.polling(True)
