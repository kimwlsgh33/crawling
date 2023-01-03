// const puppeteer = require('puppeteer');
import puppeteer from 'puppeteer';

(async () => {
  // puppeteer를 실행(default : headless)
  const browser = await puppeteer.launch();
  // 새로운 페이지 열기
  const page = await browser.newPage();
  // 페이지 접속
  await page.goto('https://www.google.com');
  // 페이지 스크린샷
  await page.screenshot({path: 'google.png'});
  // puppeteer 종료
  await browser.close();
})();
