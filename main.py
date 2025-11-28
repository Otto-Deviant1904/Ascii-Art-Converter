from ascii_art import convert_image

def main():
    print("ASCII Art Converter")
    print("--------------------")
    print("1. Ultra Detailed ASCII")
    print("2. Shadow Boosted ASCII")
    print("3. Matrix Style ASCII")
    print("4. Emoji Style")
    print("5. Colored ASCII")
    print()

    style = int(input("Enter style number: "))
    path = input("Enter image path: ")
    width = int(input("Enter ASCII width (default 120–200): "))

    print("\nConverting...\n")
    output = convert_image(path, style, width)
    print(output)

    save = input("\nSave output to file? (y/n): ").lower()
    if save == "y":
        with open("ascii_output.txt", "w", encoding="utf-8") as f:
            f.write(output)
        print("Saved as ascii_output.txt")


if __name__ == "__main__":
    main()
