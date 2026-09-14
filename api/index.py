from flask import Flask
app = Flask(__name__)

LINKS = {
    "loan": "https://alwaysmulticulturallanding.com/eqyjrvay?key=36d9019518a0abbed2b1edf977ace56f",
    "bank": "https://alwaysmulticulturallanding.com/r6qp4iz8wz?key=82ea585a5077746793acf0ffbbf5dd82",
    "demat": "https://alwaysmulticulturallanding.com/sc0srbj8fy?key=16540b5adef3bcbb6e84bfa9fc67bbc7",
    "crypto_bonus": "https://alwaysmulticulturallanding.com/e0ftsbxv?key=7f5af55a34019f7c55853e166d6c9089",
    "insurance": "https://alwaysmulticulturallanding.com/r6qp4iz8wz?key=82ea585a5077746793acf0ffbbf5dd82",
    "crypto": "https://accounts.binance.com/register?ref=YOURCODE",
    "airdrop": "https://t.me/YourUsername"
}

SERVICES = {
    "web-design": {"t": "1. Web Design", "icon": "🌐", "mention": "Responsive modern websites 3 din ma ready, mobile friendly, fast loading."},
    "web-development": {"t": "2. Web Development", "icon": "💻", "mention": "Custom development & CMS, WordPress + Flask full setup."},
    "logo-design": {"t": "3. Logo Design", "icon": "🎨", "mention": "Brand logos Rs 499 ma, 3 concept free."},
    "seo": {"t": "4. SEO Optimization", "icon": "📈", "mention": "Google ma 1st page guarantee, Siliguri local SEO."},
    "graphic-design": {"t": "5. Graphic Design", "icon": "🖌️", "mention": "Posters, banners, creatives design."},
    "social-media": {"t": "6. Social Media Management", "icon": "💬", "mention": "Facebook Insta handle manage, growth & engagement."},
    "ecommerce": {"t": "7. E-Commerce Setup", "icon": "🛒", "mention": "Online store + payment gateway + delivery."},
    "ui-ux": {"t": "8. UI/UX Design", "icon": "✒️", "mention": "User-friendly interfaces, Figma to code."},
    "app-development": {"t": "9. App Development", "icon": "📱", "mention": "Android & iOS apps Rs 9999 ma."},
    "content-writing": {"t": "10. Content Writing", "icon": "📝", "mention": "SEO blogs & article writing."},
    "web-designer-service": {"t": "11. Web Designer Service", "icon": "🌍", "mention": "Custom responsive websites for businesses."},
    "google-business": {"t": "12. Google Business Setup", "icon": "📍", "mention": "GMB verify, Map pin, 5-star review system."},
    "digital-bank": {"t": "13. Digital Bank Opening", "icon": "🏦", "mention": "Zero balance account 10 min ma - Kotak, SBI, HDFC. Video KYC.", "link": "bank"},
    "demat-account": {"t": "14. Demat Account Opening", "icon": "📊", "mention": "Zerodha, Upstox free + Rs 500-1000 bonus.", "link": "demat"},
    "crypto-exchange": {"t": "15. Crypto Exchange", "icon": "🔄", "mention": "Binance, KuCoin full KYC + P2P sikaune.", "link": "crypto"},
    "crypto-wallet": {"t": "16. Crypto Wallet", "icon": "👛", "mention": "Trust Wallet secure setup, Grand Airdrop 2030 token.", "link": "crypto"},
    "digital-loan": {"t": "17. Digital Loan", "icon": "💸", "mention": "Instant loan 5 min ma approval, CIBIL free check.", "link": "loan"},
    "insurance-service": {"t": "18. Insurance Service", "icon": "🛡️", "mention": "Life, Health, Bike insurance compare garera sasto.", "link": "bank"},
    "mining-airdrop": {"t": "19. Mining & Airdrop - Grand Airdrop 2030", "icon": "⛏️", "mention": "Daily free mining + Airdrop 2030 reward, daily 2$-5$.", "link": "airdrop"},
    "online-banking": {"t": "20. Online Banking Sewa", "icon": "🏧", "mention": "UPI fail, KYC, limit increase sabai online."},
}

def ads_box():
    return f"""
    <div class="ads"><b>⚡ SPONSORED • Partner Ads - 4 Ads Mixed</b><br><br>
    <a class="btn" style="background:#ff5722" href="{LINKS['loan']}" target="_blank">💰 Loan Offer Ads 1</a>
    <a class="btn" style="background:#1976d2" href="{LINKS['bank']}" target="_blank">🏦 Bank/Insurance Ads 2</a>
    <a class="btn" style="background:#7c4dff" href="{LINKS['demat']}" target="_blank">📈 Open Demat Ads 3</a>
    <a class="btn" style="background:#2e7d32" href="{LINKS['crypto_bonus']}" target="_blank">🎁 Crypto Bonus Ads 4</a>
    </div>"""

