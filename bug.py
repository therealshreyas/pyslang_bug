import pyslang

def get_tokens():
    tree = pyslang.SyntaxTree.fromFile('test.sv')
    tokens = []
    def handle(obj):
        if isinstance(obj, pyslang.Token):
            tokens.append(obj)
    tree.root.visit(handle)
    return tokens

def func_without_dict(tokens):
    for k in tokens:
        print(str(k))

def func_with_dict(tokens):
    ind_cnt = {}
    for i in range(50):
        ind_cnt[i] = 0
    func_without_dict(tokens)

tokens = get_tokens()

print("---- FUNCTION WITHOUT DICT ----")
func_without_dict(tokens)
print("-------------------------------")
print()

print("---- FUNCTION WITH DICT ----")
func_with_dict(tokens)
print("-------------------------------")