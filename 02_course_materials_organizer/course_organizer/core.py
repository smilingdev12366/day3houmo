import os
import shutil
from .rules import HOMEWORK_KEYWORDS, EXT_RULES, ALL_CATEGORIES


def get_file_category(filename: str) -> str:
    """
    根据文件名判断文件归属分类
    优先级：作业关键字 > 文件后缀
    """

    for kw in HOMEWORK_KEYWORDS:
        if kw in filename:
            return "homework"

    _, ext = os.path.splitext(filename.lower())
    for cat, ext_list in EXT_RULES.items():
        if ext in ext_list:
            return cat

    return "others"


def get_safe_dst_path(dst_dir: str, filename: str) -> str:
    """
    安全生成目标文件路径，同名文件自动加_1、_2后缀避免覆盖
    """
    base_name, ext = os.path.splitext(filename)
    target_path = os.path.join(dst_dir, filename)
    counter = 1
    while os.path.exists(target_path):
        new_name = f"{base_name}_{counter}{ext}"
        target_path = os.path.join(dst_dir, new_name)
        counter += 1
    return target_path


def scan_source_files(source_dir: str):
    """遍历源目录，只返回文件（排除文件夹）"""
    file_list = []
    for name in os.listdir(source_dir):
        full_path = os.path.join(source_dir, name)
        if os.path.isfile(full_path):
            file_list.append((full_path, name))
    return file_list


def organize_files(source: str, target: str, dry_run: bool, mode: str = "copy"):
    """
    主整理逻辑
    :param source: 源目录
    :param target: 目标根目录
    :param dry_run: 是否仅预览不执行操作
    :param mode: copy / move，默认复制
    :return: 操作记录列表、分类统计字典
    """

    record_list = []

    cat_count = {cat: 0 for cat in ALL_CATEGORIES}

    file_info = scan_source_files(source)
    if not file_info:
        print("源目录中未找到任何文件！")
        return record_list, cat_count

    if not dry_run:

        os.makedirs(target, exist_ok=True)
        for cat in ALL_CATEGORIES:
            cat_dir = os.path.join(target, cat)
            os.makedirs(cat_dir, exist_ok=True)


    for src_full, filename in file_info:
        cat = get_file_category(filename)
        cat_dir = os.path.join(target, cat)
        dst_full = get_safe_dst_path(cat_dir, filename)
        record_list.append((src_full, dst_full, cat))
        cat_count[cat] += 1

        print(f"[{cat}] {src_full} --> {dst_full}")

        if dry_run:
            continue

        if mode == "copy":
            shutil.copy2(src_full, dst_full)
        elif mode == "move":
            shutil.move(src_full, dst_full)

    return record_list, cat_count


def generate_report(target_dir: str, record_list, cat_count, dry_run: bool, mode: str):
    """生成整理报告.txt，写入目标目录根目录"""
    if dry_run:
        print("\n=== Dry Run模式，不生成整理报告 ===")
        return

    report_path = os.path.join(target_dir, "整理报告.txt")
    total_files = len(record_list)
    op_type = "复制" if mode == "copy" else "移动"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("课程资料整理报告\n")
        f.write("=" * 50 + "\n")
        f.write(f"操作类型：{op_type}（原始文件{'保留' if mode == 'copy' else '已移动'}）\n")
        f.write(f"本次整理文件总数：{total_files} 个\n")
        f.write("-" * 50 + "\n")
        f.write("各分类文件数量统计：\n")
        for cat, num in cat_count.items():
            f.write(f"  {cat}：{num} 个\n")
        f.write("-" * 50 + "\n")
        f.write("文件迁移明细（源路径 -> 目标路径）：\n")
        for src, dst, cat in record_list:
            f.write(f"【{cat}】{src} -> {dst}\n")
        f.write("=" * 50 + "\n")
    print(f"\n整理报告已生成：{report_path}")