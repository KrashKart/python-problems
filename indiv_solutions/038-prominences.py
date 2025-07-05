import utils

def prominences(height):
    def is_peak(idx):
        return height[idx - 1] < height[idx] > height[idx + 1]
    
    peaks = []
    highest = 0
    height.append(0)
    height.insert(0, 0)
    for i in range(1, len(height)):
        if is_peak(i):
            highest = max(highest, height[i])
            peaks.append((i - 1, height[i]))
            
    for p in range(len(peaks)):
        if peaks[p][1] == highest:
            peaks[p] = peaks[p] + (peaks[p][1],)
        else:
            left = right = None
            final_left = final_right = None
            for i in range(peaks[p][0], 0, -1):
                if is_peak(i) and height[i] > peaks[p][1]:
                    final_left = left
                    break
                left = utils.minNone(left, height[i])

            for j in range(peaks[p][0] + 1, len(height) - 1):
                if is_peak(j) and height[j] > peaks[p][1]:
                    final_right = right
                    break
                right = utils.minNone(right, height[j])
            peaks[p] = peaks[p] + (peaks[p][1] - utils.maxNone(final_left, final_right),)

    return peaks