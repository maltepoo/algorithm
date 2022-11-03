def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            binary = list('0'+bin(num)[2:])
            i = ''.join(binary).rfind('0')
            binary[i], binary[i+1] = '1', '0'
            answer.append(int(''.join(binary), 2))
    return answer