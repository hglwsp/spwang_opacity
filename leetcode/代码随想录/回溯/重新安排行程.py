import collections

# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets_dict = collections.defaultdict(list)
# for item in tickets:
#     tickets_dict[item[0]].append(item[1])
# tickets_dict["JFK"].sort()
# end = tickets_dict["JFK"].pop(0)
# print(end)

class Solution:
    def findItinerary(self, tickets):
        #defaultdict类避免KeyError异常:
        # defaultdic(list) 是为了方便直接append
        tickets_dict = collections.defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]
        #tickets_dict里面的内容是这样的
         #{'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        #pop(0),{'JFK': ['ATL'],
        path = ["JFK"]
        def backtrack(startpoint):
            if len(path) == len(tickets)+1:
                return True
            tickets_dict[startpoint].sort()  # 对里面的按照字典进行排序
            for _ in tickets_dict[startpoint]:
                # JFK ->ATL 选择，然后删除
                endpoint = tickets_dict[startpoint].pop(0)
                path.append(endpoint)
                if backtrack(endpoint):
                    return True
                path.pop()
                tickets_dict[startpoint].append(endpoint)
        backtrack("JFK")
        return path

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
test = Solution()
print(test.findItinerary(tickets))
