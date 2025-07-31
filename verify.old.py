import os

from bs4 import BeautifulSoup

dataset_dir_path = os.path.normpath(
	input("Enter the path to the dataset directory: ").strip().strip('"')
)
first_page = 1
last_page = 23
download_dir_path = os.path.normpath(
	input("Enter the path to the download directory: ").strip().strip('"')
)
expected_payments = set()
for page_number in range(first_page, last_page + 1):
	page_path = os.path.join(dataset_dir_path, f"{page_number}.html")
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
		expected_payments.add(f"{order_id}_payment.pdf")
missing_payments = expected_payments - set(os.listdir(download_dir_path))
if missing_payments:
	print("Missing invoice files:")
	for payment_path in sorted(missing_payments):
		order_id = payment_path.replace("_payment.pdf", "")
		print(
			f"- {payment_path}: https://trade.aliexpress.com/order_detail.htm?orderId={order_id}"
		)
else:
	print("All expected invoice files are present.")
