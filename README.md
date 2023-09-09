## hash-to-ash

A hash table implementation. data type -> (word, word's index on original text)

The Article class represents the hash table. The main usage scenario is to find the nth occurrence of a given word from a text, in constant expected time.

It uses open addressing, with double hashing technique. Expands based on the load factor.

You can use your own input text files. In order to shape them to the form you can use the inputify script. Script re-organizes whole file as full of lowercase letters/words and only whitespaces. 

> python3 inputify.py your_text_file.txt > new_file.txt


If you want to test your hashtable implementation, you can use main file and expected output files.