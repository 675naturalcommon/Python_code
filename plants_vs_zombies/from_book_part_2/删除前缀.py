nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix('https://'))
#如果你在地址栏中看到不包含https:// 部分的URL，可能是浏览器在幕后使⽤了类似于removeprefix() 的⽅法。

print(nostarch_url.removeprefix('nos'))  #由此可知removeprefix()只准删除前缀

print(nostarch_url.removesuffix('.com'))  #removesuffix()只准删除后缀

