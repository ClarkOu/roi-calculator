# ROI 计算器（Streamlit）

业务流程自动化效益评估工具：用于估算单个/多个流程环节的年节省工时、FTE 释放与效率提升。

## 功能

- 添加多个“环节”并汇总统计
- 表格展示明细（点击行选中）
- 对选中行进行编辑（弹窗）/删除
- 导出 CSV

> 说明：由于 Streamlit 原生表格组件限制，无法在表格单元格内直接嵌入按钮；当前实现为“选中行 → 下方按钮操作”。

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

3) 启动

```bash
streamlit run app.py
```

浏览器打开终端输出的地址（通常是 http://localhost:8501）。

## 部署（Streamlit Community Cloud）

1) 打开 https://share.streamlit.io/ 并用 GitHub 登录
2) New app / Deploy an app
3) 选择仓库：`ClarkOu/roi-calculator`
4) Branch：`main`
5) Main file path：`app.py`
6) Deploy

## 项目结构

- app.py：Streamlit 前端
- roi_calculator.py：原始计算器脚本（命令行/逻辑参考）
- requirements.txt：依赖

## 开发备注

- CSV 导出为 UTF-8 with BOM（utf-8-sig），方便 Excel 直接打开不乱码。
