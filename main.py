import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- 1. إعداداتك الخاصة (قم بتعديل هذه البيانات) ---
MY_USER = "fady_victor_7"
MY_PASS = "1228077843"
LOGIN_URL = "https://anba-mousa-class.web.app/"
CONTEST_URL = "https://anba-mousa-class.web.app/quiz/235179012"
GEMINI_API_KEY = "AlzaSyAJFAsqWEKnd5pm2-8X3u7XFOI6a_8kv2c"

# --- 2. وظيفة الذكاء الاصطناعي (Gemini) ---
def ask_gemini(question_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{
            "parts": [{"text": f"أجب باختصار شديد جداً (كلمة واحدة لو أمكن) على هذا السؤال: {question_text}"}]
        }]
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        print(f"❌ خطأ في الاتصال بـ Gemini: {e}")
        return None

# --- 3. إعداد المتصفح ليعمل على السيرفر (Headless) ---
chrome_options = Options()
chrome_options.add_argument("--headless")  # تشغيل بدون واجهة رسومية (ضروري للسيرفر)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,108
