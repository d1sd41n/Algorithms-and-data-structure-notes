def stringifyNumbers(obj):
    for x in obj:
        if type(obj[x]) in (int, float):
            obj[x] = str(obj[x])
        if type(obj[x]) == dict:
            obj[x] = stringifyNumbers(obj[x])
    
    return obj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

res = stringifyNumbers(obj)

print(res)

{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}