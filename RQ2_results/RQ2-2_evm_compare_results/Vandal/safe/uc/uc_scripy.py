import os
import shutil

contract_path = "/home/lwy/papers/vandal/0.5_safe_uc_bytecode_70/"
bin_path = os.listdir(contract_path)
sh_path = "../../bin/analyze.sh"
target_path = "/home/lwy/papers/vandal/all_resutls/uc_safe_results/"
datalog_path = "../../datalog/demo_uc_analyses.dl"

for file in bin_path:
    if file == 'a67dd2db997b051f5c042a288c875340.hex':
        continue
    file_name = file.split('.')[0]
    exec_path = f"{sh_path} {contract_path}{file} {datalog_path}"
    os.system(exec_path)
    if os.path.getsize("uncheckedCall.csv") != 0:
        if os.path.exists(file_name):
            continue
        os.mkdir(file_name)
        shutil.move("uncheckedCall.csv", file_name)
    else:
        os.remove("uncheckedCall.csv")
