import collections

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = collections.defaultdict(list)
        email_to_name = {}
        
        # 1. 构建邻接表
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                email_to_name[email] = name
                # 将该账号内的所有邮箱与第一个邮箱连接（形成一个连通分量）
                if i > 1:
                    graph[account[i-1]].append(email)
                    graph[email].append(account[i-1])
        
        # 2. DFS 遍历寻找连通分量
        visited = set()
        res = []
        
        for email in email_to_name:
            if email not in visited:
                visited.add(email)
                stack = [email]
                component = [email]
                
                while stack:
                    curr = stack.pop()
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                            component.append(neighbor)
                
                # 3. 整理结果：名字 + 排序后的邮箱列表
                res.append([email_to_name[email]] + sorted(component))
                
        return res