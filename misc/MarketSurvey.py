# Problem taken from CodeVita

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    answers = [int(x) for x in input().split()]
    responses = [answers[:]]

    for partnum in range(m):
        response = [int(x) for x in input().split()]
        responses.append(response)

        count = 0
        for i in range(n):
            if(response[i] == answers[i]):
                count += 1
        print(count)

        for i in range(n):
            freq = {}
            latest = {}
            for partnumber in range(partnum+2):
                answer = responses[partnumber][i]
                if(answer in freq):
                    freq[answer] += 1
                else:
                    freq[answer] = 1
                latest[answer] = partnumber

            mostansweredfreq = 0
            mostanswered = 0
            for choice, f in freq.items():
                if(f > mostansweredfreq):
                    answers[i] = choice
                    mostansweredfreq = f
                    mostanswered = choice
                elif(f == mostansweredfreq):
                    answers[i] = responses[max(
                        latest[choice], latest[mostanswered])][i]

    topper = 0
    score = 0
    for partnum in range(1, m+1):
        response = responses[partnum]

        count = 0
        for i in range(n):
            if(response[i] == answers[i]):
                count += 1
        if(count > score):
            topper = partnum
            score = count

    print(topper, score)
