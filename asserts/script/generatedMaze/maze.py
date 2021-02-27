from random import randint

class maze:
  def __init__(self, height, width):
    self.h = 2 * height
    self.w = 2 * width
    self.graph = [[0 for i in range(self.w)] for j in range(self.h)]


  def generate(self):
    for i in range(self.h):
      for j in range(self.w):
        if i % 2 == 0 and j % 2 == 0:
          self.graph[i][j] = 1
    self.graph.insert(0, [0 for i in range(self.w)])
    self.w += 1
    self.h += 1
    for i in range(self.h):
      self.graph[i].insert(0, 0)

    current = [1, 1]
    nonUsed = dict()
    k = 1
    for i in range(self.h):
      for j in range(self.w):
        if self.graph[i][j] == 1:
          nonUsed[(i, j)] = k
          k += 1
    nonUsed.pop((1, 1))

    def Wall(graph, x):
      return self.graph[x[0] - 1][x[1]] == 1 or self.graph[x[0] + 1][x[1]] == 1 or self.graph[x[0]][x[1] - 1] == 1 or self.graph[x[0]][x[1] + 1] == 1 

    def freeNeighbors(graph, x):
      w = len(self.graph[0])
      h = len(self.graph)
      ans = []
      up    = (x[0] - 2, x[1])
      down  = (x[0] + 2, x[1])
      left  = (x[0],     x[1] - 2)
      right = (x[0],     x[1] + 2)
      if up[0] > 0 and not Wall(self.graph, up):
        ans.append(up)
      if down[0] < h - 1 and not Wall(self.graph, down):
        ans.append(down)
      if left[1] > 0 and not Wall(self.graph, left):
        ans.append(left)
      if right[1] < w - 1 and not Wall(self.graph, right):
        ans.append(right)
      return ans

    stack = []
    while nonUsed:
      neighbors = freeNeighbors(self.graph, current)
      if neighbors:
        stack.append(current)
        randomCell = neighbors[randint(0, len(neighbors) - 1)]
        direction = (randomCell[0] - current[0], randomCell[1] - current[1])
        self.graph[current[0] + direction[0] // 2][current[1] + direction[1] // 2] = 1    
        current = [current[0] + direction[0], current[1] + direction[1]]
        nonUsed.pop(tuple(current))
      else:
        current = stack.pop(0)
    return self.graph


  def solve(self):
    self.maze = self.graph
    start = (1, 1)
    end = (len(self.maze) - 2, len(self.maze[0]) - 2)

    self.graph = dict()
    for i in range(1, self.h - 1):
      for j in range(1, len(self.maze[i]) - 1):
        if self.maze[i][j]:
          self.graph[(i, j)] = []

    for i in range(1, len(self.maze) - 1):
      for j in range(1, len(self.maze[i]) - 1):
        if self.maze[i][j]:
          if self.maze[i + 1][j]: self.graph[(i, j)].append((i + 1, j))
          if self.maze[i - 1][j]: self.graph[(i, j)].append((i - 1, j))
          if self.maze[i][j + 1]: self.graph[(i, j)].append((i, j + 1))
          if self.maze[i][j - 1]: self.graph[(i, j)].append((i, j - 1))

    used = {start}
    stack = [start]

    p = dict()
    p[start] = -1

    while stack:
      u = stack.pop(0)
      for i in range(len(self.graph[u])):
        v = self.graph[u][i]
        if v not in used:
          used.add(v)
          stack.append(v)
          p[v] = u

    self.path = set()
    while end != -1:
      self.maze[end[0]][end[1]] = 2
      self.path.add(end)
      end = p[end]

    return self.path

  def makeFile(self):
    f = open("maze.json", 'w')
    f.write("h=" + str(self.h) + '\n')
    f.write("w=" + str(self.w) + '\n' + "maze={")
    for i in range(len(self.maze) - 1):
      f.write("{}:\"{}\",".format(i, str(self.maze[i])[1:-1].replace(', ', '')))
    f.write("{}:\"{}\"".format(len(self.maze) - 1, str(self.maze[-1])[1:-1].replace(', ', '')) + '}\n')

    f.write("p={}\n".format(len(self.path)))
    f.write("Path={")
    self.path = list(self.path)
    for i in range(len(self.path) - 1):
      f.write("{}:[{},{}],".format(i, self.path[i][0], self.path[i][1]))
    f.write("{}:[{},{}]".format(i, self.path[-1][0], self.path[-1][1]) + "}\n")
    f.close()

m = maze(300, 130)
m.generate()
m.solve()
m.makeFile()