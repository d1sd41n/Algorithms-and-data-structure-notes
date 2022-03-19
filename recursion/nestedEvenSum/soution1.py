def nestedEvenSum(obj, sum=0):
    # import pdb; pdb.set_trace()

    for i in obj:
      if type(obj[i]) in (int, float):
        if obj[i] % 2 == 0:
          sum += obj[i]
      
      elif type(obj[i]) == dict:
        sum += nestedEvenSum(obj[i], sum=0)
    
    return sum

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

# print(nestedEvenSum(obj1))

assert nestedEvenSum(obj1) == 6

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

assert nestedEvenSum(obj2) == 10


obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "d": 4,
  "d2": 43,
  "e": {"e": {"e": 2, "ww": {"w": 22}}, "ee": 'car'}
}

assert nestedEvenSum(obj2) == 14 +22