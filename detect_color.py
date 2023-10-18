import sys
import webcolors

def first_color_name_to_hex(potential_colors):
    for color in potential_colors:
        try:
            hex_value = webcolors.name_to_hex(color)
            return hex_value
        except ValueError:
            # If the color name is not recognized by webcolors, ignore it
            pass

    return None

if __name__ == "__main__":
    result = first_color_name_to_hex(sys.argv)

    if result is None:
        print('ff0000')
    else:
        print(result[1:])
