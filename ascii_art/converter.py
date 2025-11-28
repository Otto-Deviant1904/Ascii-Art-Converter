from PIL import Image

# Character Sets (dark → light)
ASCII_DETAILED = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ASCII_SHADOW = "@#&WM%B8$OoahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>!il;:,\"^`'.  "
ASCII_MATRIX = "MW8&%#+=-:. "
EMOJI = "⬛🟥🟧🟨🟩🟦🟪⬜"


def resize_image(img, new_width):
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio * 0.55)
    return img.resize((new_width, new_height))


def map_brightness(brightness, charset):
    idx = int((brightness / 255) * (len(charset) - 1))
    return charset[idx]


def convert_grayscale_ascii(img, charset):
    pixels = img.getdata()
    ascii_str = "".join(map_brightness(p, charset) for p in pixels)

    width = img.width
    return "\n".join(
        ascii_str[i:i + width] 
        for i in range(0, len(ascii_str), width)
    )


def convert_color_ascii(img):
    output = []
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            brightness = int(0.299*r + 0.587*g + 0.114*b)
            ch = map_brightness(brightness, ASCII_DETAILED)
            output.append(f"\033[38;2;{r};{g};{b}m{ch}\033[0m")
        output.append("\n")
    return "".join(output)


def convert_image(path, style, width=120):
    img = Image.open(path)

    # Colored mode (needs RGB)
    if style == 5:
        img = resize_image(img, width)
        return convert_color_ascii(img)

    # Grayscale modes
    img = img.convert("L")
    img = resize_image(img, width)

    if style == 1:
        charset = ASCII_DETAILED
    elif style == 2:
        charset = ASCII_SHADOW
    elif style == 3:
        charset = ASCII_MATRIX
    elif style == 4:
        charset = EMOJI
    else:
        raise ValueError("Invalid style number")

    return convert_grayscale_ascii(img, charset)
