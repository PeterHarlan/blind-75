def adjecent_list():
    nums = [3,2,4]
    target = 6
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            num_1 = nums[i]
            num_2 = nums[j]
            if(num_1 + num_2 == target):
                print([i, j])

# Check if target is in map
# map = {}
# "target" in map // Returns true or false if "target" exits in the map

def main():
    # Your main code goes here
    series_map = {}
    if("target" not in series_map):
        print("hi")
    
   

if __name__ == "__main__":
    main()
