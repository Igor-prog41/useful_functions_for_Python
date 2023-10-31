def filter_file_with_words_five_letters_long(f_in: str, f_new: str) -> None:
    """
    The function selects words from a file that are five letters long and creates a new file with only these words
    f_in (type:str) : name for file which will sorted
    f_new (type:str) : name for file which will keep result of work sorted function ("five_letter_noun.txt")
    """
    with open(f_new, "w", encoding="utf-8") as file_new:
        file_new.write("")

    with open(f_in, 'r', encoding="utf-8") as file_in:
        with open(f_new, "a", encoding="utf-8") as file_new:
            for row in file_in:
                if len(row.strip()) == 5:
                    file_new.write(row)
