import os
import re

from bs4 import BeautifulSoup

dataset_dir_path = input("Enter the path to the dataset directory: ").strip()
first_page = 1
last_page = 23
download_dir_path = input("Enter the path to the download directory: ").strip()
expected_orders = set()
for page_number in range(first_page, last_page + 1):
	page_path = f"{dataset_dir_path}/{page_number}.html"
	if not os.path.exists(page_path):
		continue
	with open(page_path, "r", encoding="utf-8") as page_file:
		soup = BeautifulSoup(page_file.read(), "html.parser")
	for anchor in soup.find_all(
		"a",
		href=lambda href: href and "trade.aliexpress.com" in href,
	):
		order_id = (
			anchor.text.strip() or anchor["href"].split("orderId=")[1].split("&")[0]
		)
		expected_orders.add(order_id)
downloaded_orders = set(os.listdir(download_dir_path))
missing_orders = set()
for order_id in expected_orders:
	if not any(
		re.fullmatch(rf"OrderSummary\d{{8}}{order_id}\.png", name)
		for name in downloaded_orders
	):
		missing_orders.add(order_id)
if missing_orders:
	print("Missing invoice files:")
	for order_id in sorted(missing_orders):
		print(
			f"- OrderSummary????????{order_id}.png: https://trade.aliexpress.com/order_detail.htm?orderId={order_id}"
		)
else:
	print("All expected invoice files are present.")
