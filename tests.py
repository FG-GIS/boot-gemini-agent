# from subdirectory.filename import function_name
from functions.run_python import run_python_file

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

    # # get_file_content test
    # #--------------------
    # print("Test -- get_file_content('calculator','main.py')\nResult:\n")
    # print(get_file_content("calculator", "main.py"))
    # print("\n")
    # print("Test -- get_file_content('calculator','pkg/calculator.py')\nResult:\n")
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print("\n")
    # print("Test -- get_file_content('calculator','/bin/cat')\nResult:\n")
    # print(get_file_content("calculator", "/bin/cat"))
    # print("\n")
    # #--------------------

    # # write_file test
    # #--------------------
    # print("Test -- write_file('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum')")
    # print(write_file("calculator","lorem.txt","wait, this isn't lorem ipsum"))
    # print("\n")
    # print("Test -- write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    # print(write_file("calculator","pkg/morelorem.txt","lorem ipsum dolor sit amet"))
    # print("\n")
    # print("Test -- write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    # print(write_file("calculator","/tmp/temp.txt","this should not be allowed"))
    # print("\n")
    # #--------------------

    # run_python_file test
    #--------------------
    print("Testing -- run_python_file 'calculator', 'main.py'\n")
    print(run_python_file("calculator","main.py"))
    print("\n")
    print("Testing -- run_python_file 'calculator', 'tests.py'\n")
    print(run_python_file("calculator","tests.py"))
    print("\n")
    print("Testing -- run_python_file 'calculator', '../main.py'\n")
    print(run_python_file("calculator","../main.py"))
    print("\n")
    print("Testing -- run_python_file 'calculator', 'nonexistent.py'\n")
    print(run_python_file("calculator","nonexistent.py"))
    print("\n")


if __name__ == "__main__":
    main()