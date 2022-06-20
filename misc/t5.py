def max_chain_len(given_str: str) -> int:
    given_str = given_str.split(',')

    chains = []

    counter = 0
    for n, i in enumerate(given_str):
        if n + 1 >= len(given_str):
            break
        first = given_str[n][2]
        second = given_str[n + 1][0]
        if first == second:
            counter += 1
        else:
            chains.append(counter)
            counter = 0
    chains.append(counter)
    m = max(chains)
    return m+1 if m else 0


r = max_chain_len('2-3,3-4,4-5')
print(r)

r = max_chain_len('1-1,1-1,1-1,1-1')
print(r)

r = max_chain_len('1-1,2-3')
print(r)
