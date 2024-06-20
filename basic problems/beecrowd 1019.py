seconds = int(input())

print("{}:{}:{}".format(int(seconds/3600), (int(seconds%3600/60)), int(seconds%60)))