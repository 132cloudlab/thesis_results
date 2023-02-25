import os
import shutil

contract_path = "/home/lwy/tools/vandal/datasets/0.5_unsafe_tx_bytecode_700/"
bin_path = os.listdir(contract_path)
sh_path = "../../bin/analyze.sh"
target_path = "/home/lwy/tools/vandal/all_results/tx_results/"
datalog_path = "../../datalog/demo_tx_analyses.dl"

for file in bin_path:
    file_name = file.split('.')[0]
    exec_path = f"{sh_path} {contract_path}{file} {datalog_path}"
    os.system(exec_path)
    if os.path.getsize("originUsed.csv") != 0:
        os.mkdir(file_name)
        shutil.move("originUsed.csv", file_name)
    else:
        os.remove("originUsed.csv")

