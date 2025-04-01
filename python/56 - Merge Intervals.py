def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0]) # NOTE: tricky
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if result[-1][1] >= start:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result



print(merge([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]
print(merge([[1,4],[0,1]]))  #[[0,4]]