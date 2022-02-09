import os

def pretty_size(size: int)->str:
    if(size>1000000000): return f"{size/1000000000} Гб"
    elif(size>1000000): return f"{size/1000000} Мб"
    elif(size>1000): return f"{size/1000} Кб"


if __name__ == "__main__":
    os.chdir("c:\\")
    print(os.getcwd())
    for item in os.listdir():
        if not os.path.isfile(item): continue
        file_size=os.path.getsize(item)
        file_porazryad="{:,}".format(file_size)
        size_mb=file_size/1000000
        print(f"{item} | {file_size} | {file_porazryad} | {size_mb} | {pretty_size(file_size)}")