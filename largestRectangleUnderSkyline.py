def largestRectangleUnderSkyline(buildings):

    ans_arr = []

    for i in range(len(buildings)):

        checkFor = buildings[i]
        endAt = len(buildings)
        ans = 0

        for rightEle in range(i, endAt):
            if buildings[rightEle] >= checkFor:
                ans += 1          
            else:
                break

        for leftEle in range(i, i-1, -1):
            if i == 0:
                break
            elif buildings[leftEle] >= checkFor:
                if buildings[leftEle - 1] >= checkFor:
                    ans += 1
                else:
                    break
                    
        ans_arr.append(checkFor * ans)

    return max(ans_arr)


if __name__ == '__main__':

    data = [20, 2, 2, 2, 2, 2, 10, 5, 5, 5, 4, 4]
    output = largestRectangleUnderSkyline(data)
    print(output)
