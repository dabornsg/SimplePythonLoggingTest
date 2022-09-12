import logging

class TextStack:
    def __init__(self):
        self.th = list()
        logging.info("Created TextStack")

    def push_text(self, nstring):
        if not isinstance(nstring, str):
            logging.error("Input variable is not a string")
            return
        if nstring == "":
            logging.error("Tried to push empty string")
            return
        logging.info(f"Adding string {nstring} to TextStack")
        n_item = (len(nstring), nstring)
        self.th.append(n_item)
        logging.info("String added")

    def smallest_text(self):
        logging.info("Shortest string requested")
        try:
            return min(self.th)[1]
        except:
            logging.error("No items available for getting shortest string in TextStack")
            return ""
    
    def biggest_text(self):
        logging.info("Longest string requested")
        try:
            return max(self.th)[1]
        except:
            logging.error("No items available for getting longest string in TextStack")
            return ""

    def get_text(self, idx):
        logging.info(f"String in index {idx} requested")
        try:
            return self.th[idx][1]
        except (ValueError, IndexError, TypeError):
            logging.error(f"Invalid index for current TextStack: {idx}")
            return ""

    def get_size(self):
        return len(self.th)

    def compare_size(self, idx1, idx2):
        logging.info(f"String comparison in indexes {idx1} and {idx2} requested")
        try:
            if self.th[idx1][0] > self.th[idx2][0]:
                return (self.th[idx1], self.th[idx2])
            return (self.th[idx2], self.th[idx1])
        except (ValueError, IndexError, TypeError):
            logging.error(f"Couldn't use one or both of the following indexes: {idx1}, {idx2}")
            return ((0, ""), (0, ""))

def main():
    logging.basicConfig(filename='textstack.log', encoding='utf-8', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("Started logging")
    th = TextStack()
    print("Welcome to TextStack!")
    choice = "-1"
    while choice != "6":
        print("Choose an operation:\n1.- Add text to stack\n2.- Print longest text in stack\n3.- Print shortest text in stack\n4.- Print text in given index\n5.- Compare size of two strings in stack\n6.- Quit")
        try:
            choice = input()
        except:
            logging.error("There was an exception while getting input for operation choice")
            continue
        if choice == "1":
            ntext = str()
            try:
                ntext = input("Write the new text to add to the stack (leave empty to return): ")
            except:
                logging.error("There was an exception while getting input for new text")
                continue
            if ntext != "":
                th.push_text(ntext)
                print(f"\"{ntext}\" added to the stack!")
            else:
                print("Input was not a valid string")
            
        elif choice == "2":
            bt = th.biggest_text()
            if bt != "":
                print("Longest text in stack: ", bt)
            else:
                print("No text available for retrival")

        elif choice == "3":
            st = th.smallest_text()
            if st != "":
                print("Shortest text in stack: ", st)
            else:
                print("No text available for retrival")

        elif choice == "4":
            idx_s = str()
            idx = 0
            try:
                idx_s = input(f"Write the index of the item in the stack (0-{th.get_size() - 1}): ")
            except:
                logging.error("There was an exception while getting input for index")
                continue
            try:
                idx = int(idx_s)
            except ValueError:
                logging.error(f"Unable to convert input {idx_s} to an integer")
                continue
            rs = th.get_text(idx)
            if rs != "":
                print(f"Text at index {idx}: {rs}")
            else:
                print(f"Could not retrieve text at index {idx}")

        elif choice == "5":
            idx1_s = str()
            idx1 = 0
            idx2_s = str()
            idx2 = 0

            try:
                idx1_s = input(f"Write the first index of the item to compare (0-{th.get_size() - 1}): ")
                idx2_s = input(f"Write the second index of the item to compare (0-{th.get_size() - 1}): ")
            except:
                logging.error("There was an exception while getting input for indexes")
                continue
            try:
                idx1 = int(idx1_s)
                idx2 = int(idx2_s)
            except ValueError:
                logging.error(f"Unable to convert input {idx1_s} and/or {idx2_s} to an integer")
                continue
            if idx1 == idx2:
                print("Can't compare same indexes")
                continue
            ret = th.compare_size(idx1, idx2)
            if ret[0][1] != "" and ret[1][1] != "":
                if ret[0][0] == ret[1][0]:
                    print(f"\"{ret[0][1]}\" is as long as \"{ret[1][1]}\" ({ret[0][0]} = {ret[1][0]})")
                else:
                    print(f"\"{ret[0][1]}\" is longer than \"{ret[1][1]}\" ({ret[0][0]} >= {ret[1][0]})")
            else:
                print("Invalid indexes given for retrival")
            
        elif choice == "6":
            pass

        else:
            print("Invalid operation choice")

if __name__ == "__main__":
    main()
