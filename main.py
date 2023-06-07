import os
from configparser import ConfigParser
import logging
from utils import generate_certificate, get_name_list, get_date_list, get_program_list


def main():
    config = ConfigParser()
    config.read("config.cfg")

    template = config.get("config", "template")
    name_list = config.get("config", "name_list")
    date_list = config.get("config", "date_list")
    program_list = config.get("config", "program_list")
    output_folder = config.get("config", "output_folder")
    font = config.get("font", "font")
    font_size = int(config.get("font", "font_size"))
    font_color = config.get("font", "font_color")
    offset = int(config.get("font", "offset"))
    date_font = config.get("date_font", "date_font")
    date_font_size = int(config.get("date_font", "date_font_size"))
    date_font_color = config.get("date_font", "date_font_color")
    date_offset = int(config.get("date_font", "date_offset")) 
    program_font = config.get("program_font", "program_font")
    program_font_size = int(config.get("program_font", "program_font_size"))
    program_font_color = config.get("program_font", "program_font_color")
    program_offset = int(config.get("program_font", "program_offset"))
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
    programs, programs_count = get_program_list(program_list)

    if dates_count < names_count:
        logging.warning("Number of dates is less than the number of names. Some certificates may not have a date.")

    if programs_count < names_count:
        logging.warning("Number of programs is less than the number of names. Some certificates may not have a program.")

    for index, name in enumerate(names):
        name = name.title()
        date = dates[index % dates_count]  # Get the date corresponding to the current index
        program = programs[index % programs_count]  # Get the program corresponding to the current index

        logging.info(f"({index + 1}/{names_count}) Generate {name}'s certificate")

        try:
            generate_certificate(
                font=font,
                font_size=font_size,
                offset=offset,
                color=font_color,
                image=template,
                name=name,
                date=date,
                program=program,
                output_folder=output_folder,
                date_font=date_font,
                date_font_size=date_font_size,
                date_font_color=date_font_color,
                date_offset=date_offset,
                program_font=program_font,
                program_font_size=program_font_size,
                program_font_color=program_font_color,
                program_offset=program_offset
            )
        except Exception as e:
            logging.error(f"Error while generating certificate: {e}")

    logging.info("Done")


if __name__ == "__main__":
    main()
