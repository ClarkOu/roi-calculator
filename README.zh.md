# 人效提升与人力释放测算器 (Streamlit)

[English](README.md)

面向 HR 与企业管理场景的自动化提效测算工具。支持按多个流程环节估算年节省工时、FTE 释放和效率提升。

## 功能特性

- 支持添加多个流程环节并查看汇总结果
- 支持填写评估信息（场景名称、部门）
- 支持明细表查看与单行选择
- 支持编辑（弹窗）/ 删除选中行
- 支持导出 CSV（含汇总解读行）

> 说明：受 Streamlit 原生表格能力限制，暂不支持在单元格内直接嵌入按钮。当前交互方式为：先选中行，再使用下方操作按钮。

## 计算方式

工具会将流程拆分为多个环节。每个环节输入基础工作量与自动化后的效率参数后，系统会汇总估算：

- 年节省工时（小时/年）
- FTE 释放量（按工时换算）
- 效率提升（改造前后对比）

典型使用流程：

1) 填写场景名称和部门
2) 逐个添加流程环节
3) 查看明细、实时预估和汇总指标
4) 当假设变化时，选中行进行编辑或删除
5) 导出带汇总解读的 CSV 用于共享

## 本地运行

1) 克隆仓库

```bash
git clone https://github.com/ClarkOu/roi-calculator.git
cd roi-calculator
```

2) 创建虚拟环境并安装依赖

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3) 启动应用

```bash
streamlit run app.py
```

在终端输出的地址中访问（通常为 http://localhost:8501）。

## 项目结构

- app.py：Streamlit 应用
- roi_calculator.py：原始计算脚本（CLI / 逻辑参考）
- requirements.txt：依赖列表

## 备注

- CSV 导出使用 UTF-8 BOM（`utf-8-sig`），可减少 Excel 打开中文乱码问题。
