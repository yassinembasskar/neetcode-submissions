class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        num_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        if num1 == '0' or num2 == '0':
            return '0'
        results = []
        m = len(num1)
        n = len(num2)
        for i in range(m-1, -1, -1):
            reserve = 0
            result = '0' * (m-i-1)
            for j in range(len(num2)-1, -1, -1):
                now = reserve + str_num[num2[j]]*str_num[num1[i]]
                reserve = now // 10
                now = now % 10
                result = num_str[now] + result
            if reserve > 0:
                result = num_str[reserve] + result
            results.append(result)
        result = ''
        reserve = 0
        for i in range(0, len(results[-1])):
            somme = 0
            for res in results:
                idx = len(res) - 1 - i
                if idx >= 0:
                    somme += str_num[res[idx]]
            somme += reserve
            reserve = somme // 10
            somme = somme % 10
            result = num_str[somme] + result
        if reserve > 0:
            result = num_str[reserve] + result
        return result

