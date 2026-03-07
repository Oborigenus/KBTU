import re
import json

with open("Practice5/raw.txt", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r"\d[\d ]*,\d{2}", text)

price_values = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

products = re.findall(r"\d+\.\n([^\n]+)", text)

total_match = re.search(r"ИТОГО:\s*\n?(\d[\d ]*,\d{2})", text)
total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else sum(price_values)

date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)

time = re.search(r"\d{2}:\d{2}:\d{2}", text)

payment = re.search(r"(Банковская карта|Cash|Card|VISA|MasterCard)", text)

result = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date.group(),
    "time": time.group(),
    "payment_method": payment.group()
}

print(json.dumps(result, indent=4, ensure_ascii=False))