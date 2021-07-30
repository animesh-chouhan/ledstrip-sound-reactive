import colorsys


def hex_to_hsv(hex):
    h = hex.lstrip("#")
    rgb = list(int(h[i:i+2], 16) for i in (0, 2, 4))
    rgb_normalized = list(map(lambda x: x / 255, rgb))
    hsv_normalized = colorsys.rgb_to_hsv(*rgb_normalized)
    hsv = [int(i) for i in [hsv_normalized[0] * 360,
                            hsv_normalized[1] * 100,
                            hsv_normalized[2] * 100]]
    return hsv


# Correct is [123, 28, 98]
print(hex_to_hsv("#B4FBB8"))
