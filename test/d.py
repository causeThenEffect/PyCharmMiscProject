from graphviz import Digraph


def create_research_flowchart():
    # 创建一个有向图
    dot = Digraph('Research_Design', comment='Research Methodology Flowchart')
    dot.attr(rankdir='TB', size='8,10')
    dot.attr('node', shape='rectangle', style='rounded,filled', fillcolor='white', fontname='Arial')

    # 1. 参与者节点
    dot.node('P', 'Participants\nGrade 10 EFL Students\nTwo Intact Classes', shape='none', fillcolor='none')

    # 2. 前测节点
    dot.node('Pre', 'Pretest (Week 0)\nIELTS Speaking Tasks\n• Fluency\n• Accuracy\n• Pronunciation\n• Complexity',
             align='left')

    # 3. 分组节点 (使用隐形辅助节点来创建分叉)
    dot.node('Group', 'Group Assignment', shape='plaintext')

    # 4. 实验干预分支
    dot.node('AI', 'AI Feedback')
    dot.node('Teacher', 'Teacher Feedback')

    # 5. 中测与后测
    dot.node('Mid', 'Midtest (Week 6)')
    dot.node('Post', 'Posttest (Week 12)')

    # 建立连接关系
    dot.edge('P', 'Pre')
    dot.edge('Pre', 'Group')

    # 从分组到两个反馈方式
    dot.edge('Group', 'AI')
    dot.edge('Group', 'Teacher')

    # 从两个反馈方式汇聚到中测
    dot.edge('AI', 'Mid')
    dot.edge('Teacher', 'Mid')

    # 中测到后测
    dot.edge('Mid', 'Post')

    # 保存并渲染
    # 'view=True' 会自动打开生成的 PDF 文件
    dot.render('research_flowchart', format='png', cleanup=True)
    print("流程图已生成：research_flowchart.png")


if __name__ == "__main__":
    create_research_flowchart()