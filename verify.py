import os

from bs4 import BeautifulSoup

download_dir = "D:/downloads"
expected = set()
for i in range(1, 19):
	file_path = f"dataset/{i}.html"
	if os.path.exists(file_path):
		with open(file_path, "r", encoding="utf-8") as f:
			soup = BeautifulSoup(f.read(), "html.parser")
		for a in soup.find_all("a", href=lambda h: h and "trade.aliexpress.com" in h):
			order_id = a.text.strip() or a["href"].split("orderId=")[1].split("&")[0]
			expected.add(f"{order_id}_payment.pdf")
missing = expected - set(os.listdir(download_dir))
if missing:
	print("Missing invoice files:")
	for file in missing:
		order_id = file.replace("_payment.pdf", "")
		print(
			f"- {file}: https://trade.aliexpress.com/order_detail.htm?orderId={order_id}"
		)
else:
	print("All expected invoice files are present.")
