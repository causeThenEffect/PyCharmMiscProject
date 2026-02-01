from graphviz import Digraph

# 创建流程图
flow = Digraph()
flow.node('Start', shape='ellipse')
flow.node('Process', '处理数据')
flow.node('End', shape='ellipse')
flow.edge('Start', 'Process')
flow.edge('Process', 'End')

# 生成 PDF
flow.render('my_flowchart', format='pdf', view=True)