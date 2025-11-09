import argparse
import csv
import sys
from pathlib import Path

from eth_account import Account


def generate_accounts(count: int):
    # 生成指定数量的账户信息。
    for index in range(1, count + 1):
        created = Account.create_with_mnemonic(num_words=12)
        account = created[0]
        mnemonic = created[1]
        yield {
            "index": index,
            "address": account.address,
            "private_key": account.key.hex(),
            "mnemonic": mnemonic,
        }


def write_to_csv(accounts, output_path: Path):
    # 将账户信息写入 CSV 文件。
    fieldnames = ["index", "address", "private_key", "mnemonic"]
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in accounts:
            writer.writerow(row)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="批量生成以太坊地址与 12 词助记词，并导出到 CSV。"
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        help="需要生成的账户数量（正整数）。未提供时将提示输入。",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path("eth_accounts.csv"),
        help="输出 CSV 文件路径（默认：eth_accounts.csv）。",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    count = args.count
    while count is None:
        try:
            user_input = input("请输入要生成的账户数量：").strip()
            count = int(user_input)
            if count <= 0:
                print("数量必须为正整数，请重新输入。")
                count = None
        except ValueError:
            print("输入无效，请输入正整数。")

    if count <= 0:
        raise SystemExit("错误：--count 必须为正整数。")

    Account.enable_unaudited_hdwallet_features()
    accounts = list(generate_accounts(count))
    write_to_csv(accounts, args.output)
    print(f"已生成 {count} 个账户，结果保存在 {args.output.resolve()} 。")


if __name__ == "__main__":
    main(sys.argv[1:])


