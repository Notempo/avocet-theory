import json
f = open('main.json')
dict = json.load(f)
f.close()
tf = open("io1.txt", "a")
tf.write('{\n')
tf.close()
tf = open("io2.txt", "a")
tf.write('{\n')
tf.close()
for (k,v) in dict.items():
    if "/" in k or "#" in k or "^" in v or "{" in v or "}" in v or '"' in v or "1" in k or "2" in k or "3" in k or "4" in k or "5" in k or "6" in k or "7" in k or "8" in k or "9" in k or "0" in k:
        pass
    else:
        tf = open("io1.txt", "a")
        tf.write('"'+k+'": "'+v+'",\n')
        tf.close()
        tf = open("io2.txt", "a")
        tf.write('"'+v+'": "'+k+'",\n')
        tf.close()
tf = open("io1.txt", "a")
tf.write('}')
tf.close()
tf = open("io2.txt", "a")
tf.write('}')
tf.close()