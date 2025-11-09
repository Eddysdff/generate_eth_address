# 以太坊地址批量生成工具

## 安装要求

### 依赖库
```bash
pip install eth-account
```

## 使用方法

### 方式一：交互式输入

直接运行脚本，程序会提示你输入要生成的账户数量：

```bash
python3 generate_eth_addresses.py
```

然后按照提示输入数量即可。

### 方式二：命令行参数

使用 `--count` 或 `-c` 参数指定要生成的账户数量：

```bash
python3 generate_eth_addresses.py --count 10
```

或使用简短参数：

```bash
python3 generate_eth_addresses.py -c 10
```

### 自定义输出文件

使用 `--output` 或 `-o` 参数指定输出文件路径：

```bash
python3 generate_eth_addresses.py --count 100 --output my_accounts.csv
```

默认输出文件为 `eth_accounts.csv`。

## 输出格式

生成的 CSV 文件包含以下列：

| 列名 | 说明 |
|------|------|
| index | 账户序号（从 1 开始） |
| address | 以太坊地址（0x 开头的 42 位十六进制字符串） |
| private_key | 私钥（64 位十六进制字符串） |
| mnemonic | 12 词助记词（空格分隔） |

### 示例输出

```csv
index,address,private_key,mnemonic
1,0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb5,0x1234567890abcdef...,abandon ability able about above absent absorb abstract absurd .......
2,0x8ba1f109551bD432803012645Hac136c22C9c00A,0xabcdef1234567890...,accident access abuse absurd abstract absorb absent above about .......
```

## 安全注意事项

⚠️ **重要安全提示**

1. **私钥和助记词是敏感信息**：任何人获得这些信息都可以完全控制对应的账户和资金。

2. **妥善保管**：
   - 不要通过不安全的渠道分享这些文件
   - 建议使用加密存储或密码管理器保存


## 示例

### 生成 5 个账户

```bash
python3 generate_eth_addresses.py -c 5
```

输出：
```
已生成 5 个账户，结果保存在 /path/to/evm_account/eth_accounts.csv 。
```

### 生成 100 个账户并保存到指定文件

```bash
python3 generate_eth_addresses.py --count 100 --output accounts_100.csv
```


