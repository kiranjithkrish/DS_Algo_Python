# Function to check if the given list represents min-heap or not
def checkMinHeap(A, i):
    # if `i` is a leaf node, return true as every leaf node is a heap
    if 2 * i + 2 > len(A):
        return True

    # if `i` is an internal node

    # recursively check if the left child is a heap
    left = (A[i] <= A[2 * i + 1]) and checkMinHeap(A, 2 * i + 1)

    # recursively check if the right child is a heap (to avoid the list index out
    # of bounds, first check if the right child exists or not)
    right = (2 * i + 2 == len(A)) or (
        A[i] <= A[2 * i + 2] and checkMinHeap(A, 2 * i + 2)
    )

    # return true if both left and right child are heaps
    return left and right


A = [
    -975,
    -917,
    -947,
    -731,
    -877,
    -924,
    -810,
    -581,
    -702,
    -531,
    -753,
    -396,
    -739,
    -738,
    -656,
    -54,
    -488,
    -500,
    551,
    -249,
    -401,
    -685,
    -655,
    153,
    689,
    -359,
    -279,
    -578,
    343,
    -356,
    528,
    61,
    399,
    669,
    -320,
    568,
    194,
    738,
    763,
    -90,
    445,
    -45,
    452,
    993,
    394,
    195,
    713,
    153,
    329,
    788,
    844,
    867,
    266,
    556,
    904,
    -154,
    376,
    464,
    748,
    -312,
    150,
    972,
    886,
    459,
    94,
    544,
]

B = [
    -987,
    -950,
    -942,
    -949,
    -941,
    -874,
    -685,
    -823,
    -908,
    -738,
    -935,
    -817,
    -575,
    -293,
    -337,
    -363,
    -796,
    -846,
    -578,
    -733,
    -420,
    -855,
    -191,
    -120,
    125,
    -544,
    -371,
    -160,
    -36,
    -51,
    295,
    164,
    -353,
    -542,
    59,
    540,
    -730,
    -575,
    -441,
    -254,
    -469,
    -167,
    -410,
    59,
    14,
    919,
    -155,
    646,
    52,
    980,
    328,
    341,
    399,
    372,
    965,
    243,
    610,
    48,
    842,
    422,
    -13,
    700,
    800,
    183,
    829,
    -257,
    631,
    -359,
    201,
    238,
    157,
    950,
    892,
    724,
    -265,
    746,
    355,
    892,
    -415,
    323,
    490,
    490,
    -376,
    356,
    995,
    -126,
    572,
    888,
]
# start with index 0 (the root of the heap)
index = 0

if checkMinHeap(B, index):
    print("The given list is a min-heap")
else:
    print("The given list is not a min-heap")
