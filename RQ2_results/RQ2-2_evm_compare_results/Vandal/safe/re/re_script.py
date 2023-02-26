import os
import shutil

contract_path = "/home/lwy/papers/vandal/0.4_safe_re_bytecode_1400/"
bin_path = os.listdir(contract_path)
sh_path = "../../bin/analyze.sh"
target_path = "/home/lwy/papers/vandal/all_resutls/re_safe_results/"
datalog_path = "../../datalog/demo_re_analyses.dl"
for file in bin_path:
    file_name = file.split('.')[0]
    exec_path = f"{sh_path} {contract_path}{file} {datalog_path}"
    os.system(exec_path)
    if os.path.getsize("reentrantCall.csv") != 0:
        if os.path.exists(file_name):
            continue
        os.mkdir(file_name)
        shutil.move("reentrantCall.csv", file_name)
    else:
        os.remove("reentrantCall.csv")
