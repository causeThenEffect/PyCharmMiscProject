from graphviz import Digraph

# 创建有向图
dot = Digraph(comment='示例有向图')

# 添加节点
dot.node('A', '节点 A')
dot.node('B', '节点 B')
dot.node('C', '节点 C')

# 添加边
dot.edge('A', 'B', label='A到B')
dot.edge('B', 'C', label='B到C')
dot.edge('A', 'C', label='A到C')

# 输出 .dot 文件
dot.save('example_graph.dot')

# 可选：直接生成 PNG
dot.render('example_graph', format='png', cleanup=True)
