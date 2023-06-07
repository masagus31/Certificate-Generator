from PIL import Image, ImageDraw, ImageFont
import os
import logging


def generate_certificate(font, font_size, offset, color, image, name, date, program, output_folder, date_font=None, date_font_size=None, date_font_color=None, date_offset=None, program_font=None, program_font_size=None, program_font_color=None, program_offset=None):
    certificate_image = Image.open(image)
    draw = ImageDraw.Draw(certificate_image)
    name_font = ImageFont.truetype(font, font_size)
    date_font = ImageFont.truetype(date_font, date_font_size) if date_font else name_font
    program_font = ImageFont.truetype(program_font, program_font_size) if program_font else name_font
    name_width, name_height = draw.textsize(name, name_font)
    date_width, date_height = draw.textsize(date, date_font)
    program_width, program_height = draw.textsize(program, program_font)
    image_width, image_height = certificate_image.size

    # Draw name on the certificate
    draw.text(
        ((image_width - name_width) / 2, ((image_height - name_height) / 2) - offset),
        name,
        fill=color,
        font=name_font,
    )

    # Draw date on the certificate
    if date_offset is not None:  # Perubahan di sini
        date_y = image_height - date_offset - date_height


        draw.text(
            ((image_width - date_width) / 2, date_y),
            date,
            fill=date_font_color,
            font=date_font,
        )

    # Draw program on the certificate
    if program_offset is not None:
        program_y = image_height - program_offset - program_height

        draw.text(
            ((image_width - program_width) / 2, program_y),
            program,
            fill=program_font_color,
            font=program_font,
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


def get_program_list(filename):
    with open(filename, mode="r") as file:
        programs = file.read().splitlines()
        programs_count = len(programs)
        return programs, programs_count
