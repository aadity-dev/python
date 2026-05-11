if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = set(arr)
    score.remove(max(score))
    print(max(score))
    
    
    #print(sorted(set(arr))[-2])