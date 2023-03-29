import pickle
import pickletools
import base64
from PIL import Image

#l = [b"(dp0\nS'serum'\np1\nccopy_reg\n_reconstructor\np2\n(c__main__\nanti_pickle_serum\np3\nc__builtin__\nobject\np4\nNtp5\nRp6\ns."]
#l2 = [b"Aasdad"]
#for val in l2:
#    pickletools.dis(val)

# KGRwMApTJ3NlcnVtJwpwMQpjY29weV9yZWcKX3JlY29uc3RydWN0b3IKcDIKKGNfX21haW5fXwphbnRpX3BpY2tsZV9zZXJ1bQpwMwpjX19idWlsdGluX18Kb2JqZWN0CnA0Ck50cDUKUnA2CnMu


# b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x06pickle\x94\x8c\x02me\x94K\x01K\x02K\x03e.'


# x = pickle.dumps(['pickle', 'aneesh', 0, 0, 7])
# b = base64.b64encode(x)
# print(b)

# d = pickle.loads(base64.b64decode(b))

# print(d)

# x = pickle.dumps("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Risus in hendrerit gravida rutrum quisque non. Dictumst vestibulum rhoncus est pellentesque. Pellentesque habitant morbi tristique senectus et netus. At consectetur lorem donec massa sapien faucibus et molestie. Iaculis at erat pellentesque adipiscing commodo elit at. A erat nam at lectus urna duis. Ornare quam viverra orci sagittis eu. Pretium quam vulputate dignissim suspendisse in est ante in. Ipsum faucibus vitae aliquet nec ullamcorper. Proin libero nunc consequat interdum varius sit. At erat pellentesque adipiscing commodo elit at imperdiet. At erat pellentesque adipiscing commodo. Velit scelerisque in dictum non consectetur a erat nam at.
# Ac odio tempor orci dapibus ultrices in. Aliquam id diam maecenas ultricies mi eget mauris pharetra et. At elementum eu facilisis sed odio morbi quis commodo odio. Ac turpis egestas sed tempus urna et pharetra pharetra. Enim sit amet venenatis urna cursus eget nunc. Neque vitae tempus quam pellentesque. Elementum nibh tellus molestie nunc non blandit massa enim. Ultrices tincidunt arcu non sodales neque sodales ut etiam sit. Donec adipiscing tristique risus nec. Est velit egestas dui id ornare.""")
# b = base64.b64encode(x)
# print(b)

# d = pickle.loads(base64.b64decode(b))

# print(d)

# x = pickle.dumps(b'\x01\x03\x00\x00\x00')
# b = base64.b64encode(x)
# print(b)

# d = pickle.loads(base64.b64decode(b))

# print(d)

# class Test():
#     def foo():
#         return ("Something else")

# x = pickle.dumps(Test())

# x2 = pickle.dumps(x)
# b = base64.b64encode(x2)
# print(b)
# d = pickle.loads(base64.b64decode(b))
# print(d)


img = Image.open('abc.png')
x2 = pickle.dumps(img)
b = base64.b64encode(x2)
#print(b)
d = pickle.loads(base64.b64decode(b))
#print(d)