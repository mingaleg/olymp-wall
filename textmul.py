def multiply(text, coeff):
    text = list(filter(None, text.split('\n')))
    new = [[text[i//coeff][j//coeff] for j in range(len(text[0])*coeff)] for i in range(len(text*coeff))]
    return '\n'.join(''.join(t) for t in new)
