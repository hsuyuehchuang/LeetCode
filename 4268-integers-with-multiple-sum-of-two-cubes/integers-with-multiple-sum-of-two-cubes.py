class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        curr = 1
        curr_cube = 1
        cubes = []
        while curr_cube <= n:
            cubes.append(curr_cube)
            curr += 1
            curr_cube = curr**3

        count = {}
        for i in range(len(cubes)):
            for j in range(i, len(cubes)):
                sum = cubes[i] + cubes[j]
                if sum <= n:
                    count[sum] = count.get(sum, 0) + 1

        good_integers=[]
        for x, freq in count.items():
            if freq >= 2:
                good_integers.append(x)

        return sorted(good_integers)


        return sorted(seen_again)
        