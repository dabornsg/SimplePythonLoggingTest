from textheap import TextHeap
import random, sys, logging

logging.basicConfig(filename='textheap_test.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())


testheap = TextHeap()

logging.info("Started testing")

#Creating test set
random.seed()
test_set_str = list()
for _ in range(10):
    test_set_str.append(str(random.randint(0, sys.maxsize)))

test_set_len = [len(i) for i in test_set_str]

#Heap push test
logging.info("Testing string-only heap push")
testheap.push_text(test_set_len[0])
if testheap.get_size() != 0:
    logging.error("Added non-string variable to heap")
logging.info("Finished testing string-only heap push")

logging.info("Testing string heap pushing")
for i in range(len(test_set_str)):
    testheap.push_text(test_set_str[i])

if testheap.get_size() != len(test_set_str):
    logging.error("Couldn't push full test set into heap")
logging.info("Finished testing heap pushing")

#Text size test
logging.info("Testing shortest/longest text retrival")
st = testheap.smallest_text()
lg = testheap.biggest_text()
if len(st) != min(test_set_len):
    logging.error("Shortest text wasn't returned by heap")
if len(lg) != max(test_set_len):
    logging.error("Longest text wasn't returned by heap")
logging.info("Finished testing shortest/longest text retrival")

#Text index test
logging.info("Testing text at index retrival")
invalid_text = testheap.get_text(15)
if invalid_text != "":
    logging.error("Got text from invalid index")
valid_text = testheap.get_text(5)
if valid_text == "":
    logging.error("Couldn't get text from valid index")
logging.info("Finished testing index retrival")

#Text comparison test
logging.info("Testing text comparison")
invalid_comp = testheap.compare_size(15, 23)
if invalid_comp[0] != (0, "") or invalid_comp[1] != (0, ""):
    logging.error("Didn't get correct error values for invalid indexes in comparison")
idx1 = random.randint(0, 9)
idx2 = 0
while True:
    idx2 = random.randint(0, 9)
    if idx2 != idx1:
        break
valid_comp = testheap.compare_size(idx1, idx2)
if valid_comp[0][0] < valid_comp[1][0]:
    logging.error("Comparison failed to order sizes correctly")
logging.info("Finished testing text comparison")

logging.info("Finished unit test for TextHeap")
