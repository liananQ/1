import streamlit as st                    #导入streamlit并用st代替
import pandas as pd                    # 导入Pandas并用pd代替

st.title("🕶︎学生 小练-数字档案")       #标题🕶︎学生 小练-数字档案
st.header("🔑基础信息")                #章节标题🔑基础信息
st.subheader("学生ID：NEO-2023-001")    #子章节标题学生ID：NEO-2023-001
st.subheader("注册时间：':green[2023-10-01 08:30:17]' | 精神状态：✅正常")     
#子章节标题显示注册时间和精神状态
st.subheader("当前教室：':green[实训301]' | 安全等级：':green[绝密]'")        
#子章节标题显示当前教室和安全等级
 
st.header("Streamlit课程进度")          #章节标题Streamlit课程进度
st.subheader("Streamlit课程进度")       #子章节标题Streamlit课程进度
st.progress(0.5)                       #模拟进度条50%

st.subheader(' 📊技能矩阵')               #章节标题📊技能矩阵
c1, c2, c3 = st.columns(3)                 # 定义列布局，分成3列
c1.metric(label="C语言", value="95%", delta="2%")
# 在第一列显示C语言技能水平，包含当前值和变化幅度       
c2.metric(label="Python", value="87%", delta="-1%")
# 在第二列显示Python技能水平，包含当前值和变化幅度
c3.metric(label="Java", value="68%", delta="-10%")
# 在第三列显示Java技能水平，包含当前值和变化幅度


st.header("📝 任务日志")              #章节标题📝任务日志
data = {
    '日期':["2023-05-10", "2023-05-15", "2023-05-22", "2023-05-28", "2023-06-02"],
    '任务':["Python数据分析项目", "Web开发实战", "算法设计挑战", "数据库优化", "机器学习基础"],
    '状态':["✅已完成", "✅已完成", "进行中", "❌未完成", "✅已完成"],
    '难度':["★★★☆☆", "★★★★☆", "★★★★☆", "★★★☆☆", "★☆☆☆☆"],
}                                    # 定义数据,以便创建数据框
index = pd.Series(['1', '2', '3', '4', '5'])        # 定义数据框所用的索引
df = pd.DataFrame(data, index=index)      # 根据上面创建的data和index，创建数据框

st.dataframe(df)                        #j将创建的数据框显示出来


st.header("':closed_lock_with_key:'最新代码成果")             #章节标题最新代码成果
st.code('''                                              # 创建要显示的Python代码块的内容
def matrix_breach():
      while True
            if detect_vulnerability():
                 exploit()
                 return "ACCESS GRANTED"
            else:
                  stealth_evade()
''')
