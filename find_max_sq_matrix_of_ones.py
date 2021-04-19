# =======================================================
"""
Test Examples:
M = [
    [0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1]
]

M = [[1,1],
     [1,0]]
     
M = [1]
"""

# ====================================================


dfM = pd.DataFrame(M)

longest_sq = 0
for i in range(1, min(dfM.shape)+1):
    for hor in range(0, dfM.shape[0]):
        for ver in range(0, dfM.shape[1]):
            # print("=============================")
            _dfM = dfM.iloc[hor: i+hor, ver: i+ver]
            if all(dfM.iloc[hor: i+hor, ver: i+ver].prod().get_values()) and all(dfM.iloc[hor: i+hor, ver: i+ver].prod(axis = 1).get_values()) and (_dfM.shape[0] == _dfM.shape[1]) and (longest_sq <= _dfM.shape[0]):
                # print(f"{reduce((lambda x, y: x+y), _dfM)}::{_dfM.shape}")
                # print(_dfM)
                longest_sq = _dfM.shape[0]

print(f"For input:\n{M}\n\nLongest Sequence is::{longest_sq}")


# =========================OUTPUT=========================
"""
For input:
[[0, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1]]
Longest Sequence is::3
"""

"""
For input:
[[1, 1], [1, 0]]
Longest Sequence is::1
"""

"""
For input:
[1]
Longest Sequence is::1
"""

