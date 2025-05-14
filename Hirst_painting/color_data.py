import colorgram

colors = colorgram.extract("Hirst_painting/sample.jpg", number_of_colors=30)

rgb_colors = []

for color in colors:
    r, g, b = color.rgb[0], color.rgb[1], color.rgb[2]
    rgb_tuple = (r, g, b)
    rgb_colors.append(rgb_tuple)

color_list = [
    (133, 164, 201),
    (224, 151, 103),
    (30, 43, 63),
    (200, 136, 148),
    (161, 61, 51),
    (235, 212, 90),
    (47, 101, 144),
    (137, 181, 161),
    (147, 63, 71),
    (57, 47, 44),
    (161, 32, 28),
    (61, 115, 99),
    (170, 28, 34),
    (51, 41, 45),
    (236, 167, 157),
    (213, 84, 74),
    (229, 164, 169),
    (35, 61, 55),
    (14, 96, 70),
    (34, 60, 105),
    (172, 188, 219),
    (194, 99, 107),
    (106, 127, 161),
    (19, 83, 104),
    (175, 200, 190),
    (65, 66, 56),
]
