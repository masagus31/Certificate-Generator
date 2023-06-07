from PIL import Image, ImageDraw, ImageFont
import os
import logging


def generate_certificate(font, font_size, offset, color, image, name, date, output_folder, date_font=None, date_font_size=None, date_offset_x=None, date_offset_y=None):
    certificate_image = Image.open(image)
    draw = ImageDraw.Draw(certificate_image)
    name_font = ImageFont.truetype(font, font_size)
    date_font = ImageFont.truetype(date_font, date_font_size) if date_font else name_font
    name_width, name_height = draw.textsize(name, name_font)
    date_width, date_height = draw.textsize(date, date_font)
    image_width, image_height = certificate_image.size

    # Draw name on the certificate
    draw.text(
        ((image_width - name_width) / 2, ((image_height - name_height) / 2) - offset),
        name,
        fill=color,
        font=name_font,
    )

    # Draw date on the certificate
    if date_offset_x is not None and date_offset_y is not None:
        date_x = date_offset_x
        date_y = date_offset_y

        draw.text(
            (date_x, date_y),
            date,
            fill=color,
            font=date_font,
        )

    output_path = os.path.join(output_folder, f"{name}_certificate.png")

    if os.path.exists(output_path):
        logging.info(f"{name}'s certificate already exists. Replacing...")

    certificate_image.save(output_path, "PNG")


def get_name_list(filename):
    with open(filename, mode="r") as file:
        names = file.read().splitlines()
        names_count = len(names)
        return names, names_count


def get_date_list(filename):
    with open(filename, mode="r") as file:
        dates = file.read().splitlines()
        dates_count = len(dates)
        return dates, dates_count
