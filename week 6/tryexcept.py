import os
file_path = os.path.join(os.path.dirname(__file__), 'test_file.txt')
try:
    f = open(file_path  ,'r')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:#if the try function runs successfully
    print(f.read())
    f.close()
finally:#runs no matter what
    print("Finally Exit")