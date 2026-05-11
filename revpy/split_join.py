# def split_and_join(line):
#     # write your code here
#     words = line.split(" ")
#     result = ""
    
#     for i in range(len(words)):
#         result += words[i]
        
#         if i < len(words) - 1:
#             result += "-"
            
#     return result
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)