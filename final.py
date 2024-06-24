import discord
import time
import random
from datetime import datetime
from discord.ui import Button, View
from discord.ext import commands
import os, random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name}, giriş yaptı!')
    


@bot.command()
async def kronometre(ctx, sure = 5):
    if sure % 60 == 0:
        await ctx.send(f"Tabii, {sure / 60 - 0} dakikalık kronometreyi başlattım!")
    else:
        await ctx.send(f"Tabii, {sure} saniyelik kronometreyi başlattım!")
    time.sleep(sure)
    await ctx.send("Süre bitti!")
@bot.command()
async def alarm(ctx, alarm = 0 , alarm2 = 0):
    if alarm <= 23 and alarm >= 0 and alarm2 <= 59 and alarm2 >= 0:
        if datetime.now().hour < alarm: 
                await ctx.send(f"Tabii! Sana {alarm}:{alarm2} olunca haber vereceğim!")
                while True:
                    if datetime.now().hour == alarm and datetime.now().minute >= alarm2:
                        await ctx.send(f"Hey! {alarm}:{alarm2} için hazırlanan alarm çalıyor! Bzzzzz...")
                        break 
                    

         
        elif datetime.now().hour == alarm:
            if datetime.now().minute >= alarm2:
                await ctx.send("Maalesef, sana sadece bugün içinde bir alarn kurabilirim!")
            else:
                await ctx.send(f"Tabii! Sana {alarm}:{alarm2} olunca haber vereceğim!")
                while True:
                    if datetime.now().hour == alarm and datetime.now().minute >= alarm2:
                        await ctx.send(f"Hey! {alarm}:{alarm2} için hazırlanan alarm çalıyor! Bzzzzz...")
                        break
        else:
            await ctx.send("Maalesef, sana sadece bugün içinde bir alarn kurabilirim!")
    else:
        await ctx.send("Dostum, uçuk rakam söyleme!")
@bot.command()
async def yazıtura(ctx):
    
    await ctx.send("Çeviriyorum...")
    cevir = random.randint(1,2)
    if cevir == 1:
        cevir_sonuc = "Yazı"
    else:
        cevir_sonuc = "Tura"
    time.sleep(5)
    await ctx.send(f"{cevir_sonuc} çıktı!")

