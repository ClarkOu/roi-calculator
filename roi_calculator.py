#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROI 计算器 - 业务流程自动化效益评估工具
用于计算AI/自动化项目的FTE释放量和效率提升
"""

# 存储所有环节
all_steps = []

def add_step():
    """添加一个业务环节"""
    print("\n--- 添加新环节 ---")
    
    name = input("环节名称: ").strip()
    if not name:
        print("已取消")
        return
    
    weekly_freq = float(input("每周总频次: "))
    manual_time = float(input("原人工单次耗时(分钟): "))
    
    # 询问是否需要计算错误率
    has_error = input("是否需要计算错误/修正成本? (y/n，默认n): ").strip().lower()
    
    if has_error == 'y':
        accuracy = float(input("准确率/命中率 (0-100，如90表示90%): ")) / 100
        review_time = float(input("正常情况-人工复核耗时(分钟): "))
        fix_time = float(input("异常情况-修正耗时(分钟): "))
    else:
        accuracy = 1.0
        review_time = float(input("人工复核耗时(分钟，如不需要填0): "))
        fix_time = 0
    
    # 计算
    result = calculate(name, weekly_freq, manual_time, accuracy, review_time, fix_time)
    all_steps.append(result)
    
    print(f"\n✓ 已添加: {name}")
    print(f"  单次节省: {manual_time - result['new_time']:.2f} 分钟")
    print(f"  年节省工时: {result['saved_hours']:.1f} 小时")
    print(f"  FTE释放: {result['fte']:.2f}")

def calculate(name, weekly_freq, manual_time, accuracy, review_time, fix_time):
    """计算单个环节的ROI"""
    # 原流程年耗时(分钟)
    original_annual = weekly_freq * manual_time * 52
    
    # 新流程单次耗时
    if accuracy == 1.0:
        new_time = review_time
    else:
        new_time = (accuracy * review_time) + ((1 - accuracy) * fix_time)
    
    # 新流程年耗时
    new_annual = weekly_freq * new_time * 52
    
    # 节省
    saved_min = original_annual - new_annual
    saved_hours = saved_min / 60
    fte = saved_hours / 2000  # 标准年工时2000小时
    efficiency = (saved_min / original_annual) if original_annual > 0 else 0
    
    return {
        "name": name,
        "freq": weekly_freq,
        "manual_time": manual_time,
        "new_time": round(new_time, 2),
        "saved_hours": round(saved_hours, 1),
        "fte": round(fte, 3),
        "efficiency": efficiency
    }

def show_summary():
    """显示汇总报表"""
    if not all_steps:
        print("\n⚠ 暂无数据，请先添加环节")
        return
    
    print("\n" + "="*90)
    print("                        ROI 评估报告")
    print("="*90)
    print(f"{'序号':<4} | {'环节名称':<15} | {'周频次':<8} | {'原耗时':<8} | {'新耗时':<8} | {'年省工时':<10} | {'FTE':<6} | {'效率提升':<8}")
    print("-"*90)
    
    for i, r in enumerate(all_steps, 1):
        print(f"{i:<4} | {r['name']:<15} | {r['freq']:<8} | {r['manual_time']:<8} | {r['new_time']:<8} | {r['saved_hours']:<10} | {r['fte']:<6} | {r['efficiency']:.1%}")
    
    print("-"*90)
    total_fte = sum(r['fte'] for r in all_steps)
    total_hours = sum(r['saved_hours'] for r in all_steps)
    
    print(f"\n【汇总】")
    print(f"  • 环节数量:     {len(all_steps)} 个")
    print(f"  • 年节省工时:   {total_hours:.1f} 小时")
    print(f"  • 累计FTE释放:  {total_fte:.2f} 个标准人力")
    print("="*90)

def delete_step():
    """删除一个环节"""
    if not all_steps:
        print("\n⚠ 暂无数据")
        return
    
    show_summary()
    idx = input("\n输入要删除的序号 (回车取消): ").strip()
    if idx and idx.isdigit():
        idx = int(idx) - 1
        if 0 <= idx < len(all_steps):
            removed = all_steps.pop(idx)
            print(f"✓ 已删除: {removed['name']}")

def clear_all():
    """清空所有数据"""
    confirm = input("确认清空所有数据? (y/n): ").strip().lower()
    if confirm == 'y':
        all_steps.clear()
        print("✓ 已清空")

def main():
    """主程序"""
    print("\n" + "="*50)
    print("   ROI 计算器 - 业务流程自动化效益评估")
    print("="*50)
    
    while True:
        print("\n请选择操作:")
        print("  1. 添加环节")
        print("  2. 查看汇总")
        print("  3. 删除环节")
        print("  4. 清空数据")
        print("  0. 退出")
        
        choice = input("\n输入选项: ").strip()
        
        if choice == '1':
            add_step()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            delete_step()
        elif choice == '4':
            clear_all()
        elif choice == '0':
            print("\n再见!")
            break
        else:
            print("无效选项")

if __name__ == "__main__":
    main()
