import re 
text = "Мой номер 123-456-789"

numbers = re.findall(r'\d+', text )
print(numbers)

result = re.sub(r'\d', 'x', text)

print(result)

match = re.search(r'\d+', text)
if match:
    print("Нашёл:", match.group())