# thesis_results

### 目录

```
$ tree -d
├── RQ1_datasets
│   ├── EOSIO
│   │   └── RQ1-1_3881
|   |       └── ...
│   └── EVM
│       └── RQ1-1_5504
|       |   └── ...
│       └── RQ1-2_32
|           └── ...
├── RQ1_results
│   ├── RQ1-1
|   |   └── eosio_buildcfg
|   |   └── evm_buildcfg
|           └── EAEAnalyzer_results
|           └── rattle_results
|           └── vandal_results
|   └── RQ1-2
└── RQ2_datasets
|   └── safe
|       └── ...
|   └── unsafe
|       └── ...
└── RQ2_results
|   └── RQ2-1_evm_results
|   └── RQ2-2_evm_compare_results
|       └── EAEAnalyzer
|       └── Oyente
|       └── Vandal
└── RQ3_datasets
|   └── source_90
|       └── ...
└── RQ3_results
    └── RQ3-1_eosio_results
    └── RQ3-2_eosio_compare_results
    └── RQ3-3_verify_results
```

#### RQ1_datasets

包括EOSIO和EVM智能合约数据集，分为3个数据集，其中：

- RQ1-1_3881：包括3881个EOSIO智能合约字节码以及对应的ABI文件，主要用于验证构建EOSIO智能合约控制流图的准确性和有效性
- RQ1-1_5504：包括5504个以太坊智能合约字节码，主要用于验证构建以太坊智能合约控制流图的准确性和有效性
- RQ1-2_32：包括32个与gas相关的以太坊漏洞智能合约，主要用于验证一个准确的控制流图对漏洞检测的准确率影响

#### RQ1_results

主要对RQ1的数据集进行的实验结果，其中：

- RQ1-1：包括构建EOSIO以及以太坊智能合约的控制流图的结果，文件夹`eosio_buildcfg`中包含工具[EVulHunter](https://github.com/EVulHunter/EVulHunter)和本文框架构建智能合约的结果；文件夹`evm_buildcfg`中包含工具[rattle](https://github.com/crytic/rattle)、[vandal](https://github.com/usyd-blockchain/vandal)以及本文框架构建智能合约的结果，其中由于rattle和vandal的结果太大，因此保存在[Google云盘](https://drive.google.com/drive/my-drive)中
- RQ1-2：包括工具[MadMax](https://github.com/nevillegrech/MadMax)以及用本文构建智能合约控制流图的方法输入到MadMax中前后漏洞检测结果比较

#### RQ2_datasets

- safe：包括7种类型以太坊智能合约，分别为重入（1400）、未检查外部调用（70）、自毁（1400）、利用tx.origin授权（1400）、时间戳依赖（1400）、严格余额相等（20）以及拒绝服务（100）等7种安全的智能合约数据集，总共2895个

- unsafe：包括7种类型以太坊智能合约，分别为重入（700）、未检查外部调用（35）、自毁（700）、利用tx.origin授权（700）、时间戳依赖（700）、严格余额相等（10）以及拒绝服务（50）等7种不安全的智能合约数据集，总共5790个

#### RQ2_results

- RQ2-1_evm_results：包括对2895个安全和5790个不安全以太坊智能合约的最终检测结果，每个漏洞的检测结果都有对应的`json`文件和对应的结果截图
- RQ2-2_evm_compare_results：包括与工具Oyente和Vandal的对比实验结果，其中Oyente包括2种漏洞的检测结果，vandal包括4种漏洞的检测结果

#### RQ3_datasets

- source_90：包括90个EOSIO智能合约源码以及对应的字节码

#### RQ3_results

- RQ3-1_eosio_results：包括对90个EOSIO智能合约的最终检测结果
- RQ3-2_eosio_compare_results：包括与工具[WANA](https://github.com/gongbell/WANA)、[EOSFuzzer](https://github.com/gongbell/EOSFuzzer)以及EVulHunter的对比实验结果
- RQ3-3_verify_results：包括对EOSIO智能合约三种漏洞的复现过程

### 总结

最终的实验数据集以及实验结果都被放在[GitHub](https://github.com/132cloudlab/thesis_results)以及[Google云盘](https://drive.google.com/drive/my-drive)中。实验结果显示：本文提出的框架无论是在精确率、准确率、召回率、F1、假阳率以及假阴率等各方面的指标都比其他工具表现得更好、更理想，从而凸显出工具EAEAnalyzer的高准确性以及高有效性。
