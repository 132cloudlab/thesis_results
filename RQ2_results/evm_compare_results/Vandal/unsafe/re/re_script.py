import os
import shutil

contract_path = "/home/lwy/tools/vandal/datasets/0.4_unsafe_re_bytecode_700/"
bin_path = os.listdir(contract_path)
sh_path = "../../bin/analyze.sh"
target_path = "/home/lwy/tools/vandal/all_results/re_results/"
datalog_path = "../../datalog/demo_re_analyses.dl"

for file in bin_path:
    file_name = file.split('.')[0]
    exec_path = f"{sh_path} {contract_path}{file} {datalog_path}"
    os.system(exec_path)
    if os.path.getsize("reentrantCall.csv") != 0:
        os.mkdir(file_name)
        shutil.move("reentrantCall.csv", file_name)
    else:
        os.remove("reentrantCall.csv")
