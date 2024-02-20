'''import csv
from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter

# Read CSV file
with open('new.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    rows = list(csv_reader)

# Define image parameters
image_width = 685
image_height = 449
cell_width = image_width // 3
cell_height = image_height // 2

# Font settings
font_size = 16
font = ImageFont.truetype("arial.ttf", font_size)

border_size = 3
border_color = "red"

logo_width = 100
logo_height = 50
icon_width = 50
icon_height = 50

# Load logo image
logo_image = Image.open("logo.png").resize((logo_width, logo_height))

# Load icon images
icon1_image = Image.open("icon1.png").resize((icon_width, icon_height))
icon2_image = Image.open("icon2.png").resize((icon_width, icon_height))
icon3_image = Image.open("icon3.png").resize((icon_width, icon_height))

# Iterate through each row
for i, row in enumerate(rows):
    # Create a new image
    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    draw.rectangle([(0, 0), (image_width - 1, image_height - 1)], outline=border_color, width=border_size)

    # Iterate through each cell in the row
    for j, cell in enumerate(row):
        # Position content according to your layout
        if j == 2:  # First cell: top right corner
            align = "right"
            logo_x = border_size
            logo_y = border_size
            icon_x = border_size
            icon_y = border_size + logo_height + border_size

            # Paste logo onto image
            img.paste(logo_image, (logo_x, logo_y))

            # Paste icons onto image
            img.paste(icon1_image, (icon_x, icon_y))
            img.paste(icon2_image, (icon_x + icon_width, icon_y))
            img.paste(icon3_image, (icon_x + 2 * icon_width, icon_y))
        elif j == 1:  # Second cell: top left corner
            x = 0
            y = 0
            align = "left"
        elif j == 0:  # Third cell: bottom center
            x = (image_width - cell_width) // 2
            y = image_height - cell_height
            align = "center"
            barcode_value = cell  # Change this to your desired value
            ean13 = barcode.get_barcode_class('ean13')
            barcode_instance = ean13(barcode_value, writer=ImageWriter())
            img.paste(barcode_instance, (x, y))
    shtrih = row[0]
    text = row[1] + row[2]



    # Save image as PNG file
    img.save(f'C:/Users/truba/Desktop/trust/image_{i+1}.png')'''
import csv
from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter

# Read CSV file
with open('old.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    rows = list(csv_reader)


# Define image parameters
image_width = 685
image_height = 449
cell_width = image_width // 3
cell_height = image_height // 2

# Font settings
font_size = 26
font = ImageFont.truetype("arial.ttf", font_size)

border_size = 3
border_color = "red"

logo_width = 336
logo_height = 112
icon_width = 112
icon_height = 110

# Load logo image

logo_image = Image.open("logo.png").resize((logo_width, logo_height)).convert('RGBA')

# Load icon images
icon1_image = Image.open("icon1.png").resize((icon_width, icon_height)).convert('RGBA')
icon2_image = Image.open("icon2.png").resize((icon_width, icon_height)).convert('RGBA')
icon3_image = Image.open("icon3.png").resize((icon_width, icon_height)).convert('RGBA')
icon4_image = Image.open("icon4.png").resize((icon_width, icon_height)).convert('RGBA')
icon5_image = Image.open("icon5.png").resize((icon_width, icon_height)).convert('RGBA')
icon6_image = Image.open("icon6.png").resize((icon_width, icon_height)).convert('RGBA')
def addwhite(image):
    background = Image.new("RGBA", image.size, (255, 255, 255))
    background.paste(image, mask=image)
    # Save the image with white background
    return background
logo_image = addwhite(logo_image)
icon1_image = addwhite(icon1_image)
icon2_image = addwhite(icon2_image)
icon3_image = addwhite(icon3_image)
icon4_image = addwhite(icon4_image)
icon5_image = addwhite(icon5_image)
icon6_image = addwhite(icon6_image)

def split_text(text, max_chars_per_line=22):
    lines = []
    current_line = ""

    for word in text.split():
        if len(current_line) + len(word) + 1 <= max_chars_per_line:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return "\n".join(lines)

background = Image.new("RGBA", logo_image.size, (255, 255, 255))
# Iterate through each row
for i, row in enumerate(rows):
    # Create a new image
    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)


    # Paste logo onto image
    logo_x = border_size
    logo_y = border_size
    img.paste(logo_image, (logo_x, logo_y))

    # Paste icons onto image
    icon_x = 0
    icon_y = logo_height + border_size + 10
    img.paste(icon1_image, (icon_x, icon_y))
    img.paste(icon2_image, (icon_x + icon_width, icon_y))
    img.paste(icon3_image, (icon_x + 2 * icon_width, icon_y))
    img.paste(icon4_image, (icon_x + 3 * icon_width, icon_y))
    img.paste(icon5_image, (icon_x + 4 * icon_width, icon_y))
    img.paste(icon6_image, (icon_x + 5 * icon_width, icon_y))

    # Iterate through each cell in the row


    # Combine text from the second and third cells
    shtrih = row[0]
    text = split_text(row[1]) + "\n" + row[2] + "₸"

    barcode_value = shtrih  # Change this to your desired value
    ean13 = barcode.get_barcode_class('ean13')
    barcode_instance = ean13(barcode_value, writer=ImageWriter())
    barcode_instance.save('barcode')  # Save the barcode image to a file

    # Load the barcode image as a PIL image
    barcode_image = Image.open('barcode.png')

    original_width, original_height = barcode_image.size
    new_image = barcode_image.resize((420,225))
    new_image.save('newpng.png')
    # Paste the barcode onto the main image
    img.paste(new_image, (132, 240))

    # Draw text
    draw.text((350, 0), text, fill='black', font=font)

    # Save image as PNG file
    img.save(f'C:/Users/truba/Desktop/trust/image_{i+1}.png')

