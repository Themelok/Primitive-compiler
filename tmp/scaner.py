import pyparsing as pp
data = "cat Sandy Mocha Java"
label= pp.Word(pp.alphas)
rowPat = pp.OneOrMore(pp.Word(pp.alphas))
bigPat = pp.Dict(pp.Group(label+rowPat))
result = bigPat.parseString(data)
print(dict(result))