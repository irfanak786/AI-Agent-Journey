environment = ["walls", "open area", "trash bin"]
def decide_and_move(environment):
    for element in environment:
        print(f"checking: {element}")
        if element == "walls":
            print("A wall came in front of me and I am moving to another direction ")
        elif element == "open area":
            print("I am in the open area and can move freely")
        elif element == "trash bin":
            print("I found the trash bin and I'll take out all the trash from it")
        print(".......")
decide_and_move(environment)

