#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROI 计算器 - Streamlit 前端界面
业务流程自动化效益评估工具
"""

import streamlit as st
import pandas as pd

# 页面配置
st.set_page_config(
    page_title="ROI计算器",
    page_icon="🧮",
    layout="wide"
)

# 初始化session state
if 'all_steps' not in st.session_state:
    st.session_state.all_steps = []
if 'form_key' not in st.session_state:
    st.session_state.form_key = 0

def calculate_roi(name, weekly_freq, manual_time, has_error, accuracy, review_time, fix_time):
    """计算单个环节的ROI"""
    # 处理准确率
    if has_error:
        acc = accuracy / 100
    else:
        acc = 1.0
        fix_time = 0
    
    # 原流程年耗时(分钟)
    original_annual = weekly_freq * manual_time * 52
    
    # 新流程单次耗时
    if acc == 1.0:
        new_time = review_time
    else:
        new_time = (acc * review_time) + ((1 - acc) * fix_time)
    
    # 计算节省
    new_annual = weekly_freq * new_time * 52
    saved_min = original_annual - new_annual
    saved_hours = saved_min / 60
    fte = saved_hours / 2000
    efficiency = (saved_min / original_annual) if original_annual > 0 else 0
    
    return {
        "环节名称": name,
        "周频次": weekly_freq,
        "原耗时(分钟)": manual_time,
        "新耗时(分钟)": round(new_time, 2),
        "年省工时(小时)": round(saved_hours, 1),
        "FTE释放": round(fte, 3),
        "效率提升": f"{efficiency:.1%}"
    }

# 编辑弹窗
@st.dialog("编辑环节")
def edit_dialog(idx):
    step = st.session_state.all_steps[idx]
    
    edit_name = st.text_input("环节名称", value=step['环节名称'])
    edit_freq = st.number_input("每周总频次", value=float(step['周频次']))
    edit_manual = st.number_input("原人工耗时(分钟)", value=float(step['原耗时(分钟)']))
    
    had_error = step['新耗时(分钟)'] > 0
    edit_has_error = st.checkbox("需要人工复核/修正", value=had_error)
    
    if edit_has_error:
        edit_accuracy = st.slider("准确率 (%)", 0, 100, 90)
        edit_review = st.number_input("复核耗时(分钟)", value=2.0)
        edit_fix = st.number_input("修正耗时(分钟)", value=15.0)
    else:
        edit_accuracy, edit_review, edit_fix = 100, 0, 0
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 保存", type="primary", use_container_width=True):
            new_result = calculate_roi(edit_name, edit_freq, edit_manual, edit_has_error, edit_accuracy, edit_review, edit_fix)
            st.session_state.all_steps[idx] = new_result
            st.rerun()
    with col2:
        if st.button("取消", use_container_width=True):
            st.rerun()

# 标题
st.title("🧮 ROI 计算器")
st.markdown("### 业务流程自动化效益评估工具")
st.markdown("用于计算AI/自动化项目的FTE释放量和效率提升")

st.divider()

# 两列布局，增加间距
col1, spacer, col2 = st.columns([1, 0.2, 1.5])

with col1:
    st.markdown("## 📝 添加环节")
    
    name = st.text_input("环节名称", placeholder="如：订单审核、发票处理...", key=f"name_{st.session_state.form_key}")
    weekly_freq = st.number_input("每周总频次", min_value=0.0, value=100.0, step=10.0, key=f"freq_{st.session_state.form_key}")
    manual_time = st.number_input("原人工单次耗时(分钟)", min_value=0.0, value=10.0, step=1.0, key=f"manual_{st.session_state.form_key}")
    
    # 错误计算选项
    has_error = st.checkbox("需要人工复核/修正", key=f"error_{st.session_state.form_key}",
                           help="如果自动化后仍需人工检查，请勾选")
    
    if has_error:
        accuracy = st.slider("准确率/命中率 (%)", 0, 100, 90, key=f"acc_{st.session_state.form_key}")
        review_time = st.number_input("正常情况-复核耗时(分钟)", min_value=0.0, value=2.0, step=0.5, key=f"review_{st.session_state.form_key}")
        fix_time = st.number_input("异常情况-修正耗时(分钟)", min_value=0.0, value=15.0, step=1.0, key=f"fix_{st.session_state.form_key}")
    else:
        accuracy = 100
        review_time = 0
        fix_time = 0
    
    if st.button("➕ 添加环节", type="primary", use_container_width=True):
        if not name.strip():
            st.error("⚠️ 请输入环节名称")
        elif weekly_freq <= 0 or manual_time <= 0:
            st.error("⚠️ 频次和耗时必须大于0")
        else:
            result = calculate_roi(name, weekly_freq, manual_time, has_error, accuracy, review_time, fix_time)
            st.session_state.all_steps.append(result)
            st.session_state.form_key += 1
            st.rerun()

with col2:
    st.markdown("## 📊 ROI 评估报告")
    
    if st.session_state.all_steps:
        # 表格（可选择行）
        df = pd.DataFrame(st.session_state.all_steps)
        df.insert(0, "序号", range(1, len(df)+1))
        
        event = st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row"
        )
        
        # 根据选中的行显示操作按钮
        if event.selection.rows:
            idx = event.selection.rows[0]
            st.info(f"已选中: **{st.session_state.all_steps[idx]['环节名称']}**")
            c1, c2 = st.columns(2)
            if c1.button("✏️ 编辑此行", use_container_width=True):
                edit_dialog(idx)
            if c2.button("🗑️ 删除此行", type="secondary", use_container_width=True):
                st.session_state.all_steps.pop(idx)
                st.rerun()
        
        # 汇总
        total_hours = sum(r['年省工时(小时)'] for r in st.session_state.all_steps)
        total_fte = sum(r['FTE释放'] for r in st.session_state.all_steps)
        
        st.divider()
        st.markdown("### 📈 汇总统计")
        m1, m2, m3 = st.columns(3)
        m1.metric("环节数量", f"{len(st.session_state.all_steps)} 个")
        m2.metric("年节省工时", f"{total_hours:.1f} 小时")
        m3.metric("累计FTE释放", f"{total_fte:.2f} 人力")
        st.caption("💡 FTE按年标准工时2000小时计算")
        
        # 底部按钮
        st.divider()
        b1, b2 = st.columns(2)
        with b1:
            df = pd.DataFrame(st.session_state.all_steps)
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("📥 导出CSV", csv, "roi_report.csv", "text/csv", use_container_width=True)
        with b2:
            if st.button("清空所有", use_container_width=True):
                st.session_state.all_steps.clear()
                st.rerun()
    else:
        st.info("👈 请在左侧添加环节")
