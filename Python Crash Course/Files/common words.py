with open("Python Crash Course/Files/guten.txt","r") as gutenberg:
    content = gutenberg.read()
    print(content.lower().count("gutenberg"))