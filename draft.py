def getting_ranges_for_extracting_pages(ranges):
    ranges.append((int(input("Enter the starting:  ")) - 1, int(input("Enter the ending:  "))))
    while True:
        try:
            ranges.append((int(input("Enter the starting:  ")) - 1, int(input("Enter the ending:  "))))
        except ValueError:
            print(ranges)
            break


ranges = []
getting_ranges_for_extracting_pages(ranges)


