"""
Task 2

Start

Create a sentence
Replace the "!" with a space
Use the UPPER function to make the sentence upper case, then print
Print the new sentence in reverse

End

"""

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
new_sentence = (sentence.replace("!"," "))
print(new_sentence)

print(new_sentence.upper())

print(new_sentence[::-1])