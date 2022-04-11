def string_compression_array(word: str):
    # return empty string if empty string provided
    if not word:
        return ""

    result = []
    counter = 0
    for idx, val in enumerate(word):
        # if not the first idx and the current character does not match the last character
        if idx != 0 and word[idx] != word[idx - 1]:
            # extend the result with the last word and its count
            result.extend([word[idx - 1], str(counter)])
            counter = 1
        # else increment current counter for last character
        else:
            counter += 1
    # add last character in the word
    result.extend([word[-1], str(counter)])
    return "".join(result) if len(result) < len(word) else word


functions = [string_compression_array]
