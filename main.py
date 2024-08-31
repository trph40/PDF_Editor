from pypdf import PdfReader, PdfWriter


path = eval(input("Enter the path of the pdf:  ").replace("\\", '/'))
# path = (r"C:\Users\Javohir\Downloads\Telegram "
#         r"Desktop\Entrepreneurship_5th_Edition_Andrew_Zacharakis_5_Wiley_Global_Education.pdf")

def getting_ranges_for_extracting_pages(ranges):
    ranges.append((int(input("Enter the starting:  ")) - 1, int(input("Enter the ending:  "))))
    while True:
        try:
            ranges.append((int(input("Enter the starting:  ")) - 1, int(input("Enter the ending:  "))))
        except ValueError:
            print(ranges)
            break


with open(path, "rb") as input_file:
    pdf_reader = PdfReader(input_file)

    pdf_writer = PdfWriter()

    print(
        "You should now enter different ranges of pages which to be extracted from the pdf file. \nIf you have reached the end of entering different ranges, press enter to start the process")
    ranges = []
    getting_ranges_for_extracting_pages(ranges)

    for value in ranges:
        print(value[0])
        print(value[1])
        for page_num in range(value[0], value[1]):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        with open(f"{str(value)}.pdf", "wb") as output_file:
            pdf_writer.write(output_file)

        pdf_writer = PdfWriter()
