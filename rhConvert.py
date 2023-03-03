import json
f = open('main1.json')
dict1 = json.load(f)
f.close()
word = []
for (k,v) in dict1.items():
    word.append(k)
# STKPWHR AO*EU FRPBLGTSDZ
conv = {"S": "S", "T": "L", "K": "G", "P": "P", "W": "B", "H": "F", "R": "R", "A": "U", "O": "E"}
chk = "-*EU"
tf = open("io.txt", "a")
tf.write('{\n')
tf.close()
for i in range(len(word)):
    a = word[i]
    z = dict1.get(a)
    b = ""
    c = True
    d = 0
    e = False
    if a[0] in chk:
        b = "-TZ/" + a
        tf = open("io.txt", "a")
        tf.write('"'+b+'": "'+z+'",\n')
        tf.close()
    elif a[0] == "A" or a[0] == "O":
        for i in range(len(a)):
            if a[i] == "A" or a[i] == "O":
                b = conv.get(a[i]) + b
            else:
                if d == 0:
                    b += "/" + a[i]
                    d += 1
                else:
                    b += a[i]
        tf = open("io.txt", "a")
        tf.write('"'+b+'": "'+z+'",\n')
        tf.close()
    else:
        for i in range(len(a)):
            if c:
                if a[i] in chk:
                    c = False
                    b += "/" + a[i]
                    d += 1
                elif a[i] == "A" or a[i] == "O":
                    e = True
                    b = conv.get(a[i]) + b
                else:
                    if e:
                        if a[i] != "A" and a[i] != "O":
                            c = False
                            b += "/" + a[i]
                            d += 1
                    else:
                        b = conv.get(a[i]) + b
            else:
                b += a[i]
        b = "-" + b
        if d == 0:
            b += "/-TZ"
        tf = open("io.txt", "a")
        tf.write('"'+b+'": "'+z+'",\n')
        tf.close()
tf = open("io.txt", "a")
tf.write('}')
tf.close()