@bot.command()
async def mem(ctx, mem="mem1"):
    if mem == "kaybol":
        with open('images/ehe.gif', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send("Tamam dostum, görüşürüz ✌")
    
    elif mem == "nugget":
        with open('images/ehe2.gif', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send("Gedagedigedagedao 🍗")
    elif mem == "mewing":
        with open('images/ehe3.gif', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send("Bye bye... 🤫🧏‍♂️")
    else:
        await ctx.send("Dostum... Bu mem bende yok.")

@bot.command()
async def rastgele_mem(ctx):
    rastgele_resim = random.choice(os.listdir("images"))
    with open(f'images/{rastgele_resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def kanal_ekle(ctx):
    await ctx.send("[__İşte buradan__](https://discord.com/oauth2/authorize?client_id=1242528489652097064&permissions=8&integration_type=0&scope=bot) beni istediğin sunucuya davet edebilirsin!")   

@bot.command()
async def masal(ctx):
    await ctx.send("# Uzak Bir Diyarda Bir Prenses Var")
    await ctx.send("Bir varmış, bir yokmuş, uzak bir diyarda bir prenses varmış. Bu prenses çok güzelmiş, hem de çok nazik ve iyi kalpliymiş. Herkes onu çok severmiş.  Prensesin babası kralmış, annesi ise kraliçe. Prensesin bir de ağabeyi varmış. Ağabeyi yakışıklı ve cesur bir prensmiş.  Bir gün, prenses ormanda yürürken kaybolmuş. Uzun süre ne yapacağını bilememiş. Ağlamaya başlamış tam o sırada, yakışıklı bir prens ortaya çıkmış. Prens prensese yolunu sormuş ve onu şatoya geri götürmüş.  Prenses prense aşık olmuş, prens de prensese aşık olmuş. Kral ve kraliçe bu duruma çok sevinmişler ve prens ile prensesi evlendirmişler.  Prenses ve prens çok mutlu yaşamışlar. Sonsuza kadar mutlu yaşamışlar mı? Tabii ki! Masallar daima mutlu sonla biter.")
        
@bot.command()
async def çevre(ctx, bilgi=""):
    if bilgi == "":
        await ctx.send("Çevre, doğal yaşamı ve insanların yaşadığı, etkileşimde bulunduğu, çevresel faktörlerin bir araya geldiği tüm ortamları ifade eder. Çevre, biyotik (canlı) ve abiyotik (cansız) bileşenlerden oluşur.")
    elif bilgi == "sorunlar":
        await ctx.send("## Çevre Sorunları")
        await ctx.send(" - **Kirlilik:** Hava, su ve toprak kirliliği, canlıların sağlığını tehdit eder ve ekosistemleri bozar.")
        await ctx.send(" - **İklim Değişikliği:** Küresel ısınma ve iklim değişikliği, çevresel dengenin bozulmasına neden olur.")
        await ctx.send(" - **Ormansızlaşma:** Ağaçların kesilmesi, biyolojik çeşitliliğin azalmasına ve karbon döngüsünün bozulmasına yol açar.")
        await ctx.send(" - **Doğal Kaynakların Tükenmesi:** Aşırı tüketim, yenilenemez doğal kaynakların hızla tükenmesine neden olur.")
    elif bilgi == "çözümler":
        await ctx.send("Hangi çözüm türünü öğrenmek istiyorsunuz?")
        button1=Button(label="Kirliliği Azaltma",style=discord.ButtonStyle.green)
        button2=Button(label="İklim Değişikliği ile Mücadele",style=discord.ButtonStyle.green)
        button3=Button(label="Biyolojik Çeşitliliği Koruma",style=discord.ButtonStyle.green)
        button4=Button(label="Sürdürülebilir Tüketim ve Üretim",style=discord.ButtonStyle.green)
        async def button1_callback(interaction):
            await ctx.send("## Kirliliği Azaltma")

            await ctx.send("* **Hava Kirliliği:** \n - Fosil yakıt kullanımını azaltarak ve yenilenebilir enerji kaynaklarına yönelerek hava kirliliğini azaltabiliriz."
                           "\n - Toplu taşıma araçlarını kullanmak, bisiklete binmek ve yürümek gibi alternatif ulaşım yöntemleri tercih edilebilir."
                           "\n - Endüstriyel tesislerde filtre ve temizleyici sistemlerin kullanılması sağlanabilir.")
            

            await ctx.send("* **Su Kirliliği:**"

            "\n - Atık suların arıtılarak doğaya salınması sağlanabilir."
            "\n - Tarımda kullanılan kimyasal gübre ve pestisitlerin kontrolü ve azaltılması teşvik edilebilir."
            "\n - Sanayi atıklarının düzenli ve güvenli bir şekilde bertaraf edilmesi sağlanabilir.")

            await ctx.send("* **Toprak Kirliliği:**"

            "\n - Kimyasal gübre ve pestisit kullanımını azaltarak organik tarıma yönelim sağlanabilir."
            "\n - Katı atıkların geri dönüştürülmesi ve düzenli depolama alanlarının kullanılması teşvik edilebilir")

        async def button2_callback(interaction):
            await ctx.send("## İklim Değişikliği ile Mücadele")
            await ctx.send("* **Yenilenebilir Enerji:**"
                            "\n - Güneş, rüzgar, hidroelektrik ve jeotermal gibi yenilenebilir enerji kaynaklarının kullanımı artırılabilir."
                            "\n - Enerji verimliliğini artıran teknolojilere yatırım yapılabilir.")
                            
            await ctx.send("* **Karbon Ayak İzini Azaltma:**"

                            "\n - Bireyler ve şirketler, karbon ayak izini azaltmak için enerji tasarrufu sağlayan uygulamalar benimseyebilir."
                            "\n - Ormanları koruyarak ve ağaç dikerek karbon yutakları oluşturulabilir.")

            await ctx.send("* **Sürdürülebilir Tarım ve Hayvancılık:**"
                            "\n - Sürdürülebilir tarım ve hayvancılık yöntemleri teşvik edilebilir."
                            "\n - Gıda israfını azaltmak için toplum bilinçlendirilebilir.")
    
        button1.callback= button1_callback
        button2.callback= button2_callback
        view=View()
        view.add_item(button1)
        view.add_item(button2)
        await ctx.send(view=view)

            

  
bot.run("BOT CODE HERE")
