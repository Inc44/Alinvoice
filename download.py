import os
import time
import webbrowser

import pyautogui
from bs4 import BeautifulSoup

for i in range(1, 19):
	file_path = f"dataset/{i}.html"
	if os.path.exists(file_path):
		with open(file_path, "r", encoding="utf-8") as f:
			soup = BeautifulSoup(f.read(), "html.parser")
		for a in soup.find_all(
			"a", href=lambda h: h and "trade.aliexpress.com/order_detail.htm" in h
		):
			order_id = a.text.strip()
			if not order_id:
				order_id = a["href"].split("orderId=")[1].split("&")[0]
			url = f"https://trade.aliexpress.com/order_detail.htm?orderId={order_id}"
			webbrowser.open_new_tab(url)
			time.sleep(4)
			for _ in range(10):
				try:
					location = pyautogui.locateOnScreen(
						"images/download invoice button.png", confidence=0.8
					)
					if location:
						pyautogui.click(pyautogui.center(location))
						time.sleep(3)
						break
				except:
					pass
				time.sleep(3)
			pyautogui.hotkey("ctrl", "w")