@app.route("/")
def home():
    cards = ""
    for slug, s in SERVICES.items():
        cards += f'<div class="card"><div class="ico">{s["icon"]}</div><div><h2>{s["t"]}</h2><div class="story">{s["mention"]}</div><a class="btn" style="background:#000" href="/service/{slug}">Learn More →</a></div></div>'
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>DJ & dajubhaiharu - 20 Services - Siliguri</title>
    <style>body{{font-family:Arial;margin:0;background:#f0f2f8}}header{{background:#000;color:#fff;padding:22px;text-align:center;position:sticky;top:0;z-index:10}} .btn{{padding:8px 14px;color:#fff;border-radius:20px;text-decoration:none;display:inline-block;margin:3px;font-size:11px;font-weight:bold}} .card{{background:#fff;margin:8px;padding:12px;border-radius:12px;box-shadow:0 2px 8px #0001;display:flex;gap:10px}} .ico{{font-size:26px;min-width:42px;height:42px;background:#eef2ff;border-radius:50%;display:flex;align-items:center;justify-content:center}} .grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px;max-width:940px;margin:10px auto;padding:8px}}@media(max-width:600px){{.grid{{grid-template-columns:1fr}}}} .ads{{background:#fff8c4;border:2px dashed #ffb300;padding:14px;border-radius:12px;margin:12px auto;max-width:940px;text-align:center}} h2{{font-size:12px;margin:2px 0}} .story{{font-size:11px;color:#555}} .float{{position:fixed;bottom:15px;right:15px;background:#25D366;color:#fff;padding:12px 16px;border-radius:50px;text-decoration:none;font-weight:bold;z-index:99}} footer{{background:#000;color:#aaa;text-align:center;padding:14px;font-size:11px}}</style>
    </head><body><a class="float" href="https://wa.me/917318912415">💬 Chat</a>
    <header><h1 style="margin:0;font-size:28px">DJ & dajubhaiharu</h1><p style="font-size:12px;color:#ccc">Web Designer & Services • Siliguri • 20 Services | Grand Airdrop 2030</p></header>
    {ads_box()}
    <h2 style="max-width:940px;margin:10px auto;padding-left:10px;border-left:5px solid #25D366">Our 20 Services - Click Learn More for Details</h2>
    <div class="grid">{cards}</div>
    {ads_box()}
    <footer>© 2026 DJ & dajubhaiharu | 4 Ads Mixed - Loan, Bank, Demat, Crypto | Siliguri WB</footer></body></html>"""

@app.route("/service/<slug>")
def detail(slug):
    s = SERVICES.get(slug)
    if not s: return "<h2>Not Found</h2><a href='/'>Home</a>"
    link_btn = ""
    if s.get("link") == "loan": link_btn = f'<a class="big" style="background:#ff5722" href="{LINKS["loan"]}" target="_blank">💰 Loan Offer - Click Here (Ads 1)</a>'
    elif s.get("link") == "bank": link_btn = f'<a class="big" style="background:#1976d2" href="{LINKS["bank"]}" target="_blank">🏦 Bank/Insurance Offer - Click Here (Ads 2)</a>'
    elif s.get("link") == "demat": link_btn = f'<a class="big" style="background:#7c4dff" href="{LINKS["demat"]}" target="_blank">📈 Open Demat Now - Bonus (Ads 3)</a>'
    elif s.get("link") == "airdrop": link_btn = f'<a class="big" style="background:#ff9800;color:#000" href="{LINKS["airdrop"]}" target="_blank">🔥 Join Airdrop + </a><a class="big" style="background:#2e7d32" href="{LINKS["crypto_bonus"]}" target="_blank">Crypto Bonus (Ads 4)</a>'
    else: link_btn = f'<a class="big" style="background:#000" href="https://wa.me/917318912415?text={s["t"]}">WhatsApp Inquiry</a>'

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{s['t']}</title>
    <style>body{{font-family:Arial;padding:15px;max-width:600px;margin:auto;line-height:1.7}} .big{{padding:12px 20px;color:#fff;border-radius:25px;text-decoration:none;display:inline-block;margin:6px 3px;font-weight:bold}} .box{{background:#f5f7ff;padding:14px;border-radius:10px;border-left:4px solid #25D366;margin:12px 0}} .ads{{background:#fff8c4;border:1px dashed #ffb300;padding:12px;border-radius:10px;text-align:center;margin:12px 0}}</style>
    </head><body>
    <a href="/">← Back to Home</a>
    <h1>{s['icon']} {s['t']}</h1>
    <div class="box"><b>Mention:</b><br>{s['mention']}</div>
    <h3>👇 Link halne thau:</h3>
    {link_btn}
    <br><br>
    <a class="big" style="background:#25D366" href="https://wa.me/917318912415?text={s['t']} chahiyo">💬 WhatsApp Chat</a>
    <div class="ads"><b>⚡ SPONSORED • 4 Ads Mixed</b><br>
    <a class="big" style="background:#ff5722" href="{LINKS['loan']}" target="_blank">Loan Ads 1</a>
    <a class="big" style="background:#1976d2" href="{LINKS['bank']}" target="_blank">Bank Ads 2</a><br>
    <a class="big" style="background:#7c4dff" href="{LINKS['demat']}" target="_blank">Demat Ads 3</a>
    <a class="big" style="background:#2e7d32" href="{LINKS['crypto_bonus']}" target="_blank">Crypto Ads 4</a>
    </div>
    <p style="font-size:11px;color:#888">DJ & dajubhaiharu • Siliguri • Trusted 1.2k+ clients</p>
    </body></html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
