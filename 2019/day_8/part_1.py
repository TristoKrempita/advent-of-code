with open("input", "r") as file:
    img_data = file.read()

px_width = 25
px_height = 6
img_size = px_width * px_height

zero_count = float('inf')

count_1 = 0
count_2 = 0

for layer in range(len(img_data) // img_size):
    chunk = img_data[layer * img_size: (layer + 1) * img_size]
    if chunk.count('0') < zero_count:
        count_1 = chunk.count('1')
        count_2 = chunk.count('2')
        zero_count = chunk.count('0')

print(count_1*count_2)
