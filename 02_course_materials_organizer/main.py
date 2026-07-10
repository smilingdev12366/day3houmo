import argparse
from course_organizer.core import organize_files, generate_report

def main():
    # 1. 创建命令行解析器
    parser = argparse.ArgumentParser(description="课程资料自动分类整理工具")
    # 必填参数
    parser.add_argument("--source", required=True, help="原始课程资料目录路径")
    parser.add_argument("--target", required=True, help="整理后文件存放的目标目录")
    # 可选参数
    parser.add_argument("--dry-run", action="store_true", help="仅预览整理计划，不实际操作文件")
    parser.add_argument("--mode", choices=["copy", "move"], default="copy", help="文件操作模式：copy复制(默认) / move移动")

    # 解析命令行输入
    args = parser.parse_args()

    # 校验源目录是否存在
    import os
    if not os.path.isdir(args.source):
        print(f"错误：源目录 {args.source} 不存在！")
        return

    print("===== 课程资料整理器启动 =====")
    print(f"源目录：{args.source}")
    print(f"目标目录：{args.target}")
    print(f"操作模式：{args.mode}")
    print(f"Dry Run预览模式：{'开启' if args.dry_run else '关闭'}")
    print("-" * 40)

    # 执行整理
    records, cat_stats = organize_files(
        source=args.source,
        target=args.target,
        dry_run=args.dry_run,
        mode=args.mode
    )

    # 生成报告（dry_run不生成）
    generate_report(
        target_dir=args.target,
        record_list=records,
        cat_count=cat_stats,
        dry_run=args.dry_run,
        mode=args.mode
    )

    print("\n===== 整理流程结束 =====")
    print(f"共处理文件：{len(records)} 个")

if __name__ == "__main__":
    main()