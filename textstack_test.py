from textstack import TextStack
import random, sys, logging, string

logging.basicConfig(filename='textstack_test.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())


teststack = TextStack()

logging.info("Started testing")

#Creating test set
random.seed()
test_set_str = list()
test_set_len = list()
for _ in range(10):
    word_len = random.randint(1, 20)
    word = ""
    for _ in range(word_len):
        word += random.choice(string.ascii_letters)
    test_set_str.append(word)
    test_set_len.append(word_len)

#Text size with empty stack test
logging.info("Testing shortest/longest text retrival with empty stack")
st = teststack.smallest_text()
lg = teststack.biggest_text()
if st != "":
    logging.error("Unexpected value returned by TextStack")
if lg != "":
    logging.error("Unexpected value returned by TextStack")
logging.info("Finished testing shortest/longest text retrival with empty stack")

#Stack push test
logging.info("Testing string-only stack push")
teststack.push_text(test_set_len[0])
if teststack.get_size() != 0:
    logging.error("Added non-string variable to stack")
teststack.push_text("")
if teststack.get_size() != 0:
    logging.error("Added empty string to stack")
logging.info("Finished testing string-only stack push")

logging.info("Testing string stack pushing")
for i in range(len(test_set_str)):
    teststack.push_text(test_set_str[i])

if teststack.get_size() != len(test_set_str):
    logging.error("Couldn't push full test set into stack")
logging.info("Finished testing stack pushing")

#Text index test
logging.info("Testing text at index retrival")
invalid_text = teststack.get_text(15)
if invalid_text != "":
    logging.error("Got text from invalid index")
valid_text = teststack.get_text(5)
if valid_text == "":
    logging.error("Couldn't get text from valid index")
for i in range(len(test_set_str)):
    if teststack.get_text(i) != test_set_str[i]:
        logging.error("Incorrect order in stack")
logging.info("Finished testing index retrival")

#Text size test
logging.info("Testing shortest/longest text retrival")
st = teststack.smallest_text()
lg = teststack.biggest_text()
if len(st) != min(test_set_len):
    logging.error("Shortest text wasn't returned by stack")
if len(lg) != max(test_set_len):
    logging.error("Longest text wasn't returned by stack")
logging.info("Finished testing shortest/longest text retrival")

#Text comparison test
logging.info("Testing text comparison")
invalid_comp = teststack.compare_size(15, 23)
if invalid_comp[0] != (0, "") or invalid_comp[1] != (0, ""):
    logging.error("Didn't get correct error values for invalid indexes in comparison")
idx1 = random.randint(0, 9)
idx2 = 0
while True:
    idx2 = random.randint(0, 9)
    if idx2 != idx1:
        break
valid_comp = teststack.compare_size(idx1, idx2)
if valid_comp[0][0] < valid_comp[1][0]:
    logging.error("Comparison failed to order sizes correctly")
logging.info("Finished testing text comparison")

logging.info("Finished unit test for TextHeap")
