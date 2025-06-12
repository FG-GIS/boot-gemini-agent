# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info

def main():
    print("Test 1 -> args: 'calculator','.'\nResults:\n")
    print(get_files_info("calculator","."))
    print("\n")
    print("Test 2 -> args: 'calculator','pkg'\nResults:\n")
    print(get_files_info("calculator","pkg"))
    print("\n")
    print("Test 3 -> args: 'calculator','/bin'\nResults:\n")
    print(get_files_info("calculator","/bin"))
    print("\n")
    print("Test 4 -> args: 'calculator','../'\nResults:\n")
    print(get_files_info("calculator","../"))
    print("\n")

if __name__ == "__main__":
    main()