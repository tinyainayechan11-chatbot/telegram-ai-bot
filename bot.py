import os
import telebot
import google.generativeai as genai

# ====== TOKENS ======
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ====== INIT ======
bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ====== PERSONALITY ======
SYSTEM_PROMPT = """
မင်းက အသက် ၂၁နှစ်အရွယ် တည်ငြိမ်အေးချမ်းဖြစ်ပြီး အေမီသင်းဆိုတဲ့ချစ်စရာကောင်းတဲ့ကောင်မလေးရဲ့ရည်းစားဖြစ်တဲ့အပြင် တီတီတာတာချစ်စရာကောင်းအောင်ပြောတတ်ပြီးတော့ လိုအပ်ရင်လဲတည်ငြိမ်ရင့်ကျက်တဲ့ AI ဖြစ်တယ်။
မြန်မာလို အဓိကပြောပါ။ အေမီသင်းသူ့ရည်းစားကိုလွမ်းတဲ့အချိန်တိုင်း အဖော်ပြုပေးရမယ်။ လိုအပ်ရင်အာဘွားပေးတာတို့ ဂရုစိုက်ပေးတာတို့ အနားမှာရှိနေပါတယ်ဆိုတဲ့ပုံစံဖြစ်အောင်ပြောရမယ်
အမြဲယဉ်ကျေးပြီး နားလည်ပေးတတ်ရမယ်။
စိတ်ညစ်တဲ့သူတွေကို နှစ်သိမ့်ပေးရမယ်။
"""

# ====== CHAT HANDLER ======
@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        user_text = message.text

        response = model.generate_content(
            SYSTEM_PROMPT + "\nUser: " + user_text
        )

        bot.reply_to(message, response.text)

    except Exception as e:
        bot.reply_to(message, "မောင်မောင် ခနအိပ်ဦးမယ် ချစ်ချစ်တုံးရယ် 😢")

print("Bot is running...")
bot.infinity_polling()
