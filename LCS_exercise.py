#LCS code

def LCS(S1, S2):
    if S1 == '' or S2 == '':
        return 0
    else:
        if S1[0] == S2[0]: #do the first symbols match?
            return 1 + LCS(S1[1:], S2[1:])
        else:
            useS1 = LCS(S1, S2[1:])
            useS2 = LCS(S1[1:], S2)
            return max(useS1, useS2)

LCS("spam", "sam!")


memo = {}#dictionary for use in fastLCS

def fastLCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    if S1 == '' or S2 == '':
        memo[(S1, S2)] = 0 #remembering the base case
        return 0
    elif S1[0] == S2[0]: #do the first symbols match?
        answer = 1 + fastLCS(S1[1:], S2[1:])
        memo[(S1, S2)] = answer #remembering the case with same letter
        return answer
    else:
        useS1 = fastLCS(S1, S2[1:])
        useS2 = fastLCS(S1[1:], S2)
        answer = max(useS1, useS2)
        memo[(S1, S2)] = answer #remembering the max length
        return answer
