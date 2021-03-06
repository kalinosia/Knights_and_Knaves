from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# P → Q = ¬P ∨ Q     Implication
# P ⬌ Q = (P → Q) V (Q → P)      Biconditional
# ¬(P ^ Q) = ¬P V ¬Q          De Morgan’s Law
# (P ^ (Q V R)) = (P ^ Q) V (P ^ R)      Distributive Property
# (P V (Q ^ R)) = (P V Q) ^ (P V R)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(
        And(AKnight, And(AKnight, AKnave)),
        And(AKnave, Not(And(AKnight, AKnave)))
    )
)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Or(
        And(AKnight, And(AKnave, BKnave)),
        And(AKnave, Not(And(AKnave, BKnave)))
    )
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Or(
        And(AKnight, And(AKnight, BKnight)),
        And(AKnave, Not(And(AKnave, BKnave)))
    ),
    Or(
        And(BKnight, (And(AKnave, BKnight))),
        And(BKnave, Not(And(AKnight, BKnave)))
    )
    #Or(And(AKnight, Or(Not(BKnight), (Or(And(AKnight, BKnave), And(AKnave, BKnight))))),  And(AKnave, Or(Not(BKnave),  (Or(Not(And(AKnight, BKnave)), Not(And(AKnave, BKnight)))))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnave, CKnight)),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    # #we need this???? probably not because this is has no info
    Or(
        Or(
            And(AKnight, AKnight),
            And(AKnave, Not(AKnight))
        ),
        Or(
            And(AKnight, AKnave),
            And(AKnave, Not(AKnave))
        )

    ),
    # B says "A said 'I am a knave'."
    Or(
        # B is knight
        And(BKnight,
            Or(
                And(AKnight, AKnave),
                And(AKnave, Not(AKnave))
            )
        ),
        # B is knave
        And(BKnave, Not(
            Or(
                And(AKnight, AKnave),
                And(AKnave, Not(AKnave))
            ))
        )
    ),
    # ?????^

    # B says "C is a knave."
    Or(
        And(BKnight, CKnave),
        And(BKnave, Not(CKnave)),
    ),
    # C says "A is a knight."
    Or(
        And(CKnight, AKnight),
        And(CKnave, Not(AKnight))
    )
)
'''
letters=['A', 'B', 'C']
for i in letters:
    knowledge3.add(
        Or(Symbol(f"{i}Knight"), Symbol(f"{i}Knave"))
    )
    knowledge3.add(
        Not(And(Symbol(f"{i}Knight"), Symbol(f"{i}Knave")))
    )
'''
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
