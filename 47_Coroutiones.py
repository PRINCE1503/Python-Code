# Coroutiones
def search():
    import time
    info = "I am Prince. I am leave in Vadodra."
    time.sleep(4)

    while True:
        text = (yield)
        if text in info:
            print("Your text is available in the book.")
        else:
            print("Text is not available in the book.")


print("Please wait! File is reading..........")
searchline = search()
next(searchline)
print("Enter text you want to know it is available in book or not : ")
searchline.send(input())
searchline.close()
