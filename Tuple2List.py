def tolist(NestedTuple):
  # function to convert a nested tuple to a nested list
  return list(map(Tuple2List, NestedTuple)) if isinstance(NestedTuple, (list, tuple)) else NestedTuple
