import streamlit as st     #导入库
import pandas as pd
from datetime import datetime, time
st.set_page_config(page_title='个人简历生成器',page_icon='🎬',layout='wide')   #改网页名字
st.header('🎨个人简历生成器')    #标题
st.text('使用streamlit创建您的个性化简历')
c1,c2 = st.columns([1,2])
with c1:
    st.subheader('个人信息表单')
    st.markdown('***')
    name = st.text_input('姓名')
    job = st.text_input('职位')
    telephone = st.text_input('电话')
    email = st.text_input('邮箱')
    birthday = st.date_input("出生日期", value=None)
    gender = st.radio('性别：', ['男', '女'])
    options_1 = st.selectbox(
        '学历',
    ['高中','专科','本科', '研究生', '博士', '硕士'],
    )
    
    options_2 = st.multiselect(
        '语言能力',
    ['中文','英文','法语', '德语', '日语', '西班牙语'],
    )
    
   
    options_3 = st.multiselect(
        '技能（可多选）',
    ['Python','Java','JavaScript', 'HTML/CSS', 'SQL', '机器学习', '深度学习', '项目管理'],
    )    
    
    experience = st.slider('工作经验（年）', 0, 30, 3)
    
    salary = st.slider(
    '期望薪资范围（元）',
    5000,50000,(15000,30000))
    introduction = st.text_area(label='个人简介', placeholder='请简要介绍您的专业背景、职业目标和个人特点')
    
    contact_time = st.time_input("每日最佳联系时段")
    uploaded_files = st.file_uploader("上传个人照片",accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        st.write("文件名：",uploaded_file.name,"文件大小：",uploaded_file.size,"B")
with c2:
    st.subheader('简历实时预览')
    st.markdown('***')
    c1,c2 = st.columns(2)
    st.markdown('***')
    st.subheader('个人简介')
    
    if introduction:
        st.write(introduction)
    else:
        st.write("这个人很懒，什么都没有留下......")
    with c1:
        if name:
            st.markdown(f"## {name}")
        st.image(uploaded_files, width=200)
        st.write("职位：",job)
        st.write("电话：",telephone)
        st.write("邮箱：",email)
        st.write("出生日期：",birthday)
    with c2:
        st.write("性别:",gender)
        st.write("学历:",options_1)
        st.write("工作经验:",experience)
        st.write("期望薪资:",salary)
        st.write("最佳联系时段:",contact_time)
    
        # 在简历预览部分替换原来的语言能力显示
        if options_2:
           st.write("语言能力:", ", ".join(options_2))
        else:
           st.write("语言能力: 未填写")
        
    

