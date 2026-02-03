from DrissionPage import ChromiumPage, ChromiumOptions
import time
import random
import os
from datetime import datetime

TARGETS = [
    {"name": "🐍 PYTHON",       "url": "https://www.upwork.com/nx/search/jobs/?q=python&sort=recency&page=1&per_page=50"}
]

PROXY_HOST = ""
PROXY_PORT = ""
PROXY_USER = ""
PROXY_PASS = ""

def create_proxy_auth_folder(host, port, user, password):
    folder_path = os.path.abspath("proxy_auth_plugin")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": ["proxy", "tabs", "unlimitedStorage", "storage", "<all_urls>", "webRequest", "webRequestBlocking"],
        "background": {"scripts": ["background.js"]},
        "minimum_chrome_version":"22.0.0"
    }
    """
    background_js = f"""
    var config = {{
            mode: "fixed_servers",
            rules: {{
              singleProxy: {{
                scheme: "http",
                host: "{host}",
                port: parseInt({port})
              }},
              bypassList: ["localhost"]
            }}
          }};
    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
    function callbackFn(details) {{
        return {{
            authCredentials: {{
                username: "{user}",
                password: "{password}"
            }}
        }};
    }}
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {{urls: ["<all_urls>"]}},
                ['blocking']
    );
    """
    with open(os.path.join(folder_path, "manifest.json"), "w") as f:
        f.write(manifest_json)
    with open(os.path.join(folder_path, "background.js"), "w") as f:
        f.write(background_js)
    return folder_path

def start_sniper():
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] 🚀 LAUNCHING MASSIVE SCAN (NO LIMIT)...")
    
    proxy_path = create_proxy_auth_folder(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
    co = ChromiumOptions()
    co.add_extension(proxy_path)
    profile_path = os.path.abspath("Upwork_Profile")
    co.set_user_data_path(profile_path)
    co.auto_port()

    page = ChromiumPage(co)
    
    try:
        print("   🌐 Verifying Proxy IP...")
        page.get("https://api.ipify.org/")
        current_ip = page.ele("tag:body").text
        print(f"   🛡️ CONNECTED IP: {current_ip}")
        time.sleep(1)

        for target in TARGETS:
            print(f"\n   🔎 Checking {target['name']}...")
            page.get(target['url'])
            
            time.sleep(3) 
            if "Just a moment" in page.title:
                print("   ⚠️ Cloudflare check popped up. Waiting 5s...")
                time.sleep(5)

            job_cards = page.eles('tag:article')
            if not job_cards: job_cards = page.eles('.up-card-section')

            print(f"     ✅ Found {len(job_cards)} jobs.")
            
            for i, card in enumerate(job_cards):
                try:
                    title_el = card.ele('tag:a', timeout=0.5)
                    if title_el:
                        print(f"     [{i+1}] 💰 {title_el.text}")
                except:
                    pass
            
            pause = random.randint(3, 6)
            time.sleep(pause)

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        print("🛑 Batch complete. Closing browser.")
        page.quit()

while True:
    start_sniper()
    wait = random.randint(300, 500)
    print(f"\n💤 All categories scanned. Sleeping {wait}s...\n")
    time.sleep(wait)
