# Alinvoice

![Stars](https://img.shields.io/github/stars/Inc44/Alinvoice?style=social)
![Forks](https://img.shields.io/github/forks/Inc44/Alinvoice?style=social)
![Watchers](https://img.shields.io/github/watchers/Inc44/Alinvoice?style=social)
![Repo Size](https://img.shields.io/github/repo-size/Inc44/Alinvoice)
![Language Count](https://img.shields.io/github/languages/count/Inc44/Alinvoice)
![Top Language](https://img.shields.io/github/languages/top/Inc44/Alinvoice)
[![Issues](https://img.shields.io/github/issues/Inc44/Alinvoice)](https://github.com/Inc44/Alinvoice/issues?q=is%3Aopen+is%3Aissue)
![Last Commit](https://img.shields.io/github/last-commit/Inc44/Alinvoice?color=red)
[![Release](https://img.shields.io/github/release/Inc44/Alinvoice.svg)](https://github.com/Inc44/Alinvoice/releases)
[![Sponsor](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/Inc44)
[![Build](https://github.com/Inc44/Alinvoice/actions/workflows/build.yml/badge.svg)](https://github.com/Inc44/Alinvoice/actions/workflows/build.yml)

## Original Logic for AliExpress February 2025

1. Loads dataset HTML files numbered from 1 to n.
2. Finds all `<a>` tags with `href` containing `https://trade.aliexpress.com/order_detail.htm`.
3. Extracts the `<a>` tag content ID.
4. Opens a tab with `https://trade.aliexpress.com/order_detail.htm?orderId=` followed by the extracted `<a>` tag content ID.
5. Detects the image `download invoice button.png` on the screen. If not found, starts a function that records the start time and retries until the timeout is reached.
6. Clicks the detected location.
7. Closes the tab.
8. Continues to the next content ID.

## 🚀 Installation

```bash
conda create -n alinvoice python=3.9 # up to 3.13
conda activate alinvoice
git clone https://github.com/Inc44/Alinvoice.git
cd Alinvoice
pip install -r requirements.txt
```

_Run the program using_ `python -m download` _(or_ `python -OO download.py`_)._

## 🤝 Contribution

Contributions, suggestions, and new ideas are heartily welcomed. If you're considering significant modifications, please initiate an issue for discussion before submitting a pull request.

## 📜 License

[![MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💖 Support

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xamituchido)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/inc44)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/Inc44)