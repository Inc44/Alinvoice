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

Automates batch retrieval of AliExpress order receipts by combining static HTML parsing with GUI-driven browser automation.

## ⚙️ Features

- Scans local HTML datasets of [downloaded feedback pages](https://feedback.aliexpress.com/management/feedbackBuyerList.htm) to extract every order ID without additional AliExpress requests.
- Opens each order in a new browser tab and triggers the built-in "Download receipt/invoice" workflow.
- Handles both February 2025 (one PDF invoice button) and July 2025 (two receipt + PNG download buttons) layouts.
- Image-based element detection via PyAutoGUI (OpenCV backend) with configurable confidence, retries, and delays.
- Gracefully skips missing HTML pages and continues the batch.
- Verifies completeness after the run; lists any missing receipts together with direct order links.
- Requires no AliExpress API keys or logged-in scraping: all actions occur in the normal browser session.

## ⚠️ Disclaimers

- **Fragile UI Automation**: Button screenshots are tied to current AliExpress styling, scaling, and your display DPI. Any UI change may break detection.

## 🚀 Installation

```bash
conda create -n alinvoice python=3.9 -y # up to 3.11
conda activate alinvoice
git clone https://github.com/Inc44/Alinvoice.git
cd Alinvoice
pip install -r requirements.txt
```

## 🧾 Configuration

Edit the constants at the top of the script if defaults do not match your environment:

- `first_page` / `last_page`: range of local HTML files (`1.html` … `n.html`).
- `detection_confidence`: OpenCV template-match confidence for PyAutoGUI (0 – 1).
- `initial_wait_seconds`, `retry_wait_seconds`, `max_retries`, `post_click_wait_seconds`: timing parameters.
- `download_invoice_button_image`, `receipt_button_image`, `download_button_image`: reference screenshots (PNG).

## 📖 Usage Examples

### Bulk Invoice Download

```bash
python -m download # or download.old
```

### Verify Completeness

```bash
python -m verify # or verify.old
```

## 🎯 Motivation

AliExpress limits invoice retrieval to manual per-order clicks. While manageable for occasional purchases, it becomes untenable for hundreds of orders. Alinvoice removes this bottleneck by automating the process with reproducible local datasets and deterministic image matching.

## 🐛 Bugs

Not yet found.

## ⛔ Known Limitations

- Does not retry failed downloads; verification script reports missing receipts for manual follow-up.

## 🚧 TODO

- [ ] Replace GUI automation with direct authenticated HTTP download to remove display dependencies.
- [ ] Add optional `argparse` interface for non-interactive batch execution in CI environments.
- [ ] Support incremental runs by skipping already downloaded receipts.
- [ ] Implement hash-based image set selection to auto-switch between UI versions.

## 🙏 Thanks

Creators of:

- [Python](https://www.python.org)
- [PyAutoGUI](https://pyautogui.readthedocs.io)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [OpenCV](https://opencv.org)
- [tqdm](https://tqdm.github.io)

## 🤝 Contribution

Contributions, suggestions, and new ideas are heartily welcomed. If you're considering significant modifications, please initiate an issue for discussion before submitting a pull request.

## 📜 License

[![MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💖 Support

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xamituchido)
[![Ko-Fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/inc44)
[![Patreon](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/Inc44)