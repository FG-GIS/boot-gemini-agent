# from subdirectory.filename import function_name
from functions.get_file_content import get_file_content

def main():
    # # get_files_info test 
    # #--------------------
    # print("Test 1 -> args: 'calculator','.'\nResults:\n")
    # print(get_files_info("calculator","."))
    # print("\n")
    # print("Test 2 -> args: 'calculator','pkg'\nResults:\n")
    # print(get_files_info("calculator","pkg"))
    # print("\n")
    # print("Test 3 -> args: 'calculator','/bin'\nResults:\n")
    # print(get_files_info("calculator","/bin"))
    # print("\n")
    # print("Test 4 -> args: 'calculator','../'\nResults:\n")
    # print(get_files_info("calculator","../"))
    # print("\n")
    # #--------------------
    print("Test -- get_file_content('calculator','main.py')\nResult:\n")
    print(get_file_content("calculator", "main.py"))
    print("\n")
    print("Test -- get_file_content('calculator','pkg/calculator.py')\nResult:\n")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n")
    print("Test -- get_file_content('calculator','/bin/cat')\nResult:\n")
    print(get_file_content("calculator", "/bin/cat"))
    print("\n")

if __name__ == "__main__":
    main()