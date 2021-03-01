import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import Bot
from discord.ext.commands import NoPrivateMessage
import traceback
import itertools
import requests
from bs4 import BeautifulSoup
import pandas
import asyncio
import urllib
import urllib.parse
import json
import time
from selenium import webdriver
from fake_useragent import UserAgent


class _co(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='쿠폰사용', aliases=['쿠폰'])
    async def _co(sefl, ctx, arg1, arg2):
        await ctx.send(
            "서버와 연결 합니다.\n서비 응답속도에 따라 최대 1분 이상 걸릴수도 있습니다."
        )
        #계정확인
        ac = f"계정: {arg1}"
        ac2 = f"쿠폰: {arg2}"

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument('window-size=1920x1080')

        #크롬디르아비 확인


        app = webdriver.Chrome(executable_path="/Users/chaho/Desktop/루나/command/cok/chromedriver", options=options)
        #app = webdriver.Chrome("/Users/chaho/Desktop/루나/command/cok/chromedriver")
        app.implicitly_wait(0.5)
        
        #쿠폰입력 URL
        app.get("https://game.devplay.com/coupon/ck/ko")
        #계정 / 쿠폰 번호 입력
        app.find_element_by_id('email-box').send_keys(arg1)
        app.find_element_by_id('code-box').send_keys(arg2)
        app.find_element_by_xpath('/html/body/div/div[1]/div[2]/form/div[4]/div').click()
        time.sleep(0.5)
        yes = app.switch_to_alert()
        print(yes.text)
        await ctx.channel.purge(limit=1)
        embedco=(
            discord.Embed(
                title="쿠키런 킹덤 쿠폰 요청 처리 결과 입니다.", 
                description="결과내용",
                color=0xFBCB83
            )
            .add_field(
                name="계정",
                value=f"***{arg1}***",
            )
            .add_field(
                name="입력 쿠폰 번호",
                value=f"***{arg2}***",
            )
            .add_field(
                name=f"**{yes.text}**",
                value=f"처리완료",
                inline=False
            )
        )
        await ctx.send(
            embed=embedco
        )
        yes.accept()
        app.close()
    
    @commands.command(name='공지', aliases=["공지사항"])
    async def _coa(self, ctx):
        await ctx.send(
            "쿠키런 킹덤 네이버 카페 공지를 확인합니다.\n서버 상태에 따라 최대 1분 이상 응답 될수도 있습니다"
        )
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument('window-size=1920x1080')
        coaa = webdriver.Chrome(executable_path="/Users/chaho/Desktop/루나/command/cok/chromedriver", options=options)
        coaa.implicitly_wait(0.5)
        coaa.get("https://m.cafe.naver.com/ca-fe/web/cafes/30291108/menus/6")
        coaa2 = coaa.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li[1]/div/a[1]')
        title = coaa2.text
        link = coaa2.get_attribute('href')
        await ctx.channel.purge(limit=1)
        embedcoaa=(
            discord.Embed(
                title="쿠키런 킹덤 최근 공지사항 입니다.",
                description="최근 내용 1개만 불러옵니다",
                color=0xF97070
            )
            .add_field(
                name=f"제목: **{title}**",
                value=f"링크: *{link}*"
            )
        )
        coaa.close()
        await ctx.send(
            embed=embedcoaa
        )
    
    @commands.command(name='패치노트')
    async def _coup(self, ctx):
        await ctx.send(
            "쿠키런 킹덤 네이버 카페 패치노트를 확인합니다.\n서버 상태에 따라 최대 1분 이상 응답 될수도 있습니다"
        )
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument('window-size=1920x1080')
        coaa = webdriver.Chrome(executable_path="/Users/chaho/Desktop/루나/command/cok/chromedriver", options=options)
        coaa.implicitly_wait(0.5)
        coaa.get("https://m.cafe.naver.com/ca-fe/web/cafes/30291108/menus/57")
        coaa2 = coaa.find_element_by_xpath('//*[@id="ct"]/div/div/ul/li[1]/div/a[1]')
        title = coaa2.text
        link = coaa2.get_attribute('href')
        await ctx.channel.purge(limit=1)
        embedcoaa=(
            discord.Embed(
                title="쿠키런 킹덤 최근 패치노트 입니다.",
                description="최근 내용 1개만 불러옵니다",
                color=0xF97070
            )
            .add_field(
                name=f"제목: **{title}**",
                value=f"링크: *{link}*"
            )
        )
        coaa.close()
        await ctx.send(
            embed=embedcoaa
        )
            