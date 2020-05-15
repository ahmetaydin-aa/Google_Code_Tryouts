
def decompress(input_string: str) -> str:
    import re
    pattern = re.compile(r"(\d+)\[(\w+)\]")
    patterns = pattern.findall(input_string)
    return_string = input_string
    if len(patterns) == 0:
        return return_string
    else:
        for x in patterns:
            repeat_count = int(x[0])
            string_part = x[1]
            old_string = "{}[{}]".format(repeat_count, string_part)
            return_string = return_string.replace(old_string, string_part*repeat_count)
        return decompress(return_string)

if __name__ == "__main__":
    a = "3[abc]4[ab]c"
    print(decompress(a))

    b = "2[3[a]b]"
    print(decompress(b))

    b = "0[abc]"
    print(decompress(b))

    b = "a[]b"
    print(decompress(b))

    b = "2[3[a2[3[2[3[a]b2[3[a]b]]a]b]]b]c"
    print(decompress(b))