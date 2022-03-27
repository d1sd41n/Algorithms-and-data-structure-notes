def collectStrings(obj):
    words = []
    for key in obj.keys():
        if type(obj[key]) == str:
            words.append(obj[key])
        elif type(obj[key]) == dict:
            words = words + collectStrings(obj[key])
    
    return words


obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

assert collectStrings(obj) == ['foo', 'bar', 'baz']
