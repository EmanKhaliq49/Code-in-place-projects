def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    count = 0
    for keys, values in translations.items():
        correct_value = input(f"What is the Spanish translation for {keys}? ").strip().lower()
        if correct_value == values.lower():
            print("That is correct!")
            count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {keys} is {values}.")
        print()
    print(f"You got {count}/8 words correct, come study again soon!")

if __name__ == '__main__':
    main()
