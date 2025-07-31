import os
import time
import webbrowser

import pyautogui
from bs4 import BeautifulSoup

dataset_dir_path = "dataset/202507 Icy Fear"
first_page = 1
last_page = 23
order_url_template = "https://trade.aliexpress.com/order_detail.htm?orderId="
download_invoice_button_image = "images/download invoice button.png"
detection_confidence = 0.8
initial_wait_seconds = 4
retry_wait_seconds = 3
max_retries = 10
post_click_wait_seconds = 3
for page_number in range(first_page, last_page + 1):
	page_path = f"{dataset_dir_path}/{page_number}.html"
	if not os.path.exists(page_path):
		continue
	with open(page_path, "r", encoding="utf-8") as page_file:
		soup = BeautifulSoup(page_file.read(), "html.parser")
	for anchor in soup.find_all(
		"a",
		href=lambda href: href and "trade.aliexpress.com/order_detail.htm" in href,
	):
		order_id = (
			anchor.text.strip() or anchor["href"].split("orderId=")[1].split("&")[0]
		)
		webbrowser.open_new_tab(f"{order_url_template}{order_id}")
		time.sleep(initial_wait_seconds)
		for _ in range(max_retries):
			try:
				button_location = pyautogui.locateOnScreen(
					download_invoice_button_image, confidence=detection_confidence
				)
				if button_location:
					pyautogui.click(pyautogui.center(button_location))
					time.sleep(post_click_wait_seconds)
					break
			except pyautogui.ImageNotFoundException:
				pass
			time.sleep(retry_wait_seconds)
		pyautogui.hotkey("ctrl", "w")
