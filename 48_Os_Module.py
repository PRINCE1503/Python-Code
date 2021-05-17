import os
print("Your current working directory is >>>", os.getcwd())
print("----------------------------------------------------------------------")
print("The file of your 'D:/' directory are as shown \n", os.listdir("D:/"))
print("----------------------------------------------------------------------")

# for create new file:
# try:
#     os.mkdir("Randomx.py")
#     os.rename("Randomx.py", "My python main Projects")
# except Exception as e:
#     print(e)
#     print("----------------------------------------------------------------------")

print("Environment variables of path is as shown : ")
print(os.environ.get('Path'))
