# autoinsta_uploader
Automatic Instagram Posting Bot<br/>

This Program can be run for example via crontab once (or more) a day.<br/>
It takes a random video from data/videos/, its suiting quote from data/quotes/, a random thumbnail from data/thumbnails/ and a random text from data/texts/.<br/>

Then it uses [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) Selenium to log in into Instagram and proceeds to upload the previously selected data.<br/>
It uses random delays, hovering over elements and more (such as modified user agents) to prevent IG from detecting the Bot.<br/>
Also any error that might occur and daily upload notifications will be send to you through Telegram Bot API.<br/>

You will have to change the variables in the start of the file to your own values, but this should be self explanatory.<br/>
Also you need to download a suiting chromedriver and move it into the driver/ folder.<br/>
If you have any question, dont hesitate telling me!<br/>

However, even with all these safety measurements, I do not guarantee IG wont find out ur using a Bot.<br/>
Using this may result in bans and other desastrous actions regarding for example your Instagram Account. Hereby no guarantees or responsibilities are taken.<br/>

Well i tested it for many days and it worked quite well without being banned.<br/>

It is totally possible and will probably happen that IG will change its frontend interface, so it might occur that you need to change the html variables or other factors for Selenium to continue working (Maybe youll need to add another button click in the future).<br/>
But with the debugging and error logging in place, this is quite easy.<br/>


This was tested and run successfully on an Old TV-Box with armbian installed (Altough these TV-Boxes are known to have spying software preinstalled :)  )<br/>
Also works on Windows and Ubuntu!<br/>

There can be errors or mistakes in the code, it was developed in under 2 days as a small fun project.<br/>
(I also have another one for creating random memes and hashtags and music as posts on IG, I'll upload it if someone needs it)<br/>

You will have to install some libraries like [telebot/pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) and [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver), but that should not be a problem.<br/>
