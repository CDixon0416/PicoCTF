#!/usr/bin/python3
def main():
    rot13()

def rot13():
    with open('./flag') as file:
        flag_txt = file.read()
        decipher_txt = ""
        for char in flag_txt:
            char_as_ascii = ord(char)
            rot = char_as_ascii + 13
            
            # Lowercase 97-122
            if char_as_ascii >= 97 and char_as_ascii <=122:
                if rot >= 122:
                    rot = rot - 26
            # Uppercase 65-90
            elif char_as_ascii >=65 and char_as_ascii <=90:
                if rot >= 90:
                    rot = rot - 26
            # Special chars 
            else:
                rot = char_as_ascii
            decipher_txt = decipher_txt + chr(rot)
            print(decipher_txt)
        flag_solved = open('flag_solved', 'w')
        flag_solved.write(decipher_txt)

if __name__ == "__main__":
    main()
