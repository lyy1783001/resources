import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="示例程序 - 演示add_argument用法")

# 添加各种参数
parser.add_argument("input", help="输入文件（位置参数）")
parser.add_argument("-o", "--output", default="output.txt", help="输出文件（默认：output.txt）")
parser.add_argument("-n", "--number", type=int, required=True, help="必需的数字参数")
parser.add_argument("-v", "--verbose", action="store_true", help="显示详细信息")
parser.add_argument("-l", "--level", choices=["low", "medium", "high"], default="medium", help="级别选择")
parser.add_argument("--files", nargs="+", help="多个文件")

# 解析参数
args = parser.parse_args()

# 使用参数
print(f"输入文件: {args.input}")
print(f'input type:{type(args.input)}')
print(f"输出文件: {args.output}")
print(f'output type:{type(args.output)}')
print(f"数字: {args.number}")
print(f'number type:{type(args.number)}')
if args.verbose:
    print("详细模式开启")
print(f"级别: {args.level}")
if args.files:
    print(f"文件列表: {args.files}")