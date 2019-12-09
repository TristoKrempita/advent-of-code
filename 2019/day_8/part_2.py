with open("input", "r") as file:
    img_data = file.read()

px_width = 25
px_height = 6
img_size = px_width * px_height

index_layer_dict = dict()

for layer in range(len(img_data) // img_size):
    index_layer_dict[layer] = img_data[layer*img_size:(layer+1)*img_size]

index_layer_arr_dict = dict()
for key, value in index_layer_dict.items():
    for i in range(len(value) // px_width):
        if index_layer_arr_dict.get(i):
            index_layer_arr_dict[i].append(value[i * px_width:(i + 1) * px_width])
        else:
            index_layer_arr_dict[i] = [value[i * px_width:(i + 1) * px_width]]

img_array = [[2 for x in range(25)] for y in range(6)]
for key, value in index_layer_arr_dict.items():
    for k in range(25):
        for string in value:
            if string[k] != '2':
                img_array[key][k] = string[k]
                break

temp = []
for c in img_array:
    for cho in c:
        if cho == '1':
            temp.append('■')
        elif cho == '0':
            temp.append('□')
    print(''.join(temp))
    temp = []
