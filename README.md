# autoinsta_uploader
Automatic Instagram Posting Bot


This Program can be run for example via crontab once (or more) a day.
It takes a random video from videos/, its suiting quote from quotes/, a random thumbnail from thumbnails/ and a random text from texts/.

Then it uses (Firefox) Selenium to log in into Instagram and proceeds to upload the previously selected data.
It uses random delays, hovering over elements and more (such as modified user agents) to prevent IG from detecting the Bot.
Also any error that might occur and daily upload notifications will be send to you through Telegram Bot API.

However, even with all these safety measurements, I do not guarantee IG wont find out ur using a Bot.
Using this may result in bans and other desastrous actions regarding for example your Instagram Account. Hereby no guarantees or responsibilities are taken.

Well i tested it for many days and it worked quite well without being banned.

It is totally possible and will probably happen that IG will change its frontend interface, so it might occur that you need to change the html variables or other factors for Selenium to continue working (Maybe youll need to add another button click in the future). But with the debugging and error logging in place, this is quite easy.


This was tested and run successfully on an Old TV-Box with armbian installed (Altough these TV-Boxes are known to have spying software preinstalled :)  )

If you want to use this for non commercial or commercial usage, youre completely free to use it. Also for every other reason you can use it!
BUT it would be pretty cool if you'd tell me your IG channel so i could watch as you improve your IG life :)

There can be errors or mistakes in the code, it was developed in under 2 days as a small fun project.
(I also have another one for creating random memes and hashtags and music as posts on IG, I'll upload it if someone needs it)

You will have to install some libraries like telebot, but that should not be a problem.
Also you can just comment the display related stuff out, if you dont want to run it in the background or your on Windows.
