

def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        box = {}
        trap = 0
        n= len(height)
        for i in range(0,max(height)):
            box[i] = []
            for j in height:
                if(j - (i+1) >= 0):
                    box[i].append(1)
                else:
                    box[i].append(0)
            
            left = 0
            right = 1
            while left < (n-2)  and right < (n-1):
                if(box[i][left]==0):
                    left+=1
                    right+=1
                elif(box[i][left] == 1 ):
                    while box[i][right] !=1 and right<n-1:
                        right+=1
                    if(box[i][right] and right-left > 1):
                        trap+= right-left - 1
                        left = right
                        right+=1
                    else:
                        left+=1
                        right+=1
        return trap


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

            