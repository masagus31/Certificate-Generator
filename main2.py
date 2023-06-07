import os
from configparser import ConfigParser
import logging
from utils import generate_certificate, get_name_list, get_date_list


def main():
    config = ConfigParser()
    config.read("config.cfg")

    template = config.get("config", "template")
    name_list = config.get("config", "name_list")
    date_list = config.get("config", "date_list")
    output_folder = config.get("config", "output_folder")
    font = config.get("font", "font")
    font_size = config.get("font", "font_size")
    font_color = config.get("font", "font_color")
    offset = config.get("font", "offset")
    date_font = config.get("date_font", "date_font")
    date_font_size = config.get("date_font", "date_font_size")
    date_offset_x = config.get("date_font", "date_offset_x")
    date_offset_y = config.get("date_font", "date_offset_y")
    log_output = "log.txt"

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler(log_output, mode="w"),
                            logging.StreamHandler()
                        ])

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    names, names_count = get_name_list(name_list)
    dates, dates_count = get_date_list(date_list)

    if dates_count < names_count:
        logging.warning("Number of dates is less than the number of names. Some certificates may not have a date.")

    for index, name in enumerate(names):
        name = name.title()
        date = dates[index % dates_count]  # Get the date corresponding to the current index

        logging.info(f"({index + 1}/{names_count}) Generate {name}'s certificate")

        try:
            generate_certificate(
                font=font,
                font_size=int(font_size),
                offset=int(offset),
                color=font_color,
                image=template,
                name=name,
                date=date,
                output_folder=output_folder,
                date_font=date_font,
                date_font_size=int(date_font_size),
                date_offset_x=int(date_offset_x),
                date_offset_y=int(date_offset_y)
            )
        except Exception as e:
            logging.error(f"Error while generating certificate: {e}")

    logging.info("Done")


if __name__ == "__main__":
    main()
