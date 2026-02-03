# upwork Automated Job Monitor

This Python script utilizes `DrissionPage` to automate the monitoring of job listings on upwork. It is designed to handle dynamic content loading and includes a custom mechanism for proxy authentication.

## ⚙️ Features

* **Browser Automation:** Uses Chromium via DrissionPage for reliable page rendering and interaction.
* **Custom Proxy Authentication:** Dynamically creates a Chrome extension to handle proxy credentials (`user:pass`), bypassing standard pop-up limitations.
* **Anti-Detection:** Mimics human behavior with random sleep intervals and realistic browser headers.
* **Cloudflare Handling:** Basic detection and wait logic for "Just a moment" checks.
* **Session Persistence:** Saves user profile data locally to maintain login sessions.

## 🛠 Dependencies

* Python 3.x
* [DrissionPage](https://github.com/g1879/DrissionPage)

## 🚀 Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/automated-job-monitor.git](https://github.com/yourusername/automated-job-monitor.git)
    cd automated-job-monitor
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    Open `main.py` and update the proxy configuration variables at the top of the file:
    ```python
    PROXY_HOST = "your.proxy.ip"
    PROXY_PORT = "your.proxy.port"
    PROXY_USER = "username"
    PROXY_PASS = "password"
    ```

4.  **Run the script:**
    ```bash
    python main.py
    ```

## 📝 Notes

* The script runs in an infinite loop (`while True`) to continuously check for new listings. Use `Ctrl + C` to stop execution.
* Browser profile data is stored in the `Upwork_Profile` directory (excluded from version control).

## ⚠️ Disclaimer

This tool is for educational purposes only. Please ensure you comply with the Terms of Service of any website you automate interact with.
