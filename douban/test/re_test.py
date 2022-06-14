import re

#pattern = '^a...s$'
pat = re.compile('[A-Z]{2,}')   #大于等于两个大写字母
#进行字符串匹配时，建议在字符串最前面加r
test_string = r'asBACbyEsADs'
#search:查找并返回第一个匹配
result = pat.search(test_string)
#findall:查找所有，并返回结果列表
result = pat.findall(test_string)
#sub:将目标中匹配的字符串，替换为参数字符串
result = pat.sub("GG",test_string)

if result:
  print(result)
else:
  print("查找不成功.")